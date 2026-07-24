"""Censo Escolar (Educação Básica) catalog.

Microdados anuais do Censo Escolar, servidos em
download.inep.gov.br/dados_abertos/ (domínio diferente do ENEM, que usa
/microdados/). EXCEÇÃO confirmada: o arquivo de 2025 tem um underscore
extra antes da extensão (microdados_censo_escolar_2025_.zip).
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/dados_abertos"


def _censo_url(year: int) -> str:
    if year == 2025:
        return f"{_BASE}/microdados_censo_escolar_{year}_.zip"
    return f"{_BASE}/microdados_censo_escolar_{year}.zip"


def _censo_entry(year: int) -> DatasetEntry:
    return DatasetEntry(
        id=f"censo-escolar-microdados-{year}",
        base_id="censo-escolar-microdados",
        name=f"Censo Escolar Microdados — {year}",
        url=_censo_url(year),
        ext="zip",
        group="censo_escolar",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_censo_entries: list[DatasetEntry] = [_censo_entry(year) for year in range(1995, 2026)]

GROUPS_CENSO_ESCOLAR: dict[str, GroupInfo] = {
    "censo_escolar": {
        "name": "Censo Escolar (Educação Básica)",
        "entries": _censo_entries,
    },
}

GROUP_ALIASES_CENSO_ESCOLAR: dict[str, str] = {
    "censo": "censo_escolar",
}
