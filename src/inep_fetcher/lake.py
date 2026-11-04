"""Convert raw INEP microdata and educational indicators into the Hive lake.

Datasets in the Lake:
- Microdata: ``enem``, ``censo-escolar``, ``censo-educacao-superior``, ``saeb``,
  ``enade``, ``ana``, ``encceja``, ``censo-magisterio``, ``enade-licenciaturas``,
  ``enamed``, ``pnd``, ``pnera``, ``pesquisa-discriminacao``, ``idd``,
  ``enem-por-escola``, ``talis``.
- Indicadores Educacionais: 18 groups (``adequacao-formacao-docente``,
  ``complexidade-gestao-escola``, ``esforco-docente``, ``fluxo-educacao-superior``,
  ``qualidade-educacao-superior``, ``trajetoria-educacao-superior``,
  ``financeiros``, ``media-alunos-por-turma``, ``media-horas-aula-diaria``,
  ``nivel-socioeconomico``, ``docentes-curso-superior``, ``docentes-pos-graduacao``,
  ``regularidade-corpo-docente``, ``remuneracao-docentes``,
  ``taxas-distorcao-idade-serie``, ``taxas-nao-resposta``,
  ``taxas-rendimento-escolar``, ``taxas-transicao``).
"""

from __future__ import annotations

import re
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import duckdb
    import polars as pl
    from quantilica.analytics.lake import LakeError, LakeWriter
    from quantilica.core.files import decompress_archive
    from quantilica.core.lake import (
        DatasetDescriptor,
        composite_file_key,
        partition_types_for,
        select_current,
    )
