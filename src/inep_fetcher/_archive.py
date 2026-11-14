"""Extração de arquivos compactados do INEP: formato pelos bytes, 7-Zip de reserva.

O INEP publica RAR com extensão ``.zip`` (IDD 2022) e ZIP com membros em
Deflate64 (microdados do ENEM 2025), que o ``zipfile`` da biblioteca padrão não
lê. Este módulo só usa a biblioteca padrão (e o 7-Zip externo), então importa
sem o extra ``analysis``.

- O formato vem dos bytes mágicos, nunca da extensão.
- ZIP: o ``zipfile`` extrai o que sabe ler; os membros com método de compressão
  que ele não suporta (Deflate64, 9) vão pelo 7-Zip, direto para o disco, sem
  carregar o membro em memória.
- RAR e 7z: extração inteira pelo 7-Zip, com a estrutura de pastas (a lógica do
  lake depende da pasta ``DADOS/``). Um 7-Zip sem codec RAR (o do Fedora) cai
  para o ``libarchive-c``, se instalado.
"""

from __future__ import annotations

import logging
import os
import re
import shutil
import stat
import subprocess
import tempfile
import zipfile
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from pathlib import Path

logger = logging.getLogger(__name__)

_RAR_SIGNATURE = b"Rar!\x1a\x07"
_SEVENZIP_SIGNATURE = b"7z\xbc\xaf\x27\x1c"
_ZIP_SIGNATURES = (b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")

#: Métodos de compressão que o ``zipfile`` lê (bz2 e lzma são módulos opcionais).
_ZIPFILE_METHODS = frozenset(
    {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED, zipfile.ZIP_BZIP2, zipfile.ZIP_LZMA}
)

_SEVENZIP_HELP = (
    "instale o 7-Zip (Windows: https://www.7-zip.org/, com 7z.exe no PATH ou em "
    "%ProgramFiles%\\7-Zip; Fedora: `dnf install 7zip`; Debian/Ubuntu: "
    "`apt install 7zip`); QUANTILICA_7Z aponta outro executável"
)
_RAR_HELP = (
    "o 7-Zip instalado não tem codec RAR (o do Fedora não tem; o oficial do "
    "Windows tem). Use o 7-Zip oficial ou instale `libarchive-c` com a "
    "biblioteca libarchive do sistema"
)
#: Teto de uma extração pelo 7-Zip (o ENEM tem 2 GB; isto só evita travar para sempre).
_SEVENZIP_TIMEOUT = 6 * 3600
#: Acima disto, os nomes não vão na linha de comando (limite de ~8191 caracteres
#: do cmd.exe do Windows): extrai-se o arquivo inteiro.
_MAX_NAMES = 50
_MAX_NAMES_CHARS = 8000
_SEVENZIP_NOT_ARCHIVE = re.compile(
    r"can ?not open the file as|is not archive|unsupported", re.IGNORECASE
)


class ArchiveError(RuntimeError):
    """Arquivo compactado ilegível (corrompido ou sem ferramenta para lê-lo)."""


class SevenZipUnavailableError(ArchiveError):
    """O 7-Zip é necessário para este arquivo e não foi encontrado."""


class RarUnavailableError(ArchiveError):
    """Nenhum leitor de RAR neste ambiente (7-Zip sem codec RAR e sem libarchive)."""


def archive_kind(path: Path) -> str:
    """Tipo do arquivo pelos bytes mágicos: ``zip``, ``rar``, ``7z`` ou ``unknown``.

    Um ZIP com bytes antes do início (instalador, cabeçalho extra) não começa
    por ``PK``; ``zipfile.is_zipfile`` acha o diretório central no fim.
    """
    with open(path, "rb") as fh:
        head = fh.read(8)
    if head.startswith(_RAR_SIGNATURE):
        return "rar"
    if head.startswith(_SEVENZIP_SIGNATURE):
        return "7z"
    if head.startswith(_ZIP_SIGNATURES):
        return "zip"
    try:
        if zipfile.is_zipfile(path):
            return "zip"
    except OSError:
        pass
    return "unknown"


def find_sevenzip() -> str | None:
    """Executável do 7-Zip: ``QUANTILICA_7Z``, PATH ou ``%ProgramFiles%\\7-Zip``."""
    override = os.environ.get("QUANTILICA_7Z")
    if override:
        return override
    for exe in ("7z", "7z.exe", "7zz"):
        found = shutil.which(exe)
        if found:
            return found
    for var in ("ProgramFiles", "ProgramW6432", "ProgramFiles(x86)"):
        base = os.environ.get(var)
        if base:
            candidate = Path(base) / "7-Zip" / "7z.exe"
            if candidate.is_file():
                return str(candidate)
    return None


def _require_sevenzip(archive: Path, motivo: str) -> str:
    exe = find_sevenzip()
    if exe is None:
        raise SevenZipUnavailableError(f"{archive.name}: {motivo}; {_SEVENZIP_HELP}")
    return exe


def _sevenzip_extract(
    exe: str, archive: Path, dest: Path, names: list[str] | None = None
) -> None:
    """``7z x`` (com pastas) do arquivo inteiro ou só dos ``names``, direto no disco.

    ``-spd`` desliga curingas nos nomes; ``-aoa`` sobrescreve sem perguntar. O
    código de saída 1 do 7-Zip é só aviso ("Warnings: 1", comum em RAR): vale a
    checagem de presença dos arquivos feita por quem chama. 2 ou mais é falha.
    """
    cmd = [exe, "x", "-y", "-bd", "-aoa", f"-o{dest}"]
    if names:
        cmd.append("-spd")
    cmd += ["--", str(archive), *(names or [])]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            stdin=subprocess.DEVNULL,
            check=False,
            timeout=_SEVENZIP_TIMEOUT,
        )
    except subprocess.TimeoutExpired as exc:
        raise ArchiveError(
            f"{archive.name}: 7-Zip passou de {_SEVENZIP_TIMEOUT // 3600} h e foi "
            "interrompido"
        ) from exc
    except FileNotFoundError as exc:
        raise SevenZipUnavailableError(
            f"{archive.name}: não consegui executar {exe}; {_SEVENZIP_HELP}"
        ) from exc
    if proc.returncode not in (0, 1):
        detail = (
            proc.stderr.decode("utf-8", errors="replace")
            + proc.stdout.decode("utf-8", errors="replace")
        ).strip()
        raise ArchiveError(
            f"{archive.name}: 7-Zip falhou ({proc.returncode}): "
            f"{detail or 'sem detalhe'}"
        )
    if proc.returncode == 1:
        logger.warning("%s: 7-Zip terminou com avisos", archive.name)


