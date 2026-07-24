"""Tests for inep_fetcher.catalog."""

import pytest

from inep_fetcher.catalog import (
    ALL_GROUP_KEYS,
    GROUPS,
    INDICADORES_GROUP_KEYS,
    expand_group,
    list_datasets,
    resolve_group,
)

_EXPECTED_MICRODADOS_GROUPS = {
    "enem",
    "censo_escolar",
    "censo_educacao_superior",
    "saeb",
    "enade",
    "ana",
    "encceja",
    "censo_magisterio",
    "enade_licenciaturas",
    "enamed",
    "pnd",
    "pnera",
    "pesquisa_discriminacao",
    "idd",
    "enem_por_escola",
    "talis",
}

_EXPECTED_INDICADORES_GROUPS = {
    "adequacao_formacao_docente",
    "complexidade_gestao_escola",
    "esforco_docente",
    "indicadores_fluxo_educacao_superior",
    "indicadores_qualidade_educacao_superior",
    "indicadores_trajetoria_educacao_superior",
    "indicadores_financeiros_educacionais",
    "media_alunos_por_turma",
    "media_horas_aula_diaria",
    "nivel_socioeconomico",
    "docentes_curso_superior",
    "docentes_pos_graduacao",
    "regularidade_corpo_docente",
    "remuneracao_docentes",
    "taxas_distorcao_idade_serie",
    "taxas_nao_resposta",
    "taxas_rendimento_escolar",
    "taxas_transicao",
}

_EXPECTED_GROUPS = _EXPECTED_MICRODADOS_GROUPS | _EXPECTED_INDICADORES_GROUPS

_SINGLE_EDITION_GROUPS = {
    "censo_magisterio",
    "enade_licenciaturas",
    "enamed",
    "pnd",
    "pnera",
    "pesquisa_discriminacao",
}


def test_all_34_groups_present():
    assert set(GROUPS) == _EXPECTED_GROUPS
    assert set(ALL_GROUP_KEYS) == _EXPECTED_GROUPS
    assert len(GROUPS) == 34


def test_indicadores_group_keys_match_expected():
    assert set(INDICADORES_GROUP_KEYS) == _EXPECTED_INDICADORES_GROUPS
    assert len(INDICADORES_GROUP_KEYS) == 18


def test_each_group_has_name_and_entries():
    for key, info in GROUPS.items():
        assert info["name"], f"Group {key!r} missing name"
        assert len(info["entries"]) > 0, f"Group {key!r} has no entries"


def test_entry_fields_complete():
    required = {
        "id",
        "base_id",
        "name",
        "url",
        "ext",
        "group",
        "source",
        "year",
        "semester",
        "month",
    }
    for entry in list_datasets():
        missing = required - entry.keys()
        assert not missing, f"Entry {entry['id']!r} missing fields: {missing}"


def test_entry_urls_start_with_https():
    for entry in list_datasets():
        assert entry["url"].startswith("https://"), (
            f"Entry {entry['id']!r} has non-https URL: {entry['url']}"
        )


def test_entry_urls_have_no_raw_spaces_or_accents():
    for entry in list_datasets():
        for ch in entry["url"]:
            assert ch.isascii(), (
                f"Entry {entry['id']!r} has a non-ASCII char in URL: {entry['url']}"
            )
        assert " " not in entry["url"], f"Entry {entry['id']!r} has a raw space"


def test_no_duplicate_ids():
    all_entries = list_datasets()
    ids = [e["id"] for e in all_entries]
    assert len(ids) == len(set(ids)), "Duplicate entry IDs found"


def test_no_duplicate_urls_within_group():
    for group_id, info in GROUPS.items():
        urls = [e["url"] for e in info["entries"]]
        assert len(urls) == len(set(urls)), f"Duplicate URLs in group {group_id!r}"


def test_semester_and_month_always_none():
    """INEP não tem séries semestrais/mensais — todos os campos devem ser None."""
    for entry in list_datasets():
        assert entry["semester"] is None
        assert entry["month"] is None


