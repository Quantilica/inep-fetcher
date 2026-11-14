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

import logging
import re
import tempfile
import unicodedata
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
from inep_fetcher.planilha import read_planilha
from inep_fetcher.sas_layout import (
    LAYOUT_FIXES,
    SasLayout,
    parse_sas_input,
    peek_infile,
)

logger = logging.getLogger(__name__)

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


def _ascii_lower(text: str) -> str:
    """Minúsculas sem acento ("DICIONÁRIO" -> "dicionario")."""
    nfkd = unicodedata.normalize("NFKD", text)
    return nfkd.encode("ascii", "ignore").decode("ascii").lower()


# Ordem de preferência no empate. O SAEB 2021+ (educação infantil, diretor e
# secretário municipal) usa "|".
_SEPARATORS = (";", ",", "|", "\t")


def _first_line_separator(path: Path) -> str | None:
    """Separador mais frequente na primeira linha, ou None se não houver nenhum."""
    with open(path, "rb") as f:
        line = f.readline().decode("latin-1", errors="ignore")
    counts = [(line.count(s), -i, s) for i, s in enumerate(_SEPARATORS)]
    best = max(counts)
    return best[2] if best[0] else None


def _detect_separator(path: Path) -> str:
    """Sniff CSV delimiter from the first line (defaulting to semicolon)."""
    try:
        return _first_line_separator(path) or ";"
    except Exception:
        return ";"


def _require_separator(path: Path) -> None:
    """Falha se a primeira linha não tem separador conhecido (não é CSV delimitado).

    Sem isso o DuckDB lê um TXT de largura fixa como tabela de uma coluna só e
    o lake recebe um Parquet sem sentido, sem nenhum erro.
    """
    if _first_line_separator(path) is None:
        raise LakeError(
            f"{path.name}: separador de colunas não detectado "
            "(não é CSV delimitado; largura fixa precisa de layout)"
        )


def _is_lock_or_checksum(path: Path) -> bool:
    """Lock file do Office (``~$X``) ou checksum ``md5_X`` ao lado do dado."""
    return path.name.startswith("~$") or path.name.lower().startswith("md5_")


def _fixed_width_frame(txt: Path, layout: SasLayout, workdir: Path) -> pl.LazyFrame:
    """TXT de largura fixa (latin-1) como LazyFrame com uma coluna por campo.

    O arquivo é regravado em UTF-8 por blocos (o Polars só lê latin-1 pelo
    modo com perda), depois lido como uma coluna de linhas inteiras e fatiado
    por campo; o ``sink_parquet`` da escrita processa em fluxo. Texto: sem
    espaços nas pontas, vazio vira nulo. Número: ``TRY_CAST`` (o que não for
    número, como o "." do SAS, vira nulo); com decimais ``w.d`` e sem ponto no
    campo, o valor é dividido por 10^d, como o informato do SAS.
    """
    utf8 = workdir / f"{abs(hash(txt))}.utf8"
    longest = 0
    with (
        open(txt, encoding="latin-1", newline="") as src,
        open(utf8, "w", encoding="utf-8", newline="") as dst,
    ):
        for line in src:
            longest = max(longest, len(line.rstrip("\r\n")))
            dst.write(line)
    lines = pl.scan_csv(
        utf8,
        has_header=False,
        separator="\x1f",
        quote_char=None,
        new_columns=["linha"],
        schema={"linha": pl.String},
    )
    exprs = []
    for f in layout.fields:
        if f.start > longest:
            # Além do fim das linhas: com MISSOVER o SAS lê como ausente.
            logger.warning(
                "%s: campo %s (posição %d) começa depois do fim das linhas "
                "(%d colunas); coluna nula",
                txt.name,
                f.name,
                f.start,
                longest,
            )
            dtype = (
                pl.String
                if not f.numeric
                else (pl.Int64 if f.decimals == 0 else pl.Float64)
            )
            exprs.append(pl.lit(None, dtype=dtype).alias(f.name))
            continue
        raw = pl.col("linha").str.slice(f.start - 1, f.width).str.strip_chars()
        if not f.numeric:
            expr = pl.when(raw.str.len_chars() > 0).then(raw)
        elif f.decimals == 0:
            expr = raw.cast(pl.Int64, strict=False)
        else:
            num = raw.cast(pl.Float64, strict=False)
            expr = (
                pl.when(raw.str.contains(".", literal=True))
                .then(num)
                .otherwise(num / 10**f.decimals)
            )
        exprs.append(expr.alias(f.name))
    return lines.select(exprs)


