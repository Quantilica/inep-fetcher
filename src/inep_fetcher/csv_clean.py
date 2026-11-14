"""Limpeza dos CSVs de indicadores exportados de planilha (títulos e colunas vazias).

Só a biblioteca padrão, em fluxo (nunca o arquivo inteiro em memória). Dois
defeitos que o DuckDB não resolve:

- **Linhas de título acima do cabeçalho** ("Ministério da Educação;;;",
  "Resultados ENADE 2004;;;", linha vazia): o DuckDB toma a primeira linha por
  cabeçalho, o título vira o nome da 1ª coluna e o resto vira ``columnNN``.
- **Colunas finais sem nome e sem nenhum valor** (``;;;;`` no fim de cada linha;
  o CSV do conceito ENADE 2017 chega a 16382 colunas).

Escolha de projeto: só o título, sem coluna a descartar, **não reescreve** o
arquivo; ``clean_csv`` devolve ``skip`` (linhas do título) e o DuckDB lê o
original com ``skip=N``, exatamente como lia antes. Quando há colunas a
descartar, o arquivo é reescrito por um separador de campos próprio que
**preserva o texto bruto de cada campo** (aspas incluídas): o módulo ``csv`` da
biblioteca padrão tiraria as aspas de ``"FACULDADE X" - FX``, que o DuckDB
mantém.
"""

from __future__ import annotations

import logging
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

#: Quantos registros do topo são examinados atrás do cabeçalho.
_MAX_TITLE_ROWS = 30
#: Linha só de números é dado: uma linha de dados nunca vira cabeçalho.
_NUMERIC_CHARS = frozenset("0123456789.,-+ ")


@dataclass(frozen=True)
class CsvCleanup:
    """Plano de leitura: pular ``skip`` linhas e/ou ler ``path`` em vez do original.

    ``path`` é ``None`` quando só há título a pular (o original serve, com
    ``skip=N``); senão é o CSV reescrito (que já não tem título: ``skip`` = 0).
    """

    skip: int
    path: Path | None
    title_rows: int
    columns_before: int
    columns_after: int


def split_raw(line: str, sep: str) -> tuple[list[str], bool]:
    """Separa um registro em campos **brutos** (aspas preservadas).

    Aspas só valem no início do campo (como no DuckDB). Devolve também se o
    registro ficou aberto (campo entre aspas que continua na linha seguinte).
    """
    fields: list[str] = []
    i, n = 0, len(line)
    while True:
        if i < n and line[i] == '"':
            j = i + 1
            while True:
                k = line.find('"', j)
                if k < 0:
                    return [*fields, line[i:]], True
                if k + 1 < n and line[k + 1] == '"':
                    j = k + 2
                    continue
                break
            end = line.find(sep, k + 1)
            if end < 0:
                fields.append(line[i:])
                return fields, False
            fields.append(line[i:end])
            i = end + 1
            continue
        end = line.find(sep, i)
        if end < 0:
            fields.append(line[i:])
            return fields, False
        fields.append(line[i:end])
        i = end + 1


def _records(src: Path, sep: str, encoding: str) -> Iterator[tuple[list[str], int]]:
    """Registros do CSV como (campos brutos, nº de linhas físicas)."""
    with open(src, encoding=encoding, newline="") as fh:
        pending = ""
        lines = 0
        for raw in fh:
            line = raw.rstrip("\r\n")
            if pending:
                line = f"{pending}\n{line}"
            lines += 1
            fields, open_ = split_raw(line, sep)
            if open_:
                pending = line
                continue
            pending = ""
            yield fields, lines
            lines = 0
        if pending:
            yield split_raw(pending, sep)[0], lines


def _text(cell: str) -> str:
    """Conteúdo do campo sem espaços nem as aspas que o envolvem."""
    cell = cell.strip()
    if len(cell) >= 2 and cell[0] == '"' and cell[-1] == '"':
        cell = cell[1:-1].replace('""', '"')
    return cell.strip()


def _non_empty(cells: list[str]) -> list[int]:
    return [i for i, c in enumerate(cells) if _text(c)]


def _is_numeric(cell: str) -> bool:
    cell = _text(cell)
    return bool(cell) and all(ch in _NUMERIC_CHARS for ch in cell)