def test_total_dataset_count():
    """Contagem exata confirmada durante a implementação (regressão).

    149 = microdados (16 grupos) + 647 = indicadores educacionais (18 grupos).
    """
    assert len(list_datasets()) == 149 + 647
    assert len(list_datasets()) == 796


# ---------------------------------------------------------------------------
# ENEM / Censo Escolar / Censo Educação Superior (grupos "limpos")
# ---------------------------------------------------------------------------


def test_enem_covers_1998_to_2025_with_no_exceptions():
    entries = GROUPS["enem"]["entries"]
    assert len(entries) == 28
    years = {e["year"] for e in entries}
    assert years == set(range(1998, 2026))
    for e in entries:
        assert (
            e["url"]
            == f"https://download.inep.gov.br/microdados/microdados_enem_{e['year']}.zip"
        )
        assert e["ext"] == "zip"


def test_censo_escolar_2025_has_trailing_underscore():
    entry = next(e for e in GROUPS["censo_escolar"]["entries"] if e["year"] == 2025)
    assert entry["url"].endswith("microdados_censo_escolar_2025_.zip")


def test_censo_escolar_other_years_have_no_trailing_underscore():
    for e in GROUPS["censo_escolar"]["entries"]:
        if e["year"] != 2025:
            assert not e["url"].endswith("_.zip")


def test_censo_educacao_superior_covers_1995_to_2024():
    years = {e["year"] for e in GROUPS["censo_educacao_superior"]["entries"]}
    assert years == set(range(1995, 2025))


# ---------------------------------------------------------------------------
# SAEB (nomenclatura irregular)
# ---------------------------------------------------------------------------


def test_saeb_2021_has_two_entries():
    entries = [e for e in GROUPS["saeb"]["entries"] if e["year"] == 2021]
    assert len(entries) == 2
    urls = {e["url"] for e in entries}
    assert any("educacao_infantil" in u for u in urls)
    assert any("ensino_fundamental_e_medio" in u for u in urls)


def test_saeb_2023_has_two_entries():
    entries = [e for e in GROUPS["saeb"]["entries"] if e["year"] == 2023]
    assert len(entries) == 2
    urls = {e["url"] for e in entries}
    assert any("educacao_infantil" in u for u in urls)
    assert any(u.endswith("microdados_saeb_2023.zip") for u in urls)


def test_saeb_2007_2009_are_uppercase_recalculado():
    for year in (2007, 2009):
        entry = next(e for e in GROUPS["saeb"]["entries"] if e["year"] == year)
        assert f"MICRODADOS_SAEB_{year}_RECALCULADO.zip" in entry["url"]


def test_saeb_early_years_use_micro_saeb_prefix():
    for year in (1995, 1997, 1999, 2001):
        entry = next(e for e in GROUPS["saeb"]["entries"] if e["year"] == year)
        assert entry["url"].endswith(f"micro_saeb{year}.zip")


def test_saeb_total_entry_count():
    assert len(GROUPS["saeb"]["entries"]) == 17


# ---------------------------------------------------------------------------
# ENADE (sufixos LGPD, sem 2020, 2022=.rar)
# ---------------------------------------------------------------------------


def test_enade_has_no_2020_entry():
    years = {e["year"] for e in GROUPS["enade"]["entries"]}
    assert 2020 not in years


def test_enade_2022_is_rar():
    entry = next(e for e in GROUPS["enade"]["entries"] if e["year"] == 2022)
    assert entry["ext"] == "rar"
    assert entry["url"].endswith(".rar")


def test_enade_only_2022_is_rar():
    for e in GROUPS["enade"]["entries"]:
        if e["year"] != 2022:
            assert e["ext"] == "zip"


def test_enade_lgpd_suffix_years():
    lgpd_years = {e["year"] for e in GROUPS["enade"]["entries"] if "_LGPD" in e["url"]}
    assert lgpd_years == set(range(2012, 2020)) | {2022}


