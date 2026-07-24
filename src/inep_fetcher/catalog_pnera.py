"""Pesquisa Nacional de Educação na Reforma Agrária (PNERA) catalog.

Levantamento único realizado em 2004 pela SECADI/MEC em parceria com INEP,
mapeando educação em áreas de reforma agrária no Brasil.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_PNERA: dict[str, GroupInfo] = {
    "pnera": {
        "name": "Pesquisa Nacional de Educação na Reforma Agrária",
        "entries": [
            DatasetEntry(
                id="pnera-microdados-2004",
                base_id="pnera-microdados",
                name="PNERA 2004",
                url="https://download.inep.gov.br/microdados/microdados_pnera_2004.zip",
                ext="zip",
                group="pnera",
                source=_SOURCE,
                year=2004,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_PNERA: dict[str, str] = {}
