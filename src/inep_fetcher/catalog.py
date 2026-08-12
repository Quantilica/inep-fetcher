"""INEP unified dataset catalog.

Aggregates all groups from all catalog modules — 16 grupos de microdados
do INEP, cobrindo desde os grandes exames anuais (ENEM, Censo Escolar) até
avaliações de edição única (Pnera, Censo do Magistério):

- catalog_enem:                  ENEM (1998-presente, anual, sem exceções)
- catalog_censo:                 Censo Escolar (1995-presente, 1 exceção em 2025)
- catalog_censo_superior:        Censo da Educação Superior (1995-2024, sem exceções)
- catalog_saeb:                  SAEB (1995-2023, bienal, nomenclatura irregular)
- catalog_enade:                 ENADE (2004-2023 sem 2020, sufixos LGPD, 2022=.rar)
- catalog_ana:                   Avaliação Nacional da Alfabetização (2014, 2016)
- catalog_encceja:               Encceja (2013-2025, com lacunas)
- catalog_censo_magisterio:      Censo dos Profissionais do Magistério (2003)
- catalog_enade_licenciaturas:   ENADE das Licenciaturas (2025)
- catalog_enamed:                Enamed / Formação Médica (2025)
- catalog_pnd:                   Prova Nacional Docente (2025)
- catalog_pnera:                 Pesquisa Nac. de Educação na Reforma Agrária (2004)
- catalog_pesquisa_discriminacao: Pesquisa de Ações Discriminatórias (2008)
- catalog_idd:                   Indicador de Diferença Desemp. Observado/Esperado
                                  (2021-2023)
- catalog_enem_por_escola:       ENEM por Escola (2005-2015, agregado em 1 arquivo)
- catalog_talis:                 TALIS (2018, 2024)
- catalog_indicadores:           18 Indicadores Educacionais derivados (não
                                  microdados brutos — ver docstring do módulo)

Public API is stable across future waves (mais grupos podem ser adicionados
sem quebrar esta interface).
"""

from ._catalog_base import DatasetEntry, GroupInfo
from .catalog_ana import GROUP_ALIASES_ANA, GROUPS_ANA
from .catalog_censo import GROUP_ALIASES_CENSO_ESCOLAR, GROUPS_CENSO_ESCOLAR
from .catalog_censo_magisterio import (
    GROUP_ALIASES_CENSO_MAGISTERIO,
    GROUPS_CENSO_MAGISTERIO,
)
from .catalog_censo_superior import GROUP_ALIASES_CENSO_SUPERIOR, GROUPS_CENSO_SUPERIOR
from .catalog_enade import GROUP_ALIASES_ENADE, GROUPS_ENADE
from .catalog_enade_licenciaturas import (
    GROUP_ALIASES_ENADE_LICENCIATURAS,
    GROUPS_ENADE_LICENCIATURAS,
)
from .catalog_enamed import GROUP_ALIASES_ENAMED, GROUPS_ENAMED
from .catalog_encceja import GROUP_ALIASES_ENCCEJA, GROUPS_ENCCEJA
from .catalog_enem import GROUP_ALIASES_ENEM, GROUPS_ENEM
from .catalog_enem_por_escola import (
    GROUP_ALIASES_ENEM_POR_ESCOLA,
    GROUPS_ENEM_POR_ESCOLA,
)
from .catalog_idd import GROUP_ALIASES_IDD, GROUPS_IDD
from .catalog_indicadores import (
    GROUP_ALIASES_INDICADORES,
    GROUPS_INDICADORES,
    INDICADORES_GROUP_KEYS,
)
from .catalog_pesquisa_discriminacao import (
    GROUP_ALIASES_PESQUISA_DISCRIMINACAO,
    GROUPS_PESQUISA_DISCRIMINACAO,
)
from .catalog_pnd import GROUP_ALIASES_PND, GROUPS_PND
from .catalog_pnera import GROUP_ALIASES_PNERA, GROUPS_PNERA
from .catalog_saeb import GROUP_ALIASES_SAEB, GROUPS_SAEB
from .catalog_talis import GROUP_ALIASES_TALIS, GROUPS_TALIS