def _header_index(rows: list[list[str]]) -> int:
    """Posição do cabeçalho nas primeiras linhas; 0 quando não há título.

    Título é a linha do topo vazia ou só com a 1ª célula preenchida (e não
    numérica: um número sozinho na 1ª coluna é dado). O cabeçalho é a primeira
    linha com duas células ou mais, desde que não seja só de números (senão
    seria dado, e o arquivo não tem título).
    """
    for idx, cells in enumerate(rows):
        filled = _non_empty(cells)
        if len(filled) >= 2:
            if idx and all(_is_numeric(cells[i]) for i in filled):
                return 0
            return idx
        if filled and (filled[0] != 0 or _is_numeric(cells[0])):
            return 0  # 1 célula fora da 1ª coluna, ou número: é dado, não título
    return 0


def _head(src: Path, sep: str, encoding: str) -> list[tuple[list[str], int]]:
    head: list[tuple[list[str], int]] = []
    for rec in _records(src, sep, encoding):
        head.append(rec)
        if len(head) >= _MAX_TITLE_ROWS:
            break
    return head


def detect_separator(
    src: Path, candidates: tuple[str, ...], default: str, *, encoding: str = "latin-1"
) -> str:
    """Separador do cabeçalho, quando o do ``default`` (1ª linha) não o separa.

    O título pode não ter o separador do dado. Só troca ``default`` se ele deixa
    o cabeçalho com menos de duas células e outro candidato deixa duas ou mais
    (vence o de mais células; empate, a ordem de ``candidates``).
    """

    def header_cells(sep: str) -> int:
        head = _head(src, sep, encoding)
        if not head:
            return 0
        rows = [r for r, _ in head]
        return len(_non_empty(rows[_header_index(rows)]))

    if header_cells(default) >= 2:
        return default
    best, score = default, 1
    for sep in candidates:
        if sep == default:
            continue
        cells = header_cells(sep)
        if cells > score:
            best, score = sep, cells
    return best


def clean_csv(
    src: Path, sep: str, workdir: Path, *, encoding: str = "latin-1"
) -> CsvCleanup | None:
    """Plano de limpeza de ``src``, ou ``None`` se o arquivo já está bom.

    Coluna sem nome **e** sem nenhum valor sai; coluna sem nome com algum valor
    fica, com o nome ``columnNN`` (NN = posição original, base 0, como o
    DuckDB); coluna com nome fica mesmo vazia. O arquivo reescrito mantém a
    codificação de ``src``.
    """
    head = _head(src, sep, encoding)
    if not head:
        return None
    skip_rows = _header_index([r for r, _ in head])
    skip_lines = sum(lines for _, lines in head[:skip_rows])
    header = head[skip_rows][0]

    # Passagem 1: quais colunas sem nome têm algum valor, e a largura máxima.
    width = len(header)
    remaining = {i for i, c in enumerate(header) if not _text(c)}
    first_unnamed = min(remaining, default=width)
    beyond_used: set[int] = set()  # colunas além do cabeçalho com valor
    for n, (row, _) in enumerate(_records(src, sep, encoding)):
        if n <= skip_rows:
            continue
        for i in range(len(header), len(row)):
            if _text(row[i]):
                beyond_used.add(i)
        width = max(width, len(row))
        if remaining and any(c for c in row[first_unnamed:]):
            remaining.difference_update(
                i for i in list(remaining) if i < len(row) and _text(row[i])
            )

    # colunas além do cabeçalho não têm nome: as vazias saem como as demais
    drop = remaining | {i for i in range(len(header), width) if i not in beyond_used}
    if not drop:
        if not skip_rows:
            return None
        logger.info("%s: %d linha(s) de título puladas", src.name, skip_lines)
        return CsvCleanup(skip_lines, None, skip_rows, width, width)

    kept = [i for i in range(width) if i not in drop]
    out = workdir / f"{abs(hash(src))}.clean.csv"
    with open(out, "w", encoding=encoding, newline="") as fh:
        names = [
            header[i] if i < len(header) and _text(header[i]) else f"column{i:02d}"
            for i in kept
        ]
        fh.write(sep.join(names) + "\n")
        for n, (row, _) in enumerate(_records(src, sep, encoding)):
            if n <= skip_rows or row == [""]:  # linha em branco
                continue
            ln = len(row)
            fh.write(sep.join(row[i] if i < ln else "" for i in kept) + "\n")
    logger.info(
        "%s: %d linha(s) de título puladas; %d -> %d colunas",
        src.name,
        skip_rows,
        width,
        len(kept),
    )
    return CsvCleanup(0, out, skip_rows, width, len(kept))