def _check_layout_fix(txt: Path, layout: SasLayout) -> None:
    """Confere nas 200 primeiras linhas a correção de layout aplicada ao script.

    Raises:
        ValueError: os dados não confirmam o deslocamento.
    """
    fix = layout.fix
    if fix is None:
        return
    lines: list[str] = []
    with open(txt, encoding="latin-1", newline="") as f:
        for line in f:
            if line.strip():
                lines.append(line.rstrip("\r\n"))
            if len(lines) >= 200:
                break
    if not lines:
        raise ValueError("correção de layout não validada: arquivo sem dados")
    by_name = {f.name: f for f in layout.fields}
    for name in fix.dotted:
        f = by_name[name]
        if not all("." in line[f.start - 1 : f.end] for line in lines):
            raise ValueError(
                f"correção de layout não validada: {name} sem ponto decimal"
            )
    for name, (low, high) in fix.ranges.items():
        f = by_name[name]
        for line in lines:
            raw = line[f.start - 1 : f.end].strip()
            if not raw.isdigit() or not low <= int(raw) <= high:
                raise ValueError(
                    f"correção de layout não validada: {name}={raw!r} "
                    f"fora de {low}-{high}"
                )


def _unique_member_names(members: list[Path], root: Path) -> dict[Path, str]:
    """Nome de cada TXT para o ``file_key``: o stem, ou o caminho se repetir.

    Dois TXT de mesmo nome em pastas diferentes não podem cair no mesmo
    arquivo do lake; nesse caso o nome inclui as pastas (``alunos_x``).
    """
    stems = [m.stem.lower() for m in members]
    names: dict[Path, str] = {}
    for m, stem in zip(members, stems, strict=True):
        if stems.count(stem) > 1:
            parts = list(m.relative_to(root).with_suffix("").parts)
            lower = [p.lower() for p in parts]
            if "dados" in lower:
                parts = parts[lower.index("dados") + 1 :]
            names[m] = "_".join(parts)
        else:
            names[m] = m.stem
    return names


