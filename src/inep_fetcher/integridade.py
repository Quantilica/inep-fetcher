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

import contextlib
import dataclasses
import logging
import os
import re
import shutil
import threading
import time
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import Any

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


PREPARO_MAX_HORAS = 48
"""Idade (horas) a partir da qual um arquivo de preparo vira lixo, mesmo de pid vivo."""


def caminho_de_preparo(destino: Path) -> Path:
    """Arquivo de preparo ao lado do destino: ``.<nome>.<pid>-<id>.parte.tmp``.

    A extensão neutra faz o core não aplicar ao download a validação pela extensão
    do destino (ZIP, por exemplo): a conferência é a de :func:`validar_corpo`. O
    sufixo ``.tmp`` faz ``select_current``, a ingestão e a auditoria o ignorarem
    se uma execução morta o deixar para trás, e o pid dono permite a
    :func:`limpar_preparos_orfaos` saber se o dono ainda existe.
    """
    sufixo = f"{os.getpid()}-{uuid.uuid4().hex[:8]}"
    return destino.with_name(f".{destino.name}.{sufixo}.parte.tmp")


def _pid_vivo(pid: int) -> bool:
    """Se ``pid`` é um processo vivo neste host (no Windows, assume que sim)."""
    if pid <= 0:
        return False
    if os.name == "nt":  # os.kill(pid, 0) lá equivale a Ctrl+C
        return True
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except OSError:  # PermissionError: existe, é de outro usuário
        return True
    return True


def limpar_preparos_orfaos(destino: Path, *, agora: float | None = None) -> int:
    """Apaga o preparo de execução morta que ficou ao lado de ``destino``.

    Cobre o preparo (``.<nome>.<pid>-<id>.parte.tmp``), o sidecar dele, o ``.tmp``
    parcial que o core deixa ao lado do preparo e os preparos do formato antigo
    (``.<nome>.<id>.parte``, sem pid). Um preparo é órfão quando o pid dono morreu
    ou quando passou de :data:`PREPARO_MAX_HORAS` (formato antigo: só pela idade).
    Só toca nomes deste destino; o destino e o sidecar dele nunca são removidos.
    Devolve quantos arquivos removeu.
    """
    agora = time.time() if agora is None else agora
    padrao = re.compile(
        rf"^\.{{1,2}}{re.escape(destino.name)}\.(?:(?P<pid>\d+)-)?[0-9a-f]{{8}}"
        r"\.parte(?:\.tmp)?(?:\.manifest\.json)?(?:\.[a-z0-9_]{8}\.tmp)?$"
    )
    removidos = 0
    try:
        entradas = list(os.scandir(destino.parent))
    except OSError:
        return 0
    for entrada in entradas:
        achado = padrao.match(entrada.name)
        if achado is None or not entrada.is_file(follow_symlinks=False):
            continue
        try:
            velho = agora - entrada.stat(follow_symlinks=False).st_mtime > (
                PREPARO_MAX_HORAS * 3600
            )
        except OSError:
            continue
        pid = achado["pid"]
        morto = pid is not None and not _pid_vivo(int(pid))
        if not (velho or morto):
            continue
        try:
            os.unlink(entrada.path)
        except OSError as exc:  # pragma: no cover - disco com problema
            logger.warning("Não foi possível remover %s: %s", entrada.path, exc)
        else:
            removidos += 1
            logger.info("Removido preparo órfão %s", entrada.name)
    return removidos


def sidecar_de(caminho: Path) -> Path:
    """Sidecar de proveniência do arquivo (``<arquivo>.manifest.json``)."""
    return caminho.with_suffix(caminho.suffix + ".manifest.json")


