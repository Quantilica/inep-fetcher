"""Leitura de planilhas do INEP com nomes de coluna válidos.

Os indicadores educacionais (``taxas-transicao``, ``esforco-docente``...) vêm em
XLSX com título, linhas em branco, notas acima da tabela, cabeçalho em dois a
quatro níveis com células mescladas e, às vezes, uma linha extra com os nomes
técnicos das colunas (``NU_ANO_CENSO``). Lidas de uma vez, a primeira linha (o
título, às vezes com centenas de caracteres) virava o nome de uma coluna e as
demais ficavam ``__UNNAMED__N``.

:func:`read_planilha` acha o cabeçalho real, junta os níveis num nome só
(``Taxa de Aprovação - Ensino Fundamental - Anos Iniciais``), tira o que não é
dado (título, notas, rodapé) e devolve colunas com nome válido e tipo certo.
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
#: período no lugar do ano (``2010-2011``, ``2021/2022``, ``2010-11``)
_PERIOD = re.compile(r"\d{4}\s*[-/]\s*\d{2,4}")
_SEP = " - "
#: marcadores de "sem dado" dos indicadores (``--``, ``-``, ``...``, ``*``)
_NULL_MARKERS = frozenset({"--", "-", "...", "*"})

#: datasets de indicadores educacionais: as planilhas passam pelo detector de
#: cabeçalho (:func:`read_planilha`). Microdados e demais fontes leem como sempre.
INDICADORES_DATASETS = frozenset(
    {
        "adequacao-formacao-docente",
        "complexidade-gestao-escola",
        "docentes-curso-superior",
        "docentes-pos-graduacao",
        "esforco-docente",
        "financeiros",
        "fluxo-educacao-superior",
        "media-alunos-por-turma",
        "media-horas-aula-diaria",
        "nivel-socioeconomico",
        "qualidade-educacao-superior",
        "regularidade-corpo-docente",
        "remuneracao-docentes",
        "taxas-distorcao-idade-serie",
        "taxas-nao-resposta",
        "taxas-rendimento-escolar",
        "taxas-transicao",
        "trajetoria-educacao-superior",
    }
)

#: quantas linhas do topo da planilha o detector examina para achar o cabeçalho
_HEAD_ROWS = 80
#: fração mínima de células numéricas (com piso de duas) para uma linha ser dado
_DATA_FRACTION = 0.1


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
    return bool(_NUMBER.fullmatch(value) or _PERIOD.fullmatch(value))


def _data_like(value: str) -> bool:
    """Valor de linha de dados: número, período (``2010-2011``) ou ``--``, ``*``."""
    return _numeric_like(value) or value in _NULL_MARKERS


# --- rótulos do cabeçalho -----------------------------------------------------

#: remissões de nota: sobrescritos (``¹²³``), asteriscos, ``(1)`` e dígitos
#: colados na palavra (``Média6``, ``docentes1,2``, ``Bruta5``)
_SUPERSCRIPT = re.compile("[¹²³⁰⁴-⁹]+")
_STAR = re.compile(r"\s*\*+")
_PAREN_NOTE = re.compile(r"\s*\(\d{1,2}\)")
_GLUED_NOTE = re.compile(r"(?<=[^\W\d_])\d{1,2}(?:,\d{1,2})*(?=\W|$)")


def _star_free(text: str) -> str:
    return _STAR.sub("", text).strip()


def _label(value: Any) -> str:
    """Rótulo de cabeçalho legível: sem remissão de nota nem espaço repetido."""
    text = _text(value)
    text = _SUPERSCRIPT.sub("", text)
    text = _STAR.sub("", text)
    text = _PAREN_NOTE.sub("", text)
    text = _GLUED_NOTE.sub("", text)
    return _CONTROL_RUN.sub(" ", text).strip(" :")


def _code_like(cell: str) -> bool:
    """Nome técnico de coluna: ``NU_ANO_CENSO``, ``TIPOLOCA``, ``no_cod``."""
    if " " in cell or cell in _NULL_MARKERS:
        return False
    return "_" in cell or (len(cell) >= 3 and cell.isupper()) or cell.islower()


def _is_code_row(cells: list[str]) -> bool:
    """Linha dos nomes técnicos das colunas: 60% ou mais das células são código."""
    filled = [c for c in cells if c]
    return len(filled) >= 2 and sum(_code_like(c) for c in filled) * 10 >= (
        len(filled) * 6
    )


def _is_data_row(cells: list[str]) -> bool:
    """Linha de dados: ao menos duas células numéricas, 10% ou mais do total."""
    filled = [c for c in cells if c]
    if len(filled) < 2:
        return False
    numeric = sum(_data_like(c) for c in filled)
    return numeric >= 2 and numeric >= _DATA_FRACTION * len(filled)


def _header_block(rows: list[list[str]]) -> tuple[int, int] | None:
    """Intervalo ``[inicio, fim)`` das linhas de cabeçalho, ou ``None``.

    Pula o que vem antes do cabeçalho (título, instituição, notas: linhas com no
    máximo uma célula preenchida) e vai até a primeira linha de dados. Os
    cabeçalhos são só texto; a linha de dados tem números, períodos ou ``--``.
    """
    start = 0
    while start < len(rows) and sum(1 for v in rows[start] if v) <= 1:
        start += 1
    for i in range(start + 1, len(rows)):
        if _is_data_row(rows[i]):
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


def _column_levels(header: list[list[str]], width: int) -> list[list[str]]:
    """Níveis de cada coluna a partir das linhas de rótulos, sem preencher à toa.

    A célula mesclada guarda o valor no canto esquerdo; o que vem à direita está
    vazio. Em vez de repetir o rótulo por todas as vazias (o que invade grupos
    vizinhos: "Anos Finais" cobrindo o Ensino Médio), cada rótulo vale só para o
    seu grupo:

    - rótulo **sem** rótulo abaixo na mesma coluna é folha: vale a própria coluna;
    - rótulo **com** rótulo abaixo na mesma coluna é grupo: vale até o próximo
      rótulo da mesma linha ou de uma linha de cima (o grupo de cima mudou).
    """
    n = len(header)
    labels = [[j for j in range(width) if header[r][j]] for r in range(n)]
    per_col: list[list[str]] = [[] for _ in range(width)]
    for r in range(n):
        for c in labels[r]:
            if not any(header[r2][c] for r2 in range(r + 1, n)):
                stop = c + 1
            else:
                stop = width
                for r2 in range(r + 1):
                    nxt = next((j for j in labels[r2] if j > c), width)
                    stop = min(stop, nxt)
            for j in range(c, min(stop, width)):
                per_col[j].append(header[r][c])
    return per_col


def _unique(names: list[str]) -> list[str]:
    """Nomes sem repetição: o DataFrame não aceita duas colunas com o mesmo nome."""
    seen: dict[str, int] = {}
    out = []
    for name in names:
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{_fit(name)[:120]}_{seen[name]}")
    return out


# --- corpo da tabela ----------------------------------------------------------


def _normalized(body: pl.DataFrame) -> pl.DataFrame:
    """Vazio e marcadores de "sem dado" viram nulo; o resto fica como veio."""
    nullish = ["", *_NULL_MARKERS]
    return body.select(
        pl.when(pl.col(c).str.strip_chars().is_in(nullish))
        .then(None)
        .otherwise(pl.col(c))
        .alias(c)
        for c in body.columns
    )


def _footer_rows(body: pl.DataFrame) -> int:
    """Quantas linhas do fim são rodapé: vazias ou com texto em uma célula só.

    Só o bloco final conta ("Fonte: ...", "Notas: ...", endereços); uma linha com
    uma célula só no meio da tabela fica, e uma linha final só numérica é dado.
    """
    tail = body.tail(500).rows()
    dropped = 0
    for row in reversed(tail):
        cells = [v for v in row if v is not None]
        if len(cells) > 1 or (len(cells) == 1 and _numeric_like(cells[0].strip())):
            break
        dropped += 1
    return dropped


def _typed(series: pl.Series) -> pl.Series:
    """Série com inteiro ou decimal quando todos os valores são numéricos."""
    present = series.drop_nulls()
    if present.len() == 0:
        return series
    if present.str.contains(f"^{_INTEGER.pattern}$").all():
        try:
            return series.cast(pl.Int64)
        except pl.exceptions.PolarsError:
            pass
    if present.str.contains(f"^{_NUMBER.pattern}$").all():
        return series.cast(pl.Float64)
    return series


def _assemble(raw: pl.DataFrame) -> pl.DataFrame | None:
    """Tabela com o cabeçalho real, ou ``None`` se não acha cabeçalho nem dados."""
    top = [[_text(v) for v in r] for r in raw.head(_HEAD_ROWS).rows()]
    block = _header_block(top)
    if block is None:
        return None
    start, end = block
    width = raw.width

    header = top[start:end]
    human = [r for r in header if not _is_code_row(r)]
    codes = [r for r in header if _is_code_row(r)]
    if human:
        labels = [[_label(v) for v in r] for r in human]
        code_row = [_star_free(v) for v in codes[-1]] if codes else [""] * width
        per_col = _column_levels(labels, width)
    else:
        # só nomes técnicos (INSE: ``MEDIA_INSE*``): a linha é o cabeçalho
        labels = [[_star_free(v) for v in codes[-1]]]
        code_row = [""] * width
        per_col = _column_levels(labels, width)

    body = _normalized(raw.slice(end))
    body = body.head(body.height - _footer_rows(body))
    # o intervalo usado da planilha pode passar da tabela (células soltas à direita)
    used = [j for j, c in enumerate(body.columns) if body[c].null_count() < body.height]
    if not used:
        return None
    names = _names([per_col[j] for j in used])
    names = [
        n or code_row[j] or f"__UNNAMED__{j}" for j, n in zip(used, names, strict=True)
    ]
    columns = [_typed(body[body.columns[j]]) for j in used]
    out = pl.DataFrame(columns)
    out.columns = _unique(names)
    return clean_columns(out)


def read_planilha(
    source: Any, dataset_id: str | None = None, **kwargs: Any
) -> pl.DataFrame:
    """Lê a primeira aba de um XLSX/XLS.

    Nos indicadores educacionais (:data:`INDICADORES_DATASETS`), quando a primeira
    linha não é o cabeçalho (algum nome de coluna lido é vazio: título, notas acima
    da tabela, cabeçalho em vários níveis), o cabeçalho real é detectado: o título
    e as notas de cima saem, os níveis mesclados (``Taxa de Promoção`` > ``Ensino
    Fundamental`` > ``Anos Iniciais``) viram um nome só (``" - "``) sem remissão de
    nota (``*``, ``¹``, ``(1)``, ``Média6``), a linha dos nomes técnicos
    (``NU_ANO_CENSO``) só entra onde falta rótulo legível, as notas do rodapé saem,
    ``--``, ``-``, ``...`` e ``*`` viram nulo e as colunas numéricas voltam tipadas.

    Planilhas que já começam no cabeçalho, e os demais datasets, leem como
    ``pl.read_excel`` sempre leu.
    """
    df = pl.read_excel(source, **kwargs)
    if dataset_id not in INDICADORES_DATASETS:
        return df
    if any(_BLANK_NAME.fullmatch(_text(c)) for c in df.columns):
        raw = pl.read_excel(source, has_header=False, **kwargs)
        repaired = _assemble(raw.cast(pl.String))
        if repaired is not None:
            return repaired
    return clean_columns(df)
