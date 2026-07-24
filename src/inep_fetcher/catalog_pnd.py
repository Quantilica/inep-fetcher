"""Prova Nacional Docente (PND) catalog.

Primeira edição da Prova Nacional Docente realizada em 2025,
publicada em maio de 2026 como programa novo de avaliação de docentes.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_PND: dict[str, GroupInfo] = {
    "pnd": {
        "name": "Prova Nacional Docente",
        "entries": [
            DatasetEntry(
                id="pnd-microdados-2025",
                base_id="pnd-microdados",
                name="PND 2025",
                url="https://download.inep.gov.br/microdados/microdados_pnd_2025.zip",
                ext="zip",
                group="pnd",
                source=_SOURCE,
                year=2025,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_PND: dict[str, str] = {"docente": "pnd"}
