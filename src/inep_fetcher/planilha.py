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
_CONTROL_RUN = re.compile(
    "[\\x00-\\x20\\x7f-\\xa0\\u200b-\\u200f\\u2028\\u2029\\ufeff]+"
)
_BLANK_NAME = re.compile(r"(_duplicated_\d+|__UNNAMED__\d+)?")
_NUMBER = re.compile(r"-?\d+(\.\d+)?([eE][-+]?\d+)?")
_INTEGER = re.compile(r"-?(0|[1-9]\d*)")
_SEP = " - "
#: marcadores de "sem dado" dos indicadores (``--``, ``-``, ``...``, ``*``)
_NULL_MARKERS = frozenset({"--", "-", "...", "*"})


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


def _data_like(value: str) -> bool:
    """Valor de linha de dados: número, período (``2010-2011``) ou ``--``, ``*``."""
    return _numeric_like(value) or value in _NULL_MARKERS


def _header_block(rows: list[list[str]]) -> tuple[int, int] | None:
    """Intervalo ``[inicio, fim)`` das linhas de cabeçalho, ou ``None``.

    Pula as linhas de título (no máximo uma célula preenchida) e vai até a
    primeira linha de dados: a que tem metade ou mais das células numéricas
    (``8.4``, ``2010-2011``) ou de "sem dado" (``--``). Os cabeçalhos são só texto.
    """
    start = 0
    while start < len(rows) and sum(1 for v in rows[start] if v) <= 1:
        start += 1
    for i in range(start + 1, len(rows)):
        cells = [v for v in rows[i] if v]
        if len(cells) >= 2 and sum(_data_like(v) for v in cells) * 2 >= len(cells):
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


def _cell(value: Any) -> str | None:
    """Valor da célula como texto; vazio e marcadores de "sem dado" viram ``None``."""
    if value is None:
        return None
    text = str(value).strip()
    return None if not text or text in _NULL_MARKERS else str(value)


def _trim_footnotes(rows: list[list[str | None]]) -> list[list[str | None]]:
    """Tira do fim as notas de rodapé ("Fonte: ...", "Notas: ..."): texto em uma célula.

    Só o bloco final conta; uma linha de dado com uma célula só no meio da tabela
    fica. Linha final só numérica é dado.
    """
    end = len(rows)
    while end:
        cells = [v for v in rows[end - 1] if v is not None]
        if len(cells) > 1 or (len(cells) == 1 and _numeric_like(cells[0].strip())):
            break
        end -= 1
    return rows[:end]


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
    body = _trim_footnotes([[_cell(v) for v in r] for r in raw.slice(end).rows()])
    # o intervalo usado da planilha pode passar da tabela (células soltas à direita)
    used = [j for j in range(width) if any(r[j] is not None for r in body)]
    names = _names([[lvl[j] for lvl in levels] for j in used])
    columns = {f"_c{j}": _typed([row[j] for row in body]) for j in used}
    df = pl.DataFrame(columns)
    df.columns = _unique(
        [n or f"__UNNAMED__{j}" for j, n in zip(used, names, strict=True)]
    )
    return clean_columns(df)


#: datasets cujas planilhas têm título e cabeçalho em níveis. Os demais
#: indicadores seguem lidos como sempre, sem mudança de esquema.
MULTI_LEVEL_DATASETS = frozenset({"financeiros", "fluxo-educacao-superior"})


#: datasets cujas planilhas trazem notas (``* ...``) acima do cabeçalho de um nível
NOTES_ABOVE_DATASETS = frozenset({"nivel-socioeconomico"})
_FOOTNOTE_MARK = re.compile(r"\s*\*+$")


def _header_row_below_notes(source: Any, **kwargs: Any) -> int:
    """Índice da linha do cabeçalho: a primeira com duas células ou mais.

    As linhas de cima, com no máximo uma célula preenchida, são notas.
    """
    head = pl.read_excel(source, has_header=False, **kwargs).head(50)
    for i, row in enumerate(head.rows()):
        if sum(1 for v in row if _text(v)) >= 2:
            return i
    return 0


def _read_below_notes(source: Any, **kwargs: Any) -> pl.DataFrame | None:
    """Lê a planilha com o cabeçalho depois das notas; ``None`` se não há nota.

    O INSE 2019 (estados, municípios) abre com uma ou duas notas de rodapé
    (``* Não há escala...``) *acima* do cabeçalho; a nota virava o nome da
    primeira coluna e as outras ficavam ``__UNNAMED__N``. As notas saem e o
    asterisco de remissão nos nomes (``MEDIA_INSE*``) também.
    """
    row = _header_row_below_notes(source, **kwargs)
    if row == 0:
        return None
    options = {**kwargs.pop("read_options", {}), "header_row": row}
    df = pl.read_excel(source, read_options=options, **kwargs)
    df.columns = [_FOOTNOTE_MARK.sub("", _text(c)) or c for c in df.columns]
    return df


def read_planilha(
    source: Any, dataset_id: str | None = None, **kwargs: Any
) -> pl.DataFrame:
    """Lê a primeira aba de um XLSX/XLS.

    Só em ``financeiros`` e ``fluxo-educacao-superior`` (:data:`MULTI_LEVEL_DATASETS`)
    a primeira linha deixa de ser cabeçalho: quando metade ou mais dos nomes lidos
    é vazio (título e cabeçalho em vários níveis), o cabeçalho real é montado
    juntando os níveis (``" - "``), o título e as notas de rodapé saem, ``--``,
    ``-``, ``...`` e ``*`` viram nulo e as colunas numéricas voltam tipadas. Os
    demais datasets leem como ``pl.read_excel`` sempre leu.

    Exceção: em ``nivel-socioeconomico`` (:data:`NOTES_ABOVE_DATASETS`), quando
    a primeira linha é uma nota e não o cabeçalho (INSE 2019), o cabeçalho é a
    primeira linha com duas células ou mais e as notas acima saem.
    """
    df = pl.read_excel(source, **kwargs)
    if dataset_id in NOTES_ABOVE_DATASETS:
        unnamed = sum(1 for c in df.columns if _BLANK_NAME.fullmatch(_text(c)))
        if df.width > 1 and unnamed * 2 >= df.width:
            below = _read_below_notes(source, **kwargs)
            if below is not None:
                return clean_columns(below)
        return df
    if dataset_id not in MULTI_LEVEL_DATASETS:
        return df
    unnamed = sum(1 for c in df.columns if _BLANK_NAME.fullmatch(_text(c)))
    if df.width > 1 and unnamed * 2 >= df.width:
        multi = _multi_level(pl.read_excel(source, has_header=False, **kwargs))
        if multi is not None:
            return multi
    return clean_columns(df)
