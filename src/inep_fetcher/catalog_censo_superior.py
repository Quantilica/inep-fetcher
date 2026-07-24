"""Censo da Educação Superior catalog.

Microdados anuais, publicados em download.inep.gov.br/microdados/. Padrão
de URL confirmado sem exceções para todo o intervalo 1995-2024.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados"


def _censo_superior_entry(year: int) -> DatasetEntry:
    return DatasetEntry(
        id=f"censo-educacao-superior-microdados-{year}",
        base_id="censo-educacao-superior-microdados",
        name=f"Censo da Educação Superior Microdados — {year}",
        url=f"{_BASE}/microdados_censo_da_educacao_superior_{year}.zip",
        ext="zip",
        group="censo_educacao_superior",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_censo_superior_entries: list[DatasetEntry] = [
    _censo_superior_entry(year) for year in range(1995, 2025)
]

GROUPS_CENSO_SUPERIOR: dict[str, GroupInfo] = {
    "censo_educacao_superior": {
        "name": "Censo da Educação Superior",
        "entries": _censo_superior_entries,
    },
}

GROUP_ALIASES_CENSO_SUPERIOR: dict[str, str] = {
    "censo-superior": "censo_educacao_superior",
}