def test_enade_total_entry_count():
    assert len(GROUPS["enade"]["entries"]) == 19


# ---------------------------------------------------------------------------
# Encceja (anos não sequenciais)
# ---------------------------------------------------------------------------


def test_encceja_has_gaps_in_2015_2016_2021():
    years = {e["year"] for e in GROUPS["encceja"]["entries"]}
    assert 2015 not in years
    assert 2016 not in years
    assert 2021 not in years
    assert 2014 in years
    assert 2025 in years


def test_encceja_total_entry_count():
    assert len(GROUPS["encceja"]["entries"]) == 10


# ---------------------------------------------------------------------------
# ANA / IDD (poucas edições)
# ---------------------------------------------------------------------------


def test_ana_has_exactly_2014_and_2016():
    years = {e["year"] for e in GROUPS["ana"]["entries"]}
    assert years == {2014, 2016}


def test_idd_has_exactly_2021_2022_2023():
    years = {e["year"] for e in GROUPS["idd"]["entries"]}
    assert years == {2021, 2022, 2023}


def test_idd_url_uses_uppercase_idd():
    for e in GROUPS["idd"]["entries"]:
        assert "microdados_IDD_" in e["url"]


# ---------------------------------------------------------------------------
# ENEM por Escola / TALIS (path aninhado)
# ---------------------------------------------------------------------------


def test_enem_por_escola_is_single_aggregate_entry():
    entries = GROUPS["enem_por_escola"]["entries"]
    assert len(entries) == 1
    assert entries[0]["year"] is None
    assert "2005_a_2015" in entries[0]["url"]


def test_talis_has_two_editions_with_different_url_patterns():
    entries = GROUPS["talis"]["entries"]
    assert len(entries) == 2
    years = {e["year"] for e in entries}
    assert years == {2018, 2024}
    entry_2024 = next(e for e in entries if e["year"] == 2024)
    assert "microdados_do_brasil_na_talis_2024_v2" in entry_2024["url"]


# ---------------------------------------------------------------------------
# Grupos de edição única
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("group_id", sorted(_SINGLE_EDITION_GROUPS))
def test_single_edition_groups_have_exactly_one_entry(group_id):
    assert len(GROUPS[group_id]["entries"]) == 1


# ---------------------------------------------------------------------------
# resolve_group / expand_group / list_datasets
# ---------------------------------------------------------------------------


def test_resolve_canonical_keys():
    for key in ALL_GROUP_KEYS:
        assert resolve_group(key) == key


def test_resolve_unknown_returns_none():
    assert resolve_group("nonexistent") is None


def test_resolve_aliases():
    assert resolve_group("censo") == "censo_escolar"
    assert resolve_group("censo-superior") == "censo_educacao_superior"
    assert resolve_group("magisterio") == "censo_magisterio"
    assert resolve_group("licenciaturas") == "enade_licenciaturas"
    assert resolve_group("discriminacao") == "pesquisa_discriminacao"
    assert resolve_group("docente") == "pnd"


def test_expand_group_unknown_returns_empty():
    assert expand_group("nonexistent") == []


def test_expand_group_single_group_is_singleton_list():
    assert expand_group("enem") == ["enem"]


def test_list_datasets_all():
    all_entries = list_datasets()
    assert len(all_entries) > 0
    groups_present = {e["group"] for e in all_entries}
    assert groups_present == set(ALL_GROUP_KEYS)


def test_list_datasets_filtered():
    entries = list_datasets("ana")
    assert all(e["group"] == "ana" for e in entries)
    assert len(entries) == 2

    via_alias = list_datasets("censo")
    assert via_alias == list_datasets("censo_escolar")


def test_list_datasets_unknown_group_raises():
    with pytest.raises(ValueError, match="Unknown group"):
        list_datasets("bogus")


# ---------------------------------------------------------------------------
# Indicadores Educacionais (18 grupos derivados — descoberta via fragmento
# AJAX por ano, não da página estática; ver catalog_indicadores.py)
# ---------------------------------------------------------------------------


