"""Limpeza dos CSVs de indicadores: título acima do cabeçalho e colunas vazias."""

from __future__ import annotations

import time
import zipfile
from pathlib import Path

import polars as pl

from inep_fetcher.csv_clean import CsvCleanup, clean_csv, detect_separator, split_raw
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


def _lido(src: Path, plan: CsvCleanup) -> list[str]:
    """Linhas que o DuckDB leria: o CSV reescrito, ou o original com ``skip``."""
    base = plan.path or src
    return base.read_text(encoding="latin-1").splitlines()[plan.skip :]


def test_split_raw_preserva_aspas() -> None:
    assert split_raw('a;"FACULDADE X" - FX;"b;c";d', ";") == (
        ["a", '"FACULDADE X" - FX', '"b;c"', "d"],
        False,
    )
    assert split_raw('a;"aberto', ";")[1] is True
    assert split_raw('"x ""y"" z";b', ";")[0] == ['"x ""y"" z"', "b"]


def test_pula_tres_linhas_de_titulo_e_linha_vazia_sem_reescrever(
    tmp_path: Path,
) -> None:
    src = _write(tmp_path / "a.csv", TITULO_3 + CORPO.replace(";\n", "\n"))
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert (plan.skip, plan.path, plan.title_rows) == (4, None, 4)
    assert _lido(src, plan)[0] == "co_grupo;co_ies;Área;Média"
    assert not list(tmp_path.glob("*.clean.csv"))


def test_pula_uma_linha_de_titulo(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "CONCEITO ENADE - 2012;;;\n" + CORPO)
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None and plan.skip == 1
    assert _lido(src, plan)[0].startswith("co_grupo")


def test_csv_normal_nao_e_tocado(tmp_path: Path) -> None:
    assert clean_csv(_write(tmp_path / "a.csv", CORPO), ";", tmp_path) is None
    um = _write(tmp_path / "b.csv", "codigo;nome\n1;x\n")
    assert clean_csv(um, ";", tmp_path) is None
    # coluna sem nome com valor: nada a fazer, o DuckDB nomeia
    valor = _write(tmp_path / "c.csv", "a;b;\n1;2;3\n")
    assert clean_csv(valor, ";", tmp_path) is None


