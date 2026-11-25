"""Recusa de corpo que não é o arquivo esperado (offline, respostas simuladas).

Caso real (nov/2026): o firewall do servidor devolveu HTTP 200 com uma página
"Request Rejected" de 243 bytes e o ENADE 2022 (.rar) foi gravado como se fosse o
arquivo, com carimbo mais novo que a versão real.
"""

from __future__ import annotations

import os
from pathlib import Path

import httpx2
import pytest
from quantilica.core.exceptions import CorruptPayloadError
from quantilica.core.http import HttpClient

from inep_fetcher.catalog import list_datasets
from inep_fetcher.integridade import TAMANHO_MINIMO, validar_corpo
from inep_fetcher.plugin import InepFetcherApp, fetcher

PAGINA_ERRO = (
    b"<html><head><title>Request Rejected</title></head><body>The requested URL "
    b"was rejected. Please consult with your administrator.<br><br>Your support "
    b"ID is: <3098271814246632>11<br><br><a href='javascript:history.back();'>"
    b"[Go Back]</a></body></html>"
)
RAR_OK = b"Rar!\x1a\x07\x01\x00" + b"\x00" * 4096
ZIP_OK = b"PK\x03\x04" + b"\x00" * 4096  # só a assinatura; o teste de ZIP usa HTML
LAST_MODIFIED = "Tue, 20 Aug 2024 19:08:41 GMT"


def _entry(ext: str) -> dict:
    ano = 2022 if ext == "rar" else 2021
    return next(dict(e) for e in list_datasets("enade") if e["year"] == ano)


def _cliente(corpo: bytes, content_type: str = "application/octet-stream"):
    chamadas: list[str] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        chamadas.append(request.method)
        cabecalhos = {
            "Content-Type": content_type,
            "Content-Length": str(len(corpo)),
        }
        if request.method == "HEAD":
            return httpx2.Response(200, headers=cabecalhos)
        return httpx2.Response(200, headers=cabecalhos, content=corpo)

    return HttpClient(attempts=1, transport=httpx2.MockTransport(handler)), chamadas


@pytest.fixture
def app(monkeypatch: pytest.MonkeyPatch):
    def _usar(corpo: bytes, content_type: str = "application/octet-stream"):
        cliente, chamadas = _cliente(corpo, content_type)
        monkeypatch.setattr(fetcher, "client", cliente)
        return chamadas

    return _usar


def _arquivos(pasta: Path) -> list[str]:
    return sorted(p.name for p in pasta.rglob("*") if p.is_file())


def test_plugin_usa_o_app_com_recusa() -> None:
    assert isinstance(fetcher, InepFetcherApp)


def test_rar_valido_e_gravado(app, tmp_path: Path) -> None:
    app(RAR_OK)
    destino = fetcher.download_entry(_entry("rar"), tmp_path)
    assert destino.suffix == ".rar"
    assert destino.read_bytes() == RAR_OK
    assert destino.with_name(destino.name + ".manifest.json").exists()


