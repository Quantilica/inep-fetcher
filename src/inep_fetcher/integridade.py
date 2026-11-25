"""Recusa de corpo que não é o arquivo esperado (página de erro salva como dado).

O servidor do INEP, atrás de um firewall de aplicação, responde HTTP 200 com uma
página HTML ("Request Rejected") quando bloqueia o cliente. Sem esta checagem o
HTML era gravado com a extensão do dado (``.rar``) e, por ter carimbo mais novo,
passava por versão atual.

O ``quantilica-core`` valida o arquivo pela extensão do destino, e a tabela dele não
conhece ``.rar``; além disso, o IDD 2022 é um RAR5 publicado com extensão ``.zip``
e o core o recusaria como ZIP inválido. Por isso o download vai para um arquivo de
preparo ao lado do destino (:func:`caminho_de_preparo`), com extensão neutra, e só
depois de conferido aqui (:func:`validar_corpo`) ele substitui o destino
(:func:`promover`). Um destino que já existe, e o sidecar dele, nunca são tocados
por um corpo recusado.
"""

from __future__ import annotations

import json
import logging
import os
import shutil
import uuid
from pathlib import Path

from quantilica.core.exceptions import InvalidPayloadSignatureError

logger = logging.getLogger(__name__)

# Primeiros bytes de cada formato de dado do catálogo do INEP.
ASSINATURAS: dict[str, tuple[bytes, ...]] = {
    # O IDD 2022 é um RAR5 publicado como .zip: o .zip aceita também RAR.
    "zip": (b"PK\x03\x04", b"PK\x05\x06", b"Rar!\x1a\x07"),
    "xlsx": (b"PK\x03\x04", b"PK\x05\x06"),
    "rar": (b"Rar!\x1a\x07",),  # RAR 1.5-4.x (…\x00) e RAR 5 (…\x01\x00)
    "7z": (b"7z\xbc\xaf\x27\x1c",),
    # .xls: OLE2 (formato antigo) ou, em exportações recentes, um pacote OOXML.
    "xls": (b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", b"PK\x03\x04"),
}

# Menor tamanho plausível de um arquivo de dado com assinatura binária. Uma página
# de erro tem poucas centenas de bytes; o menor microdado do INEP tem centenas de KB.
TAMANHO_MINIMO = 1024

_ASSINATURA_RAR = b"Rar!\x1a\x07"

_PREFIXOS_HTML = (b"<!doctype", b"<html", b"<head", b"<body", b"<script", b"<?xml")


def extensao_de(caminho: Path | str) -> str:
    """Extensão do arquivo sem o ponto e em minúsculas (``x@1.rar`` vira ``rar``)."""
    return Path(caminho).suffix.lower().lstrip(".")


def eh_rar(caminho: Path) -> bool:
    """Se o arquivo começa com a assinatura RAR (qualquer extensão)."""
    with open(caminho, "rb") as fh:
        return fh.read(len(_ASSINATURA_RAR)) == _ASSINATURA_RAR


def validar_corpo(
    caminho: Path, ext: str | None = None, nome: str | None = None
) -> None:
    """Confere que o arquivo baixado é do formato que o nome promete.

    Só lê o cabeçalho (nada é aberto nem extraído). Extensões sem assinatura
    declarada (``csv``, por exemplo) só passam pela recusa de HTML.

    Args:
        caminho: Arquivo já gravado em disco.
        ext: Extensão esperada; por padrão a do nome do arquivo.
        nome: Nome do arquivo final, para as mensagens (``caminho`` pode ser o
            arquivo de preparo).

    Raises:
        InvalidPayloadSignatureError: corpo HTML, pequeno demais ou com
            assinatura diferente da esperada para a extensão.
    """
    ext = (ext or extensao_de(caminho)).lower().lstrip(".")
    nome = nome or caminho.name
    tamanho = caminho.stat().st_size
    with open(caminho, "rb") as fh:
        cabecalho = fh.read(512)

    inicio = cabecalho.removeprefix(b"\xef\xbb\xbf").lstrip().lower()
    if inicio.startswith(_PREFIXOS_HTML) and ext not in ("html", "htm", "xml"):
        previa = inicio[:100].decode("ascii", errors="replace")
        raise InvalidPayloadSignatureError(
            f"{nome}: o servidor devolveu uma página HTML no lugar do "
            f"arquivo .{ext} ({tamanho} bytes): {previa!r}"
        )

    assinaturas = ASSINATURAS.get(ext)
    if assinaturas is None:
        return
    if tamanho < TAMANHO_MINIMO:
        raise InvalidPayloadSignatureError(
            f"{nome}: corpo de {tamanho} bytes é pequeno demais para um "
            f"arquivo .{ext} (mínimo {TAMANHO_MINIMO})"
        )
    if not cabecalho.startswith(assinaturas):
        raise InvalidPayloadSignatureError(
            f"{nome}: assinatura {cabecalho[:8]!r} não confere com "
            f".{ext} ({tamanho} bytes)"
        )


def caminho_de_preparo(destino: Path) -> Path:
    """Arquivo de preparo ao lado do destino, com extensão neutra (``.parte``).

    A extensão neutra faz o core não aplicar ao download a validação pela extensão
    do destino (ZIP, por exemplo): a conferência é a de :func:`validar_corpo`.
    """
    return destino.with_name(f".{destino.name}.{uuid.uuid4().hex[:8]}.parte")


def sidecar_de(caminho: Path) -> Path:
    """Sidecar de proveniência do arquivo (``<arquivo>.manifest.json``)."""
    return caminho.with_suffix(caminho.suffix + ".manifest.json")


def preparar(destino: Path, preparo: Path) -> None:
    """Espelha o destino no preparo para o core decidir o frescor do mesmo jeito.

    O arquivo existente entra por link físico (ou simbólico, se o sistema de
    arquivos não os tem), sem copiar dados; o sidecar é copiado (modo efêmero:
    sem o arquivo, só o sidecar). Quando o core baixa, ele troca o preparo por um
    arquivo novo e o destino fica como estava.
    """
    if destino.exists():
        try:
            os.link(destino, preparo)
        except OSError:
            try:
                os.symlink(destino.resolve(), preparo)
            except OSError:
                logger.debug("sem link para %s: o frescor será ignorado", destino)
    sidecar = sidecar_de(destino)
    if sidecar.is_file():
        try:
            shutil.copy2(sidecar, sidecar_de(preparo))
        except OSError:  # pragma: no cover - disco com problema
            logger.debug("sidecar de %s não copiado", destino)


def baixou(destino: Path, preparo: Path) -> bool:
    """Se o core gravou um arquivo novo no preparo (e não só espelhou o destino)."""
    if not preparo.exists():
        return False
    if not destino.exists():
        return True
    return not os.path.samestat(os.stat(preparo), os.stat(destino))


def promover(preparo: Path, destino: Path) -> None:
    """Coloca o arquivo conferido (e o sidecar dele) no lugar do destino."""
    sidecar = sidecar_de(preparo)
    os.replace(preparo, destino)
    if not sidecar.exists():
        return
    final = sidecar_de(destino)
    try:
        dados = json.loads(sidecar.read_text(encoding="utf-8"))
        dados["path"] = str(destino.absolute())
        temporario = final.with_name(f".{final.name}.{uuid.uuid4().hex[:8]}.tmp")
        temporario.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        os.replace(temporario, final)
        sidecar.unlink()
    except (OSError, ValueError, TypeError):
        os.replace(sidecar, final)  # o caminho no sidecar fica o do preparo


def limpar_preparo(preparo: Path) -> None:
    """Remove o preparo e o sidecar dele, se ainda existirem."""
    for alvo in (preparo, sidecar_de(preparo)):
        try:
            alvo.unlink()
        except FileNotFoundError:
            pass
        except OSError as exc:  # pragma: no cover - disco com problema
            logger.error("Não foi possível remover %s: %s", alvo, exc)