def test_cabecalho_de_anos_depois_do_titulo(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "Taxas de aprovação;;;\nUF;2019;2020\nSP;90;91\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan)[0] == "UF;2019;2020"


def test_linha_de_dados_nunca_vira_cabecalho(tmp_path: Path) -> None:
    # "Ano;;" é o cabeçalho; a linha seguinte, só de números, é dado
    src = _write(tmp_path / "a.csv", "Ano;;\n2004;10;20\n2005;11;21\n")
    assert clean_csv(src, ";", tmp_path) is None


def test_primeira_celula_numerica_sozinha_e_dado_nao_titulo(tmp_path: Path) -> None:
    # "1;;" e "2;;y" são dados: nenhuma linha some (só a coluna 1, vazia e sem nome)
    src = _write(tmp_path / "a.csv", "a;;\n1;;\n2;;y\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None and plan.title_rows == 0
    assert _lido(src, plan) == ["a;column02", "1;", "2;y"]


def test_descarta_colunas_sem_nome_e_sem_valor(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b;;;\n1;2;;;\n3;4;;;\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert (plan.columns_before, plan.columns_after) == (5, 2)
    assert _lido(src, plan) == ["a;b", "1;2", "3;4"]


def test_coluna_sem_nome_com_valor_fica_com_nome_posicional(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b;;;\n1;2;;x;\n3;4;;;\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan) == ["a;b;column03", "1;2;x", "3;4;"]


def test_coluna_nomeada_e_vazia_fica(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;obs;;\n1;;;\n2;;;\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan)[0] == "a;obs"


def test_valor_alem_do_cabecalho_em_linha_mais_estreita_que_a_maior(
    tmp_path: Path,
) -> None:
    # a linha 2 é a mais larga (4 campos); o "x" da linha 3 está na coluna 2
    src = _write(tmp_path / "a.csv", "a;b\n1;2;;\n3;4;x;\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan) == ["a;b;column02", "1;2;", "3;4;x"]


def test_linhas_mais_largas_que_o_cabecalho(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b\n1;2;;;9\n3;4\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan) == ["a;b;column04", "1;2;9", "3;4;"]


def test_reescrita_preserva_aspas_e_campos_com_separador(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", 'a;b;c;;\n"x;y";"FACULDADE X" - FX;3;;\n')
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan)[1] == '"x;y";"FACULDADE X" - FX;3'


def test_reescrita_preserva_campo_com_quebra_de_linha(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", 'a;b;;\n"l1\nl2";2;;\n3;4;;\n')
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None and plan.path is not None
    assert plan.path.read_text(encoding="latin-1") == 'a;b\n"l1\nl2";2\n3;4\n'


def test_linha_so_de_separadores_nos_dados_e_mantida(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", "a;b;;\n1;2;;\n;;;\n3;4;;\n")
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None
    assert _lido(src, plan) == ["a;b", "1;2", ";", "3;4"]


def test_separador_detectado_na_linha_do_cabecalho(tmp_path: Path) -> None:
    # a 1ª linha (título) tem ";", mas o cabeçalho e o dado usam ","
    src = _write(tmp_path / "a.csv", "Resultados;;;\nco_grupo,co_ies,area\n1,2,x\n")
    assert detect_separator(src, (";", ",", "|", "\t"), ";") == ","
    ok = _write(tmp_path / "b.csv", CORPO)
    assert detect_separator(ok, (";", ",", "|", "\t"), ";") == ";"
    titulo = _write(tmp_path / "c.csv", TITULO_3 + CORPO)
    assert detect_separator(titulo, (";", ",", "|", "\t"), ";") == ";"


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


def test_converter_so_titulo_le_como_o_duckdb_leria_sem_o_titulo(
    tmp_path: Path,
) -> None:
    raw = tmp_path / "raw" / "qualidade-educacao-superior"
    raw.mkdir(parents=True)
    corpo = 'nome;sigla\n"FACULDADE X" - FX;FX\n'
    _write(
        raw / "qualidade-educacao-superior-2012@20200217.csv", "CONCEITO;;\n" + corpo
    )
    _write(raw / "qualidade-educacao-superior-2013@20200217.csv", corpo)
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    dfs = {
        p.parent.name: pl.read_parquet(p)
        for p in (tmp_path / "lake").rglob("*.parquet")
    }
    assert dfs["ano=2012"].equals(dfs["ano=2013"])
    assert dfs["ano=2012"].columns == ["nome", "sigla"]


def test_microdados_nao_passam_pela_limpeza(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "enem"
    raw.mkdir(parents=True)
    _write(raw / "enem_2023@20240101.csv", "a;b;;\n1;2;;\n")
    res = LakeConverter().convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors
    df = pl.read_parquet(next((tmp_path / "lake").rglob("*.parquet")))
    assert df.width == 4  # as colunas sem nome continuam: só os indicadores limpam


def test_aspa_aberta_nao_engole_o_arquivo_nem_fica_quadratica(tmp_path: Path) -> None:
    n = 50_000
    corpo = "".join(f"{i};ESCOLA {i};{i * 2};;\n" for i in range(n))
    texto = 'a;b;c;;\n1;" (aspa sozinha);3;;\n' + corpo
    src = _write(tmp_path / "a.csv", texto)

    t0 = time.perf_counter()
    plan = clean_csv(src, ";", tmp_path)
    dt = time.perf_counter() - t0

    assert dt < 2.0, f"{dt:.1f} s"
    assert plan is not None and plan.path is not None
    saida = plan.path.read_text(encoding="latin-1").splitlines()
    # nenhuma linha some e a aspa solta segue como texto
    assert len(saida) == n + 2
    assert saida[0] == "a;b;c"
    assert saida[1] == '1;" (aspa sozinha);3'
    assert saida[2] == "0;ESCOLA 0;0"
    assert saida[-1] == f"{n - 1};ESCOLA {n - 1};{(n - 1) * 2}"


def test_campo_entre_aspas_com_quebra_de_linha_continua_unido(tmp_path: Path) -> None:
    src = _write(tmp_path / "a.csv", 'a;b;;\n"l1\nl2\nl3";2;;\n5;6;;\n')
    plan = clean_csv(src, ";", tmp_path)
    assert plan is not None and plan.path is not None
    assert plan.path.read_text(encoding="latin-1") == 'a;b\n"l1\nl2\nl3";2\n5;6\n'
