"""Recusa de corpo que não é o arquivo esperado (página de erro salva como dado).

O servidor do INEP, atrás de um firewall de aplicação, responde HTTP 200 com uma
página HTML ("Request Rejected") quando bloqueia o cliente. Sem esta checagem o
HTML era gravado com a extensão do dado (``.rar``) e, por ter carimbo mais novo,
passava por versão atual.

O ``quantilica-core`` valida a assinatura no ``.tmp`` antes de confirmar o
download, mas só para as extensões que conhece (``.zip``, ``.xlsx``, ``.7z``...);
``.rar`` não está na tabela dele. Aqui ficam a tabela de assinaturas do INEP, o
tamanho mínimo plausível e a verificação do arquivo já gravado.
"""

from __future__ import annotations

import logging
from pathlib import Path

from quantilica.core.exceptions import InvalidPayloadSignatureError

logger = logging.getLogger(__name__)

# Primeiros bytes de cada formato de dado do catálogo do INEP.
ASSINATURAS: dict[str, tuple[bytes, ...]] = {
    "zip": (b"PK\x03\x04", b"PK\x05\x06"),
    "xlsx": (b"PK\x03\x04", b"PK\x05\x06"),
    "rar": (b"Rar!\x1a\x07",),  # RAR 1.5-4.x (…\x00) e RAR 5 (…\x01\x00)
    "7z": (b"7z\xbc\xaf\x27\x1c",),
    # .xls: OLE2 (formato antigo) ou, em exportações recentes, um pacote OOXML.
    "xls": (b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", b"PK\x03\x04"),
}

# Menor tamanho plausível de um arquivo de dado com assinatura binária. Uma página
# de erro tem poucas centenas de bytes; o menor microdado do INEP tem centenas de KB.
TAMANHO_MINIMO = 1024

_PREFIXOS_HTML = (b"<!doctype", b"<html", b"<head", b"<body", b"<script", b"<?xml")


def extensao_de(caminho: Path | str) -> str:
    """Extensão do arquivo sem o ponto e em minúsculas (``x@1.rar`` vira ``rar``)."""
    return Path(caminho).suffix.lower().lstrip(".")


def validar_corpo(caminho: Path, ext: str | None = None) -> None:
    """Confere que o arquivo baixado é do formato que o nome promete.

    Só lê o cabeçalho (nada é aberto nem extraído). Extensões sem assinatura
    declarada (``csv``, por exemplo) só passam pela recusa de HTML.

    Args:
        caminho: Arquivo já gravado em disco.
        ext: Extensão esperada; por padrão a do nome do arquivo.

    Raises:
        InvalidPayloadSignatureError: corpo HTML, pequeno demais ou com
            assinatura diferente da esperada para a extensão.
    """
    ext = (ext or extensao_de(caminho)).lower().lstrip(".")
    tamanho = caminho.stat().st_size
    with open(caminho, "rb") as fh:
        cabecalho = fh.read(512)

    inicio = cabecalho.removeprefix(b"\xef\xbb\xbf").lstrip().lower()
    if inicio.startswith(_PREFIXOS_HTML) and ext not in ("html", "htm", "xml"):
        previa = inicio[:100].decode("ascii", errors="replace")
        raise InvalidPayloadSignatureError(
            f"{caminho.name}: o servidor devolveu uma página HTML no lugar do "
            f"arquivo .{ext} ({tamanho} bytes): {previa!r}"
        )

    assinaturas = ASSINATURAS.get(ext)
    if assinaturas is None:
        return
    if tamanho < TAMANHO_MINIMO:
        raise InvalidPayloadSignatureError(
            f"{caminho.name}: corpo de {tamanho} bytes é pequeno demais para um "
            f"arquivo .{ext} (mínimo {TAMANHO_MINIMO})"
        )
    if not cabecalho.startswith(assinaturas):
        raise InvalidPayloadSignatureError(
            f"{caminho.name}: assinatura {cabecalho[:8]!r} não confere com "
            f".{ext} ({tamanho} bytes)"
        )


def descartar_versao_nova(caminho: Path) -> None:
    """Remove a versão recém-criada por este download e o sidecar dela."""
    for alvo in (caminho, caminho.with_name(caminho.name + ".manifest.json")):
        try:
            alvo.unlink()
        except FileNotFoundError:
            pass
        except OSError as exc:  # pragma: no cover - disco com problema
            logger.error("Não foi possível remover %s: %s", alvo, exc)
