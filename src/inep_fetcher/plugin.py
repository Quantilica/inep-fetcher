"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path
from typing import Any

from quantilica.cli.sdk import FetcherApp
from quantilica.core.exceptions import CorruptPayloadError
from quantilica.core.registry import FetcherInfo
from quantilica.core.storage import expected_format_for_path
from quantilica.core.sync import FreshnessPolicy

from . import catalog
from .catalog import GROUP_ALIASES, GROUPS, list_datasets
from .integridade import (
    ASSINATURAS,
    descartar_versao_nova,
    extensao_de,
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
    bloqueia o cliente. O core valida a assinatura antes de confirmar o download,
    mas não conhece ``.rar``; aqui o formato é repassado ao core (rejeição de
    HTML/WAF no ``.tmp``) e, depois, a versão recém-criada é conferida (assinatura,
    tamanho mínimo). Em recusa a versão nova não fica no disco, o erro vai para a
    lista de falhas da execução e a versão anterior segue como a atual.
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
        if (
            expected_format is None
            and ext in ASSINATURAS
            and expected_format_for_path(output.name) is None
        ):
            expected_format = ext  # o core ainda não tem tabela para esta extensão
        existia = output.exists()
        try:
            resultado = super()._download_file(
                url, output, progress, expected_format=expected_format, **kwargs
            )
        except CorruptPayloadError as exc:
            # Recusado pelo core antes de confirmar o download: nada foi gravado.
            raise CorruptPayloadError(
                f"{output.name}: download recusado, versão anterior mantida: {exc}"
            ) from exc
        resultado = Path(resultado)
        if not resultado.exists():
            return resultado  # modo efêmero: só o sidecar ficou, nada novo a conferir
        try:
            validar_corpo(resultado, ext)
        except CorruptPayloadError as exc:
            if existia or resultado != output:
                # Arquivo que já estava lá (acervo): nunca é apagado aqui.
                logger.warning("arquivo existente com conteúdo suspeito: %s", exc)
                return resultado
            descartar_versao_nova(resultado)
            raise CorruptPayloadError(
                f"download recusado, versão anterior mantida: {exc}"
            ) from exc  # a mensagem do validar_corpo já traz o nome do arquivo
        return resultado


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