def _convert_fixed_width(
    path: Path,
    root: Path,
    year: int | None,
    writer: LakeWriter,
    part_vals: dict[str, Any],
    result: ConvertResult,
) -> bool:
    """SAEB 1995-2005: TXT de largura fixa em ``DADOS/`` + scripts SAS de layout.

    ``root`` é a pasta onde o ZIP foi extraído. Devolve ``False`` quando o ZIP
    não tem esse formato (o chamador segue pelo caminho de CSV). Os ZIPs
    dentro de ``DADOS/`` (1999) são extraídos um nível. Cada TXT é pareado ao
    layout pelo nome do ``INFILE``; TXT sem layout, layout sem TXT e script
    inválido entram em ``result.errors`` sem derrubar os demais.
    """
    scripts = sorted(
        m
        for m in root.rglob("*")
        if m.is_file() and m.suffix.lower() == ".sas" and not m.name.startswith("~$")
    )
    if not scripts:
        return False

    def in_dados(m: Path) -> bool:
        return "dados" in {p.lower() for p in m.relative_to(root).parts[:-1]}

    for inner in sorted(root.rglob("*")):
        if inner.is_file() and inner.suffix.lower() == ".zip" and in_dados(inner):
            decompress_archive(inner, inner.parent / inner.stem)
    txts = sorted(
        m
        for m in root.rglob("*")
        if m.is_file()
        and m.suffix.lower() == ".txt"
        and in_dados(m)
        and not _is_lock_or_checksum(m)
        and not any(
            doc in _ascii_lower(m.relative_to(root).as_posix()) for doc in _DOC_PATTERNS
        )
    )
    if not txts:
        return False

    layouts: dict[str, list[tuple[Path, SasLayout]]] = {}
    broken: set[str] = set()
    for script in scripts:
        text = script.read_text(encoding="latin-1")
        fix = LAYOUT_FIXES.get((year, peek_infile(text) or "")) if year else None
        try:
            layout = parse_sas_input(text, fix)
        except ValueError as exc:
            result.errors.append(f"{path.name}: {script.name}: {exc}")
            name = peek_infile(text)
            if name:
                broken.add(name)
            continue
        layouts.setdefault(layout.infile, []).append((script, layout))

    names = _unique_member_names(txts, root)
    matched: set[str] = set()
    for txt in txts:
        name = txt.name.lower()
        cands = layouts.get(name, [])
        if not cands:
            if name not in broken:
                result.errors.append(f"{path.name}: {txt.name}: sem layout SAS")
            continue
        matched.add(name)
        if any(c[1].fields != cands[0][1].fields for c in cands):
            result.errors.append(
                f"{path.name}: {txt.name}: layouts SAS divergentes "
                f"({', '.join(c[0].name for c in cands)})"
            )
            continue
        layout = cands[0][1]
        try:
            _check_layout_fix(txt, layout)
            with tempfile.TemporaryDirectory() as work:
                written = writer.write_polars(
                    _fixed_width_frame(txt, layout, Path(work)),
                    path,
                    partitions=part_vals,
                    file_key_name=composite_file_key(path, names[txt]),
                    converter=f"inep-fetcher {__version__}",
                )
        except Exception as exc:
            first_line = (str(exc).strip().splitlines() or [repr(exc)])[0]
            result.errors.append(f"{path.name}: {txt.name}: {first_line}")
            continue
        if written.status == "skipped":
            result.skipped += 1
        else:
            result.converted += 1
    for name, cands in sorted(layouts.items()):
        if name not in matched:
            script = cands[0][0].name
            result.errors.append(
                f"{path.name}: {script}: arquivo de dados {name} não encontrado"
            )
    return True


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
                    _require_separator(path)
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
                    df = read_planilha(path)
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
                        if _convert_fixed_width(
                            path, Path(tmp), year, writer, part_vals, result
                        ):
                            continue
                        all_members = sorted(
                            m
                            for m in Path(tmp).rglob("*")
                            if m.is_file()
                            and m.suffix.lower() in {".csv", ".txt", ".xlsx", ".xls"}
                            # "~$X.xlsx": lock file do Office esquecido no ZIP;
                            # "md5_X.txt": checksum que o INEP põe ao lado do dado
                            and not m.name.startswith("~$")
                            and not m.name.lower().startswith("md5_")
                        )
                        # Filter out documentation and dictionary subpaths
                        data_members = [
                            m
                            for m in all_members
                            if not any(
                                doc in _ascii_lower(m.as_posix())
                                for doc in _DOC_PATTERNS
                            )
                        ]
                        # Com pasta DADOS/ (ENEM, SAEB, censos), o dado é só o
                        # que está nela: provas em texto (DOSVOX) e outros
                        # anexos ficam de fora.
                        em_dados = [
                            m
                            for m in data_members
                            if "dados"
                            in {p.lower() for p in m.relative_to(tmp).parts[:-1]}
                        ]
                        if em_dados:
                            data_members = em_dados
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
                            if member.suffix.lower() in {".xlsx", ".xls"}:
                                written = writer.write_polars(
                                    read_planilha(member),
                                    path,
                                    partitions=part_vals,
                                    file_key_name=key,
                                    converter=f"inep-fetcher {__version__}",
                                )
                                if written.status == "skipped":
                                    result.skipped += 1
                                else:
                                    result.converted += 1
                                continue
                            try:
                                _require_separator(member)
                            except LakeError as exc:
                                result.errors.append(f"{path.name}: {exc}")
                                continue
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
