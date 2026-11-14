"""Conversão do lake para arquivos fora do padrão: checksum, RAR e Deflate64."""

from __future__ import annotations

import logging
import os
import shutil
import subprocess
import types
import zipfile
from pathlib import Path

import polars as pl
import pytest

from inep_fetcher import _archive
from inep_fetcher._archive import (
    ArchiveError,
    RarUnavailableError,
    SevenZipUnavailableError,
    archive_kind,
    extract_archive,
    scratch_dir,
)
from inep_fetcher.lake import LakeConverter, _is_checksum_file

from .rar_fixture import build_rar5

CSV = "co_ies;no_ies\n1;Alfa\n2;Beta\n"
MD5 = (
    "d41d8cd98f00b204e9800998ecf8427e *tx_rend_escolas_2023.xlsx\n"
    "0cc175b9c0f1b6a831c399e269772661 *tx_rend_escolas_2023.ods\n"
)


def _parquets(lake: Path) -> list[Path]:
    return sorted(lake.rglob("*.parquet"))


def _txt(base: Path, name: str, text: str) -> Path:
    path = base / name
    path.write_text(text)
    return path


def _write_xlsx(path: Path) -> None:
    pl.DataFrame({"uf": ["SP", "RJ"], "alunos": [30, 28]}).write_excel(path)


# ---------------------------------------------------------------- checksum


def test_is_checksum_file_por_conteudo_e_extensao(tmp_path: Path) -> None:
    md5 = tmp_path / "x.txt"
    md5.write_text(MD5 + "\n")
    assert _is_checksum_file(md5)
    sha = tmp_path / "y.txt"
    sha.write_text(f"{'a' * 64}  arquivo com espaço.csv\r\n")
    assert _is_checksum_file(sha)
    assert _is_checksum_file(tmp_path / "z.sha256")  # pela extensão
    dado = tmp_path / "dado.txt"
    dado.write_text("co_ies;no_ies\n1;Alfa\n")
    assert not _is_checksum_file(dado)
    misto = tmp_path / "misto.txt"
    misto.write_text(MD5 + "co_ies;no_ies\n")
    assert not _is_checksum_file(misto)
    # TXT de largura fixa só de dígitos (32 dígitos + nome com extensão): é dado
    largura = tmp_path / "largura.txt"
    largura.write_text("12345678901234567890123456789012 ESCOLA1.csv\n" * 3)
    assert not _is_checksum_file(largura)
    # hash de tamanho que nenhum algoritmo usa, ou nome sem extensão
    assert not _is_checksum_file(_txt(tmp_path, "h.txt", f"{'a' * 33} x.csv\n"))
    assert not _is_checksum_file(_txt(tmp_path, "n.txt", f"{'a' * 32} semextensao\n"))
    vazio = tmp_path / "vazio.txt"
    vazio.write_text("\n\n")
    assert not _is_checksum_file(vazio)


def test_zip_com_checksum_xlsx_e_ods_gera_so_o_parquet_da_planilha(
    tmp_path: Path,
) -> None:
    raw = tmp_path / "raw" / "taxas-rendimento-escolar"
    raw.mkdir(parents=True)
    xlsx = tmp_path / "t.xlsx"
    _write_xlsx(xlsx)
    with zipfile.ZipFile(
        raw / "taxas-rendimento-escolar-t-2023@20240813.zip", "w"
    ) as zf:
        zf.write(xlsx, "t/t.xlsx")
        zf.writestr("t/t.ods", b"conteudo ods qualquer")
        zf.writestr("t/t.txt", MD5)
    lake = tmp_path / "lake"

    res = LakeConverter().convert(tmp_path / "raw", lake)

    assert not res.errors
    assert (res.converted, res.skipped) == (1, 0)
    assert len(_parquets(lake)) == 1
    assert pl.read_parquet(_parquets(lake)[0]).shape == (2, 2)


