"""Censo dos Profissionais do Magistério catalog.

Levantamento único realizado em 2003 que mapeou os profissionais do magistério
em instituições de educação básica no Brasil.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_CENSO_MAGISTERIO: dict[str, GroupInfo] = {
    "censo_magisterio": {
        "name": "Censo dos Profissionais do Magistério",
        "entries": [
            DatasetEntry(
                id="censo-magisterio-microdados-2003",
                base_id="censo-magisterio-microdados",
                name="Censo dos Profissionais do Magistério 2003",
                url="https://download.inep.gov.br/microdados/microdados_censo_profissionais_do_magisterio_2003.zip",
                ext="zip",
                group="censo_magisterio",
                source=_SOURCE,
                year=2003,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_CENSO_MAGISTERIO: dict[str, str] = {"magisterio": "censo_magisterio"}
