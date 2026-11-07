"""SAEB 1995-2005 end to end: fixed-width TXT + SAS layout -> lake Parquet."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import polars as pl
import pytest
from quantilica.analytics.lake import check_dataset

from inep_fetcher.lake import LakeConverter

FIXTURES = Path(__file__).parent / "fixtures" / "saeb"


def _zip(path: Path, members: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w") as z:
        for name, data in members.items():
            z.writestr(name, data)


def _fx(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


def _lines(name: str) -> list[bytes]:
    return _fx(name).replace(b"\r\n", b"\n").split(b"\n")[:-1]


def _convert(tmp_path: Path):
    lake = tmp_path / "lake"
    result = LakeConverter().convert(tmp_path / "raw", lake)
    return result, lake / "inep" / "saeb"


def _read(root: Path, key: str) -> pl.DataFrame:
    (path,) = list(root.rglob(f"{key}.parquet"))
    return pl.read_parquet(path)


@pytest.fixture
def raw(tmp_path: Path) -> Path:
    d = tmp_path / "raw" / "saeb"
    d.mkdir(parents=True)
    return d


def test_zip_1995_format(tmp_path: Path, raw: Path) -> None:
    _zip(
        raw / "saeb-microdados_1995@20240101.zip",
        {
            "INPUTS_SAS_SPSS/DIRETOR/INPUT_SAS_DIRETOR_95.sas": _fx(
                "INPUT_SAS_DIRETOR_95.sas"
            ),
            "DADOS/DIRETOR/DIRETOR_95.TXT": _fx("DIRETOR_95.TXT"),
        },
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    assert result.converted == 1
    df = _read(root, "saeb-microdados_1995__diretor_95")
    assert df.height == 5
    assert "ano" not in df.columns  # vai na partição ano=1995 do lake
    assert (root / "ano=1995").is_dir()
    assert df.schema["serie"] == pl.Int64
    assert df.schema["d_001"] == pl.Int64
    assert df["serie"].to_list() == [8, 3, 4, 8, 3]
    assert df["peso_ec"].to_list()[0] == 828
    assert df["uf"].to_list() == [11] * 5
    # campo em branco no TXT vira nulo, não zero
    assert df.null_count().sum_horizontal().item() > 0
    assert not check_dataset(root)
    # reconversão é idempotente
    again, _ = _convert(tmp_path)
    assert again.converted == 0 and again.skipped == 1


def test_zip_1999_format_with_inner_zip(tmp_path: Path, raw: Path) -> None:
    inner = io.BytesIO()
    with zipfile.ZipFile(inner, "w") as z:
        z.writestr("ALUNOS/MATEMATICA_04SERIE.TXT", _fx("MATEMATICA_04SERIE_99.TXT"))
    _zip(
        raw / "saeb-microdados_1999@20240101.zip",
        {
            "INPUTS_SAS_SPSS/ALUNOS/INPUT_SAS_MATEMATICA_04SERIE.SAS": _fx(
                "INPUT_SAS_MATEMATICA_04SERIE.SAS"
            ),
            # lock file do Office, sem INFILE: ignorado
            "INPUTS_SAS_SPSS/ALUNOS/~$PUT_SAS_QUIMICA_03ANO.SAS": b"\x05Dk",
            "DADOS/ALUNOS.zip": inner.getvalue(),
        },
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    df = _read(root, "saeb-microdados_1999__matematica_04serie")
    assert df.height == 5
    # decimais com ponto explícito (8.4): vale o ponto do campo
    assert df.schema["peso_ac"] == pl.Float64
    assert df["peso_ac"].to_list()[0] == pytest.approx(
        float(_lines("MATEMATICA_04SERIE_99.TXT")[0][58:66].strip())
    )
    assert any(dt == pl.String for dt in df.schema.values())  # $char13.
    assert not check_dataset(root)


def test_zip_2005_imput_and_dir_names(tmp_path: Path, raw: Path) -> None:
    _zip(
        raw / "saeb-microdados_2005@20240101.zip",
        {
            "INPUTS_SAS_SPSS/ALUNOS/IMPUT_SAS_MATEMATICA_03ANO.sas": _fx(
                "IMPUT_SAS_MATEMATICA_03ANO.sas"
            ),
            "DADOS/ALUNOS/MATEMATICA_03ANO.TXT": _fx("MATEMATICA_03ANO_05.TXT"),
            "DICIONARIO/DICIONARIO.TXT": b"x",
        },
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    df = _read(root, "saeb-microdados_2005__matematica_03ano")
    assert df.height == 5
    assert df["mascara"].null_count() == 0


def test_errors_do_not_stop_other_members(tmp_path: Path, raw: Path) -> None:
    _zip(
        raw / "saeb-microdados_2005@20240101.zip",
        {
            "INPUTS_SAS_SPSS/ALUNOS/IMPUT_SAS_MATEMATICA_03ANO.sas": _fx(
                "IMPUT_SAS_MATEMATICA_03ANO.sas"
            ),
            # layout inválido (campo além do LRECL) e seu TXT
            "INPUTS_SAS_SPSS/ALUNOS/INPUT_SAS_BIOLOGIA_03ANO.SAS": _fx(
                "INPUT_SAS_BIOLOGIA_03ANO_gabarito_alem_lrecl.SAS"
            ),
            "DADOS/ALUNOS/BIOLOGIA_03ANO.TXT": b"abc\r\n",
            # layout sem TXT
            "INPUTS_SAS_SPSS/ESCOLA/INPUT_SAS_ESCOLA_05.sas": _fx(
                "INPUT_SAS_ESCOLA_05.sas"
            ),
            "DADOS/ALUNOS/MATEMATICA_03ANO.TXT": _fx("MATEMATICA_03ANO_05.TXT"),
            # TXT sem layout
            "DADOS/ALUNOS/SOBRA.TXT": b"1234\r\n",
        },
    )
    result, root = _convert(tmp_path)
    assert result.converted == 1
    assert len(result.errors) == 3
    joined = "\n".join(result.errors)
    assert "além do LRECL" in joined
    assert "SOBRA.TXT: sem layout SAS" in joined
    assert "escola_05.txt não encontrado" in joined
    assert "BIOLOGIA_03ANO.TXT: sem layout" not in joined  # só o erro do script
    assert _read(root, "saeb-microdados_2005__matematica_03ano").height == 5


def test_same_txt_name_in_two_folders_gets_distinct_keys(
    tmp_path: Path, raw: Path
) -> None:
    script = b"INFILE 'D:\\X.TXT' LRECL=8;\r\nINPUT\r\n@1 A 4.\r\n@5 B $Char4.;\r\n"
    _zip(
        raw / "saeb-microdados_2003@20240101.zip",
        {
            "INPUTS_SAS_SPSS/A/INPUT_X.sas": script,
            "DADOS/A/X.TXT": b"  12abc\r\n",
            "DADOS/B/X.TXT": b"  34 de\r\n",
        },
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    assert result.converted == 2
    got = sorted(p.name for p in root.rglob("*.parquet"))
    assert got == [
        "saeb-microdados_2003__a_x.parquet",
        "saeb-microdados_2003__b_x.parquet",
    ]


def test_implicit_and_explicit_decimals_and_text(tmp_path: Path, raw: Path) -> None:
    script = (
        b"DATA T;\r\nINFILE 'D:\\T.TXT'\r\nLRECL=31 MISSOVER;\r\nINPUT\r\n"
        b"@1\tN\t4.\t/*n*/\r\n"
        b"@5\tIMPL\t8.2\t/*implicito*/\r\n"
        b"@13\tEXPL\t8.2\t/*explicito*/\r\n"
        b"@21\tTXT\t$Char8.\t/*texto*/\r\n"
        b"@29\tEND\t3.;\r\n"
    )

    def row(n: str, impl: str, expl: str, txt: str, end: str) -> str:
        return n.rjust(4) + impl.rjust(8) + expl.rjust(8) + txt.ljust(8) + end.rjust(3)

    data = "\r\n".join(
        [
            row("1", "12345", "1.5000", "caf\xe9", "7"),
            row("2", "", ".", "", ""),
            row("3", "-5", "-2.25", "abc", "."),
            "",
            row("5", "99999", "0.1", "x", ""),
        ]
    )
    data = (data + "\r\n").encode("latin-1")
    _zip(
        raw / "saeb-microdados_2001@20240101.zip",
        {"INPUTS_SAS_SPSS/T/INPUT_T.sas": script, "DADOS/T/T.TXT": data},
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    df = _read(root, "saeb-microdados_2001__t")
    assert df.height == 5  # linha em branco vira linha toda nula, como no SAS
    assert df["n"].to_list() == [1, 2, 3, None, 5]
    # sem ponto: divide por 10^d; com ponto: vale o ponto; vazio ou ".": nulo
    assert df["impl"].to_list() == [
        pytest.approx(123.45),
        None,
        pytest.approx(-0.05),
        None,
        pytest.approx(999.99),
    ]
    assert df["expl"].to_list() == [
        pytest.approx(1.5),
        None,
        pytest.approx(-2.25),
        None,
        pytest.approx(0.1),
    ]
    assert df["txt"].to_list() == ["café", None, "abc", None, "x"]
    assert df["end"].to_list() == [7, None, None, None, None]


def test_zip_2007_csv_is_unchanged(tmp_path: Path, raw: Path) -> None:
    _zip(
        raw / "saeb-microdados_2021@20240101.zip",
        {
            "DADOS/TS_ALUNO.csv": b"id_aluno;proficiencia\n1;250,5\n2;300\n",
            "INPUTS_SAS_SPSS/leia.TXT": b"x",
        },
    )
    result, root = _convert(tmp_path)
    assert result.errors == []
    df = _read(root, "saeb-microdados_2021__ts_aluno")
    assert df.height == 2
    assert df.columns == ["id_aluno", "proficiencia"]


def test_txt_without_separator_on_csv_path_is_an_error(
    tmp_path: Path, raw: Path
) -> None:
    _zip(
        raw / "saeb-microdados_2009@20240101.zip",
        {
            "DADOS/SEM_LAYOUT.TXT": b"    1995       8     110\r\n    1995       3\r\n",
            "DADOS/OK.csv": b"a;b\n1;2\n",
        },
    )
    loose = tmp_path / "raw" / "enem"
    loose.mkdir()
    (loose / "enem_2023@20240101.csv").write_text("so_uma_coluna\n1\n2\n")
    result, root = _convert(tmp_path)
    assert result.converted == 1  # OK.csv
    assert any("SEM_LAYOUT.TXT: separador" in e for e in result.errors)
    assert any("enem_2023@20240101.csv: separador" in e for e in result.errors)
    assert not list(root.rglob("*sem_layout*"))
