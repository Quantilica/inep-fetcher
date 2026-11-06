"""Tests for the INEP Parquet Lake converter."""

from __future__ import annotations

import zipfile
from pathlib import Path

import polars as pl
import pytest
from quantilica.analytics.lake import check_dataset
from quantilica.core.lake import DatasetDescriptor

from inep_fetcher.lake import LakeConverter, resolve_dataset, resolve_year


@pytest.fixture
def lake_converter() -> LakeConverter:
    return LakeConverter()


def test_datasets_list(lake_converter: LakeConverter) -> None:
    ds = lake_converter.datasets()
    assert "enem" in ds
    assert "censo-escolar" in ds
    assert "censo-educacao-superior" in ds
    assert "saeb" in ds
    assert "enade" in ds
    assert "adequacao-formacao-docente" in ds


def test_resolve_dataset_and_year() -> None:
    p1 = Path("/data/inep/enem/enem_2023@20240101.zip")
    assert resolve_dataset(p1) == "enem"
    assert resolve_year(p1) == 2023

    p2 = Path(
        "/data/inep/indicadores/adequacao-formacao-docente/afd_2022@20230501.xlsx"
    )
    assert resolve_dataset(p2) == "adequacao-formacao-docente"
    assert resolve_year(p2) == 2022

    p3 = Path("/data/inep/enem-por-escola/enem_por_escola_2005-2015@20200101.zip")
    assert resolve_dataset(p3) == "enem-por-escola"


def test_convert_csv_and_zip(tmp_path: Path, lake_converter: LakeConverter) -> None:
    raw_dir = tmp_path / "raw"
    lake_dir = tmp_path / "lake"

    # 1. Plain CSV in enem
    enem_dir = raw_dir / "enem"
    enem_dir.mkdir(parents=True)
    csv_file = enem_dir / "enem_2023@20240101.csv"
    csv_file.write_text(
        "nu_inscricao;nu_ano;tp_sexo\n10001;2023;M\n10002;2023;F\n",
        encoding="latin-1",
    )

    # 2. Zipped microdata with internal DADOS/ subfolder and DICIONARIO/ file
    censo_dir = raw_dir / "censo-escolar"
    censo_dir.mkdir(parents=True)
    zip_path = censo_dir / "censo_escolar_2022@20230201.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr(
            "DADOS/microdados_ed_basica_2022.csv",
            "co_entidade;no_entidade\n1234;Escola A\n5678;Escola B\n",
        )
        zf.writestr(
            "DICIONARIO/dicionario_dados.csv",
            "coluna;descricao\nco_entidade;Codigo\n",
        )
        zf.writestr("LEIA_ME.txt", "Instruções sobre os dados.")

    res = lake_converter.convert(raw_dir, lake_dir)
    assert res.converted == 2
    assert res.skipped == 0
    assert not res.errors

    # Verify ENEM parquet and descriptor
    enem_parquet = lake_dir / "inep" / "enem" / "ano=2023" / "enem_2023.parquet"
    assert enem_parquet.is_file()
    df_enem = pl.read_parquet(enem_parquet)
    assert df_enem.shape == (2, 3)

    desc_enem = DatasetDescriptor.load(lake_dir / "inep" / "enem")
    assert desc_enem.partition_types == {"ano": "int"}
    assert not check_dataset(lake_dir / "inep" / "enem")

    # Verify CENSO parquet and descriptor
    censo_part_dir = lake_dir / "inep" / "censo-escolar" / "ano=2022"
    censo_name = "censo_escolar_2022__microdados_ed_basica_2022.parquet"
    censo_parquet = censo_part_dir / censo_name
    assert censo_parquet.is_file()
    df_censo = pl.read_parquet(censo_parquet)
    assert df_censo.shape == (2, 2)

    desc_censo = DatasetDescriptor.load(lake_dir / "inep" / "censo-escolar")
    assert desc_censo.partition_types == {"ano": "int"}
    assert not check_dataset(lake_dir / "inep" / "censo-escolar")

    # Idempotent second run
    res2 = lake_converter.convert(raw_dir, lake_dir)
    assert res2.converted == 0
    assert res2.skipped == 2


