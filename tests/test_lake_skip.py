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
from quantilica.core import manifests

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

    original_path_open = Path.open

    def path_open(self: Path, *args: Any, **kwargs: Any) -> Any:
        if "raw" in self.parts and not self.name.endswith(".manifest.json"):
            vistos.append(f"Path.open:{self}")
        return original_path_open(self, *args, **kwargs)

    monkeypatch.setattr(Path, "open", path_open)
    # O sha256 vem do sidecar: calcular o hash lendo o bruto é acesso ao bruto.
    monkeypatch.setattr(
        manifests, "sha256_file", espia("sha256_file", manifests.sha256_file)
    )
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


_SAEB = Path(__file__).parent / "fixtures" / "saeb"


def _saeb_zip(raw: Path, *, com_sobra: bool = False) -> Path:
    pasta = raw / "saeb"
    pasta.mkdir(parents=True, exist_ok=True)
    z = pasta / "saeb-microdados_2005@20240101.zip"
    with zipfile.ZipFile(z, "w") as zf:
        for nome, destino in (
            ("IMPUT_SAS_MATEMATICA_03ANO.sas", "INPUTS_SAS_SPSS/A/IMPUT_MAT.sas"),
            ("MATEMATICA_03ANO_05.TXT", "DADOS/ALUNOS/MATEMATICA_03ANO.TXT"),
            ("INPUT_SAS_ESCOLA_05.sas", "INPUTS_SAS_SPSS/E/INPUT_ESCOLA.sas"),
            ("ESCOLA_05.TXT", "DADOS/ESCOLA/ESCOLA_05.TXT"),
        ):
            zf.writestr(destino, (_SAEB / nome).read_bytes())
        if com_sobra:
            zf.writestr("DADOS/ALUNOS/SOBRA.TXT", b"1234\r\n")
    _sidecar(z)
    return z


def _falha_gravando(monkeypatch: pytest.MonkeyPatch, trecho: str) -> None:
    """Faz falhar a gravação da saída cuja chave contém ``trecho``."""
    for nome in ("write_polars", "write_duckdb"):
        original = getattr(lake_mod.LakeWriter, nome)

        def falha(self: Any, *args: Any, _o: Any = original, **kwargs: Any) -> Any:
            if trecho in (kwargs.get("file_key_name") or "").lower():
                raise RuntimeError(f"falha simulada em {trecho}")
            return _o(self, *args, **kwargs)

        monkeypatch.setattr(lake_mod.LakeWriter, nome, falha)


def _parquets(lake: Path, dataset: str) -> int:
    return len(list((lake / "inep" / dataset).rglob("*.parquet")))