def test_zip_xlsx_e_xls_do_mesmo_nome_viram_um_so_parquet(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "taxas-rendimento-escolar"
    raw.mkdir(parents=True)
    xlsx = tmp_path / "t.xlsx"
    _write_xlsx(xlsx)
    with zipfile.ZipFile(
        raw / "taxas-rendimento-escolar-t-2023@20240813.zip", "w"
    ) as zf:
        zf.write(xlsx, "t/t.xlsx")
        zf.writestr("t/t.xls", b"nao e uma planilha valida")
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors
    assert res.converted == 1


# ------------------------------------------------------------- RAR (magic)


def test_formato_pelos_bytes_e_nao_pela_extensao(tmp_path: Path) -> None:
    rar = tmp_path / "idd@2024.zip"
    rar.write_bytes(b"Rar!\x1a\x07\x01\x00" + b"\x00" * 32)
    assert archive_kind(rar) == "rar"
    sete = tmp_path / "x.zip"
    sete.write_bytes(b"7z\xbc\xaf\x27\x1c\x00\x04" + b"\x00" * 32)
    assert archive_kind(sete) == "7z"
    z = tmp_path / "real.dat"
    with zipfile.ZipFile(z, "w") as zf:
        zf.writestr("a.csv", CSV)
    assert archive_kind(z) == "zip"
    lixo = tmp_path / "lixo.zip"
    lixo.write_bytes(b"nada a ver")
    assert archive_kind(lixo) == "unknown"
    with pytest.raises(ArchiveError, match="não reconhecido"):
        extract_archive(lixo, tmp_path / "out")


def test_rar_sem_7zip_pede_para_instalar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rar = tmp_path / "idd@2024.zip"
    rar.write_bytes(build_rar5({"a.csv": CSV.encode()}))
    monkeypatch.setattr(_archive, "find_sevenzip", lambda: None)
    monkeypatch.setattr(_archive, "_libarchive_available", lambda: False)
    with pytest.raises(SevenZipUnavailableError, match="instale o 7-Zip"):
        extract_archive(rar, tmp_path / "out")


_REQUIRE_7Z = bool(os.environ.get("INEP_REQUIRE_7Z"))


def _rar_legivel(tmp_path: Path) -> bool:
    """Há leitor de RAR (7-Zip com codec ou libarchive) neste ambiente?

    Só "ferramenta ausente" vira skip; qualquer outro erro falha o teste. Com
    ``INEP_REQUIRE_7Z=1`` (CI), até a falta do 7-Zip falha.
    """
    probe = tmp_path / "probe.rar"
    probe.write_bytes(build_rar5({"a.txt": b"x"}))
    try:
        extract_archive(probe, tmp_path / "probe_out")
    except SevenZipUnavailableError:
        if _REQUIRE_7Z:
            raise
        return False
    except RarUnavailableError:
        return False
    return True


def test_rar_com_extensao_zip_e_convertido(tmp_path: Path) -> None:
    if not _rar_legivel(tmp_path):
        pytest.skip("nem 7-Zip com codec RAR nem libarchive disponíveis")
    raw = tmp_path / "raw" / "idd"
    raw.mkdir(parents=True)
    rar = raw / "idd-microdados_2022@20240820.zip"
    rar.write_bytes(
        build_rar5(
            {
                "Microdados_IDD_2022/1.LEIA-ME/Manual.txt": b"leia-me",
                "Microdados_IDD_2022/2.DADOS/MICRODADOS_IDD_2022.txt": CSV.encode(),
            }
        )
    )
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors
    assert res.converted == 1
    assert pl.read_parquet(_parquets(tmp_path / "lake")[0]).shape == (2, 2)


@pytest.mark.skipif(shutil.which("rar") is None, reason="utilitário rar ausente")
def test_rar_real_gerado_pelo_rar(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.csv").write_text(CSV)
    out = tmp_path / "idd@2024.zip"
    subprocess.run(
        ["rar", "a", "-ep", str(tmp_path / "t.rar"), str(src / "a.csv")], check=True
    )
    (tmp_path / "t.rar").rename(out)
    files = extract_archive(out, tmp_path / "out")
    assert [f.name for f in files] == ["a.csv"]


# -------------------------------------------------------------- Deflate64

_SEVENZIP = _archive.find_sevenzip()


def _zip_deflate64(tmp_path: Path, arc: str, name: str, content: str) -> Path:
    src = tmp_path / "src" / name
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    out = tmp_path / arc
    subprocess.run(
        [_SEVENZIP or "7z", "a", "-tzip", "-mm=Deflate64", str(out), str(src)],
        check=True,
        capture_output=True,
        cwd=src.parent,
    )
    with zipfile.ZipFile(out) as zf:
        assert zf.infolist()[0].compress_type == 9
    return out


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_zip_misto_store_e_deflate64_extrai_tudo(tmp_path: Path) -> None:
    conteudo = "co_ies;valor\n" + "".join(f"{i};{i * 3}\n" for i in range(20000))
    _zip_deflate64(tmp_path, "d64.zip", "RESULTADOS.csv", conteudo)
    misto = tmp_path / "misto.zip"
    with zipfile.ZipFile(misto, "w") as dst:
        dst.writestr("pacote/LEIA_ME.txt", "ola")
    # 7z acrescenta o membro Deflate64 ao ZIP que o Python criou (store)
    subprocess.run(
        [
            _SEVENZIP or "7z",
            "a",
            "-tzip",
            "-mm=Deflate64",
            str(misto),
            str(tmp_path / "src" / "RESULTADOS.csv"),
        ],
        check=True,
        capture_output=True,
        cwd=tmp_path / "src",
    )
    files = extract_archive(misto, tmp_path / "out")
    nomes = {f.name for f in files}
    assert nomes == {"LEIA_ME.txt", "RESULTADOS.csv"}
    assert (tmp_path / "out" / "RESULTADOS.csv").read_text() == conteudo


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_convert_zip_com_membro_deflate64(tmp_path: Path) -> None:
    conteudo = "co_ies;valor\n" + "".join(f"{i};{i * 3}\n" for i in range(20000))
    arc = _zip_deflate64(tmp_path, "enem.zip", "RESULTADOS_2025.csv", conteudo)
    raw = tmp_path / "raw" / "enem"
    raw.mkdir(parents=True)
    shutil.copy(arc, raw / "enem-microdados_2025@20260915.zip")

    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")

    assert not res.errors, res.errors
    assert res.converted == 1
    assert pl.read_parquet(_parquets(tmp_path / "lake")[0]).shape == (20000, 2)


def test_deflate64_sem_7zip_pede_para_instalar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = tmp_path / "d64.zip"
    with zipfile.ZipFile(arc, "w") as zf:
        zf.writestr("a.csv", CSV)
    # força o método 9 no cabeçalho central (o conteúdo não será lido)
    data = bytearray(arc.read_bytes())
    for sig in (b"PK\x03\x04", b"PK\x01\x02"):
        i = data.index(sig)
        off = i + (8 if sig == b"PK\x03\x04" else 10)
        data[off : off + 2] = (9).to_bytes(2, "little")
    arc.write_bytes(bytes(data))
    monkeypatch.setattr(_archive, "find_sevenzip", lambda: None)
    with pytest.raises(SevenZipUnavailableError, match="instale o 7-Zip"):
        extract_archive(arc, tmp_path / "out")


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_convert_deflate64_so_dados_e_ignora_dicionario(tmp_path: Path) -> None:
    conteudo = "co_ies;valor\n" + "".join(f"{i};{i * 3}\n" for i in range(20000))
    src = tmp_path / "src"
    (src / "pasta" / "DADOS").mkdir(parents=True)
    (src / "DICIONÁRIO").mkdir()
    (src / "pasta" / "DADOS" / "RESULTADOS_2025.csv").write_text(conteudo)
    (src / "DICIONÁRIO" / "dicionario.csv").write_text(conteudo)
    raw = tmp_path / "raw" / "enem"
    raw.mkdir(parents=True)
    subprocess.run(
        [
            _SEVENZIP or "7z",
            "a",
            "-tzip",
            "-mm=Deflate64",
            str(raw / "enem-microdados_2025@20260915.zip"),
            "pasta",
            "DICIONÁRIO",
        ],
        check=True,
        capture_output=True,
        cwd=src,
    )
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 1
    paths = _parquets(tmp_path / "lake")
    assert len(paths) == 1 and "resultados_2025" in paths[0].name.lower()


def _zip_com_muitos_membros(tmp_path: Path, n: int) -> Path:
    arc = tmp_path / "muitos.zip"
    with zipfile.ZipFile(arc, "w", zipfile.ZIP_DEFLATED) as zf:
        for i in range(n):
            zf.writestr(f"DADOS/parte_{i:03d}.csv", f"a;b\n{i};{i}\n")
    return arc


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_muitos_membros_nao_suportados_vao_pelo_arquivo_inteiro(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = _zip_com_muitos_membros(tmp_path, 60)
    monkeypatch.setattr(_archive, "_ZIPFILE_METHODS", frozenset({zipfile.ZIP_STORED}))
    chamadas: list[list[str] | None] = []
    real = _archive._sevenzip_extract

    def espia(exe, archive, dest, names=None):  # noqa: ANN001, ANN202
        chamadas.append(names)
        return real(exe, archive, dest, names)

    monkeypatch.setattr(_archive, "_sevenzip_extract", espia)
    files = extract_archive(arc, tmp_path / "out")
    assert chamadas == [None]  # 60 nomes > 50: sem lista na linha de comando
    assert len(files) == 60


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_membro_que_o_7zip_nao_acha_refaz_com_o_arquivo_inteiro(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = _zip_com_muitos_membros(tmp_path, 3)
    monkeypatch.setattr(_archive, "_ZIPFILE_METHODS", frozenset({zipfile.ZIP_STORED}))
    chamadas: list[list[str] | None] = []
    real = _archive._sevenzip_extract

    def sem_achar_por_nome(exe, archive, dest, names=None):  # noqa: ANN001, ANN202
        chamadas.append(names)
        if names:  # simula nome com outra codificação: nada extraído
            return None
        return real(exe, archive, dest, names)

    monkeypatch.setattr(_archive, "_sevenzip_extract", sem_achar_por_nome)
    files = extract_archive(arc, tmp_path / "out")
    assert len(chamadas) == 2 and chamadas[1] is None
    assert sorted(f.name for f in files) == [f"parte_{i:03d}.csv" for i in range(3)]


def _proc(code: int) -> types.SimpleNamespace:
    return types.SimpleNamespace(returncode=code, stdout=b"", stderr=b"erro 7z")


def test_7zip_codigo_1_e_aviso_e_2_e_falha(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = tmp_path / "x.zip"
    arc.write_bytes(b"")
    monkeypatch.setattr(_archive.subprocess, "run", lambda *a, **k: _proc(1))
    _archive._sevenzip_extract("7z", arc, tmp_path)  # não levanta
    monkeypatch.setattr(_archive.subprocess, "run", lambda *a, **k: _proc(2))
    with pytest.raises(ArchiveError, match="erro 7z"):
        _archive._sevenzip_extract("7z", arc, tmp_path)


def test_7zip_estourou_o_tempo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def run(*a, **k):  # noqa: ANN002, ANN003, ANN202
        raise subprocess.TimeoutExpired("7z", 1)

    monkeypatch.setattr(_archive.subprocess, "run", run)
    with pytest.raises(ArchiveError, match="interrompido"):
        _archive._sevenzip_extract("7z", tmp_path / "x.zip", tmp_path)


def test_executavel_do_7zip_inexistente_pede_para_instalar(tmp_path: Path) -> None:
    with pytest.raises(SevenZipUnavailableError, match="instale o 7-Zip"):
        _archive._sevenzip_extract(str(tmp_path / "nao-existe"), tmp_path, tmp_path)


def test_libarchive_com_erro_qualquer_vira_archive_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def file_reader(_path: str):  # noqa: ANN202
        raise RuntimeError("quebrou")

    monkeypatch.setitem(
        __import__("sys").modules,
        "libarchive",
        types.SimpleNamespace(file_reader=file_reader),
    )
    with pytest.raises(ArchiveError, match="libarchive falhou"):
        _archive._libarchive_extract(tmp_path / "x.rar", tmp_path)
    monkeypatch.setitem(__import__("sys").modules, "libarchive", None)
    assert not _archive._libarchive_available()


def test_falha_ao_apagar_o_temporario_vira_aviso(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    def sempre_falha(_path: str) -> None:
        raise OSError("em uso")

    def rmtree(path, onexc=None):  # noqa: ANN001, ANN202
        onexc(sempre_falha, str(path), OSError("em uso"))

    monkeypatch.setattr(_archive.shutil, "rmtree", rmtree)
    monkeypatch.setenv("QUANTILICA_LAKE_SCRATCH", str(tmp_path))
    with caplog.at_level(logging.WARNING), scratch_dir() as work:
        assert work.parent == tmp_path
    assert "em uso" in caplog.text


def test_temporario_com_arquivo_somente_leitura_e_apagado_sem_aviso(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    chamadas: list[str] = []

    def rmtree(path, onexc=None):  # noqa: ANN001, ANN202
        # 1ª tentativa falhou por permissão; o handler libera a escrita e repete
        onexc(lambda p: chamadas.append(p), str(path), PermissionError("ro"))

    chmods: list[str] = []
    monkeypatch.setattr(_archive.os, "chmod", lambda p, m: chmods.append(p))
    monkeypatch.setattr(_archive.shutil, "rmtree", rmtree)
    monkeypatch.setenv("QUANTILICA_LAKE_SCRATCH", str(tmp_path))
    with caplog.at_level(logging.WARNING), scratch_dir():
        pass
    assert len(chmods) == len(chamadas) == 1
    assert not caplog.text


@pytest.mark.skipif(_SEVENZIP is None and not _REQUIRE_7Z, reason="7-Zip ausente")
def test_extracao_inteira_pelo_7zip_nao_mexe_no_que_ja_estava_no_destino(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = _zip_com_muitos_membros(tmp_path, 60)
    out = tmp_path / "out"
    (out / "OUTRO").mkdir(parents=True)
    (out / "OUTRO" / "de_fora.csv").write_text("x;y\n1;2\n")
    monkeypatch.setattr(_archive, "_ZIPFILE_METHODS", frozenset({zipfile.ZIP_STORED}))
    files = extract_archive(arc, out)
    assert (out / "OUTRO" / "de_fora.csv").read_text() == "x;y\n1;2\n"
    assert len(files) == 61
    assert not [p for p in out.iterdir() if p.name.startswith(".extract-")]


def test_7zip_com_aviso_e_nada_extraido_nao_e_sucesso(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rar = tmp_path / "x.zip"
    rar.write_bytes(build_rar5({"a.csv": CSV.encode()}))
    monkeypatch.setattr(_archive, "find_sevenzip", lambda: "7z")
    monkeypatch.setattr(_archive.subprocess, "run", lambda *a, **k: _proc(1))
    out = tmp_path / "out"
    out.mkdir()
    (out / "ja_existia.txt").write_text("x")  # conteúdo de fora não conta como extraído
    with pytest.raises(ArchiveError, match="não tem arquivos"):
        extract_archive(rar, out)
    assert (out / "ja_existia.txt").exists()
    assert [p.name for p in out.iterdir()] == ["ja_existia.txt"]


def test_zip_com_extracao_inteira_que_falta_arquivo_falha(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    arc = _zip_com_muitos_membros(tmp_path, 3)
    monkeypatch.setattr(_archive, "_ZIPFILE_METHODS", frozenset({zipfile.ZIP_STORED}))
    monkeypatch.setattr(_archive, "find_sevenzip", lambda: "7z")
    monkeypatch.setattr(_archive.subprocess, "run", lambda *a, **k: _proc(1))
    with pytest.raises(ArchiveError, match="0 de 3"):
        extract_archive(arc, tmp_path / "out")
