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
#: marcadores de "sem dado" dos indicadores (``--``, ``-``, ``...``, ``*``, ``***``)
_MARKER = re.compile(r"\*+|--|-|\.\.\.")
#: o mesmo, como padrão de coluna de texto (vazio também é "sem dado")
_MARKER_COLUMN = r"^(\*+|--|-|\.\.\.)?$"
#: ano solto (``2019``, ``2019.0``) e sigilo de dado (``x``): em linha de dados
_YEAR = re.compile(r"(?:19|20)\d{2}(?:\.0)?")
_SIGILO = frozenset({"x", "X"})
#: começo de nota de rodapé
_FOOTER_START = re.compile(
    r"(?i)\s*(fonte|notas?|obs|observa|\*|\(\d+\)|\d+\)|https?://)"
)

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

#: datasets cujas colunas sempre passaram por :func:`clean_columns`; nos demais,
#: planilha que já começa no cabeçalho é lida sem nenhuma alteração
_ALWAYS_CLEAN = frozenset({"financeiros", "fluxo-educacao-superior"})

#: quantas linhas do topo da planilha o detector examina para achar o cabeçalho
_HEAD_ROWS = 80
#: fração mínima de células numéricas (com piso de duas) para uma linha ser dado
_DATA_FRACTION = 0.1


def _text(value: Any) -> str:
    """Texto da célula, com controles e espaços repetidos reduzidos a um espaço."""
    return "" if value is None else _CONTROL_RUN.sub(" ", str(value)).strip()


