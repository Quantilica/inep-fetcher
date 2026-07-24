"""File location management for inep-fetcher.

Filenames follow the ecosystem convention:
    {base_id}@{YYYYMMDD}.{ext}          — sem ano definido (ex. enem_por_escola)
    {base_id}_{year}@{YYYYMMDD}.{ext}   — anuais (maioria dos datasets do INEP)
"""

import datetime as dt
from pathlib import Path

from quantilica.core.storage import (
    BaseDataRepository,
    build_stamped_filename,
    stamp_filename,
)

# Import de ._catalog_base (não de .catalog) para evitar dependência de
# ordem de import: outros módulos ainda estão construindo .catalog em
# paralelo, e este arquivo só precisa do tipo DatasetEntry para tipar.
from ._catalog_base import DatasetEntry

_GROUP_DIRS: dict[str, str] = {
    "enem": "enem",
    "censo_escolar": "censo-escolar",
    "censo_educacao_superior": "censo-educacao-superior",
    "saeb": "saeb",
    "enade": "enade",
    "ana": "ana",
    "encceja": "encceja",
    "censo_magisterio": "censo-magisterio",
    "enade_licenciaturas": "enade-licenciaturas",
    "enamed": "enamed",
    "pnd": "pnd",
    "pnera": "pnera",
    "pesquisa_discriminacao": "pesquisa-discriminacao",
    "idd": "idd",
    "enem_por_escola": "enem-por-escola",
    "talis": "talis",
}


class DataRepository(BaseDataRepository):
    """Manages local storage for inep-fetcher files."""

    def __init__(self, root: Path | str):
        super().__init__(root)

    def path_for_entry(
        self,
        entry: DatasetEntry,
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Compute the local path for a dataset entry."""
        group_dir = _GROUP_DIRS[entry["group"]]
        ext = entry["ext"]
        base_id = entry["base_id"]
        year = entry["year"]
        month = entry["month"]

        if year is None:
            filename = stamp_filename(base_id, ext, last_modified)
        elif month is not None:
            partition = f"{year}-{month:02d}"
            filename = build_stamped_filename(
                base_id, partition, ext=ext, timestamp=last_modified
            )
        else:
            filename = build_stamped_filename(
                base_id, year, ext=ext, timestamp=last_modified
            )

        return self.storage.path_for(f"{group_dir}/{filename}")
