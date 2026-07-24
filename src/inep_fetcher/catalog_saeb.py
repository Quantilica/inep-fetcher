"""SAEB (Sistema de Avaliação da Educação Básica) catalog.

Nomenclatura irregular confirmada via curl — NÃO é gerável por range()/fórmula:
maiúsculas em 2007/2009, sufixo _RECALCULADO, prefixo diferente em 1995-2001,
e arquivos duplos (educação infantil + fundamental/médio) em 2021 e 2023.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "inep-microdados"
_BASE = "https://download.inep.gov.br/microdados"


def _entry(id_: str, base_id: str, name: str, url: str, year: int) -> DatasetEntry:
    return DatasetEntry(
        id=id_,
        base_id=base_id,
        name=name,
        url=url,
        ext="zip",
        group="saeb",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


_saeb_entries: list[DatasetEntry] = [
    # 1995/1997/1999/2001: prefixo "micro_saeb" sem underscore antes do ano
    *[
        _entry(
            f"saeb-microdados-{y}",
            "saeb-microdados",
            f"SAEB Microdados — {y}",
            f"{_BASE}/micro_saeb{y}.zip",
            y,
        )
        for y in (1995, 1997, 1999, 2001)
    ],
    # padrão normal
    *[
        _entry(
            f"saeb-microdados-{y}",
            "saeb-microdados",
            f"SAEB Microdados — {y}",
            f"{_BASE}/microdados_saeb_{y}.zip",
            y,
        )
        for y in (2003, 2005, 2011, 2013, 2015, 2017, 2019)
    ],
    # 2007/2009: maiúsculas + _RECALCULADO
    *[
        _entry(
            f"saeb-microdados-{y}",
            "saeb-microdados",
            f"SAEB Microdados — {y}",
            f"{_BASE}/MICRODADOS_SAEB_{y}_RECALCULADO.zip",
            y,
        )
        for y in (2007, 2009)
    ],
    # 2021: dois arquivos
    _entry(
        "saeb-microdados-2021-infantil",
        "saeb-microdados-infantil",
        "SAEB Microdados — 2021 (Educação Infantil)",
        f"{_BASE}/microdados_saeb_2021_educacao_infantil.zip",
        2021,
    ),
    _entry(
        "saeb-microdados-2021-fund-medio",
        "saeb-microdados-fund-medio",
        "SAEB Microdados — 2021 (Fundamental e Médio)",
        f"{_BASE}/microdados_saeb_2021_ensino_fundamental_e_medio.zip",
        2021,
    ),
    # 2023: dois arquivos
    _entry(
        "saeb-microdados-2023-infantil",
        "saeb-microdados-infantil",
        "SAEB Microdados — 2023 (Educação Infantil)",
        f"{_BASE}/microdados_saeb_2023_educacao_infantil.zip",
        2023,
    ),
    _entry(
        "saeb-microdados-2023-fund-medio",
        "saeb-microdados-fund-medio",
        "SAEB Microdados — 2023 (Fundamental e Médio)",
        f"{_BASE}/microdados_saeb_2023.zip",
        2023,
    ),
]

GROUPS_SAEB: dict[str, GroupInfo] = {
    "saeb": {
        "name": "SAEB (Sistema de Avaliação da Educação Básica)",
        "entries": _saeb_entries,
    },
}

GROUP_ALIASES_SAEB: dict[str, str] = {}
