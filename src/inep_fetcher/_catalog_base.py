"""Shared types and helper constructors for INEP dataset catalogs."""

from typing import TypedDict


class DatasetEntry(TypedDict):
    id: str
    base_id: str
    name: str
    url: str
    ext: str  # "zip" | "rar" — ENADE 2022 is the only .rar entry in the catalog
    group: str
    source: str
    year: int | None
    semester: int | None  # N/A for INEP — always None
    month: int | None  # N/A for INEP — always None


class GroupInfo(TypedDict):
    name: str
    entries: list[DatasetEntry]


def _static(
    group: str,
    source: str,
    id_: str,
    name: str,
    url: str,
    ext: str,
    year: int | None = None,
) -> DatasetEntry:
    return DatasetEntry(
        id=id_,
        base_id=id_,
        name=name,
        url=url,
        ext=ext,
        group=group,
        source=source,
        year=year,
        semester=None,
        month=None,
    )
