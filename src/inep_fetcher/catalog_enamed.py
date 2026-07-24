"""Exame Nacional de Avaliação da Formação Médica (ENAMED) catalog.

Primeira edição do ENAMED realizada em 2025, programa novo de avaliação
de cursos de medicina e formação de profissionais da saúde.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_ENAMED: dict[str, GroupInfo] = {
    "enamed": {
        "name": "Exame Nacional de Avaliação da Formação Médica",
        "entries": [
            DatasetEntry(
                id="enamed-microdados-2025",
                base_id="enamed-microdados",
                name="ENAMED 2025",
                url="https://download.inep.gov.br/microdados/microdados_enamed_2025.zip",
                ext="zip",
                group="enamed",
                source=_SOURCE,
                year=2025,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_ENAMED: dict[str, str] = {}
