"""Leitura de planilhas do INEP com nomes de coluna válidos.

Os indicadores educacionais (``financeiros``, ``fluxo-educacao-superior``...)
vêm em XLSX com título, linhas em branco e cabeçalho em dois ou três níveis com
células mescladas. Lidas de uma vez, a primeira linha (o título, às vezes com
quebra de linha e centenas de caracteres) virava o nome de uma coluna e as demais
ficavam ``__UNNAMED__N``.
"""

from __future__ import annotations

import re
from typing import Any

try:
    import polars as pl
except ImportError as exc:  # pragma: no cover - o extra 'analysis' traz o polars
    raise ImportError(
        "inep_fetcher.planilha requer o extra 'analysis': "
        "uv add 'inep-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

MAX_COLUMN_NAME = 128
_CONTROL_RUN = re.compile(r"[\x00-\x20\x7f-\xa0​-‏  ﻿]+")
_BLANK_NAME = re.compile(r"(_duplicated_\d+|__UNNAMED__\d+)?")
_NUMBER = re.compile(r"-?\d+(\.\d+)?([eE][-+]?\d+)?")
_INTEGER = re.compile(r"-?(0|[1-9]\d*)")
_SEP = " - "


def _text(value: Any) -> str:
    """Texto da célula, com controles e espaços repetidos reduzidos a um espaço."""
    return "" if value is None else _CONTROL_RUN.sub(" ", str(value)).strip()


def _fit(name: str) -> str:
    return name[:MAX_COLUMN_NAME].rstrip()


def clean_columns(df: pl.DataFrame) -> pl.DataFrame:
    """Garante nomes de colunas válidos: sem controle, não vazios, únicos, <= 128.

    - Controles, quebras de linha e espaços repetidos viram um espaço só.
    - Nome vazio (``__UNNAMED__N``, ``_duplicated_N``): a coluna é descartada
      quando não tem nenhum valor; com valores, ganha ``coluna_<posição>``.
    - Nome com mais de 128 caracteres é cortado; repetidos ganham ``_2``, ``_3``.
    """
    keep: list[str] = []
    final: list[str] = []
    seen: set[str] = set()
    for pos, col in enumerate(df.columns, start=1):
        name = _text(col)
        if _BLANK_NAME.fullmatch(name):
            series = df[col]
            if series.dtype == pl.String:
                series = series.str.strip_chars().replace("", None)
            if series.null_count() == series.len():
                continue
            name = f"coluna_{pos}"
        candidate, n = _fit(name), 1
        while candidate in seen:
            n += 1
            suffix = f"_{n}"
            candidate = _fit(name)[: MAX_COLUMN_NAME - len(suffix)].rstrip() + suffix
        seen.add(candidate)
        keep.append(col)
        final.append(candidate)
    out = df.select(keep)
    out.columns = final
    return out


def _numeric_like(value: str) -> bool:
    return bool(_NUMBER.fullmatch(value) or re.fullmatch(r"\d{4}-\d{2,4}", value))


def _header_block(rows: list[list[str]]) -> tuple[int, int] | None:
    """Intervalo ``[inicio, fim)`` das linhas de cabeçalho, ou ``None``.

    Pula as linhas de título (no máximo uma célula preenchida) e vai até a
    primeira linha de dados: a que tem metade ou mais das células numéricas
    (``8.4``, ``2010-2011``). Os cabeçalhos são só texto.
    """
    start = 0
    while start < len(rows) and sum(1 for v in rows[start] if v) <= 1:
        start += 1
    for i in range(start + 1, len(rows)):
        cells = [v for v in rows[i] if v]
        if len(cells) >= 2 and sum(_numeric_like(v) for v in cells) * 2 >= len(cells):
            return start, i
    return None


def _levels(parts: list[str]) -> list[str]:
    """Níveis do cabeçalho de uma coluna: sem vazios nem repetidos em sequência."""
    levels: list[str] = []
    for p in parts:
        if p and (not levels or levels[-1] != p):
            levels.append(p)
    return levels


def _names(columns: list[list[str]]) -> list[str]:
    """Junta os níveis de cada coluna (``" - "``), sem estourar 128 caracteres.

    Quando alguma coluna estoura, o título da tabela repetido nas células
    mescladas (nível com mais de 60 caracteres que aparece em duas colunas ou
    mais) sai de todas, para os nomes seguirem o mesmo critério. O que ainda
    passar do limite perde os níveis mais altos, um a um, e por fim é cortado.
    """
    levels = [_levels(c) for c in columns]
    if any(len(_SEP.join(lv)) > MAX_COLUMN_NAME for lv in levels):
        counts: dict[str, int] = {}
        for lv in levels:
            for text in set(lv):
                counts[text] = counts.get(text, 0) + 1
        titles = {t for t, n in counts.items() if n >= 2 and len(t) > 60}
        levels = [[t for t in lv if t not in titles] or lv[-1:] for lv in levels]
    names = []
    for lv in levels:
        while len(lv) > 1 and len(_SEP.join(lv)) > MAX_COLUMN_NAME:
            lv = lv[1:]
        names.append(_fit(_SEP.join(lv)))
    return names


def _typed(values: list[str | None]) -> pl.Series:
    """Série com inteiro ou decimal quando todos os valores são numéricos."""
    present = [v for v in values if v is not None]
    if present and all(_INTEGER.fullmatch(v) for v in present):
        return pl.Series(
            [None if v is None else int(v) for v in values], dtype=pl.Int64
        )
    if present and all(_NUMBER.fullmatch(v) for v in present):
        return pl.Series(
            [None if v is None else float(v) for v in values], dtype=pl.Float64
        )
    return pl.Series(values, dtype=pl.String)


def _unique(names: list[str]) -> list[str]:
    """Nomes sem repetição: o DataFrame não aceita duas colunas com o mesmo nome."""
    seen: dict[str, int] = {}
    out = []
    for name in names:
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{_fit(name)[:120]}_{seen[name]}")
    return out


def _multi_level(raw: pl.DataFrame) -> pl.DataFrame | None:
    rows = [[_text(v) for v in r] for r in raw.rows()]
    block = _header_block(rows)
    if block is None:
        return None
    start, end = block
    width = raw.width
    levels: list[list[str]] = []
    for r in range(start, end):
        row = rows[r]
        if r < end - 1:
            # mescladas dos níveis de cima: o valor vale para as vazias à direita
            filled, last = [], ""
            for v in row:
                last = v or last
                filled.append(last)
            row = filled
        levels.append(row)
    body = [
        r
        for r in raw.slice(end).rows()
        # linhas de nota de rodapé ("Fonte: ...", "Notas: ...") têm uma célula só
        if sum(1 for v in r if v is not None and str(v).strip()) > 1
    ]
    # o intervalo usado da planilha pode passar da tabela (células soltas à direita)
    used = [
        j
        for j in range(width)
        if any(r[j] is not None and str(r[j]).strip() for r in body)
    ]
    names = _names([[lvl[j] for lvl in levels] for j in used])
    columns = {
        f"_c{j}": _typed(
            [
                None if (v := row[j]) is None or not str(v).strip() else str(v)
                for row in body
            ]
        )
        for j in used
    }
    df = pl.DataFrame(columns)
    df.columns = _unique(
        [n or f"__UNNAMED__{j}" for j, n in zip(used, names, strict=True)]
    )
    return clean_columns(df)


def read_planilha(source: Any, **kwargs: Any) -> pl.DataFrame:
    """Lê a primeira aba de um XLSX/XLS com nomes de coluna válidos.

    Planilha com cabeçalho na primeira linha lê como antes. Quando a primeira
    linha não é cabeçalho (metade ou mais dos nomes vazios: título e cabeçalho em
    vários níveis), o cabeçalho real é montado juntando os níveis (``" - "``),
    o título e as notas de rodapé saem, e as colunas numéricas voltam tipadas.
    """
    df = pl.read_excel(source, **kwargs)
    unnamed = sum(1 for c in df.columns if _BLANK_NAME.fullmatch(_text(c)))
    if df.width > 1 and unnamed * 2 >= df.width:
        multi = _multi_level(pl.read_excel(source, has_header=False, **kwargs))
        if multi is not None:
            return multi
    return clean_columns(df)