__all__ = [
    "DatasetEntry",
    "GroupInfo",
    "GROUPS",
    "GROUP_ALIASES",
    "ALL_GROUP_KEYS",
    "INDICADORES_GROUP_KEYS",
    "resolve_group",
    "expand_group",
    "list_datasets",
]

GROUPS: dict[str, GroupInfo] = {
    **GROUPS_ENEM,
    **GROUPS_CENSO_ESCOLAR,
    **GROUPS_CENSO_SUPERIOR,
    **GROUPS_SAEB,
    **GROUPS_ENADE,
    **GROUPS_ANA,
    **GROUPS_ENCCEJA,
    **GROUPS_CENSO_MAGISTERIO,
    **GROUPS_ENADE_LICENCIATURAS,
    **GROUPS_ENAMED,
    **GROUPS_PND,
    **GROUPS_PNERA,
    **GROUPS_PESQUISA_DISCRIMINACAO,
    **GROUPS_IDD,
    **GROUPS_ENEM_POR_ESCOLA,
    **GROUPS_TALIS,
    **GROUPS_INDICADORES,
}

GROUP_ALIASES: dict[str, str] = {
    **GROUP_ALIASES_ENEM,
    **GROUP_ALIASES_CENSO_ESCOLAR,
    **GROUP_ALIASES_CENSO_SUPERIOR,
    **GROUP_ALIASES_SAEB,
    **GROUP_ALIASES_ENADE,
    **GROUP_ALIASES_ANA,
    **GROUP_ALIASES_ENCCEJA,
    **GROUP_ALIASES_CENSO_MAGISTERIO,
    **GROUP_ALIASES_ENADE_LICENCIATURAS,
    **GROUP_ALIASES_ENAMED,
    **GROUP_ALIASES_PND,
    **GROUP_ALIASES_PNERA,
    **GROUP_ALIASES_PESQUISA_DISCRIMINACAO,
    **GROUP_ALIASES_IDD,
    **GROUP_ALIASES_ENEM_POR_ESCOLA,
    **GROUP_ALIASES_TALIS,
    **GROUP_ALIASES_INDICADORES,
}

ALL_GROUP_KEYS: list[str] = list(GROUPS)

# Macro-alias que expande para os 18 grupos de indicadores educacionais de
# uma vez, no mesmo espírito do alias "aerodromos" do anac-fetcher.
_MACRO_GROUPS: dict[str, list[str]] = {
    "indicadores_educacionais": INDICADORES_GROUP_KEYS,
}


def resolve_group(key: str) -> str | None:
    """Resolve a group key or alias to a canonical group id.

    Does not resolve macro-aliases (see :func:`expand_group`), since those
    map to multiple groups.

    Args:
        key: The group key or alias to resolve.

    Returns:
        The canonical group id if found, otherwise None.
    """
    if key in GROUPS:
        return key
    return GROUP_ALIASES.get(key)


def expand_group(key: str) -> list[str]:
    """Expand a group key, alias, or macro-alias to canonical group id(s).

    "indicadores_educacionais" expands to all 18 indicator groups at once.

    Args:
        key: The group key, alias, or macro-alias to expand.

    Returns:
        A list of canonical group ids. Returns an empty list if the key is not recognized.
    """
    if key in _MACRO_GROUPS:
        return list(_MACRO_GROUPS[key])
    canon = resolve_group(key)
    return [canon] if canon is not None else []


def list_datasets(group: str | None = None) -> list[DatasetEntry]:
    """Return all dataset entries, optionally filtered by group.

    Args:
        group: Optional group key or alias to filter datasets by.

    Returns:
        A list of dataset entries matching the group, or all if no group is specified.

    Raises:
        ValueError: If a group is provided but not recognized.
    """
    if group is not None:
        canon = resolve_group(group)
        if canon is None:
            raise ValueError(f"Unknown group: {group!r}")
        return list(GROUPS[canon]["entries"])
    return [entry for info in GROUPS.values() for entry in info["entries"]]
