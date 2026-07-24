"""ENADE das Licenciaturas catalog.

Primeira edição do ENADE específico para programas de licenciaturas,
realizada em 2025 como programa novo de avaliação de cursos de formação docente.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_ENADE_LICENCIATURAS: dict[str, GroupInfo] = {
    "enade_licenciaturas": {
        "name": "ENADE das Licenciaturas",
        "entries": [
            DatasetEntry(
                id="enade-licenciaturas-microdados-2025",
                base_id="enade-licenciaturas-microdados",
                name="ENADE Licenciaturas 2025",
                url="https://download.inep.gov.br/microdados/microdados_enade_licenciaturas_2025.zip",
                ext="zip",
                group="enade_licenciaturas",
                source=_SOURCE,
                year=2025,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_ENADE_LICENCIATURAS: dict[str, str] = {
    "licenciaturas": "enade_licenciaturas"
}
