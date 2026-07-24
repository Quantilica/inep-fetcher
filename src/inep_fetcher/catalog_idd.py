"""Indicador de Diferença entre os Desempenhos Observado e Esperado (IDD) catalog.

Indicador que compara o desempenho observado dos alunos em avaliações nacionais
com o desempenho esperado para sua série, com edições em 2021, 2022 e 2023.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_IDD: dict[str, GroupInfo] = {
    "idd": {
        "name": "Indicador de Diferença entre os Desempenhos Observado e Esperado",
        "entries": [
            DatasetEntry(
                id="idd-microdados-2021",
                base_id="idd-microdados",
                name="IDD 2021",
                url="https://download.inep.gov.br/microdados/microdados_IDD_2021.zip",
                ext="zip",
                group="idd",
                source=_SOURCE,
                year=2021,
                semester=None,
                month=None,
            ),
            DatasetEntry(
                id="idd-microdados-2022",
                base_id="idd-microdados",
                name="IDD 2022",
                url="https://download.inep.gov.br/microdados/microdados_IDD_2022.zip",
                ext="zip",
                group="idd",
                source=_SOURCE,
                year=2022,
                semester=None,
                month=None,
            ),
            DatasetEntry(
                id="idd-microdados-2023",
                base_id="idd-microdados",
                name="IDD 2023",
                url="https://download.inep.gov.br/microdados/microdados_IDD_2023.zip",
                ext="zip",
                group="idd",
                source=_SOURCE,
                year=2023,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_IDD: dict[str, str] = {}
