"""Avaliação Nacional da Alfabetização (ANA) catalog.

Levantamento único realizado em 2014 e 2016 pelo INEP, avaliando habilidades em
leitura, escrita e matemática de alunos do 3º ano do ensino fundamental.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_ANA: dict[str, GroupInfo] = {
    "ana": {
        "name": "Avaliação Nacional da Alfabetização",
        "entries": [
            DatasetEntry(
                id="ana-microdados-2014",
                base_id="ana-microdados",
                name="ANA 2014",
                url="https://download.inep.gov.br/microdados/microdados_ana_2014.zip",
                ext="zip",
                group="ana",
                source=_SOURCE,
                year=2014,
                semester=None,
                month=None,
            ),
            DatasetEntry(
                id="ana-microdados-2016",
                base_id="ana-microdados",
                name="ANA 2016",
                url="https://download.inep.gov.br/microdados/microdados_ana_2016.zip",
                ext="zip",
                group="ana",
                source=_SOURCE,
                year=2016,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_ANA: dict[str, str] = {}
