"""Recusa de corpo que não é o arquivo esperado (offline, respostas simuladas).

Caso real (nov/2026): o firewall do servidor devolveu HTTP 200 com uma página
"Request Rejected" de 243 bytes e o ENADE 2022 (.rar) foi gravado como se fosse o
arquivo, com carimbo mais novo que a versão real.
"""

from __future__ import annotations

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