def test_zip_interrompido_num_membro_e_completado_na_rodada_seguinte(
    tmp_path: Path, acessos: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    with monkeypatch.context() as m:
        _falha_gravando(m, "b_2022")  # a_2022 grava, b_2022 falha
        res = converter.convert(raw, lake, datasets=[_CENSO])
    assert (res.converted, res.skipped) == (1, 0)
    assert len(res.errors) == 1 and "falha simulada" in res.errors[0]
    assert _parquets(lake, _CENSO) == 1

    acessos.clear()
    res2 = converter.convert(raw, lake, datasets=[_CENSO])
    assert (res2.converted, res2.skipped, res2.errors) == (1, 1, [])
    assert acessos  # o ZIP foi reaberto

    acessos.clear()
    res3 = converter.convert(raw, lake, datasets=[_CENSO])
    assert (res3.converted, res3.skipped, res3.errors) == (0, 2, [])
    assert acessos == []


def test_membro_sem_separador_segue_dando_erro_a_cada_build(
    tmp_path: Path, acessos: list[str]
) -> None:
    """O membro que não é CSV não grava saída: o ZIP nunca fica em dia."""
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    z = raw / _CENSO / "censo_escolar_2022@20230201.zip"
    with zipfile.ZipFile(z, "a") as zf:
        zf.writestr("DADOS/c_2022.csv", "umacolunasó\nx\n")
    _sidecar(z)

    for rodada in range(3):
        acessos.clear()
        res = converter.convert(raw, lake, datasets=[_CENSO])
        assert (res.converted, res.skipped) == ((2, 0) if rodada == 0 else (0, 2))
        assert len(res.errors) == 1 and "separador" in res.errors[0]
        assert acessos  # reaberto
    assert _parquets(lake, _CENSO) == 2


def test_saeb_erros_por_membro_seguem_a_cada_build(
    tmp_path: Path, acessos: list[str]
) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _saeb_zip(raw, com_sobra=True)
    primeira: list[str] = []
    for rodada in range(3):
        acessos.clear()
        res = converter.convert(raw, lake, datasets=["saeb"])
        assert (res.converted, res.skipped) == ((2, 0) if rodada == 0 else (0, 2))
        assert len(res.errors) == 1 and "SOBRA.TXT: sem layout SAS" in res.errors[0]
        assert acessos  # reaberto: a declaração tem o TXT sem layout
        primeira = primeira or res.errors
        assert res.errors == primeira
    assert _parquets(lake, "saeb") == 2


def test_saeb_completo_pula_sem_abrir(tmp_path: Path, acessos: list[str]) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _saeb_zip(raw)
    res = converter.convert(raw, lake, datasets=["saeb"])
    assert (res.converted, res.skipped, res.errors) == (2, 0, [])
    acessos.clear()
    res2 = converter.convert(raw, lake, datasets=["saeb"])
    assert (res2.converted, res2.skipped, res2.errors) == (0, 2, [])
    assert acessos == []


def test_saeb_interrompido_num_txt_e_completado_na_rodada_seguinte(
    tmp_path: Path, acessos: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _saeb_zip(raw)
    with monkeypatch.context() as m:
        _falha_gravando(m, "escola_05")
        res = converter.convert(raw, lake, datasets=["saeb"])
    assert (res.converted, res.skipped) == (1, 0) and len(res.errors) == 1

    res2 = converter.convert(raw, lake, datasets=["saeb"])
    assert (res2.converted, res2.skipped, res2.errors) == (1, 1, [])
    acessos.clear()
    res3 = converter.convert(raw, lake, datasets=["saeb"])
    assert (res3.converted, res3.skipped, res3.errors) == (0, 2, [])
    assert acessos == []


@pytest.mark.parametrize("dataset", [_CENSO, _MAT])
def test_lake_sem_declaracao_reconverte_uma_vez_e_depois_pula(
    tmp_path: Path,
    acessos: list[str],
    monkeypatch: pytest.MonkeyPatch,
    dataset: str,
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    with monkeypatch.context() as m:
        for nome in ("write_polars", "write_duckdb"):
            original = getattr(lake_mod.LakeWriter, nome)

            def sem(self: Any, *a: Any, _o: Any = original, **k: Any) -> Any:
                k.pop("origin_outputs", None)  # lake gravado antes da declaração
                return _o(self, *a, **k)

            m.setattr(lake_mod.LakeWriter, nome, sem)
        res = converter.convert(raw, lake, datasets=[dataset])
    n = 2 if dataset == _CENSO else 1
    assert (res.converted, res.skipped, res.errors) == (n, 0, [])

    acessos.clear()
    res2 = converter.convert(raw, lake, datasets=[dataset])
    assert (res2.converted, res2.skipped, res2.errors) == (n, 0, [])
    assert acessos

    acessos.clear()
    res3 = converter.convert(raw, lake, datasets=[dataset])
    assert (res3.converted, res3.skipped, res3.errors) == (0, n, [])
    assert acessos == []


def test_saeb_layout_sem_dado_segue_dando_erro_a_cada_build(
    tmp_path: Path, acessos: list[str]
) -> None:
    """Um erro sem TXT (script sem arquivo de dados) também reabre o ZIP."""
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    z = _saeb_zip(raw)
    with zipfile.ZipFile(z, "a") as zf:
        zf.writestr(
            "INPUTS_SAS_SPSS/X/INPUT_SAS_ORFAO.sas",
            b"INFILE 'D:\\ORFAO.TXT' LRECL=4;\r\nINPUT\r\n@1 A 4.;\r\n",
        )
    _sidecar(z)
    for rodada in range(3):
        acessos.clear()
        res = converter.convert(raw, lake, datasets=["saeb"])
        assert (res.converted, res.skipped) == ((2, 0) if rodada == 0 else (0, 2))
        assert len(res.errors) == 1 and "orfao.txt não encontrado" in res.errors[0]
        assert acessos
