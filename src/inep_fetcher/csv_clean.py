"""Limpeza dos CSVs de indicadores exportados de planilha (títulos e colunas vazias).

Só a biblioteca padrão, em fluxo (nunca o arquivo inteiro em memória). Dois
defeitos que o DuckDB não resolve:

- **Linhas de título acima do cabeçalho** ("Ministério da Educação;;;",
  "Resultados ENADE 2004;;;", linha vazia): o DuckDB toma a primeira linha por
  cabeçalho, o título vira o nome da 1ª coluna e o resto vira ``columnNN``.
- **Colunas finais sem nome e sem nenhum valor** (``;;;;`` no fim de cada linha;
  o CSV do conceito ENADE 2017 chega a 16382 colunas).

O arquivo só é reescrito quando algo muda; senão ``clean_csv`` devolve ``None``
e o original segue direto para o DuckDB.
"""

from __future__ import annotations

import csv
import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

#: Quantas linhas do topo são examinadas atrás do cabeçalho.
_MAX_TITLE_ROWS = 30
#: Linha só de números é dado: uma linha de dados nunca vira cabeçalho.
_NUMERIC_CHARS = frozenset("0123456789.,-+ ")


@dataclass(frozen=True)
class CsvCleanup:
    """Resultado de uma limpeza: o CSV novo e o que mudou."""

    path: Path
    title_rows: int
    columns_before: int
    columns_after: int


def _non_empty(cells: list[str]) -> list[int]:
    return [i for i, c in enumerate(cells) if c.strip()]


def _is_numeric(cell: str) -> bool:
    cell = cell.strip()
    return bool(cell) and all(ch in _NUMERIC_CHARS for ch in cell)


def _header_index(rows: list[list[str]]) -> int:
    """Posição do cabeçalho nas primeiras linhas; 0 quando não há título.

    Título é a linha do topo vazia ou só com a 1ª célula preenchida. O
    cabeçalho é a primeira linha com duas células ou mais, desde que não seja
    só de números (senão seria dado, e o arquivo não tem título).
    """
    for idx, cells in enumerate(rows):
        filled = _non_empty(cells)
        if len(filled) >= 2:
            if idx and all(_is_numeric(cells[i]) for i in filled):
                return 0
            return idx
        if filled and filled[0] != 0:
            return 0  # linha de 1 célula fora da 1ª coluna: não é título
    return 0


def _read_rows(src: Path, sep: str, encoding: str):
    with open(src, encoding=encoding, newline="") as fh:
        yield from csv.reader(fh, delimiter=sep)


def clean_csv(
    src: Path, sep: str, workdir: Path, *, encoding: str = "latin-1"
) -> CsvCleanup | None:
    """Reescreve ``src`` sem título e sem colunas finais vazias, ou ``None``.

    Coluna sem nome **e** sem nenhum valor sai; coluna sem nome com algum valor
    fica, com o nome ``columnNN`` (NN = posição original, base 0, como o
    DuckDB); coluna com nome fica mesmo vazia. O arquivo novo mantém a
    codificação de ``src``.
    """
    head: list[list[str]] = []
    for i, row in enumerate(_read_rows(src, sep, encoding)):
        head.append(row)
        if i + 1 >= _MAX_TITLE_ROWS:
            break
    if not head:
        return None
    skip = _header_index(head)
    header = head[skip]

    # Passagem 1: quais colunas sem nome têm algum valor, e a largura máxima.
    width = len(header)
    unnamed_in_header = {i for i, c in enumerate(header) if not c.strip()}
    first_unnamed = min(unnamed_in_header, default=width)
    remaining = set(unnamed_in_header)  # sem nome e ainda sem valor visto
    beyond_used: set[int] = set()  # colunas além do cabeçalho com valor
    for n, row in enumerate(_read_rows(src, sep, encoding)):
        if n <= skip:
            continue
        if len(row) > width:
            for i in range(width, len(row)):
                if row[i].strip():
                    beyond_used.add(i)
            width = len(row)
        if remaining and any(row[first_unnamed:]):
            found = [i for i in remaining if i < len(row) and row[i].strip()]
            remaining.difference_update(found)

    # colunas além do cabeçalho: sem nome; as vazias entram em ``drop``
    drop = remaining | {i for i in range(len(header), width) if i not in beyond_used}
    if not skip and not drop:
        return None

    kept = [i for i in range(width) if i not in drop]
    out = workdir / f"{abs(hash(src))}.clean.csv"
    with open(out, "w", encoding=encoding, newline="") as fh:
        writer = csv.writer(fh, delimiter=sep, lineterminator="\n")
        names = [
            header[i] if i < len(header) and header[i].strip() else f"column{i:02d}"
            for i in kept
        ]
        writer.writerow(names)
        for n, row in enumerate(_read_rows(src, sep, encoding)):
            if n <= skip or not row:
                continue
            ln = len(row)
            writer.writerow([row[i] if i < ln else "" for i in kept])
    result = CsvCleanup(out, skip, width, len(kept))
    logger.info(
        "%s: %d linha(s) de título puladas; %d -> %d colunas",
        src.name,
        skip,
        width,
        len(kept),
    )
    return result
