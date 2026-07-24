"""Pesquisa de Ações Discriminatórias no Âmbito Escolar catalog.

Levantamento único realizado em 2008 sobre ações discriminatórias
em instituições de educação básica no Brasil.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"

GROUPS_PESQUISA_DISCRIMINACAO: dict[str, GroupInfo] = {
    "pesquisa_discriminacao": {
        "name": "Pesquisa de Ações Discriminatórias no Âmbito Escolar",
        "entries": [
            DatasetEntry(
                id="pesquisa-discriminacao-microdados-2008",
                base_id="pesquisa-discriminacao-microdados",
                name="Pesquisa Ações Discriminatórias 2008",
                url="https://download.inep.gov.br/microdados/microdados_pesquisa_acoes_discriminatorias_ambito_escolar_2008.zip",
                ext="zip",
                group="pesquisa_discriminacao",
                source=_SOURCE,
                year=2008,
                semester=None,
                month=None,
            ),
        ],
    },
}

GROUP_ALIASES_PESQUISA_DISCRIMINACAO: dict[str, str] = {
    "discriminacao": "pesquisa_discriminacao"
}
