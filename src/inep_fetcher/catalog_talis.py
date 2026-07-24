"""TALIS (Teaching and Learning International Survey) catalog.

Pesquisa internacional de docência, só 2 edições no Brasil. Path aninhado
em /microdados/talis/. Nomenclatura MUDOU completamente entre as edições —
não há padrão comum, cada URL é literal.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados/talis"

_talis_entries: list[DatasetEntry] = [
    DatasetEntry(
        id="talis-microdados-2018",
        base_id="talis-microdados",
        name="TALIS Microdados — 2018",
        url=f"{_BASE}/microdados_talis_2018.zip",
        ext="zip",
        group="talis",
        source=_SOURCE,
        year=2018,
        semester=None,
        month=None,
    ),
    DatasetEntry(
        id="talis-microdados-2024",
        base_id="talis-microdados",
        name="TALIS Microdados — 2024",
        url=f"{_BASE}/microdados_do_brasil_na_talis_2024_v2.zip",
        ext="zip",
        group="talis",
        source=_SOURCE,
        year=2024,
        semester=None,
        month=None,
    ),
]

GROUPS_TALIS: dict[str, GroupInfo] = {
    "talis": {
        "name": "TALIS (Teaching and Learning International Survey)",
        "entries": _talis_entries,
    },
}

GROUP_ALIASES_TALIS: dict[str, str] = {}