def test_indicadores_macro_alias_expands_to_18_groups():
    expanded = expand_group("indicadores_educacionais")
    assert set(expanded) == _EXPECTED_INDICADORES_GROUPS


def test_indicadores_macro_alias_datasets_count():
    entries = [
        e for g in expand_group("indicadores_educacionais") for e in list_datasets(g)
    ]
    assert len(entries) == 647


def test_indicadores_entries_have_year_none():
    """O nome público do arquivo já embute o período (ano único ou
    intervalo, varia por indicador) — year fica None para não duplicar/
    ambiguar; o período vive em `name`/`base_id`."""
    entries = [e for g in INDICADORES_GROUP_KEYS for e in list_datasets(g)]
    assert all(e["year"] is None for e in entries)


def test_indicadores_source_is_distinct_from_microdados():
    entries = [e for g in INDICADORES_GROUP_KEYS for e in list_datasets(g)]
    assert all(e["source"] == "inep-indicadores-educacionais" for e in entries)
    microdados_entries = [
        e for g in _EXPECTED_MICRODADOS_GROUPS for e in list_datasets(g)
    ]
    assert all(e["source"] == "inep-microdados" for e in microdados_entries)


def test_taxas_rendimento_escolar_has_3_files_for_2025():
    entries = [
        e for e in list_datasets("taxas_rendimento_escolar") if "2025" in e["url"]
    ]
    assert len(entries) == 3
    levels = {e["url"].rsplit("/", 1)[-1] for e in entries}
    assert levels == {
        "tx_rend_brasil_regioes_ufs_2025.zip",
        "tx_rend_escolas_2025.zip",
        "tx_rend_municipios_2025.zip",
    }


def test_taxas_nao_resposta_has_no_spurious_2010_duplicate():
    """Achado da coleta: a aba "2010" de taxas-de-nao-resposta no site do
    INEP na verdade serve os MESMOS arquivos de 2011 (bug do próprio site,
    confirmado por re-fetch) — removido do catálogo para não duplicar dados
    de 2011 sob um rótulo de ano incorreto."""
    urls = {e["url"] for e in list_datasets("taxas_nao_resposta")}
    assert not any("/2010/" in u for u in urls)
    assert any("2011" in u for u in urls)


def test_nivel_socioeconomico_has_4_files_per_year():
    entries = [e for e in list_datasets("nivel_socioeconomico") if "2023" in e["url"]]
    assert len(entries) == 4


def test_indicadores_financeiros_is_static_without_year_in_filename():
    """Os 10 arquivos de indicadores financeiros não têm aba por ano — são
    séries históricas completas em um único arquivo cada."""
    entries = list_datasets("indicadores_financeiros_educacionais")
    assert len(entries) == 10
    for e in entries:
        assert e["year"] is None


def test_indicadores_urls_start_with_https():
    entries = [e for g in INDICADORES_GROUP_KEYS for e in list_datasets(g)]
    for e in entries:
        assert e["url"].startswith("https://download.inep.gov.br/")


def test_indicadores_no_duplicate_ids_globally():
    """Os ids dos 18 grupos de indicadores não colidem entre si nem com os
    16 grupos de microdados."""
    all_entries = list_datasets()
    ids = [e["id"] for e in all_entries]
    assert len(ids) == len(set(ids))


def test_indicadores_naming_era_shift_within_same_group():
    """Regressão do achado principal: dentro de um MESMO indicador, a
    nomenclatura muda de era (prefixo maiúsculo compacto nos anos recentes
    vs. nome descritivo em português com subdiretório extra nos anos
    antigos) — não existe fórmula única por range()."""
    urls = [e["url"] for e in list_datasets("media_horas_aula_diaria")]
    recent = [u for u in urls if "/2025/HAD_2025" in u]
    old = [u for u in urls if "media_hora_aula_diaria/2010" in u]
    assert recent, "formato recente (HAD_2025_*) não encontrado"
    assert old, "formato antigo (media_hora_aula_diaria/2010/*) não encontrado"