def _libarchive_extract(archive: Path, dest: Path) -> list[Path]:
    """Extrai com ``libarchive-c`` (reserva para RAR quando o 7-Zip não tem o codec)."""
    try:
        import libarchive  # type: ignore[import-not-found]

        resolved = dest.resolve()
        written: list[Path] = []
        with libarchive.file_reader(str(archive)) as entries:
            for entry in entries:
                if entry.isdir:
                    continue
                target = (resolved / entry.pathname).resolve()
                if not target.is_relative_to(resolved):
                    raise ArchiveError(
                        f"{archive.name}: caminho fora do destino: {entry.pathname}"
                    )
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "wb") as out:
                    for block in entry.get_blocks():
                        out.write(block)
                written.append(target)
    except ArchiveError:
        raise
    except Exception as exc:  # libarchive-c levanta ArchiveError próprio, OSError...
        raise ArchiveError(
            f"{archive.name}: libarchive falhou ({type(exc).__name__}: {exc})"
        ) from exc
    return written


def _list_files(dest: Path) -> list[Path]:
    return sorted(p for p in dest.rglob("*") if p.is_file())


def _extract_zip(archive: Path, dest: Path) -> None:
    resolved = dest.resolve()
    unsupported: list[str] = []
    done: list[Path] = []  # o que o zipfile gravou (só isto se desfaz na reserva)
    expected = 0
    try:
        with zipfile.ZipFile(archive) as zf:
            expected = len({i.filename for i in zf.infolist() if not i.is_dir()})
            for info in zf.infolist():
                target = (resolved / info.filename).resolve()
                if not target.is_relative_to(resolved):
                    raise ArchiveError(
                        f"{archive.name}: caminho fora do destino: {info.filename}"
                    )
                if info.is_dir():
                    continue
                if info.compress_type not in _ZIPFILE_METHODS:
                    unsupported.append(info.filename)
                    continue
                zf.extract(info, resolved)
                done.append(target)
    except zipfile.BadZipFile as exc:
        raise ArchiveError(f"{archive.name}: ZIP inválido ({exc})") from exc
    if unsupported:
        logger.info(
            "%s: %d membro(s) com compressão que o zipfile não lê (Deflate64?); "
            "extraindo pelo 7-Zip",
            archive.name,
            len(unsupported),
        )
        exe = _require_sevenzip(
            archive,
            f"{len(unsupported)} membro(s) usam um método de compressão "
            f"que o Python não lê (ex.: {unsupported[0]})",
        )
        too_long = (
            len(unsupported) > _MAX_NAMES
            or sum(len(n) + 3 for n in unsupported) > _MAX_NAMES_CHARS
        )
        if not too_long:
            _sevenzip_extract(exe, archive, resolved, unsupported)
            if all((resolved / n).is_file() for n in unsupported):
                return
            logger.warning(
                "%s: o 7-Zip não achou membros pelo nome (codificação dos nomes?); "
                "extraindo o arquivo inteiro",
                archive.name,
            )
        # Linha de comando longa, ou nomes que o 7-Zip grafa de outro jeito: o
        # arquivo inteiro vai pelo 7-Zip, numa pasta de preparo dentro do destino
        # (que pode ter conteúdo de fora). Só o que o zipfile gravou é desfeito,
        # para o mesmo membro não ficar sob dois nomes.
        with _staged(resolved) as stage:
            _sevenzip_extract(exe, archive, stage)
            got = len(_list_files(stage))
            if got < expected:
                raise ArchiveError(
                    f"{archive.name}: o 7-Zip extraiu {got} de {expected} arquivos"
                )
            for p in done:
                p.unlink(missing_ok=True)