def test_convert_errors(tmp_path: Path, lake_converter: LakeConverter) -> None:
    non_existent = tmp_path / "does_not_exist"
    res = lake_converter.convert(non_existent, tmp_path / "lake")
    assert "não existe" in res.errors[0]

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    res_unknown = lake_converter.convert(
        raw_dir, tmp_path / "lake", datasets=["invalid-dataset"]
    )
    assert "dataset desconhecido: invalid-dataset" in res_unknown.errors[0]


def test_convert_comma_separated_zip(
    tmp_path: Path, lake_converter: LakeConverter
) -> None:
    raw_dir = tmp_path / "raw"
    lake_dir = tmp_path / "lake"

    saeb_dir = raw_dir / "saeb"
    saeb_dir.mkdir(parents=True)
    zip_path = saeb_dir / "saeb_2021@20220101.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr(
            "TS_ALUNO_2021.csv",
            "id_aluno,id_turma,proficiencia\n1,10,250.5\n2,10,310.2\n",
        )

    res = lake_converter.convert(raw_dir, lake_dir)
    assert res.converted == 1
    assert not res.errors

    saeb_parquet = (
        lake_dir / "inep" / "saeb" / "ano=2021" / "saeb_2021__ts_aluno_2021.parquet"
    )
    assert saeb_parquet.is_file()
    df = pl.read_parquet(saeb_parquet)
    assert df.shape == (2, 3)
    assert set(df.columns) == {"id_aluno", "id_turma", "proficiencia"}


def test_zip_com_membros_excel(
    lake_converter: LakeConverter, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """ZIP so com planilhas (.xls/.xlsx): cada membro vira um Parquet, sem erro."""
    raw_dir = tmp_path / "raw" / "indicadores" / "media-alunos-por-turma"
    raw_dir.mkdir(parents=True)
    zip_path = (
        raw_dir / "media-alunos-por-turma-alunos-turma-brasil-regioes-ufs-2011"
        "@20130613.zip"
    )
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("BRASIL 2011.xls", b"planilha brasil")
        zf.writestr("ESTADOS 2011.xlsx", b"planilha estados")
    lake_dir = tmp_path / "lake"
    lake_dir.mkdir()

    lidos: list[str] = []

    def _read_excel(path, *args, **kwargs):
        lidos.append(Path(path).name)
        return pl.DataFrame({"uf": ["SP", "RJ"], "alunos": [30, 28]})

    monkeypatch.setattr(pl, "read_excel", _read_excel)

    res = lake_converter.convert(tmp_path / "raw", lake_dir)
    assert not res.errors
    assert (res.converted, res.skipped) == (2, 0)
    assert sorted(lidos) == ["BRASIL 2011.xls", "ESTADOS 2011.xlsx"]
    dataset_dir = lake_dir / "inep" / "media-alunos-por-turma" / "ano=2011"
    assert len(list(dataset_dir.glob("*.parquet"))) == 2

    # idempotente: a segunda rodada pula os dois membros
    res2 = lake_converter.convert(tmp_path / "raw", lake_dir)
    assert not res2.errors
    assert (res2.converted, res2.skipped) == (0, 2)


def test_zip_ignora_lock_file_do_office(
    lake_converter: LakeConverter, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Lock file "~$X.xlsx" esquecido no ZIP não é planilha e não vira erro."""
    raw_dir = tmp_path / "raw" / "indicadores" / "taxas-transicao"
    raw_dir.mkdir(parents=True)
    zip_path = raw_dir / "taxas-transicao-tx-transicao-2021@20250826.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("TX_2021/TX_TRANSICAO_2021.xlsx", b"planilha")
        zf.writestr("TX_2021/~$TX_TRANSICAO_2021.xlsx", b"\x1eJulio C")
        zf.writestr("TX_2021/TX_TRANSICAO_2021.ods", b"PK")
    lake_dir = tmp_path / "lake"
    lake_dir.mkdir()

    lidos: list[str] = []

    def _read_excel(path, *args, **kwargs):
        lidos.append(Path(path).name)
        return pl.DataFrame({"uf": ["SP"], "taxa": [1.5]})

    monkeypatch.setattr(pl, "read_excel", _read_excel)

    res = lake_converter.convert(tmp_path / "raw", lake_dir)
    assert not res.errors
    assert lidos == ["TX_TRANSICAO_2021.xlsx"]
    assert res.converted == 1