def test_rar_com_pagina_html_e_recusado(app, tmp_path: Path) -> None:
    app(PAGINA_ERRO, content_type="text/html")
    with pytest.raises(CorruptPayloadError, match="HTML"):
        fetcher.download_entry(_entry("rar"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_rar_html_com_content_type_enganoso_e_recusado(app, tmp_path: Path) -> None:
    app(PAGINA_ERRO, content_type="application/x-rar-compressed")
    with pytest.raises(CorruptPayloadError):
        fetcher.download_entry(_entry("rar"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_recusa_mantem_a_versao_anterior(app, tmp_path: Path) -> None:
    anterior = tmp_path / "enade" / "enade-microdados_2022@20240820.rar"
    anterior.parent.mkdir()
    anterior.write_bytes(RAR_OK)
    sidecar = anterior.with_name(anterior.name + ".manifest.json")
    sidecar.write_text("{}")
    app(PAGINA_ERRO, content_type="text/html")
    with pytest.raises(CorruptPayloadError):
        fetcher.download_entry(_entry("rar"), tmp_path)
    assert _arquivos(tmp_path) == sorted([anterior.name, sidecar.name])
    assert anterior.read_bytes() == RAR_OK


def test_rar_com_assinatura_errada_e_recusado(app, tmp_path: Path) -> None:
    app(b"\x00\x01\x02\x03" * 2048)
    with pytest.raises(CorruptPayloadError, match="assinatura"):
        fetcher.download_entry(_entry("rar"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_rar_com_assinatura_certa_mas_minusculo_e_recusado(app, tmp_path: Path) -> None:
    app(b"Rar!\x1a\x07\x00" + b"\x00" * 20)
    with pytest.raises(CorruptPayloadError, match="pequeno demais"):
        fetcher.download_entry(_entry("rar"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_zip_com_pagina_html_e_recusado_antes_de_gravar(app, tmp_path: Path) -> None:
    app(PAGINA_ERRO, content_type="text/html")
    with pytest.raises(CorruptPayloadError):
        fetcher.download_entry(_entry("zip"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_arquivo_existente_suspeito_nao_e_apagado(app, tmp_path: Path, caplog) -> None:
    """O bruto é acervo: o download nunca apaga o que já estava lá."""
    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    destino.write_bytes(PAGINA_ERRO)
    app(PAGINA_ERRO, content_type="text/html")
    with caplog.at_level("WARNING"):
        fetcher.download_entry(entry, tmp_path)  # fresco: nada a baixar
    assert destino.read_bytes() == PAGINA_ERRO


def test_falha_aparece_na_lista_de_erros_do_sync(app, tmp_path: Path) -> None:
    app(PAGINA_ERRO, content_type="text/html")
    baixados, total, erros = fetcher.download_datasets(
        [_entry("rar")], tmp_path, workers=1
    )
    assert (baixados, total) == (0, 1)
    assert len(erros) == 1
    assert erros[0][0] == "enade-microdados-2022"
    assert "versão anterior mantida" in erros[0][1]
    assert _arquivos(tmp_path) == []


@pytest.mark.parametrize(
    ("nome", "corpo"),
    [
        ("a.zip", ZIP_OK),
        ("a.xlsx", ZIP_OK),
        ("a.xls", b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1" + b"\x00" * 2048),
        ("a.7z", b"7z\xbc\xaf\x27\x1c" + b"\x00" * 2048),
        ("a.rar", b"Rar!\x1a\x07\x00" + b"\x00" * 2048),
        ("a.csv", b"CO_ANO;CO_CURSO\n2022;1\n"),
    ],
)
def test_validar_corpo_aceita_formatos_validos(
    tmp_path: Path, nome: str, corpo: bytes
) -> None:
    p = tmp_path / nome
    p.write_bytes(corpo)
    validar_corpo(p)


@pytest.mark.parametrize("nome", ["a.zip", "a.xlsx", "a.xls", "a.7z", "a.rar", "a.csv"])
def test_validar_corpo_recusa_html_em_qualquer_extensao(
    tmp_path: Path, nome: str
) -> None:
    p = tmp_path / nome
    p.write_bytes(PAGINA_ERRO)
    with pytest.raises(CorruptPayloadError, match="HTML"):
        validar_corpo(p)


def test_validar_corpo_html_com_bom_e_espacos(tmp_path: Path) -> None:
    p = tmp_path / "a.zip"
    p.write_bytes(b"\xef\xbb\xbf  \n<!DOCTYPE html><html></html>")
    with pytest.raises(CorruptPayloadError, match="HTML"):
        validar_corpo(p)


def test_validar_corpo_tamanho_minimo(tmp_path: Path) -> None:
    p = tmp_path / "a.zip"
    p.write_bytes(b"PK\x03\x04" + b"\x00" * (TAMANHO_MINIMO - 5))
    with pytest.raises(CorruptPayloadError, match="pequeno demais"):
        validar_corpo(p)
    p.write_bytes(b"PK\x03\x04" + b"\x00" * (TAMANHO_MINIMO - 4))
    validar_corpo(p)


def test_todo_ext_do_catalogo_tem_assinatura_ou_e_csv() -> None:
    from inep_fetcher.integridade import ASSINATURAS

    exts = {e["ext"] for e in list_datasets()}
    assert exts - set(ASSINATURAS) <= {"csv"}


RAR5_COMO_ZIP = b"Rar!\x1a\x07\x01\x00" + b"\x01" * 4096


def _entry_idd_2022() -> dict:
    return next(
        dict(e) for e in list_datasets("idd") if e["id"] == "idd-microdados-2022"
    )


def _zip_de_verdade() -> bytes:
    import io
    import zipfile

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("dados.csv", "a;b\n1;2\n" * 200)
    return buf.getvalue()


def test_idd_2022_rar5_com_extensao_zip_e_aceito(app, tmp_path: Path) -> None:
    """O IDD 2022 é RAR5 publicado como .zip: o core o recusaria como ZIP."""
    app(RAR5_COMO_ZIP)
    destino = fetcher.download_entry(_entry_idd_2022(), tmp_path)
    assert destino.suffix == ".zip"
    assert destino.read_bytes() == RAR5_COMO_ZIP
    sidecar = destino.with_name(destino.name + ".manifest.json")
    assert sidecar.exists()
    import json

    assert json.loads(sidecar.read_text())["path"] == str(destino.absolute())
    assert _arquivos(tmp_path) == sorted([destino.name, sidecar.name])


def test_zip_de_verdade_e_gravado(app, tmp_path: Path) -> None:
    corpo = _zip_de_verdade()
    app(corpo)
    destino = fetcher.download_entry(_entry("zip"), tmp_path)
    assert destino.read_bytes() == corpo
    assert len(_arquivos(tmp_path)) == 2  # arquivo + sidecar, sem preparo


def test_zip_truncado_e_recusado_e_nao_deixa_rastro(app, tmp_path: Path) -> None:
    app(_zip_de_verdade()[:300])
    with pytest.raises(CorruptPayloadError):
        fetcher.download_entry(_entry("zip"), tmp_path)
    assert _arquivos(tmp_path) == []


def test_rar_com_assinatura_errada_nao_sobrescreve_o_existente(
    app, tmp_path: Path
) -> None:
    """O core troca o .tmp pelo destino antes de qualquer conferência do INEP."""
    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    destino.write_bytes(RAR_OK)
    sidecar = destino.with_name(destino.name + ".manifest.json")
    sidecar.write_text('{"sha256": "antigo"}')
    app(b"\x00\x01\x02\x03" * 2048)  # tamanho diferente: o core baixa
    with pytest.raises(CorruptPayloadError, match="versão anterior mantida"):
        fetcher.download_entry(entry, tmp_path)
    assert destino.read_bytes() == RAR_OK
    assert sidecar.read_text() == '{"sha256": "antigo"}'
    assert _arquivos(tmp_path) == sorted([destino.name, sidecar.name])


def test_rar_valido_novo_substitui_o_existente_e_o_sidecar(app, tmp_path: Path) -> None:
    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    destino.write_bytes(RAR_OK)
    novo = b"Rar!\x1a\x07\x01\x00" + b"\x02" * 9000
    app(novo)
    fetcher.download_entry(entry, tmp_path)
    assert destino.read_bytes() == novo
    import json

    meta = json.loads(destino.with_name(destino.name + ".manifest.json").read_text())
    assert meta["size_bytes"] == len(novo)
    assert meta["path"] == str(destino.absolute())
    assert len(_arquivos(tmp_path)) == 2


def test_modo_efemero_recusa_sem_apagar_o_sidecar_existente(
    app, tmp_path: Path
) -> None:
    """Só o sidecar ficou (arquivo apagado do local): um corpo ruim não o apaga."""
    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    sidecar = destino.with_name(destino.name + ".manifest.json")
    sidecar.write_text("{}")  # ilegível para o core: ele baixa de novo
    assert not destino.exists()
    app(PAGINA_ERRO, content_type="text/html")
    with pytest.raises(CorruptPayloadError):
        fetcher.download_entry(entry, tmp_path)
    assert not destino.exists()
    assert sidecar.read_text() == "{}"
    assert _arquivos(tmp_path) == [sidecar.name]


def test_validar_corpo_zip_aceita_rar_mas_recusa_o_resto(tmp_path: Path) -> None:
    p = tmp_path / "a.zip"
    p.write_bytes(RAR5_COMO_ZIP)
    validar_corpo(p)
    p.write_bytes(b"\x00" * 2048)
    with pytest.raises(CorruptPayloadError, match="assinatura"):
        validar_corpo(p)


# --- preparo de execução morta ---------------------------------------------------


def _pid_morto() -> int:
    """Pid de um processo que já terminou (a execução morta simulada)."""
    import subprocess
    import sys

    proc = subprocess.Popen([sys.executable, "-c", "pass"])
    proc.wait()
    return proc.pid


def _velho(caminho: Path, horas: float) -> None:
    import os
    import time

    passado = time.time() - horas * 3600
    os.utime(caminho, (passado, passado))


def test_preparo_termina_em_tmp_e_leva_o_host_e_o_pid(tmp_path: Path) -> None:
    import os

    from inep_fetcher.integridade import _hospedeiro, caminho_de_preparo

    destino = tmp_path / "x@20260101.zip"
    preparo = caminho_de_preparo(destino)
    assert preparo.name.endswith(".tmp")  # ignorado por select_current/ingest/auditoria
    assert preparo.name.startswith(f".{destino.name}.{_hospedeiro()}-{os.getpid()}-")
    assert preparo != caminho_de_preparo(destino)  # único por download
    assert preparo.parent == destino.parent


def test_preparo_de_execucao_morta_e_limpo_no_proximo_preparo(
    app, tmp_path: Path
) -> None:
    from inep_fetcher.integridade import (
        _hospedeiro,
        caminho_de_preparo,
        preparar,
    )

    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    destino.write_bytes(RAR_OK)
    sidecar = destino.with_name(destino.name + ".manifest.json")
    sidecar.write_text("{}")
    morto = _pid_morto()
    host = _hospedeiro()
    base = f".{destino.name}.{host}-{morto}-aaaaaaaa.parte.tmp"
    lixo = [
        destino.with_name(base),
        destino.with_name(base + ".manifest.json"),
        # .tmp parcial que o core deixa ao lado do preparo
        destino.with_name("." + base + ".k3_x9z0q.tmp"),
    ]
    for item in lixo:
        item.write_bytes(b"parcial")
    vivo = destino.with_name(f".{destino.name}.{host}-{os.getpid()}-bbbbbbbb.parte.tmp")
    vivo.write_bytes(b"de outra thread")
    # formatos antigos (sem host): só pela idade, e ela é a do ctime (recente aqui)
    antigos = [
        destino.with_name(f".{destino.name}.cafebabe.parte"),
        destino.with_name(f".{destino.name}.{morto}-aaaaaaaa.parte.tmp"),
    ]
    for item in antigos:
        item.write_bytes(b"talvez em andamento")
    de_outro = destino.with_name(f".outro.zip.{host}-{morto}-aaaaaaaa.parte.tmp")
    de_outro.write_bytes(b"de outro destino")

    preparar(destino, caminho_de_preparo(destino))

    assert not any(item.exists() for item in lixo)
    assert vivo.exists() and de_outro.exists()
    assert all(item.exists() for item in antigos)
    assert destino.read_bytes() == RAR_OK  # o destino e o sidecar nunca são tocados
    assert sidecar.read_text() == "{}"


def test_preparo_de_pid_vivo_do_proprio_host_nunca_cai_pela_idade(
    tmp_path: Path,
) -> None:
    """O preparo é link físico do destino e herda o mtime dele (meses): o pid decide."""
    import time

    from inep_fetcher.integridade import _hospedeiro, limpar_preparos_orfaos

    destino = tmp_path / "x@20260101.zip"
    destino.write_bytes(b"destino de meses atras")
    _velho(destino, 24 * 100)
    vivo = (
        tmp_path / f".{destino.name}.{_hospedeiro()}-{os.getpid()}-bbbbbbbb.parte.tmp"
    )
    os.link(destino, vivo)  # herda o mtime velho do destino
    assert time.time() - vivo.stat().st_mtime > 48 * 3600
    assert limpar_preparos_orfaos(destino) == 0
    assert limpar_preparos_orfaos(destino, agora=time.time() + 400 * 24 * 3600) == 0
    assert vivo.exists() and destino.exists()


def test_preparo_de_outro_host_so_cai_depois_de_48h_de_ctime(tmp_path: Path) -> None:
    import time

    from inep_fetcher.integridade import _hospedeiro, limpar_preparos_orfaos

    destino = tmp_path / "x@20260101.zip"
    destino.write_bytes(b"x")
    outro = "0" * 8 if _hospedeiro() != "0" * 8 else "1" * 8
    de_fora = tmp_path / f".{destino.name}.{outro}-{_pid_morto()}-bbbbbbbb.parte.tmp"
    de_fora.write_bytes(b"de outro host, pid sem sentido aqui")
    parcial = tmp_path / f"..{destino.name}.{outro}-1-bbbbbbbb.parte.tmp.k3_x9z0q.tmp"
    parcial.write_bytes(b"parcial do core")
    _velho(de_fora, 24 * 100)  # o mtime velho não conta: vale o ctime
    agora = time.time()
    assert limpar_preparos_orfaos(destino, agora=agora + 47 * 3600) == 0
    assert limpar_preparos_orfaos(destino, agora=agora + 49 * 3600) == 2
    assert not de_fora.exists() and not parcial.exists()
    assert destino.exists()


def test_preparo_de_formato_antigo_so_cai_pela_idade_do_ctime(tmp_path: Path) -> None:
    import time

    from inep_fetcher.integridade import limpar_preparos_orfaos

    destino = tmp_path / "x@20260101.zip"
    destino.write_bytes(b"x")
    antigo = tmp_path / f".{destino.name}.cafebabe.parte"
    antigo.write_bytes(b"x")
    com_pid = tmp_path / f".{destino.name}.{_pid_morto()}-aaaaaaaa.parte.tmp"
    com_pid.write_bytes(b"x")
    assert limpar_preparos_orfaos(destino) == 0
    assert limpar_preparos_orfaos(destino, agora=time.time() + 49 * 3600) == 2


def test_limpeza_de_um_processo_nao_apaga_o_preparo_de_outro_vivo(
    tmp_path: Path,
) -> None:
    """Dois processos no mesmo destino: o vivo (de pid de verdade) não é apagado."""
    import subprocess
    import sys

    from inep_fetcher.integridade import (
        _hospedeiro,
        caminho_de_preparo,
        limpar_preparos_orfaos,
        preparar,
    )

    destino = tmp_path / "x@20260101.zip"
    destino.write_bytes(b"destino antigo")
    _velho(destino, 24 * 90)
    vivo = subprocess.Popen(
        [sys.executable, "-c", "import time; time.sleep(60)"],
        stdin=subprocess.DEVNULL,
    )
    try:
        preparo_do_vivo = tmp_path / (
            f".{destino.name}.{_hospedeiro()}-{vivo.pid}-aaaaaaaa.parte.tmp"
        )
        os.link(destino, preparo_do_vivo)  # mtime de 90 dias, como no download real
        preparar(destino, caminho_de_preparo(destino))  # segundo processo (este)
        assert preparo_do_vivo.exists()
        vivo.kill()
        vivo.wait()
        assert limpar_preparos_orfaos(destino) >= 1  # morto: agora cai
        assert not preparo_do_vivo.exists()
    finally:
        vivo.kill()
        vivo.wait()
    assert destino.read_bytes() == b"destino antigo"


def test_download_depois_de_execucao_morta_nao_deixa_rastro(
    app, tmp_path: Path
) -> None:
    entry = _entry("rar")
    destino = fetcher.path_builder(tmp_path, entry, None)
    destino.parent.mkdir(parents=True)
    from inep_fetcher.integridade import _hospedeiro

    morto = destino.with_name(
        f".{destino.name}.{_hospedeiro()}-{_pid_morto()}-aaaaaaaa.parte.tmp"
    )
    morto.write_bytes(b"parcial")
    app(RAR_OK)
    fetcher.download_entry(entry, tmp_path)
    assert not morto.exists()
    assert destino.read_bytes() == RAR_OK
    assert not [n for n in _arquivos(tmp_path) if n.startswith(".")]


# --- quebra de linha final quando o tamanho não foi conferido --------------------


def test_conferir_csv_sem_quebra_final_so_recusa_quando_exigido(
    tmp_path: Path,
) -> None:
    from inep_fetcher.plugin import _conferir

    preparo = tmp_path / ".t.csv.1-aaaaaaaa.parte.tmp"
    preparo.write_bytes(b"a;b\n1;2\n3;4")  # sem \n final: transferência truncada?
    _conferir(preparo, "t.csv", "csv", None)  # tamanho conferido: aceita
    with pytest.raises(CorruptPayloadError, match="quebra de linha"):
        _conferir(preparo, "t.csv", "csv", None, require_final_newline=True)
    preparo.write_bytes(b"a;b\n1;2\n3;4\n")
    _conferir(preparo, "t.csv", "csv", None, require_final_newline=True)


def _csv_entry() -> dict:
    return next(
        dict(e)
        for g in __import__("inep_fetcher.catalog", fromlist=["GROUPS"]).GROUPS
        for e in list_datasets(g)
        if str(e.get("url", "")).lower().endswith(".csv")
    )


def test_csv_truncado_sem_content_length_e_recusado(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    corpo = b"a;b\n" + b"1;2\n" * 400 + b"3;"  # corta no meio da linha

    def handler(request: httpx2.Request) -> httpx2.Response:
        if request.method == "HEAD":
            return httpx2.Response(200)
        # corpo em pedaços: sem Content-Length
        return httpx2.Response(200, content=iter([corpo[:100], corpo[100:]]))

    monkeypatch.setattr(
        fetcher,
        "client",
        HttpClient(attempts=1, transport=httpx2.MockTransport(handler)),
    )
    entry = _csv_entry()
    with pytest.raises(CorruptPayloadError, match="quebra de linha"):
        fetcher.download_entry(entry, tmp_path)
    assert _arquivos(tmp_path) == []


def test_csv_sem_quebra_final_com_content_length_e_aceito(app, tmp_path: Path) -> None:
    app(b"a;b\n" + b"1;2\n" * 400 + b"3;4")  # tamanho conferido pelo core
    entry = _csv_entry()
    destino = fetcher.download_entry(entry, tmp_path)
    assert destino is not None and Path(destino).exists()


def test_promover_regrava_o_sidecar_com_o_writer_do_core(
    app, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import quantilica.core.manifests as manifests

    chamadas: list[Path] = []
    real = manifests.write_manifest_sidecar

    def espiao(alvo, manifesto):
        chamadas.append(Path(alvo))
        return real(alvo, manifesto)

    monkeypatch.setattr(manifests, "write_manifest_sidecar", espiao)
    entry = _entry("rar")
    app(RAR_OK)
    destino = fetcher.path_builder(tmp_path, entry, None)
    fetcher.download_entry(entry, tmp_path)
    assert chamadas == [destino]
    assert not [n for n in _arquivos(tmp_path) if n.startswith(".")]
