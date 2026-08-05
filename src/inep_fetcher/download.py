"""Download functions for inep-fetcher."""

import concurrent.futures
import contextlib
import datetime as dt
import ssl
import time
from pathlib import Path

import certifi
from quantilica.core.http import HttpClient, ProgressCallback
from quantilica.core.logging import get_logger
from quantilica.core.progress import batch_progress, file_progress

from .catalog import DatasetEntry, expand_group, list_datasets
from .storage import DataRepository

logger = get_logger(__name__)

# (entry, exception) pairs for datasets that failed to download.
DownloadError = tuple[DatasetEntry, Exception]

_CERTS_DIR = Path(__file__).parent / "_certs"
_EXTRA_CA = _CERTS_DIR / "rnp_icpedu_gr46_ov_tls_ca_2025.pem"


def _build_ssl_context() -> ssl.SSLContext:
    """Build a TLS verification context with the RNP/ICPEdu intermediate CA.

    ``download.inep.gov.br`` (domínio de todos os downloads do INEP) só serve
    o certificado-folha na negociação TLS, sem a CA intermediária
    ("RNP ICPEdu GR46 OV TLS CA 2025") — confirmado ao vivo via curl/openssl.
    Isso quebra a verificação padrão do httpx/certifi com
    ``SSLCertVerificationError: unable to get local issuer certificate``.
    A CA que falta é emitida pela raiz pública GlobalSign Root R46 (já
    presente no bundle do certifi); só falta o elo intermediário, que
    carregamos aqui a partir de ``_certs/``. Montamos o contexto em memória
    (sem escrever bundle combinado em disco) para não depender de um
    diretório de pacote gravável em produção.
    """
    ctx = ssl.create_default_context(cafile=certifi.where())
    ctx.load_verify_locations(cafile=str(_EXTRA_CA))
    return ctx


client = HttpClient(
    timeout=300.0,  # SAEB tem arquivos de ~700MB, ANA ~190MB — bem acima da média
    verify=_build_ssl_context(),  # type: ignore[arg-type]  # httpx aceita ssl.SSLContext
    headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/142.0.0.0 Safari/537.36"
        ),
    },
)


def _safe_head_date(url: str) -> dt.date | None:
    with contextlib.suppress(Exception):
        return client.head_last_modified_date(url)
    return None


def download_file(
    url: str,
    output: Path,
    *,
    progress: ProgressCallback | None = None,
) -> Path:
    """Download a single file, writing atomically with a manifest."""
    dataset_id = output.parent.name
    return client.download_with_manifest(
        url,
        output,
        source_id="inep",
        dataset_id=dataset_id,
        producer="inep-fetcher",
        progress=progress,
    )


def download_entry(
    entry: DatasetEntry,
    repo: DataRepository,
    *,
    dry_run: bool = False,
    show_progress: bool = False,
    progress: ProgressCallback | None = None,
) -> Path:
    """Download one dataset entry and return the destination path."""
    last_modified = _safe_head_date(entry["url"])
    output = repo.path_for_entry(entry, last_modified=last_modified)
    if dry_run:
        return output
    if progress is not None:
        return download_file(entry["url"], output, progress=progress)
    if show_progress:
        with file_progress(output.name) as progress_cb:
            return download_file(entry["url"], output, progress=progress_cb)
    return download_file(entry["url"], output)


def download_group(
    group_id: str,
    output: Path,
    *,
    dry_run: bool = False,
    show_progress: bool = False,
    errors: list[DownloadError] | None = None,
    sleep: float = 0.0,
    workers: int = 1,
) -> list[Path]:
    """Download all datasets for one group.

    Returns the destination paths of the entries that succeeded (in
    dry-run mode, every entry "succeeds"). A failure downloading one entry
    is logged and does not stop the rest of the group; pass ``errors`` (a
    list) to collect the ``(entry, exception)`` pairs for entries that
    failed.

    ``sleep`` (seconds) is applied between requests within the group, as a
    courtesy pause for large sequential batches — negligible cost for small
    groups.
    """
    canon = expand_group(group_id)
    if not canon:
        raise ValueError(f"Unknown group: {group_id!r}")
    entries = [e for g in canon for e in list_datasets(g)]
    repo = DataRepository(output)
    paths: list[Path] = []
    with batch_progress("inep-fetcher", total=len(entries)) as batch_pbar:
        if workers > 1 and not dry_run:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {}
                for i, entry in enumerate(entries):
                    if sleep > 0 and i > 0:
                        time.sleep(sleep)
                    future = executor.submit(
                        download_entry, entry, repo, dry_run=False, show_progress=False
                    )
                    futures[future] = entry

                for future in concurrent.futures.as_completed(futures):
                    entry = futures[future]
                    try:
                        path = future.result()
                        paths.append(path)
                    except Exception as exc:
                        logger.warning("Failed to download %s: %s", entry["id"], exc)
                        if errors is not None:
                            errors.append((entry, exc))
                    finally:
                        batch_pbar.update()
        else:
            for i, entry in enumerate(entries):
                if sleep > 0 and i > 0 and not dry_run:
                    time.sleep(sleep)
                try:
                    path = download_entry(
                        entry, repo, dry_run=dry_run, show_progress=show_progress
                    )
                except Exception as exc:
                    logger.warning("Failed to download %s: %s", entry["id"], exc)
                    if errors is not None:
                        errors.append((entry, exc))
                else:
                    paths.append(path)
                finally:
                    batch_pbar.update()
    return paths


def download_all(
    output: Path,
    *,
    groups: list[str] | None = None,
    dry_run: bool = False,
    show_progress: bool = False,
    errors: list[DownloadError] | None = None,
    sleep: float = 0.0,
    workers: int = 1,
) -> list[Path]:
    """Download all (or selected) groups.

    Returns the destination paths of every entry that succeeded across all
    groups. A group whose entries all fail (or that has no entries) does not
    stop the remaining groups; pass ``errors`` (a list) to collect the
    ``(entry, exception)`` pairs for every failed entry, across all groups.

    ``sleep`` (seconds) is forwarded to :func:`download_group` and applied
    between requests within each group.
    """
    from .catalog import ALL_GROUP_KEYS

    target_groups = groups if groups is not None else ALL_GROUP_KEYS
    resolved: list[str] = []
    for g in target_groups:
        expanded = expand_group(g)
        if not expanded:
            raise ValueError(f"Unknown group: {g!r}")
        for canon in expanded:
            if canon not in resolved:
                resolved.append(canon)

    paths: list[Path] = []
    for group_id in resolved:
        paths.extend(
            download_group(
                group_id,
                output,
                dry_run=dry_run,
                show_progress=show_progress,
                errors=errors,
                sleep=sleep,
                workers=workers,
            )
        )
    return paths
