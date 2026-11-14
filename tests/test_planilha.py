"""Planilhas do INEP com título e cabeçalho em vários níveis."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
xlsxwriter = pytest.importorskip("xlsxwriter")
pytest.importorskip("fastexcel")

from inep_fetcher.lake import LakeConverter  # noqa: E402
from inep_fetcher.planilha import MAX_COLUMN_NAME, read_planilha  # noqa: E402

DS = "fluxo-educacao-superior"


def _valid(names: list[str]) -> bool:
    return all(
        n.strip()
        and len(n) <= MAX_COLUMN_NAME
        and not n.startswith("__UNNAMED__")
        and not any(ord(c) < 32 or 127 <= ord(c) <= 159 for c in n)
        for n in names
    ) and len(names) == len(set(names))


def _fluxo(path: Path, *, extra_cell: bool = False) -> None:
    """Título, cabeçalho de dois níveis com mesclagem, dados e notas de rodapé."""
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    sheet.write(0, 2, "Ministério da Educação\nInstituto Nacional de Estudos")
    sheet.write(1, 0, "Taxa de Evasão de Alunos no Brasil - 2010 a 2024")
    sheet.write(3, 0, "Ano Fluxo")
    sheet.write(3, 1, "Total")
    sheet.merge_range(3, 2, 3, 3, "Sexo")
    sheet.write(4, 2, "Feminino")
    sheet.write(4, 3, "Masculino")
    for i, (ano, total, fem, masc) in enumerate(
        [("2010-2011", 11.3, 10.5, 12.3), ("2011-2012", 11.1, 10.3, 12.1)]
    ):
        sheet.write(5 + i, 0, ano)
        sheet.write(5 + i, 1, total)
        sheet.write(5 + i, 2, fem)
        sheet.write(5 + i, 3, masc)
    sheet.write(8, 0, "Fonte: Censo da Educação Superior")
    sheet.write(9, 0, "Nota: 1 - não inclui alunos sem declaração")
    if extra_cell:
        sheet.write(3, 30, "Sobra")
    book.close()


def test_cabecalho_de_dois_niveis_com_titulo_e_notas(tmp_path: Path) -> None:
    src = tmp_path / "fluxo.xlsx"
    _fluxo(src)
    df = read_planilha(src, DS)
    assert df.columns == ["Ano Fluxo", "Total", "Sexo - Feminino", "Sexo - Masculino"]
    assert df.height == 2  # as notas de rodapé não são dados
    assert df["Ano Fluxo"].to_list() == ["2010-2011", "2011-2012"]
    assert df["Total"].to_list() == [11.3, 11.1]
    assert df.schema["Sexo - Feminino"] == pl.Float64


def test_celula_solta_a_direita_nao_cria_colunas(tmp_path: Path) -> None:
    src = tmp_path / "fluxo.xlsx"
    _fluxo(src, extra_cell=True)
    assert read_planilha(src, DS).width == 4


def test_titulo_longo_com_quebra_de_linha(tmp_path: Path) -> None:
    # financeiros: o título (com mais de 128 caracteres) ficava como nome de coluna
    titulo = "Estimativa do Investimento Público Direto em Educação\nPor Estudante " * 3
    book = xlsxwriter.Workbook(str(tmp_path / "fin.xlsx"))
    sheet = book.add_worksheet()
    sheet.write(0, 0, titulo)
    sheet.write(1, 0, "Ano")
    sheet.merge_range(1, 1, 1, 3, titulo)
    sheet.write(2, 1, "Todos os Níveis")
    sheet.merge_range(2, 2, 2, 3, "Níveis de Ensino")
    sheet.write(3, 2, "Educação Básica")
    sheet.write(3, 3, "Educação Superior")
    for i, ano in enumerate((2000, 2001)):
        sheet.write(4 + i, 0, ano)
        sheet.write(4 + i, 1, 2936.8 + i)
        sheet.write(4 + i, 2, 2444.7 + i)
        sheet.write(4 + i, 3, 26812.2 + i)
    book.close()
    df = read_planilha(tmp_path / "fin.xlsx", DS)
    assert _valid(df.columns)
    assert df.columns[0] == "Ano"
    assert df.columns[1] == "Todos os Níveis"
    assert df.columns[2:] == [
        "Níveis de Ensino - Educação Básica",
        "Níveis de Ensino - Educação Superior",
    ]
    assert df.schema["Ano"] == pl.Int64
    assert df.height == 2


def test_planilha_comum_nao_muda(tmp_path: Path) -> None:
    src = tmp_path / "comum.xlsx"
    pl.DataFrame({"uf": ["SP", "RJ"], "alunos": [30, 28]}).write_excel(src)
    df = read_planilha(src, DS)
    assert df.columns == ["uf", "alunos"]
    assert df["alunos"].to_list() == [30, 28]


def test_lake_converte_zip_de_indicadores_com_titulo(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "indicadores" / "fluxo-educacao-superior"
    raw.mkdir(parents=True)
    xlsx = tmp_path / "INDIC_BRASIL_2010_2024.xlsx"
    _fluxo(xlsx)
    zip_path = raw / "indicadores-fluxo-educacao-superior-brasil-2010-2024@20250902.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(xlsx, "INDIC_BRASIL_2010_2024.xlsx")
    lake = tmp_path / "lake"
    lake.mkdir()
    res = LakeConverter().convert(tmp_path / "raw", lake)
    assert not res.errors
    parquets = list((lake / "inep" / "fluxo-educacao-superior").rglob("*.parquet"))
    assert len(parquets) == 1
    df = pl.read_parquet(parquets[0])
    assert _valid(df.columns)
    assert "Sexo - Feminino" in df.columns


def _com_marcadores(path: Path) -> None:
    """Primeira linha de dados só de marcadores e uma linha com uma célula só."""
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    sheet.write(0, 0, "Variação do investimento")
    sheet.write(1, 0, "Ano")
    sheet.merge_range(1, 1, 1, 2, "Educação Básica")
    sheet.write(2, 1, "∆% Direto")
    sheet.write(2, 2, "∆% Por Estudante")
    rows = [
        (2000, "--", "-"),
        (2001, 5.1, "..."),
        (2002, "*", 3.3),
        ("Sem dado em 2003", None, None),
        (2004, 4.0, 2.0),
    ]
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            if v is not None:
                sheet.write(3 + i, j, v)
    sheet.write(9, 0, "Fonte: INEP")
    book.close()


def test_marcadores_viram_nulo_e_linha_de_uma_celula_no_meio_fica(
    tmp_path: Path,
) -> None:
    src = tmp_path / "variacao.xlsx"
    _com_marcadores(src)
    df = read_planilha(src, "financeiros")
    assert df.columns == [
        "Ano",
        "Educação Básica - ∆% Direto",
        "Educação Básica - ∆% Por Estudante",
    ]
    # a linha de marcadores é dado (não cabeçalho), o ano não vai para o nome
    assert df["Ano"].to_list() == ["2000", "2001", "2002", "Sem dado em 2003", "2004"]
    assert df["Educação Básica - ∆% Direto"].to_list() == [None, 5.1, None, None, 4.0]
    assert df.height == 5  # a linha de uma célula no meio fica; a nota final sai


def test_fora_dos_indicadores_leem_como_sempre(tmp_path: Path) -> None:
    # microdados e outras fontes: o esquema não muda, nada de detector de cabeçalho
    src = tmp_path / "fluxo.xlsx"
    _fluxo(src)
    for dataset in ("enem-por-escola", None):
        df = read_planilha(src, dataset)
        assert df.columns == pl.read_excel(src).columns
        assert df.height == pl.read_excel(src).height


def test_indicador_com_cabecalho_na_primeira_linha_nao_muda(tmp_path: Path) -> None:
    src = tmp_path / "ok.xlsx"
    pl.DataFrame(
        {"uf": ["SP", "RJ"], "taxa": [93.6, 91.2], "ano": ["2021", "2021"]}
    ).write_excel(src)
    for dataset in ("taxas-rendimento-escolar", "esforco-docente"):
        df = read_planilha(src, dataset)
        assert df.equals(pl.read_excel(src))


def _inse_2019(path: Path, *, notas: int = 2) -> None:
    """INSE 2019: notas de rodapé *acima* do cabeçalho, que traz ``*`` de remissão."""
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    textos = [
        "* Foi calculado o INSE apenas para os Municípios com 10 alunos ou mais",
        "** Não há escala interpretada do indicador. Consulte a Nota Técnica.",
    ]
    for i in range(notas):
        sheet.write(i, 0, textos[i])
    cab = ["CO_UF", "NOME_UF", "CO_MUNICIPIO*", "MEDIA_INSE**", "PC_NIVEL_1"]
    for j, nome in enumerate(cab):
        sheet.write(notas, j, nome)
    for i, linha in enumerate(
        [(11, "Rondônia", 1100015, 4.86, 0.31), (53, "DF", 5300108, 5.27, 0.3)]
    ):
        for j, v in enumerate(linha):
            sheet.write(notas + 1 + i, j, v)
    book.close()


@pytest.mark.parametrize("notas", [1, 2])
def test_inse_2019_nota_acima_do_cabecalho_nao_vira_coluna(
    tmp_path: Path, notas: int
) -> None:
    src = tmp_path / "inse.xlsx"
    _inse_2019(src, notas=notas)
    df = read_planilha(src, "nivel-socioeconomico")
    assert df.columns == [
        "CO_UF",
        "NOME_UF",
        "CO_MUNICIPIO",
        "MEDIA_INSE",
        "PC_NIVEL_1",
    ]
    assert _valid(df.columns)
    assert df.height == 2  # as notas não são dados
    assert df["CO_MUNICIPIO"].to_list() == [1100015, 5300108]
    assert df["MEDIA_INSE"].dtype == pl.Float64


def test_inse_com_cabecalho_na_primeira_linha_nao_muda(tmp_path: Path) -> None:
    # INSE 2021/2023: cabeçalho na primeira linha, sem nota acima
    src = tmp_path / "inse21.xlsx"
    pl.DataFrame({"CO_UF": [11, 53], "MEDIA_INSE": [4.86, 5.27]}).write_excel(src)
    df = read_planilha(src, "nivel-socioeconomico")
    assert df.columns == ["CO_UF", "MEDIA_INSE"]
    assert df.height == 2


def test_lake_converte_inse_2019_sem_nome_invalido(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "indicadores" / "nivel-socioeconomico"
    raw.mkdir(parents=True)
    _inse_2019(raw / "nivel-socioeconomico-inse-2019-municipios@20210602.xlsx")
    lake = tmp_path / "lake"
    lake.mkdir()
    res = LakeConverter().convert(tmp_path / "raw", lake)
    assert not res.errors
    parquets = list((lake / "inep" / "nivel-socioeconomico").rglob("*.parquet"))
    assert len(parquets) == 1
    df = pl.read_parquet(parquets[0])
    assert _valid(df.columns)
    assert df.height == 2


# --- indicadores com cabeçalho em níveis (taxas, AFD, esforço docente...) -------

TAXAS = "taxas-transicao"


def _taxas(path: Path, *, codigos: bool = True, primeira_so_supressao: bool = False):
    """Título, cabeçalho em 3 níveis mesclados, nomes técnicos, dados e rodapé.

    Layout (colunas): 0 Ano | 1 UF | 2-6 Taxa de Promoção (Ensino Fundamental:
    Total, Anos Iniciais, Anos Finais; Ensino Médio: sem subnível, 2 colunas) |
    7-8 Taxa de Evasão (Ensino Fundamental sem subnível)
    """
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    sheet.write(0, 1, "Ministério da Educação")
    sheet.write(1, 1, "Instituto Nacional de Estudos e Pesquisas Educacionais")
    sheet.write(2, 0, "Fluxo Escolar - Taxas de Transição (1)")
    sheet.write(3, 0, "Taxas de Transição(1) por unidade geográfica")
    sheet.write(4, 0, "Ano")
    sheet.write(4, 1, "Unidade da Federação")
    sheet.merge_range(4, 2, 4, 6, "Taxa de Promoção")
    sheet.merge_range(4, 7, 4, 8, "Taxa de Evasão (2)")
    sheet.merge_range(5, 2, 5, 4, "Ensino Fundamental")
    sheet.merge_range(5, 5, 5, 6, " Ensino Médio")
    sheet.merge_range(5, 7, 5, 8, "Ensino Fundamental")
    sheet.write(6, 2, "Total")
    sheet.write(6, 3, "Anos Iniciais")
    sheet.write(6, 4, "Anos Finais")
    sheet.write(6, 5, "1ª série")
    sheet.write(6, 6, "2ª série")
    sheet.write(6, 7, "Total")
    sheet.write(6, 8, "Anos Iniciais")
    linha = 7
    if codigos:
        nomes = ["NU_ANO_CENSO", "NO_UF", "PROM_FUN", "PROM_AI", "PROM_AF"]
        nomes += ["PROM_EM1", "PROM_EM2", "EVAS_FUN", "EVAS_AI"]
        for j, nome in enumerate(nomes):
            sheet.write(linha, j, nome)
        linha += 1
    dados = [
        ("2021/2022", "Rondônia", 93.6, 95.5, 91.2, 80.1, 82.3, "--", 1.5),
        ("2021/2022", "Acre", 91.0, "--", 90.2, 79.0, 81.1, 0.4, 1.1),
    ]
    if primeira_so_supressao:
        # primeira linha de dado com quase só códigos de supressão: continua dado
        dados.insert(0, ("2021/2022", "Brasil", "d", "d", "d", "d", "d", 0.2, "d"))
    for i, linha_dados in enumerate(dados):
        for j, v in enumerate(linha_dados):
            sheet.write(linha + i, j, v)
    fim = linha + len(dados)
    sheet.write(fim, 0, "Fonte: Censo da Educação Básica/Inep.")
    sheet.write(fim + 1, 0, "Nota: (1) - Taxa de promoção: a) proporção de alunos")
    book.close()


NOMES_TAXAS = [
    "Ano",
    "Unidade da Federação",
    "Taxa de Promoção - Ensino Fundamental - Total",
    "Taxa de Promoção - Ensino Fundamental - Anos Iniciais",
    "Taxa de Promoção - Ensino Fundamental - Anos Finais",
    "Taxa de Promoção - Ensino Médio - 1ª série",
    "Taxa de Promoção - Ensino Médio - 2ª série",
    "Taxa de Evasão - Ensino Fundamental - Total",
    "Taxa de Evasão - Ensino Fundamental - Anos Iniciais",
]


@pytest.mark.parametrize("codigos", [True, False])
def test_tres_niveis_mesclados_viram_um_nome_so(tmp_path: Path, codigos: bool) -> None:
    src = tmp_path / "taxas.xlsx"
    _taxas(src, codigos=codigos)
    df = read_planilha(src, TAXAS)
    assert df.columns == NOMES_TAXAS
    assert _valid(df.columns)
    # nenhuma linha de título, nota, cabeçalho ou rodapé vira dado
    assert df.height == 2
    assert df["Ano"].to_list() == ["2021/2022", "2021/2022"]
    assert df["Unidade da Federação"].to_list() == ["Rondônia", "Acre"]
    promocao = "Taxa de Promoção - Ensino Fundamental - Total"
    assert df[promocao].to_list() == [93.6, 91.0]
    assert df.schema[promocao] == pl.Float64
    # "--" é nulo e não rebaixa a coluna para texto
    evasao = "Taxa de Evasão - Ensino Fundamental - Total"
    assert df[evasao].to_list() == [None, 0.4]


def test_grupo_sem_subnivel_nao_herda_o_rotulo_do_vizinho(tmp_path: Path) -> None:
    # "Ensino Médio" não tem subnível de coluna Total/Anos Finais: "Anos Finais"
    # (da coluna anterior) não pode ser repetido à direita até o Ensino Médio
    src = tmp_path / "taxas.xlsx"
    _taxas(src)
    df = read_planilha(src, TAXAS)
    assert not any("Anos Finais" in c for c in df.columns[5:7])
    assert "Taxa de Promoção - Ensino Médio - 1ª série" in df.columns


def test_primeira_linha_de_dados_so_com_supressao_continua_dado(
    tmp_path: Path,
) -> None:
    src = tmp_path / "taxas.xlsx"
    _taxas(src, primeira_so_supressao=True)
    df = read_planilha(src, TAXAS)
    assert df.columns == NOMES_TAXAS
    assert df.height == 3
    assert df["Unidade da Federação"].to_list()[0] == "Brasil"
    # letras de supressão de sigilo ficam como texto na coluna
    assert df["Taxa de Promoção - Ensino Fundamental - Total"].dtype == pl.String


def test_remissao_de_nota_sai_do_nome(tmp_path: Path) -> None:
    book = xlsxwriter.Workbook(str(tmp_path / "rem.xlsx"))
    sheet = book.add_worksheet()
    sheet.write(0, 1, "Ministério da Educação")
    sheet.write(1, 0, "Remuneração média dos docentes")
    sheet.write(2, 0, "Ano")
    sheet.write(2, 1, "Número de docentes/Censo Escolar2")
    sheet.merge_range(2, 2, 2, 3, "Remuneração4 Bruta5 em R$")
    sheet.write(2, 4, "Percentual de docentes1,2 por grupo4*")
    sheet.write(3, 2, "1º quartil")
    sheet.write(3, 3, "Média6")
    for i, linha in enumerate([(2021, 36913, 8718.06, 9000.5, 86.5)]):
        for j, v in enumerate(linha):
            sheet.write(4 + i, j, v)
    sheet.write(5, 0, "Fonte: Censo da Educação Básica")
    book.close()
    df = read_planilha(tmp_path / "rem.xlsx", "remuneracao-docentes")
    assert df.columns == [
        "Ano",
        "Número de docentes/Censo Escolar",
        "Remuneração Bruta em R$ - 1º quartil",
        "Remuneração Bruta em R$ - Média",
        "Percentual de docentes por grupo",
    ]
    assert df.height == 1


def test_codigos_so_entram_quando_falta_rotulo(tmp_path: Path) -> None:
    book = xlsxwriter.Workbook(str(tmp_path / "cod.xlsx"))
    sheet = book.add_worksheet()
    sheet.write(0, 0, "Título da tabela")
    sheet.write(1, 0, "Ano")
    sheet.write(1, 2, "Taxa")
    for j, nome in enumerate(["NU_ANO_CENSO", "CO_MUN", "TX_ALGUMA"]):
        sheet.write(2, j, nome)
    sheet.write_row(3, 0, [2021, 1100015, 9.5])
    sheet.write_row(4, 0, [2021, 1100023, 8.5])
    book.close()
    df = read_planilha(tmp_path / "cod.xlsx", "taxas-nao-resposta")
    assert df.columns == ["Ano", "CO_MUN", "Taxa"]


def test_so_nomes_tecnicos_na_linha_do_cabecalho(tmp_path: Path) -> None:
    # INSE 2015 e por escola: título e nota acima, uma linha só de nomes técnicos
    book = xlsxwriter.Workbook(str(tmp_path / "inse15.xlsx"))
    sheet = book.add_worksheet()
    sheet.write(0, 0, "Indicador de Nível Socioeconômico por escola")
    sheet.write(1, 0, "*Mais informações sobre o Indicador")
    for j, nome in enumerate(["CO_ESCOLA", "NOME_ESCOLA", "INSE_VALOR_ABSOLUTO*"]):
        sheet.write(2, j, nome)
    sheet.write_row(3, 0, [11000058, "CENTRO DE ENSINO", 64.17])
    sheet.write_row(4, 0, [11000171, "CENTRO EDUCACIONAL", 54.96])
    book.close()
    df = read_planilha(tmp_path / "inse15.xlsx", "nivel-socioeconomico")
    assert df.columns == ["CO_ESCOLA", "NOME_ESCOLA", "INSE_VALOR_ABSOLUTO"]
    assert df.schema["CO_ESCOLA"] == pl.Int64
    assert df.height == 2


def test_grupos_vizinhos_sem_mescla_nao_vazam(tmp_path: Path) -> None:
    # financeiros: dois grupos lado a lado; o rótulo da última coluna de um grupo
    # ("Educação Superior") não vale para a primeira coluna do grupo seguinte
    book = xlsxwriter.Workbook(str(tmp_path / "dur.xlsx"))
    sheet = book.add_worksheet()
    sheet.write(0, 0, "Estimativa do Investimento")
    sheet.write(1, 0, "Ano")
    sheet.write(1, 1, "Duração Teórica do Ensino *  (anos)")
    sheet.write(1, 4, "Investimento Cumulativo por Estudante")
    sheet.write(2, 1, "Todos os Níveis")
    sheet.write(2, 2, "Níveis de Ensino")
    sheet.write(2, 4, "Todos os Níveis")
    sheet.write(2, 5, "Níveis de Ensino")
    sheet.write(3, 2, "Educação Básica")
    sheet.write(3, 3, "Educação Superior")
    sheet.write(3, 5, "Educação Básica")
    sheet.write(3, 6, "Educação Superior")
    sheet.write_row(4, 0, [2000, 18, 14, 4, 142778.7, 35529.6, 9252.7])
    sheet.write_row(5, 0, [2001, 18, 14, 4, 142172.5, 36190.8, 8256.2])
    sheet.write(6, 0, "Fonte: Inep/MEC")
    book.close()
    df = read_planilha(tmp_path / "dur.xlsx", "financeiros")
    assert df.columns == [
        "Ano",
        "Duração Teórica do Ensino (anos) - Todos os Níveis",
        "Duração Teórica do Ensino (anos) - Níveis de Ensino - Educação Básica",
        "Duração Teórica do Ensino (anos) - Níveis de Ensino - Educação Superior",
        "Investimento Cumulativo por Estudante - Todos os Níveis",
        "Investimento Cumulativo por Estudante - Níveis de Ensino - Educação Básica",
        "Investimento Cumulativo por Estudante - Níveis de Ensino - Educação Superior",
    ]
    assert df.height == 2


def test_rodape_so_sai_no_fim_e_dados_nao_se_perdem(tmp_path: Path) -> None:
    src = tmp_path / "taxas.xlsx"
    _taxas(src)
    raw = pl.read_excel(src, has_header=False)
    numericas = sum(
        1
        for r in raw.rows()
        if sum(1 for v in r if isinstance(v, (int, float)) or str(v)[:1].isdigit()) >= 3
    )
    assert read_planilha(src, TAXAS).height == numericas == 2


def test_lake_converte_zip_de_taxas_sem_coluna_sem_nome(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "indicadores" / TAXAS
    raw.mkdir(parents=True)
    xlsx = tmp_path / "TX_TRANSICAO_BRASIL_REGIOES_UFS_2021_2022.xlsx"
    _taxas(xlsx)
    zip_path = (
        raw / "taxas-transicao-tx-transicao-brasil-regioes-ufs-2021-2022@20250826.zip"
    )
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(xlsx, "TX_TRANSICAO_BRASIL_REGIOES_UFS_2021_2022.xlsx")
    lake = tmp_path / "lake"
    lake.mkdir()
    res = LakeConverter().convert(tmp_path / "raw", lake)
    assert not res.errors
    parquets = list((lake / "inep" / TAXAS).rglob("*.parquet"))
    assert len(parquets) == 1
    df = pl.read_parquet(parquets[0])
    assert df.columns == NOMES_TAXAS
    assert df.height == 2
