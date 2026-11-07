"""Tests for the SAS INPUT layout reader (SAEB 1995-2005)."""

from __future__ import annotations

from pathlib import Path

import pytest

from inep_fetcher.sas_layout import parse_sas_input, peek_infile

FIXTURES = Path(__file__).parent / "fixtures" / "saeb"


def _read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="latin-1")


def test_parse_1995_script_with_tabs_and_crlf() -> None:
    layout = parse_sas_input(_read("INPUT_SAS_DIRETOR_95.sas"))
    assert layout.infile == "diretor_95.txt"
    assert layout.lrecl == 472
    first = layout.fields[0]
    assert (first.name, first.start, first.width) == ("ano", 1, 8)
    assert first.numeric and first.decimals == 0
    assert first.label == "Ano"
    upa = next(f for f in layout.fields if f.name == "upa")
    assert upa.label == "Unidade Primaria de Amostragem"
    # sem sobreposição, em ordem de posição
    ends = [f.end for f in layout.fields]
    assert ends == sorted(ends)


def test_parse_1999_script_uppercase_extension_and_decimals() -> None:
    layout = parse_sas_input(_read("INPUT_SAS_MATEMATICA_04SERIE.SAS"))
    assert layout.infile == "matematica_04serie.txt"
    assert layout.lrecl == 217
    peso = next(f for f in layout.fields if f.name == "peso_ac")
    assert (peso.width, peso.decimals, peso.numeric) == (8, 4, True)
    assert any(not f.numeric for f in layout.fields)  # $char13.


def test_parse_2005_imput_script_with_split_infile_and_double_quotes() -> None:
    layout = parse_sas_input(_read("IMPUT_SAS_MATEMATICA_03ANO.sas"))
    assert layout.infile == "matematica_03ano.txt"
    assert layout.lrecl == 327
    assert layout.fields[0].name == "mascara"
    assert layout.fields[0].label.startswith("Número gerado")


def test_parse_char_informats_any_case() -> None:
    text = (
        "DATA X;\n INFILE 'C:\\a\\B.TXT' LRECL=40 MISSOVER;\n INPUT\n"
        "@1\t\tA\t$Char1.\t/*um*/\n"
        "@2 B $char13. /*dois*/\n"
        "@15\tC\t12.10\n"
        "@27 D 2.;\n"
    )
    layout = parse_sas_input(text)
    assert layout.infile == "b.txt"
    by_name = {f.name: f for f in layout.fields}
    assert (by_name["a"].numeric, by_name["a"].width) == (False, 1)
    assert (by_name["b"].numeric, by_name["b"].width) == (False, 13)
    assert (by_name["c"].width, by_name["c"].decimals) == (12, 10)
    assert by_name["d"].label == ""


def test_comment_with_semicolon_does_not_end_input() -> None:
    text = "INFILE 'x.txt' LRECL=20;\nINPUT\n@1 A 4. /* a; b */\n@5 B 4. /* INPUT */\n;"
    layout = parse_sas_input(text)
    assert [f.name for f in layout.fields] == ["a", "b"]
    assert layout.fields[0].label == "a; b"


def test_overlap_is_an_error() -> None:
    text = "INFILE 'x.txt' LRECL=40;\nINPUT\n@1 A 8.\n@5 B 8.\n;"
    with pytest.raises(ValueError, match="se sobrepõem"):
        parse_sas_input(text)


def test_field_beyond_lrecl_is_an_error() -> None:
    with pytest.raises(ValueError, match="além do LRECL"):
        parse_sas_input(_read("INPUT_SAS_BIOLOGIA_03ANO_gabarito_alem_lrecl.SAS"))


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("INPUT\n@1 A 8.;", "sem INFILE"),
        ("INFILE 'x.txt';\nINPUT\n@1 A 8.;", "sem LRECL"),
        ("INFILE 'x.txt' LRECL=9;\n", "sem bloco INPUT"),
        ("INFILE 'x.txt' LRECL=9;\nINPUT\n;", "sem campos"),
        ("INFILE 'x.txt' LRECL=9;\nINPUT\n@1 A 4.\n@5 A 4.;", "repetido"),
        ("INFILE 'x.txt' LRECL=9;\nINPUT\n@1 A DATE9.;", "não suportado"),
        ("INFILE 'x.txt' LRECL=9;\nINPUT\n@1 A 4.\n@5 B;", "não reconhecido"),
    ],
)
def test_malformed_scripts(text: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_sas_input(text)


def test_peek_infile_survives_invalid_script() -> None:
    text = _read("INPUT_SAS_BIOLOGIA_03ANO_gabarito_alem_lrecl.SAS")
    assert peek_infile(text) == "biologia_03ano.txt"
    assert peek_infile("sem nada") is None
