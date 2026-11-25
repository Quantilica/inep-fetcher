"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path
from typing import Any

from quantilica.cli.sdk import FetcherApp
from quantilica.core.exceptions import CorruptPayloadError
from quantilica.core.files import check_payload
from quantilica.core.registry import FetcherInfo
from quantilica.core.storage import expected_format_for_path, validate_payload_signature
from quantilica.core.sync import FreshnessPolicy

from . import catalog
from .catalog import GROUP_ALIASES, GROUPS, list_datasets
from .integridade import (
    baixou,
    caminho_de_preparo,
    eh_rar,
    extensao_de,
    limpar_preparo,
    preparar,
    promover,
    validar_corpo,
)
from .storage import DataRepository

logger = logging.getLogger(__name__)


def path_builder(
    output_dir: Path, entry: dict[str, Any], last_modified: dt.date | None
) -> Path:
    """Build the local storage path for a given dataset entry.

    Args:
        output_dir: The root directory for data storage.
        entry: The dataset entry metadata dictionary.
        last_modified: The last modified date of the dataset, if available.

    Returns:
        The computed local path for saving the dataset.
    """
    return DataRepository(output_dir).path_for_entry(entry, last_modified=last_modified)


class InepFetcherApp(FetcherApp):
    """FetcherApp que recusa corpo que não é o arquivo esperado.

    O servidor do INEP devolve HTTP 200 com uma página HTML quando o firewall
    bloqueia o cliente, e o IDD 2022 é um RAR5 com extensão ``.zip``. O core valida
    pela extensão do destino (não conhece ``.rar`` e recusaria o RAR5 como ZIP),
    então o download vai para um arquivo de preparo de extensão neutra, ao lado do
    destino, e só substitui o destino depois de conferido (assinatura, tamanho
    mínimo, integridade do ZIP). Em recusa o preparo é apagado, o erro vai para a
    lista de falhas da execução e o destino (e o sidecar dele), se existia, segue
    intacto como a versão atual.
    """

    def _download_file(
        self,
        url: str,
        output: Path,
        progress: Any = None,
        *,
        expected_format: str | None = None,
        **kwargs: Any,
    ) -> Path:
        ext = extensao_de(output)
        fmt = (
            expected_format
            if expected_format is not None
            else expected_format_for_path(output.name)
        )
        preparo = caminho_de_preparo(output)
        preparar(output, preparo)
        try:
            # ``expected_format=""``: o core não valida o preparo; vale o abaixo.
            super()._download_file(url, preparo, progress, expected_format="", **kwargs)
            if not baixou(output, preparo):
                # Fresco, ou modo efêmero (só o sidecar): nada novo a conferir.
                if output.exists():
                    try:
                        validar_corpo(output, ext)
                    except CorruptPayloadError as exc:
                        # Arquivo que já estava lá (acervo): nunca é apagado aqui.
                        logger.warning(
                            "arquivo existente com conteúdo suspeito: %s", exc
                        )
                return output
            try:
                _conferir(preparo, output.name, ext, fmt)
            except CorruptPayloadError as exc:
                raise CorruptPayloadError(
                    f"download recusado, versão anterior mantida: {exc}"
                ) from exc  # a mensagem já traz o nome do arquivo
            promover(preparo, output)
            return output
        finally:
            limpar_preparo(preparo)


def _conferir(preparo: Path, nome: str, ext: str, fmt: str | None) -> None:
    """Confere o corpo baixado antes de ele substituir o destino ``nome``."""
    validar_corpo(preparo, ext, nome)
    if ext == "zip" and eh_rar(preparo):
        return  # RAR com extensão .zip (IDD 2022): sem teste de ZIP
    if fmt:
        validate_payload_signature(preparo, fmt)  # type: ignore[arg-type]
    check_payload(preparo, nome, allow_header_only=True)


aliases = {k: [v] for k, v in GROUP_ALIASES.items()}
if hasattr(catalog, "_MACRO_GROUPS"):
    aliases.update(catalog._MACRO_GROUPS)

fetcher = InepFetcherApp(
    name="inep-fetcher",
    help="Microdados abertos do INEP (educação).",
    info=FetcherInfo(
        id="inep",
        nome="INEP - Microdados da Educação",
        orgao=(
            "Instituto Nacional de Estudos e Pesquisas Educacionais "
            "Anísio Teixeira (INEP)"
        ),
        licenca=(
            "Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) "
            "e Decreto 8.777/2016"
        ),
        homepage="https://www.gov.br/inep/",
        cadencia="yearly",
        dominio="educacao",
    ),
    groups_dict=GROUPS,
    aliases_dict=aliases,
    list_datasets=list_datasets,
    path_builder=path_builder,
    default_output=Path("/data/inep"),
    freshness_policy=FreshnessPolicy.HEAD_FALLBACK_GET,
)


def convert(
    input_dir: Path,
    lake_dir: Path,
    *,
    dataset: list[str] | None = None,
    force: bool = False,
) -> Any:
    """Converte arquivos brutos do INEP para o lake Hive (Parquet)."""
    try:
        from inep_fetcher import lake
    except ImportError as exc:
        raise ImportError(
            "Conversão para o lake requer o extra 'analysis'. "
            "Instale com: quantilica install inep --extra analysis"
        ) from exc

    return lake.converter.convert(input_dir, lake_dir, datasets=dataset, force=force)


fetcher.command_convert(convert)
fetcher.command_pipeline(convert)

app = fetcher.app
