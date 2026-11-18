"""O build do lake pula, sem ler o bruto, o que já está em dia."""

from __future__ import annotations

import builtins
import hashlib
import io
import json
import zipfile
from pathlib import Path
from typing import Any

import pytest
import xlsxwriter

import inep_fetcher.lake as lake_mod
from inep_fetcher.lake import converter

_ENEM = "enem"
_CENSO = "censo-escolar"
_AFD = "adequacao-formacao-docente"
_MAT = "media-alunos-por-turma"


def _sidecar(path: Path) -> None:
    """Sidecar de manifesto confiável: o sha256 vem dele, sem ler o bruto."""
    data = path.read_bytes()
    sidecar = path.with_name(path.name + ".manifest.json")
    sidecar.write_text(
        json.dumps(
            {"sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)}
        ),
        encoding="utf-8",
    )


def _xlsx(path: Path) -> None:
    wb = xlsxwriter.Workbook(str(path))
    ws = wb.add_worksheet()
    ws.write_row(0, 0, ["uf", "alunos"])
    ws.write_row(1, 0, ["SP", 10])
    ws.write_row(2, 0, ["RJ", 20])
    wb.close()


def _bruto(tmp_path: Path) -> Path:
    raw = tmp_path / "raw"
    enem = raw / _ENEM
    enem.mkdir(parents=True)
    csv = enem / "enem_2023@20240101.csv"
    csv.write_text("nu;sexo\n1;M\n2;F\n", encoding="latin-1")
    _sidecar(csv)

    censo = raw / _CENSO
    censo.mkdir()
    z = censo / "censo_escolar_2022@20230201.zip"
    with zipfile.ZipFile(z, "w") as zf:
        zf.writestr("DADOS/a_2022.csv", "co;no\n1;A\n2;B\n")
        zf.writestr("DADOS/b_2022.csv", "co;no\n3;C\n")
        zf.writestr("DICIONARIO/dicionario.csv", "col;desc\nco;codigo\n")
    _sidecar(z)

    afd = raw / "indicadores" / _AFD
    afd.mkdir(parents=True)
    x = afd / "afd_2022@20230501.xlsx"
    _xlsx(x)
    _sidecar(x)

    mat = raw / "indicadores" / _MAT
    mat.mkdir(parents=True)
    xz = mat / "media-alunos-por-turma-2011@20130613.zip"
    tmp_x = tmp_path / "ESTADOS 2011.xlsx"
    _xlsx(tmp_x)
    with zipfile.ZipFile(xz, "w") as zf:
        zf.write(tmp_x, "ESTADOS 2011.xlsx")
    _sidecar(xz)
    return raw


@pytest.fixture
def acessos(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Registra todo acesso ao bruto: abertura de ZIP, leitores e ``open``."""
    vistos: list[str] = []

    def espia(nome: str, original: Any) -> Any:
        def _f(*args: Any, **kwargs: Any) -> Any:
            vistos.append(nome)
            return original(*args, **kwargs)

        return _f

    monkeypatch.setattr(zipfile, "ZipFile", espia("ZipFile", zipfile.ZipFile))
    for nome in (
        "extract_archive",
        "read_planilha",
        "_require_separator",
        "_detect_separator",
        "clean_csv",
    ):
        monkeypatch.setattr(lake_mod, nome, espia(nome, getattr(lake_mod, nome)))

    original_open = builtins.open

    def aberto(file: Any, *args: Any, **kwargs: Any) -> Any:
        if "raw" in Path(str(file)).parts and not str(file).endswith(".manifest.json"):
            vistos.append(f"open:{file}")
        return original_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", aberto)
    monkeypatch.setattr(io, "open", aberto)
    return vistos


@pytest.mark.parametrize("dataset", [_ENEM, _CENSO, _AFD, _MAT])
def test_segunda_rodada_por_dataset_nao_le_o_bruto(
    tmp_path: Path, acessos: list[str], dataset: str
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake, datasets=[dataset])
    assert not res.errors
    primeira = (res.converted, res.skipped)
    assert res.skipped == 0 and res.converted == (2 if dataset == _CENSO else 1)
    assert acessos  # a primeira rodada lê o bruto

    acessos.clear()
    res2 = converter.convert(raw, lake, datasets=[dataset])
    assert not res2.errors
    assert (res2.converted, res2.skipped) == (0, primeira[0])
    assert acessos == []


def test_sem_datasets_continua_convertendo_e_pulando(
    tmp_path: Path, acessos: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped, res.errors) == (5, 0, [])
    acessos.clear()
    res2 = converter.convert(raw, lake)
    assert (res2.converted, res2.skipped, res2.errors) == (0, 5, [])
    assert acessos == []


def test_force_le_o_bruto_e_reconverte(tmp_path: Path, acessos: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[_CENSO])
    acessos.clear()
    res = converter.convert(raw, lake, datasets=[_CENSO], force=True)
    assert (res.converted, res.skipped) == (2, 0)
    assert "ZipFile" in acessos or "extract_archive" in acessos


def test_bruto_novo_converte_e_o_antigo_nao_e_lido(
    tmp_path: Path, acessos: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[_ENEM])
    novo = raw / _ENEM / "enem_2024@20250101.csv"
    novo.write_text("nu;sexo\n9;M\n", encoding="latin-1")
    _sidecar(novo)

    acessos.clear()
    res = converter.convert(raw, lake, datasets=[_ENEM])
    assert (res.converted, res.skipped, res.errors) == (1, 1, [])
    # só o CSV novo foi lido
    assert all("enem_2023" not in a for a in acessos)
    assert any("enem_2024" in a or a == "_require_separator" for a in acessos)


def test_zip_alterado_reconverte(tmp_path: Path, acessos: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[_CENSO])
    z = raw / _CENSO / "censo_escolar_2022@20230201.zip"
    with zipfile.ZipFile(z, "w") as zf:
        zf.writestr("DADOS/a_2022.csv", "co;no\n1;A\n2;B\n3;Z\n")
        zf.writestr("DADOS/b_2022.csv", "co;no\n3;C\n")
    _sidecar(z)

    acessos.clear()
    res = converter.convert(raw, lake, datasets=[_CENSO])
    assert (res.converted, res.skipped, res.errors) == (2, 0, [])
    assert acessos
