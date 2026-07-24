"""ENEM por Escola catalog.

Um único arquivo agregado cobrindo o período 2005-2015 (confirmado: não
existem arquivos por ano individual — todo ano testado fora desse arquivo
combinado deu HTTP 404). Path aninhado, diferente do resto do catálogo.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

_enem_por_escola_entries: list[DatasetEntry] = [
    DatasetEntry(
        id="enem-por-escola-2005-2015",
        base_id="enem-por-escola",
        name="ENEM por Escola — 2005 a 2015 (agregado)",
        url="https://download.inep.gov.br/microdados/enem_por_escola/2005_a_2015/microdados_enem_por_escola.zip",
        ext="zip",
        group="enem_por_escola",
        source=_SOURCE,
        year=None,
        semester=None,
        month=None,
    ),
]

GROUPS_ENEM_POR_ESCOLA: dict[str, GroupInfo] = {
    "enem_por_escola": {
        "name": "ENEM por Escola",
        "entries": _enem_por_escola_entries,
    },
}

GROUP_ALIASES_ENEM_POR_ESCOLA: dict[str, str] = {}
