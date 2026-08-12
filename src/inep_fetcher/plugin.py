"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

from quantilica.cli.sdk import FetcherApp

from . import catalog
from .catalog import GROUP_ALIASES, GROUPS, list_datasets
from .storage import DataRepository


def path_builder(
    output_dir: Path, entry: dict[str, Any], last_modified: dt.date | None
) -> Path:
    """Build the local storage path for a given dataset entry.

    Args:
        output_dir: The root directory for data storage.
        entry: The dataset entry metadata dictionary.
        last_modified: The last modified date of the dataset, if available.

    Returns:
        The computed local path for saving the dataset.
    """
    return DataRepository(output_dir).path_for_entry(entry, last_modified=last_modified)


aliases = {k: [v] for k, v in GROUP_ALIASES.items()}
if hasattr(catalog, "_MACRO_GROUPS"):
    aliases.update(catalog._MACRO_GROUPS)

fetcher = FetcherApp(
    name="inep-fetcher",
    help="Microdados abertos do INEP (educação).",
    groups_dict=GROUPS,
    aliases_dict=aliases,
    list_datasets=list_datasets,
    path_builder=path_builder,
)

app = fetcher.app
