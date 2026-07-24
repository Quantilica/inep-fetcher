"""Encceja (Exame Nacional para Certificação de Competências de Jovens e
Adultos) catalog.

Padrão de nome uniforme, mas os anos NÃO são um intervalo contínuo —
2015, 2016 e 2021 confirmados sem dataset (HTTP 404). Use a tupla literal
de anos, não range().
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados"

_ENCCEJA_YEARS = (2013, 2014, 2017, 2018, 2019, 2020, 2022, 2023, 2024, 2025)


def _encceja_entry(year: int) -> DatasetEntry:
    return DatasetEntry(
        id=f"encceja-microdados-{year}",
        base_id="encceja-microdados",
        name=f"Encceja Microdados — {year}",
        url=f"{_BASE}/microdados_encceja_{year}.zip",
        ext="zip",
        group="encceja",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_encceja_entries: list[DatasetEntry] = [_encceja_entry(y) for y in _ENCCEJA_YEARS]

GROUPS_ENCCEJA: dict[str, GroupInfo] = {
    "encceja": {
        "name": "Encceja (Certificação de Competências)",
        "entries": _encceja_entries,
    },
}

GROUP_ALIASES_ENCCEJA: dict[str, str] = {}
