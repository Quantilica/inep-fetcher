"""ENADE (Exame Nacional de Desempenho dos Estudantes) catalog.

Nomenclatura irregular confirmada via curl: sufixo _LGPD aparece e some
entre edições, 2020 não existe (ENADE não aplicado — pandemia), e 2022 é
o único dataset .rar de todo o catálogo INEP (não .zip).
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados"


def _entry(year: int, url: str, ext: str = "zip") -> DatasetEntry:
    return DatasetEntry(
        id=f"enade-microdados-{year}",
        base_id="enade-microdados",
        name=f"ENADE Microdados — {year}",
        url=url,
        ext=ext,
        group="enade",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_enade_entries: list[DatasetEntry] = [
    *[_entry(y, f"{_BASE}/microdados_enade_{y}.zip") for y in range(2004, 2012)],
    *[_entry(y, f"{_BASE}/microdados_enade_{y}_LGPD.zip") for y in range(2012, 2020)],
    # 2020: não existe (ENADE não foi aplicado)
    _entry(2021, f"{_BASE}/microdados_enade_2021.zip"),
    _entry(2022, f"{_BASE}/microdados_enade_2022_LGPD.rar", ext="rar"),
    _entry(2023, f"{_BASE}/microdados_enade_2023.zip"),
]

GROUPS_ENADE: dict[str, GroupInfo] = {
    "enade": {
        "name": "ENADE (Exame Nacional de Desempenho dos Estudantes)",
        "entries": _enade_entries,
    },
}

GROUP_ALIASES_ENADE: dict[str, str] = {}
