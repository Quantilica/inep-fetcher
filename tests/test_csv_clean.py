"""Limpeza dos CSVs de indicadores: título acima do cabeçalho e colunas vazias."""

from __future__ import annotations

import zipfile
from pathlib import Path

import polars as pl

from inep_fetcher.csv_clean import clean_csv
from inep_fetcher.lake import LakeConverter

TITULO_3 = (
    "Ministério da Educação;;;;\n"
    "Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira;;;;\n"
    "Resultados ENADE 2004;;;;\n"
    ";;;;\n"
)
CORPO = "co_grupo;co_ies;Área;Média\n17;588;AGRONOMIA;42,5\n17;1230;DIREITO;39,7\n"


def _write(path: Path, text: str) -> Path:
    path.write_text(text, encoding="latin-1", newline="")
    return path


def _read(path: Path) -> list[list[str]]:
    return [ln.split(";") for ln in path.read_text(encoding="latin-1").splitlines()]


def test_pula_tres_linhas_de_titulo_e_linha_vazia(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", TITULO_3 + CORPO.replace(";\n", "\n"))
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert out.title_rows == 4
    rows = _read(out.path)
    assert rows[0] == ["co_grupo", "co_ies", "Área", "Média"]
    assert len(rows) == 3


def test_pula_uma_linha_de_titulo(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "CONCEITO ENADE - 2012;;;\n" + CORPO)
    out = clean_csv(src, ";", tmp_path)
    assert out is not None and out.title_rows == 1
    assert _read(out.path)[0][0] == "co_grupo"


def test_csv_normal_nao_e_tocado(tmp_path: Path) -> None:
    assert clean_csv(_write(tmp_path / "a.csv", CORPO), ";", tmp_path) is None
    # cabeçalho de uma coluna só com valor, dado numérico: não é título
    um = _write(tmp_path / "b.csv", "codigo;nome\n1;x\n")
    assert clean_csv(um, ";", tmp_path) is None
    # coluna sem nome com valor: nada a fazer, o DuckDB nomeia
    valor = _write(tmp_path / "c.csv", "a;b;\n1;2;3\n")
    assert clean_csv(valor, ";", tmp_path) is None


def test_cabecalho_de_anos_depois_do_titulo(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "Taxas de aprovação;;;\nUF;2019;2020\nSP;90;91\n")
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert _read(out.path)[0] == ["UF", "2019", "2020"]


def test_linha_de_dados_nunca_vira_cabecalho(tmp_path: Path) -> None:
    # "Ano;;" é o cabeçalho; a linha seguinte, só de números, é dado
    src = _write(tmp_path / "a.csv", "Ano;;\n2004;10;20\n2005;11;21\n")
    assert clean_csv(src, ";", tmp_path) is None


def test_descarta_colunas_sem_nome_e_sem_valor(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b;;;\n1;2;;;\n3;4;;;\n")
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert (out.columns_before, out.columns_after) == (5, 2)
    assert _read(out.path) == [["a", "b"], ["1", "2"], ["3", "4"]]


def test_coluna_sem_nome_com_valor_fica_com_nome_posicional(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b;;;\n1;2;;x;\n3;4;;;\n")
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert _read(out.path) == [["a", "b", "column03"], ["1", "2", "x"], ["3", "4", ""]]


def test_coluna_nomeada_e_vazia_fica(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;obs;;\n1;;;\n2;;;\n")
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert _read(out.path)[0] == ["a", "obs"]


def test_linhas_mais_largas_que_o_cabecalho(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b\n1;2;;;9\n3;4\n")
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert _read(out.path) == [["a", "b", "column04"], ["1", "2", "9"], ["3", "4", ""]]


def test_preserva_campos_entre_aspas_com_separador(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", 'a;b;;\n"x;y";2;;\n')
    out = clean_csv(src, ";", tmp_path)
    assert out is not None
    assert out.path.read_text(encoding="latin-1").splitlines()[1] == '"x;y";2'


def test_converter_indicador_com_titulo_e_colunas_vazias(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "qualidade-educacao-superior"
    raw.mkdir(parents=True)
    _write(
        raw / "qualidade-educacao-superior-2004-enade@20200217.csv",
        TITULO_3 + CORPO.replace("\n", ";;\n"),
    )
    with zipfile.ZipFile(
        raw / "qualidade-educacao-superior-2012@20200217.zip", "w"
    ) as zf:
        zf.writestr(
            "DADOS/c.csv", "CONCEITO ENADE - 2012;;\n" + CORPO.replace("\n", ";;\n")
        )
    lake = tmp_path / "lake"

    res = LakeConverter().convert(tmp_path / "raw", lake)

    assert not res.errors, res.errors
    assert res.converted == 2
    for p in lake.rglob("*.parquet"):
        df = pl.read_parquet(p)
        assert df.columns[:2] == ["co_grupo", "co_ies"], p
        assert df.shape == (2, 4)


def test_microdados_nao_passam_pela_limpeza(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "enem"
    raw.mkdir(parents=True)
    _write(raw / "enem_2023@20240101.csv", "a;b;;\n1;2;;\n")
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors
    df = pl.read_parquet(next((tmp_path / "lake").rglob("*.parquet")))
    assert df.width == 4  # as colunas sem nome continuam: só os indicadores limpam