def _cell_text(value: Any) -> str:
    """Texto da célula; número inteiro guardado como decimal (``2020.0``) é inteiro."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return _text(value)


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
    """Valor de linha de dados: número, período, ``--``, ``*`` ou ``x``."""
    return _numeric_like(value) or bool(_MARKER.fullmatch(value)) or value in _SIGILO


# --- rótulos do cabeçalho -----------------------------------------------------

#: remissões de nota: sobrescritos (``¹²³``), asteriscos, ``(1)`` e dígitos
#: colados na palavra (``Média6``, ``docentes1,2``, ``Bruta5``)
_SUPERSCRIPT = re.compile("[¹²³⁰⁴-⁹]+")
_STAR = re.compile(r"\s*\*+")
_PAREN_NOTE = re.compile(r"\s*\(\d{1,2}\)")
_GLUED_NOTE = re.compile(r"(?<=[^\W\d_])\d{1,2}(?:,\d{1,2})*(?=\W|$)")
#: ano no fim do rótulo ("Taxa de Aprovação - 2007"): muda a cada edição e não é
#: parte do nome da coluna
_TRAILING_YEAR = re.compile(r"(?<!\d{4})\s+[-\u2013]\s+(?:19|20)\d{2}$")


def _star_free(text: str) -> str:
    return _STAR.sub("", text).strip()


#: remissão separada por espaço no fim do rótulo, só onde a fonte a usa para nota
#: ("Total 1", "... Correção de Fluxo 2"); "Nível 1", "Grupo 1", "Série 4",
#: "Ano 2" e afins são parte do nome e ficam, mesmo em rótulo longo
_NOTE_HOSTS = frozenset({"total", "fluxo"})
_TRAILING_NOTE = re.compile(r"^(?P<base>.*\S)\s(?P<n>[1-9])$")


def _strip_trailing_note(text: str) -> str:
    match = _TRAILING_NOTE.match(text)
    if match and match["base"].split()[-1].casefold() in _NOTE_HOSTS:
        return match["base"]
    return text


def _label(value: Any) -> str:
    """Rótulo de cabeçalho legível: sem remissão de nota nem espaço repetido."""
    text = _text(value)
    if _MARKER.fullmatch(text):
        return ""  # "-" no lugar de célula vazia do cabeçalho
    text = _SUPERSCRIPT.sub("", text)
    text = _STAR.sub("", text)
    text = _PAREN_NOTE.sub("", text)
    text = _GLUED_NOTE.sub("", text)
    text = _TRAILING_YEAR.sub("", text)
    return _strip_trailing_note(_CONTROL_RUN.sub(" ", text).strip(" :"))


def _code_like(cell: str) -> bool:
    """Nome técnico de coluna: ``NU_ANO_CENSO``, ``TIPOLOCA``, ``no_cod``."""
    if " " in cell or _MARKER.fullmatch(cell):
        return False
    return "_" in cell or (len(cell) >= 3 and cell.isupper()) or cell.islower()


def _is_code_row(cells: list[str]) -> bool:
    """Linha dos nomes técnicos das colunas: 60% ou mais das células são código."""
    filled = [c for c in cells if c]
    return len(filled) >= 2 and sum(_code_like(c) for c in filled) * 10 >= (
        len(filled) * 6
    )


def _is_data_row(cells: list[str]) -> bool:
    """Linha de dados: ao menos duas células numéricas, 10% ou mais do total.

    Cabeçalho só com anos (``2019 | 2020 | 2021``) não é dado: ao menos uma das
    células numéricas tem de não ser um ano (taxa, código, ``--``, ``x``).
    """
    filled = [c for c in cells if c]
    if len(filled) < 2:
        return False
    numeric = [c for c in filled if _data_like(c)]
    if len(numeric) < 2 or len(numeric) < _DATA_FRACTION * len(filled):
        return False
    return any(not _YEAR.fullmatch(c) for c in numeric)


def _header_block(rows: list[list[str]]) -> tuple[int, int] | None:
    """Intervalo ``[inicio, fim)`` das linhas de cabeçalho, ou ``None``.

    Pula o que vem antes do cabeçalho (título, instituição, notas: linhas com no
    máximo uma célula preenchida) e vai até a primeira linha de dados. Os
    cabeçalhos são só texto; a linha de dados tem números, períodos, ``--`` ou
    ``x``. A primeira linha de dados com um valor só, ou sem valor nenhum
    (``Brasil | | |``), também é dado quando a seguinte é.
    """
    start = 0
    while start < len(rows) and sum(1 for v in rows[start] if v) <= 1:
        start += 1
    if start >= len(rows):
        return None
    first = next(j for j, v in enumerate(rows[start]) if v)
    for i in range(start + 1, len(rows)):
        if _is_data_row(rows[i]):
            return start, i
        cells = [j for j, v in enumerate(rows[i]) if v]
        # primeira linha de dados com um valor só, ou sem nenhum, logo antes de dados:
        # o valor é numérico (marcador e unidade entre parênteses são de cabeçalho)
        # ou a única célula, na primeira coluna, é um nome ("Brasil")
        one_value = any(
            _numeric_like(rows[i][j]) and not _YEAR.fullmatch(rows[i][j]) for j in cells
        )
        only_key = cells == [first] and not rows[i][first].startswith("(")
        if (one_value or only_key) and i + 1 < len(rows) and _is_data_row(rows[i + 1]):
            return start, i
    return None


def _levels(parts: list[str]) -> list[str]:
    """Níveis do cabeçalho de uma coluna: sem vazios nem repetidos em sequência."""
    levels: list[str] = []
    for p in parts:
        if p and (not levels or levels[-1] != p):
            levels.append(p)
    return levels


def _drop_prefixes(levels: list[str]) -> list[str]:
    """Tira o nível que só repete o começo do seguinte ("Taxa de Aprovação" antes
    de "Taxa de Aprovação - Ensino Fundamental")."""
    return [
        t
        for i, t in enumerate(levels)
        if i + 1 == len(levels) or not levels[i + 1].casefold().startswith(t.casefold())
    ]


def _title_spans(
    columns: list[list[_Span]], measure_cols: list[int], row_counts: dict[int, int]
) -> set[_Span]:
    """Rótulos que são título da tabela, não nome de coluna.

    Título é rótulo com mais de 60 caracteres que cobre todas as colunas de medida
    ("Percentual de docentes por grupo de adequação..."), ou é o único rótulo da
    sua linha, ou repete (e estende) o título de faixa de cima no mesmo trecho
    ("Taxa de Aprovação" e "Taxa de Aprovação por Localização e a Dependência...").
    O rótulo de grupo que cobre só parte das medidas (Ensino Fundamental, Ensino
    Médio) nunca é título, qualquer que seja o tamanho.
    """
    spans = {sp for col in columns for sp in col}
    titles: set[_Span] = set()
    for sp in spans:
        row, start, stop, text = sp
        if len(text) <= 60:
            continue
        covered = [m for m in measure_cols if start <= m < stop]
        covers_all = len(covered) >= 2 and len(covered) == len(measure_cols)
        sole = row_counts.get(row, 0) == 1
        elaborates = any(
            o[0] < row
            and (o[1], o[2]) == (start, stop)
            and text.casefold().startswith(o[3].casefold())
            for o in spans
        )
        if covers_all or sole or elaborates:
            titles.add(sp)
    return titles


def _names(
    columns: list[list[_Span]],
    measure_cols: list[int] | None = None,
    row_counts: dict[int, int] | None = None,
) -> list[str]:
    """Junta os níveis de cada coluna (``" - "``), sem estourar 128 caracteres.

    O título descritivo (:func:`_title_spans`) sai de todas as colunas, para os
    nomes não variarem com o tamanho do cabeçalho de cada edição; se isso deixasse
    dois nomes iguais, ele fica. O que ainda passar de 128 caracteres perde os
    níveis mais altos, um a um, e por fim é cortado.
    """
    cols: list[list[_Span]] = []
    for col in columns:
        kept: list[_Span] = []
        for sp in sorted(col):
            if sp[3] and (not kept or kept[-1][3] != sp[3]):
                kept.append(sp)
        cols.append(kept)
    full = [[sp[3] for sp in col] for col in cols]
    titles = _title_spans(cols, measure_cols or [], row_counts or {})
    levels = full
    if titles:
        short = [
            _drop_prefixes([sp[3] for sp in col if sp not in titles]) or [col[-1][3]]
            for col in cols
        ]
        before = [_SEP.join(lv) for lv in full]
        joined = [_SEP.join(lv) for lv in short]
        collides = len(set(joined)) < len(joined) and len(set(before)) == len(before)
        if not collides:
            levels = short
    names = []
    for lv in levels:
        lv = _drop_prefixes(lv)
        while len(lv) > 1 and len(_SEP.join(lv)) > MAX_COLUMN_NAME:
            lv = lv[1:]
        names.append(_fit(_SEP.join(lv)))
    return names


#: (linha do cabeçalho, coluna onde o rótulo começa, coluna onde termina, texto)
_Span = tuple[int, int, int, str]


def _column_levels(header: list[list[str]], width: int) -> list[list[_Span]]:
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
    per_col: list[list[_Span]] = [[] for _ in range(width)]
    for r in range(n):
        for c in labels[r]:
            if not any(header[r2][c] for r2 in range(r + 1, n)):
                stop = c + 1
            else:
                stop = width
                for r2 in range(r + 1):
                    nxt = next((j for j in labels[r2] if j > c), width)
                    stop = min(stop, nxt)
            stop = min(stop, width)
            for j in range(c, stop):
                per_col[j].append((r, c, stop, header[r][c]))
    return per_col


def _key_columns(sample: pl.DataFrame, used: list[int]) -> int:
    """Quantas colunas do começo são chave (ano, região, código, nome...).

    Chave é o que vem antes da primeira coluna de medida: a que tem decimal
    (``52.2``) ou marcador de "sem dado" (``--``) nas primeiras linhas de dados.
    """
    measure = r"^\s*-?\d+[.,]\d+\s*$|^\s*(--|-|\.\.\.|\*)\s*$"
    for k, j in enumerate(used):
        column = sample[sample.columns[j]].drop_nulls()
        if column.str.contains(measure).any():
            return k
    return len(used)


def _band_free(levels: list[_Span], first_col: int, key_end: int) -> list[_Span]:
    """Tira de uma coluna-chave o título de faixa que cobre também as medidas.

    Planilhas antigas põem "Taxa de Aprovação - 2007" mesclado desde a primeira
    coluna (``Ano``, ``Região``...) até o fim das taxas daquele grupo; o título é
    das medidas, não das chaves.
    """
    own = max((r for r, c, _, _ in levels), default=0)
    return [
        lv
        for lv in levels
        if not (lv[0] < own and lv[1] == first_col and lv[2] > key_end)
    ]


def _unique(names: list[str]) -> list[str]:
    """Nomes sem repetição: o DataFrame não aceita duas colunas com o mesmo nome."""
    seen: dict[str, int] = {}
    out = []
    for name in names:
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{_fit(name)[:120]}_{seen[name]}")
    return out


# --- corpo da tabela ----------------------------------------------------------


def _normalized(series: pl.Series) -> pl.Series:
    """Texto vazio e marcadores de "sem dado" viram nulo; número fica como veio."""
    if series.dtype.is_numeric():
        return series
    if series.dtype != pl.String:
        series = series.cast(pl.String)
    blank = series.str.strip_chars().str.contains(_MARKER_COLUMN)
    return pl.select(
        pl.when(blank.fill_null(False)).then(None).otherwise(series).alias(series.name)
    ).to_series()


def _numeric_cell(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    text = str(value).strip()
    return _numeric_like(text) or bool(_MARKER.fullmatch(text)) or text in _SIGILO


def _is_footer(cells: list[Any]) -> bool:
    """Linha de rodapé: vazia, com uma célula de texto ou com duas de nota.

    "Fonte: ...", "Notas: ...", endereços. Linha só numérica, ou com texto e
    números, é dado.
    """
    if not cells:
        return True
    if len(cells) == 1:
        return not _numeric_cell(cells[0])
    if len(cells) == 2:
        return not any(_numeric_cell(v) for v in cells) and any(
            len(str(v).strip()) >= 15 or _FOOTER_START.match(str(v)) for v in cells
        )
    return False


def _footer_rows(body: pl.DataFrame) -> int:
    """Quantas linhas do fim são rodapé (:func:`_is_footer`).

    Só o bloco final conta; uma linha com uma célula só no meio da tabela fica.
    """
    dropped = 0
    for row in reversed(body.tail(500).rows()):
        if not _is_footer([v for v in row if v is not None]):
            break
        dropped += 1
    return dropped


def _typed(series: pl.Series) -> tuple[pl.Series, bool]:
    """Série com inteiro ou decimal quando todo valor de texto é numérico.

    Devolve também se a coluna tem decimais em texto, que o leitor de planilhas
    corta em 9 casas e :func:`_assemble` relê como número. Código com zero à
    esquerda (``04``, ``0012``) fica texto: virar número perde o código.
    """
    if series.dtype != pl.String:
        return series, False
    present = series.drop_nulls()
    if present.len() == 0 or present.str.contains(r"^\s*-?0\d").any():
        return series, False
    if present.str.contains(f"^{_INTEGER.pattern}$").all():
        try:
            return series.cast(pl.Int64), False
        except pl.exceptions.PolarsError:
            pass
    if present.str.contains(f"^{_NUMBER.pattern}$").all():
        return series.cast(pl.Float64), True
    return series, bool(present.str.contains(r"^-?\d+\.\d+$").any())


def _read(source: Any, kwargs: dict[str, Any], **options: Any) -> pl.DataFrame:
    """Planilha sem cabeçalho, com as linhas e colunas vazias (índice = da folha).

    ``skip_rows`` conta sempre da primeira linha da folha (``0`` por padrão): sem
    ele o leitor pula as linhas vazias do começo e as leituras do topo e do corpo
    deixam de concordar sobre onde está o cabeçalho.
    """
    extra = dict(kwargs.get("read_options", {}))
    rest = {k: v for k, v in kwargs.items() if k != "read_options"}
    return pl.read_excel(
        source,
        has_header=False,
        drop_empty_rows=False,
        drop_empty_cols=False,
        read_options={"skip_rows": 0, **extra, **options},
        **rest,
    )


def _assemble(source: Any, kwargs: dict[str, Any]) -> pl.DataFrame | None:
    """Tabela com o cabeçalho real, ou ``None`` se não acha cabeçalho nem dados."""
    head = _read(source, kwargs, n_rows=_HEAD_ROWS)
    top = [[_cell_text(v) for v in r] for r in head.rows()]
    block = _header_block(top)
    if block is None:
        return None
    start, end = block
    width = head.width

    header = top[start:end]
    human = [r for r in header if not _is_code_row(r)]
    codes = [r for r in header if _is_code_row(r)]
    if human:
        labels = [[_label(v) for v in r] for r in human]
        code_row = [_star_free(v) for v in codes[-1]] if codes else [""] * width
    else:
        # só nomes técnicos (INSE: ``MEDIA_INSE*``): a linha é o cabeçalho
        labels = [[_star_free(v) for v in codes[-1]]]
        code_row = [""] * width
    spans = _column_levels(labels, width)
    row_counts = {r: sum(1 for v in row if v) for r, row in enumerate(labels)}

    # corpo todo como texto: nada é anulado nem convertido por inferência de tipo
    raw = _read(source, kwargs, skip_rows=end, dtypes="string")
    body = pl.DataFrame([_normalized(raw[c]) for c in raw.columns])
    footer = _footer_rows(body)
    blank = body.select(pl.all_horizontal(pl.all().is_null())).to_series()
    keep = ~blank & (pl.int_range(body.height, eager=True) < body.height - footer)
    body = body.filter(keep)
    if body.is_empty():
        return None
    # o intervalo usado da planilha pode passar da tabela (células soltas à direita)
    used = [j for j, c in enumerate(body.columns) if body[c].null_count() < body.height]
    key_n = _key_columns(raw.head(200), used)
    if key_n < len(used):
        first, key_end = used[0], used[key_n - 1] + 1 if key_n else used[0]
        for j in used[:key_n]:
            spans[j] = _band_free(spans[j], first, key_end)
    names = _names([spans[j] for j in used], used[key_n:], row_counts)
    names = [
        n or code_row[j] or f"__UNNAMED__{j}" for j, n in zip(used, names, strict=True)
    ]

    typed = [_typed(body[body.columns[j]]) for j in used]
    decimals = {j: "float" for j, (_, texto) in zip(used, typed, strict=True) if texto}
    if decimals:
        # o texto dos números tem 9 casas no máximo: a precisão vem da leitura como
        # número, só onde ela e o texto concordam
        exact = _read(source, kwargs, skip_rows=end, dtypes=decimals).filter(keep)
        for k, j in enumerate(used):
            if j in decimals:
                typed[k] = (_exact(typed[k][0], exact[exact.columns[j]]), False)
    out = pl.DataFrame([series for series, _ in typed])
    out.columns = _unique(names)
    return clean_columns(out)


def _exact(series: pl.Series, number: pl.Series) -> pl.Series:
    """Devolve ``series`` com a precisão de ``number`` onde os dois batem (1e-9).

    ``series`` é a coluna já tipada (Float64) ou o texto dela; ``number`` é a
    mesma coluna lida como número. Valor que só existe de um lado, ou em que o
    texto e o número divergem, fica como estava.
    """
    number = number.cast(pl.Float64, strict=False)
    if series.dtype == pl.Float64:
        parsed, decimal = series, pl.Series([True] * series.len())
    else:
        parsed = series.cast(pl.Float64, strict=False)
        decimal = series.str.contains(r"^-?\d+\.\d+$").fill_null(False)
    same = (number - parsed).abs() < 1e-9
    use = (same.fill_null(False)) & decimal
    if series.dtype == pl.Float64:
        return pl.select(pl.when(use).then(number).otherwise(series)).to_series()
    return pl.select(
        pl.when(use).then(number.cast(pl.String)).otherwise(series)
    ).to_series()


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
    ``--``, ``-``, ``...`` e ``*``/``***`` viram nulo e as colunas numéricas voltam
    tipadas, com os decimais da planilha por inteiro e o código com zero à
    esquerda (``04``) como texto.

    Planilhas que já começam no cabeçalho, e os demais datasets, leem como
    ``pl.read_excel`` sempre leu.
    """
    df = pl.read_excel(source, **kwargs)
    if dataset_id not in INDICADORES_DATASETS:
        return df
    if any(_BLANK_NAME.fullmatch(_text(c)) for c in df.columns):
        repaired = _assemble(source, kwargs)
        if repaired is not None:
            return repaired
        return clean_columns(df)
    # já começa no cabeçalho: só os datasets que sempre passaram por clean_columns
    return clean_columns(df) if dataset_id in _ALWAYS_CLEAN else df