@contextmanager
def _staged(dest: Path) -> Iterator[Path]:
    """Pasta de preparo dentro de ``dest``; ao sair sem erro, move tudo para ``dest``.

    Evita limpar ou misturar com o conteúdo que já estava no destino (caso do ZIP
    aninhado) quando uma extração falha no meio ou precisa ser refeita. Em erro,
    o preparo é apagado e o destino fica como estava.
    """
    stage = Path(tempfile.mkdtemp(prefix=".extract-", dir=dest))
    try:
        yield stage
        for src in _list_files(stage):
            target = dest / src.relative_to(stage)
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(src, target)
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def _extract_with_sevenzip(archive: Path, dest: Path, kind: str) -> None:
    exe = find_sevenzip()
    with _staged(dest) as stage:
        if exe is None:
            if kind == "rar" and _libarchive_available():
                _libarchive_extract(archive, stage)
            else:
                raise SevenZipUnavailableError(
                    f"{archive.name}: arquivo {kind.upper()} requer o 7-Zip; "
                    f"{_SEVENZIP_HELP}"
                )
        else:
            try:
                _sevenzip_extract(exe, archive, stage)
            except ArchiveError as exc:
                if kind != "rar" or not _SEVENZIP_NOT_ARCHIVE.search(str(exc)):
                    raise
                if not _libarchive_available():
                    raise RarUnavailableError(f"{archive.name}: {_RAR_HELP}") from exc
                shutil.rmtree(stage)
                stage.mkdir()
                _libarchive_extract(archive, stage)
        if not _list_files(stage):
            # código 1 (aviso) sem nenhum arquivo não é sucesso
            raise ArchiveError(f"{archive.name}: o arquivo compactado não tem arquivos")


def _libarchive_available() -> bool:
    try:
        import libarchive  # type: ignore[import-not-found]  # noqa: F401
    except Exception:  # ImportError, OSError (libarchive.so ausente) e afins
        return False
    return True


def extract_archive(archive: Path, dest: Path) -> list[Path]:
    """Extrai ``archive`` em ``dest`` preservando as pastas; devolve os arquivos.

    Raises:
        ArchiveError: arquivo corrompido, formato desconhecido ou RAR sem leitor.
        SevenZipUnavailableError: o arquivo exige 7-Zip e ele não está instalado.
    """
    archive = Path(archive)
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    kind = archive_kind(archive)
    if kind == "zip":
        _extract_zip(archive, dest)
    elif kind in {"rar", "7z"}:
        _extract_with_sevenzip(archive, dest, kind)
    else:
        raise ArchiveError(
            f"{archive.name}: formato de arquivo compactado não reconhecido "
            "(nem ZIP, nem RAR, nem 7z)"
        )
    files = _list_files(dest)
    if not files:
        raise ArchiveError(f"{archive.name}: o arquivo compactado não tem arquivos")
    return files


@contextmanager
def scratch_dir() -> Iterator[Path]:
    """Diretório temporário para extrair; ``QUANTILICA_LAKE_SCRATCH`` muda o disco.

    Falha ao apagar (arquivo aberto no Windows, antivírus) vira aviso no log, não
    erro: a conversão já terminou.
    """
    tmp = Path(tempfile.mkdtemp(dir=os.environ.get("QUANTILICA_LAKE_SCRATCH") or None))

    def _warn(func: Callable[[str], object], path: str, exc: BaseException) -> None:
        # arquivo somente leitura (Windows): libera a escrita e tenta de novo
        try:
            os.chmod(path, os.stat(path).st_mode | stat.S_IWRITE)
            func(path)
            return
        except Exception:  # noqa: BLE001 - qualquer falha aqui vira aviso
            pass
        logger.warning("não consegui apagar %s: %s", path, exc)

    try:
        yield tmp
    finally:
        shutil.rmtree(tmp, onexc=_warn)
