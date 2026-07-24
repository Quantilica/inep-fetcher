"""ENEM (Exame Nacional do Ensino Médio) catalog.

Microdados anuais do ENEM, publicados em download.inep.gov.br. Padrão de
URL confirmado sem exceções para todo o intervalo 1998-2025.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados"


def _enem_entry(year: int) -> DatasetEntry:
    return DatasetEntry(
        id=f"enem-microdados-{year}",
        base_id="enem-microdados",
        name=f"ENEM Microdados — {year}",
        url=f"{_BASE}/microdados_enem_{year}.zip",
        ext="zip",
        group="enem",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_enem_entries: list[DatasetEntry] = [_enem_entry(year) for year in range(1998, 2026)]

GROUPS_ENEM: dict[str, GroupInfo] = {
    "enem": {"name": "ENEM (Exame Nacional do Ensino Médio)", "entries": _enem_entries},
}

GROUP_ALIASES_ENEM: dict[str, str] = {}