def preparar(destino: Path, preparo: Path) -> None:
    """Espelha o destino no preparo para o core decidir o frescor do mesmo jeito.

    O arquivo existente entra por link físico (ou simbólico, se o sistema de
    arquivos não os tem), sem copiar dados; o sidecar é copiado (modo efêmero:
    sem o arquivo, só o sidecar). Quando o core baixa, ele troca o preparo por um
    arquivo novo e o destino fica como estava. Antes, apaga o preparo órfão que uma
    execução morta deixou ao lado do destino (:func:`limpar_preparos_orfaos`).
    """
    limpar_preparos_orfaos(destino)
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
    """Coloca o arquivo conferido (e o sidecar dele) no lugar do destino.

    O sidecar é regravado com ``write_manifest_sidecar`` do core, com o
    ``path`` do destino; sem ele (core antigo) o sidecar do preparo é movido.
    """
    sidecar = sidecar_de(preparo)
    manifesto = _ler_manifesto(preparo) if sidecar.exists() else None
    os.replace(preparo, destino)
    if not sidecar.exists():
        return
    try:
        if manifesto is None:
            raise ValueError("sem manifesto legível")
        from quantilica.core.manifests import write_manifest_sidecar

        write_manifest_sidecar(
            destino, dataclasses.replace(manifesto, path=str(destino.absolute()))
        )
        sidecar.unlink()
    except (ImportError, OSError, ValueError, TypeError):
        os.replace(
            sidecar, sidecar_de(destino)
        )  # o caminho no sidecar fica o do preparo


def _ler_manifesto(preparo: Path) -> Any | None:
    try:
        from quantilica.core.manifests import read_manifest_sidecar

        return read_manifest_sidecar(preparo)
    except Exception:  # noqa: BLE001 - core antigo ou sidecar ilegível
        return None


# --- tamanho conferido pelo servidor ---------------------------------------------
# O core exige quebra de linha final num .csv/.tsv/.txt quando o tamanho do
# download não pôde ser conferido (sem Content-Length nem total de Content-Range):
# é o sinal de transferência truncada. Como o download vai para um preparo de
# extensão neutra, a checagem do core não vale para ele; o plugin repete a regra
# a partir dos cabeçalhos da resposta, observados por :func:`observar_tamanho`.

_observado = threading.local()
_TOTAL_DO_RANGE = re.compile(r"^bytes\s+(?:\d+-\d+|\*)/(\d+)$", re.IGNORECASE)


def _tamanho_anunciado(cabecalhos: Any) -> bool:
    comprimento = str(cabecalhos.get("Content-Length") or "").strip()
    if comprimento.isdigit() and int(comprimento) > 0:
        return True
    return _TOTAL_DO_RANGE.match(str(cabecalhos.get("Content-Range") or "")) is not None


def observar_tamanho(cliente: Any) -> None:
    """Faz ``cliente.stream`` anotar (por thread) se a resposta anunciou o tamanho.

    Idempotente; sem efeito num cliente sem ``stream``.
    """
    original = getattr(cliente, "stream", None)
    if original is None or getattr(original, "_inep_observa", False):
        return

    @contextlib.contextmanager
    def stream(*args: Any, **kwargs: Any) -> Iterator[Any]:
        with original(*args, **kwargs) as resposta:
            try:
                _observado.verificado = _tamanho_anunciado(resposta.headers)
            except Exception:  # noqa: BLE001
                _observado.verificado = False
            yield resposta

    stream._inep_observa = True  # type: ignore[attr-defined]
    try:
        cliente.stream = stream
    except (AttributeError, TypeError):  # pragma: no cover - cliente imutável
        pass


def esquecer_tamanho() -> None:
    """Zera a observação desta thread (chamar antes de cada download)."""
    _observado.verificado = False


def tamanho_conferido() -> bool:
    """Se a última resposta desta thread anunciou o tamanho do corpo."""
    return bool(getattr(_observado, "verificado", False))


def limpar_preparo(preparo: Path) -> None:
    """Remove o preparo e o sidecar dele, se ainda existirem."""
    for alvo in (preparo, sidecar_de(preparo)):
        try:
            alvo.unlink()
        except FileNotFoundError:
            pass
        except OSError as exc:  # pragma: no cover - disco com problema
            logger.error("Não foi possível remover %s: %s", alvo, exc)