except ImportError as exc:
    raise ImportError(
        "inep_fetcher.lake requer o extra 'analysis': "
        "uv add 'inep-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from inep_fetcher import __version__

SOURCE_ID = "inep"

MICRODATA_GROUPS = [
    "enem",
    "censo-escolar",
    "censo-educacao-superior",
    "saeb",
    "enade",
    "ana",
    "encceja",
    "censo-magisterio",
    "enade-licenciaturas",
    "enamed",
    "pnd",
    "pnera",
    "pesquisa-discriminacao",
    "idd",
    "enem-por-escola",
    "talis",
]

INDICADORES_GROUPS = [
    "adequacao-formacao-docente",
    "complexidade-gestao-escola",
    "esforco-docente",
    "fluxo-educacao-superior",
    "qualidade-educacao-superior",
    "trajetoria-educacao-superior",
    "financeiros",
    "media-alunos-por-turma",
    "media-horas-aula-diaria",
    "nivel-socioeconomico",
    "docentes-curso-superior",
    "docentes-pos-graduacao",
    "regularidade-corpo-docente",
    "remuneracao-docentes",
    "taxas-distorcao-idade-serie",
    "taxas-nao-resposta",
    "taxas-rendimento-escolar",
    "taxas-transicao",
]

ALL_DATASETS = sorted(MICRODATA_GROUPS + INDICADORES_GROUPS)

_DOC_PATTERNS = (
    "dicionario",
    "leia_me",
    "leia-me",
    "leiame",
    "anexo",
    "manual",
    "documentacao",
)

_YEAR = re.compile(r"[-_](?P<ano>(?:19|20)\d{2})(?:@|\.|$|\b)")


@dataclass
class ConvertResult:
    """Counts of a conversion run; ``errors`` holds one message per failure."""

    converted: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


def resolve_dataset(path: Path) -> str | None:
    """Infer dataset id from parent directory or filename."""
    parent = path.parent.name.lower().replace("_", "-")
    if parent in ALL_DATASETS:
        return parent
    grandparent = path.parent.parent.name.lower().replace("_", "-")
    if grandparent in ALL_DATASETS:
        return grandparent
    # Try filename prefix
    norm_name = path.name.lower().replace("_", "-")
    for ds in ALL_DATASETS:
        if norm_name.startswith(ds):
            return ds
    return None


def resolve_year(path: Path) -> int | None:
    """Extract integer 4-digit year from filename or folder."""
    match = _YEAR.search(path.name)
    if match:
        return int(match["ano"])
    if path.parent.name.isdigit() and len(path.parent.name) == 4:
        return int(path.parent.name)
    return None


def _detect_separator(path: Path) -> str:
    """Sniff CSV delimiter from the first line (defaulting to semicolon)."""
    try:
        with open(path, "rb") as f:
            line = f.readline().decode("latin-1", errors="ignore")
            if ";" in line:
                return ";"
            if "," in line:
                return ","
    except Exception:
        pass
    return ";"


class LakeConverter:
    """Converter registered under the ``quantilica.lake`` entry point."""

    source_id = SOURCE_ID

    def datasets(self) -> list[str]:
        """Dataset ids this converter writes to the lake."""
        return list(ALL_DATASETS)

    def convert(
        self,
        input_dir: Path,
        lake_dir: Path,
        *,
        datasets: list[str] | None = None,
        force: bool = False,
    ) -> ConvertResult:
        """Convert raw INEP files into ``lake_dir``.

        Args:
            input_dir: Root directory containing raw files.
            lake_dir: Root of the lake.
            datasets: Optional list of dataset ids to convert; None converts all.
            force: Reconvert even if sha256 already matches in the lake.

        Returns:
            ConvertResult: Files converted, skipped, and error messages.
        """
        input_dir = Path(input_dir)
        lake_dir = Path(lake_dir)
        result = ConvertResult()
        if not input_dir.is_dir():
            result.errors.append(f"diretório '{input_dir}' não existe")
            return result

        allowed = set(datasets) if datasets else set(ALL_DATASETS)
        unknown = allowed - set(ALL_DATASETS)
        if unknown:
            for u in sorted(unknown):
                result.errors.append(f"dataset desconhecido: {u}")
            return result

        candidates = sorted(
            p
            for p in input_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".csv", ".xlsx", ".zip", ".7z"}
        )

        current = set(
            select_current(p.relative_to(input_dir).as_posix() for p in candidates)
        )
        files = []
        for path in candidates:
            if path.relative_to(input_dir).as_posix() in current:
                files.append(path)
                continue
            ds = resolve_dataset(path)
            if ds and ds in allowed:
                result.skipped += 1

        writers: dict[str, LakeWriter] = {}

        for path in files:
            dataset_id = resolve_dataset(path)
            if not dataset_id or dataset_id not in allowed:
                continue

            year = resolve_year(path)
            part_keys: list[str] = ["ano"] if year is not None else []
            part_vals: dict[str, Any] = {"ano": year} if year is not None else {}

            writer_key = f"{dataset_id}:" + ",".join(part_keys)
            if writer_key not in writers:
                writers[writer_key] = LakeWriter(
                    lake_dir / SOURCE_ID / dataset_id,
                    DatasetDescriptor(
                        source_id=SOURCE_ID,
                        dataset_id=dataset_id,
                        alias=dataset_id.replace("-", "_"),
                        partition_keys=part_keys,
                        partition_types=partition_types_for(part_keys),
                    ),
                    force=force,
                )
            writer = writers[writer_key]

            suffix = path.suffix.lower()
            try:
                if suffix == ".csv":
                    sep = _detect_separator(path)
                    fallback_sep = "," if sep == ";" else ";"
                    try:
                        written = writer.write_duckdb(
                            path,
                            partitions=part_vals,
                            separator=sep,
                            encoding="latin-1",
                            converter=f"inep-fetcher {__version__}",
                        )
                    except (LakeError, duckdb.Error):
                        written = writer.write_duckdb(
                            path,
                            partitions=part_vals,
                            separator=fallback_sep,
                            encoding="latin-1",
                            converter=f"inep-fetcher {__version__}",
                        )
                    if written.status == "skipped":
                        result.skipped += 1
                    else:
                        result.converted += 1

                elif suffix == ".xlsx":
                    df = pl.read_excel(path)
                    written = writer.write_polars(
                        df,
                        path,
                        partitions=part_vals,
                        converter=f"inep-fetcher {__version__}",
                    )
                    if written.status == "skipped":
                        result.skipped += 1
                    else:
                        result.converted += 1

                elif suffix in {".zip", ".7z"}:
                    with tempfile.TemporaryDirectory() as tmp:
                        extracted = decompress_archive(path, Path(tmp))
                        all_members = sorted(
                            m
                            for m in Path(tmp).rglob("*")
                            if m.is_file() and m.suffix.lower() in {".csv", ".txt"}
                        )
                        # Filter out documentation and dictionary subpaths
                        data_members = [
                            m
                            for m in all_members
                            if not any(
                                doc in m.as_posix().lower() for doc in _DOC_PATTERNS
                            )
                        ]
                        if not data_members and all_members:
                            data_members = all_members
                        elif not data_members and extracted.is_file():
                            data_members = [extracted]

                        if not data_members:
                            result.errors.append(
                                f"{path.name}: nenhum arquivo de dados encontrado"
                            )
                            continue

                        for member in data_members:
                            member_name = member.stem
                            key = composite_file_key(path, member_name)
                            sep = _detect_separator(member)
                            fallback_sep = "," if sep == ";" else ";"
                            try:
                                written = writer.write_duckdb(
                                    member,
                                    partitions=part_vals,
                                    file_key_name=key,
                                    src_origin=path,
                                    separator=sep,
                                    encoding="latin-1",
                                    converter=f"inep-fetcher {__version__}",
                                )
                            except (LakeError, duckdb.Error):
                                written = writer.write_duckdb(
                                    member,
                                    partitions=part_vals,
                                    file_key_name=key,
                                    src_origin=path,
                                    separator=fallback_sep,
                                    encoding="latin-1",
                                    converter=f"inep-fetcher {__version__}",
                                )

                            if written.status == "skipped":
                                result.skipped += 1
                            else:
                                result.converted += 1

            except (
                LakeError,
                OSError,
                zipfile.BadZipFile,
                duckdb.Error,
                pl.exceptions.PolarsError,
                Exception,
            ) as exc:
                message = str(exc).strip()
                first_line = message.splitlines()[0] if message else repr(exc)
                result.errors.append(f"{path.name}: {first_line}")
                continue

        return result


converter = LakeConverter()
