"""Tests for inep_fetcher.download."""

import ssl
from pathlib import Path
from unittest.mock import patch

import pytest

from inep_fetcher.catalog import list_datasets
from inep_fetcher.download import (
    DownloadError,
    client,
    download_all,
    download_entry,
    download_group,
)
from inep_fetcher.storage import DataRepository


def test_client_uses_custom_ssl_context_not_plain_verify_true():
    """Regressão: download.inep.gov.br não envia a CA intermediária no
    handshake TLS — o client precisa de um ssl.SSLContext customizado
    (bundle certifi + CA da RNP/ICPEdu), não apenas verify=True/certifi puro."""
    assert isinstance(client.verify, ssl.SSLContext)


def test_download_entry_dry_run(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("pnera")[0]

    with patch("inep_fetcher.download._safe_head_date", return_value=None):
        path = download_entry(entry, repo, dry_run=True)

    assert isinstance(path, Path)
    assert not path.exists()


def test_download_entry_calls_download_with_manifest(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("pnera")[0]
    fake_path = tmp_path / "pnera" / "pnera-microdados-2004.zip"

    with (
        patch("inep_fetcher.download._safe_head_date", return_value=None),
        patch(
            "inep_fetcher.download.client.download_with_manifest",
            return_value=fake_path,
        ) as mock_dl,
    ):
        download_entry(entry, repo)

    mock_dl.assert_called_once()
    call_kwargs = mock_dl.call_args
    assert call_kwargs.args[0] == entry["url"]
    assert call_kwargs.kwargs["source_id"] == "inep"
    assert call_kwargs.kwargs["producer"] == "inep-fetcher"


def test_download_all_dry_run_returns_paths(tmp_path):
    with patch("inep_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["pnera"], dry_run=True)

    entries = list_datasets("pnera")
    assert len(paths) == len(entries)
    for path in paths:
        assert not path.exists()


def test_download_all_unknown_group_raises(tmp_path):
    with pytest.raises(ValueError, match="Unknown group"):
        download_all(tmp_path, groups=["nonexistent"])


def test_download_group_unknown_group_raises(tmp_path):
    with pytest.raises(ValueError, match="Unknown group"):
        download_group("nonexistent", tmp_path)


def test_download_all_alias_accepted(tmp_path):
    """Group aliases (e.g., 'censo') should work in download_all."""
    with patch("inep_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["censo"], dry_run=True)

    assert len(paths) == len(list_datasets("censo_escolar"))


def test_download_group_continues_after_entry_failure(tmp_path):
    """A failing entry must not abort the rest of the group (SAEB tem 17
    entradas com múltiplos arquivos por ano — uma falha isolada não pode
    travar o grupo inteiro)."""
    entries = list_datasets("saeb")
    assert len(entries) == 17
    call_count = 0

    def fake_download(url, output, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            raise RuntimeError("boom")
        return output

    errors: list[DownloadError] = []
    with (
        patch("inep_fetcher.download._safe_head_date", return_value=None),
        patch(
            "inep_fetcher.download.client.download_with_manifest",
            side_effect=fake_download,
        ),
    ):
        paths = download_group("saeb", tmp_path, errors=errors)

    assert len(paths) == 16
    assert len(errors) == 1
    assert errors[0][0]["id"] == entries[0]["id"]
    assert isinstance(errors[0][1], RuntimeError)


def test_download_all_continues_after_group_failure(tmp_path):
    """A group where every entry fails must not stop subsequent groups."""
    with (
        patch("inep_fetcher.download._safe_head_date", return_value=None),
        patch(
            "inep_fetcher.download.client.download_with_manifest",
            side_effect=RuntimeError("boom"),
        ),
    ):
        errors: list[DownloadError] = []
        paths = download_all(tmp_path, groups=["pnera", "pnd"], errors=errors)

    assert paths == []
    assert len(errors) == len(list_datasets("pnera")) + len(list_datasets("pnd"))


def test_download_group_without_errors_list_does_not_raise(tmp_path):
    with (
        patch("inep_fetcher.download._safe_head_date", return_value=None),
        patch(
            "inep_fetcher.download.client.download_with_manifest",
            side_effect=RuntimeError("boom"),
        ),
    ):
        paths = download_group("pnera", tmp_path)

    assert paths == []


def test_download_all_default_covers_all_34_groups(tmp_path):
    with patch("inep_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, dry_run=True)

    assert len(paths) == len(list_datasets())
    assert len(paths) == 796


def test_download_all_indicadores_macro_alias(tmp_path):
    """O macro-alias 'indicadores_educacionais' deve funcionar em download_all,
    igual ao 'aerodromos' do anac-fetcher."""
    with patch("inep_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(
            tmp_path, groups=["indicadores_educacionais"], dry_run=True
        )

    assert len(paths) == 647
