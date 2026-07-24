"""Tests for inep_fetcher.storage."""

import datetime as dt

from inep_fetcher.catalog import GROUPS, list_datasets
from inep_fetcher.storage import _GROUP_DIRS, DataRepository


def test_group_dirs_cover_all_groups():
    assert set(_GROUP_DIRS) == set(GROUPS)


def test_path_for_annual_entry(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(e for e in list_datasets("enem") if e["year"] == 2023)
    date = dt.date(2026, 7, 24)
    path = repo.path_for_entry(entry, last_modified=date)
    assert path.parent.name == "enem"
    assert "enem-microdados_2023@20260724" in path.name
    assert path.suffix == ".zip"


def test_path_for_static_entry_without_year(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("enem_por_escola")[0]
    assert entry["year"] is None
    path = repo.path_for_entry(entry)
    assert path.parent.name == "enem-por-escola"
    assert path.name.startswith("enem-por-escola")


def test_path_for_rar_extension(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(e for e in list_datasets("enade") if e["year"] == 2022)
    assert entry["ext"] == "rar"
    path = repo.path_for_entry(entry)
    assert path.suffix == ".rar"


def test_path_for_single_edition_group(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("pnera")[0]
    path = repo.path_for_entry(entry)
    assert path.parent.name == "pnera"


def test_paths_are_absolute(tmp_path):
    repo = DataRepository(tmp_path)
    for entry in list_datasets("idd"):
        path = repo.path_for_entry(entry)
        assert path.is_absolute()


def test_different_entries_produce_different_paths(tmp_path):
    repo = DataRepository(tmp_path)
    entries = list_datasets("saeb")
    date = dt.date(2026, 6, 1)
    paths = [repo.path_for_entry(e, last_modified=date) for e in entries]
    assert len(paths) == len(set(paths)), "Duplicate paths in saeb group"


def test_saeb_duplicate_year_entries_produce_different_paths(tmp_path):
    """SAEB 2021 e 2023 têm 2 entradas cada (infantil vs fund/médio) — os
    paths devem divergir mesmo com o mesmo ano."""
    repo = DataRepository(tmp_path)
    entries_2023 = [e for e in list_datasets("saeb") if e["year"] == 2023]
    assert len(entries_2023) == 2
    paths = [repo.path_for_entry(e) for e in entries_2023]
    assert paths[0] != paths[1]
