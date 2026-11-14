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
    df = read_planilha(src)
    assert df.columns == ["Ano Fluxo", "Total", "Sexo - Feminino", "Sexo - Masculino"]
    assert df.height == 2  # as notas de rodapé não são dados
    assert df["Ano Fluxo"].to_list() == ["2010-2011", "2011-2012"]
    assert df["Total"].to_list() == [11.3, 11.1]
    assert df.schema["Sexo - Feminino"] == pl.Float64


def test_celula_solta_a_direita_nao_cria_colunas(tmp_path: Path) -> None:
    src = tmp_path / "fluxo.xlsx"
    _fluxo(src, extra_cell=True)
    assert read_planilha(src).width == 4


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
    df = read_planilha(tmp_path / "fin.xlsx")
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
    df = read_planilha(src)
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
