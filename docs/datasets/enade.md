---
dataset:
  id: enade
  fonte: inep
  titulo: Enade — microdados
  resumo: 'Microdados do Exame Nacional de Desempenho dos Estudantes (Enade), edições 2010 a 2023: curso, presença, notas e questionário do estudante, em arquivos separados que só se ligam pelo código do curso.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual por ciclo; uma edição por ano de 2010 a 2023, exceto 2020 (sem edição)
  cobertura:
    inicio: '2010'
    fim: '2023'
  unidade: um estudante concluinte inscrito no Enade em cada arquivo `arqN`; os arquivos têm a mesma população, mas as linhas não correspondem entre arquivos
  granularidade:
    espacial: curso (código do curso, município, UF e região do curso e instituição); sem identificação do estudante
    temporal: ano da edição
  formato_bruto: ZIP anual (em 2022, RAR) com `LEIA-ME` (manual do usuário, questionário e dicionário em xlsx e ods) e `DADOS` com arquivos `.txt` separados por ponto e vírgula, um por grupo de variáveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 160
  unidades_de_medida:
    nt_ger: pontos de 0 a 100
    nt_fg: pontos de 0 a 100
    nt_obj_fg: pontos de 0 a 100
    nt_dis_fg: pontos de 0 a 100
    nt_fg_d1: pontos de 0 a 100
    nt_fg_d2: pontos de 0 a 100
    nt_ce: pontos de 0 a 100
    nt_obj_ce: pontos de 0 a 100
    nt_dis_ce: pontos de 0 a 100
    nt_ce_d1: pontos de 0 a 100
    nt_ce_d2: pontos de 0 a 100
    nt_ce_d3: pontos de 0 a 100
    nt_fg_d1_pt: pontos de 0 a 100
    nt_fg_d1_ct: pontos de 0 a 100
    nt_fg_d2_pt: pontos de 0 a 100
    nt_fg_d2_ct: pontos de 0 a 100
    nu_idade: anos
    nu_item_ofg: itens
    nu_item_oce: itens
    nu_item_ofg_z: itens
    nu_item_ofg_x: itens
    nu_item_ofg_n: itens
    nu_item_oce_z: itens
    nu_item_oce_x: itens
    nu_item_oce_n: itens
    ano_fim_em: ano
    ano_in_grad: ano
  dados_pessoais:
  - coluna: tp_sexo
    categoria: sexo do estudante (arquivo próprio, sem ligação com as demais respostas)
  - coluna: nu_idade
    categoria: idade do estudante no dia da prova
  - coluna: qe_i04
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i05
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i06
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i07
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i08
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i09
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i10
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i11
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i12
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i13
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i14
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i15
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i16
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i17
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i18
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i19
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i20
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i21
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i22
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i23
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i24
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i25
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i26
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i27
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i28
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i29
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i30
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i31
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i32
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i33
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i34
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i35
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i36
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i37
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i38
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i39
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i40
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i41
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i42
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i43
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i44
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i45
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i46
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i47
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i48
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i49
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i50
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i51
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i52
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i53
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i54
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i01
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i02
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i03
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i55
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i56
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i57
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i58
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i59
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i60
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i61
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i62
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i63
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i64
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i65
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i66
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i67
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i69
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i70
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i71
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i72
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i73
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i74
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i75
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i68
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i76
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i77
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i78
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i79
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i80
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i81
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i82
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i83
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i84
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i85
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i86
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i87
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i88
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i89
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i90
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i91
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: qe_i92
    categoria: resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)
  - coluna: co_rs_i1
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i2
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i3
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i4
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i5
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i6
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i7
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i8
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: co_rs_i9
    categoria: resposta individual ao questionário de percepção da prova
  - coluna: ano_fim_em
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: ano_in_grad
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: in_matut
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: in_vesper
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: in_noturno
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: co_turno_graduacao
    categoria: trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)
  - coluna: ds_vt_esc_ofg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: ds_vt_ace_ofg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: ds_vt_esc_oce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: ds_vt_ace_oce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pres
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pr_ger
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pr_ob_fg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pr_di_fg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pr_ob_ce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_pr_di_ce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_sfg_d1
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_sfg_d2
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_sce_d1
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_sce_d2
    categoria: presença e desempenho individual do estudante na prova
  - coluna: tp_sce_d3
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_ger
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_obj_fg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_dis_fg
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d1
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d2
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_ce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_obj_ce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_dis_ce
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_ce_d1
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_ce_d2
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_ce_d3
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d1_pt
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d1_ct
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d2_pt
    categoria: presença e desempenho individual do estudante na prova
  - coluna: nt_fg_d2_ct
    categoria: presença e desempenho individual do estudante na prova
  eras:
  - desde: '2010'
    mudanca: o exame passa a ser censitário para todos os estudantes habilitados; os dados chegam já separados em arquivos `arqN` (27 arquivos em 2010 a 2012)
  - desde: '2011'
    mudanca: só os estudantes concluintes fazem a prova; os ingressantes são dispensados do exame
  - desde: '2013'
    mudanca: novo Questionário do Estudante (25 perguntas, 31 arquivos); a avaliação do processo formativo vai de QE_I26 a QE_I67
  - desde: '2014'
    mudanca: as edições com licenciaturas (2014, 2017 e 2021) trazem perguntas de licenciatura (QE_I69 a QE_I81) em arquivos próprios, e o Questionário do Estudante passa a ter 26 perguntas e QE_I27 a QE_I68 de avaliação do processo formativo
  - desde: '2017'
    mudanca: o turno deixa de vir em IN_MATUT, IN_VESPER e IN_NOTURNO e passa a vir agregado em CO_TURNO_GRADUACAO; em 2017 o Inep também registra a adequação dos microdados à LGPD e a exclusão de respostas de questionário quando há só um respondente no curso
  - desde: '2021'
    mudanca: questionário complementar da pandemia em arquivo próprio (QE_I82 a QE_I92 em 2021; QE_I69 a QE_I79 em 2022)
  - desde: '2022'
    mudanca: o pacote vem em RAR, único formato desse tipo no catálogo do Inep; o dicionário é o único documento do pacote
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Enade — microdados

## Resumo

Microdados do Enade, exame do Sistema Nacional de Avaliação da Educação Superior (Sinaes) aplicado pelo Inep aos estudantes concluintes dos cursos de graduação de cada área avaliada no ano. Cada edição traz, por estudante, a caracterização do curso e da instituição, a situação de presença, as notas e os vetores de respostas da prova (formação geral e componente específico), as respostas do Questionário do Estudante e do questionário de percepção da prova. Em atenção à LGPD, os dados vêm repartidos em dezenas de arquivos `arqN` ordenados por variáveis diferentes: dá para agrupar os arquivos por curso, mas não por estudante. O lake cobre as edições de 2010 a 2023 (sem 2020, quando o exame não foi aplicado).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/enade` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual por ciclo; uma edição por ano de 2010 a 2023, exceto 2020 (sem edição) |
| Cobertura | 2010 a 2023 |
| Unidade (uma linha) | um estudante concluinte inscrito no Enade em cada arquivo `arqN`; os arquivos têm a mesma população, mas as linhas não correspondem entre arquivos |
| Granularidade | espacial: curso (código do curso, município, UF e região do curso e instituição); sem identificação do estudante; temporal: ano da edição |
| Formato bruto | ZIP anual (em 2022, RAR) com `LEIA-ME` (manual do usuário, questionário e dicionário em xlsx e ods) e `DADOS` com arquivos `.txt` separados por ponto e vírgula, um por grupo de variáveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 160 |
| Unidades de medida | `nt_ger`: pontos de 0 a 100; `nt_fg`: pontos de 0 a 100; `nt_obj_fg`: pontos de 0 a 100; `nt_dis_fg`: pontos de 0 a 100; `nt_fg_d1`: pontos de 0 a 100; `nt_fg_d2`: pontos de 0 a 100; `nt_ce`: pontos de 0 a 100; `nt_obj_ce`: pontos de 0 a 100; `nt_dis_ce`: pontos de 0 a 100; `nt_ce_d1`: pontos de 0 a 100; `nt_ce_d2`: pontos de 0 a 100; `nt_ce_d3`: pontos de 0 a 100; `nt_fg_d1_pt`: pontos de 0 a 100; `nt_fg_d1_ct`: pontos de 0 a 100; `nt_fg_d2_pt`: pontos de 0 a 100; `nt_fg_d2_ct`: pontos de 0 a 100; `nu_idade`: anos; `nu_item_ofg`: itens; `nu_item_oce`: itens; `nu_item_ofg_z`: itens; `nu_item_ofg_x`: itens; `nu_item_ofg_n`: itens; `nu_item_oce_z`: itens; `nu_item_oce_x`: itens; `nu_item_oce_n`: itens; `ano_fim_em`: ano; `ano_in_grad`: ano |
| Dados pessoais | `tp_sexo` (sexo do estudante (arquivo próprio, sem ligação com as demais respostas)); `nu_idade` (idade do estudante no dia da prova); `qe_i04` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i05` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i06` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i07` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i08` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i09` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i10` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i11` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i12` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i13` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i14` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i15` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i16` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i17` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i18` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i19` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i20` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i21` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i22` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i23` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i24` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i25` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i26` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i27` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i28` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i29` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i30` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i31` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i32` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i33` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i34` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i35` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i36` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i37` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i38` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i39` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i40` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i41` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i42` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i43` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i44` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i45` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i46` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i47` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i48` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i49` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i50` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i51` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i52` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i53` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i54` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i01` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i02` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i03` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i55` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i56` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i57` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i58` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i59` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i60` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i61` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i62` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i63` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i64` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i65` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i66` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i67` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i69` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i70` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i71` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i72` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i73` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i74` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i75` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i68` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i76` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i77` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i78` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i79` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i80` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i81` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i82` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i83` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i84` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i85` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i86` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i87` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i88` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i89` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i90` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i91` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `qe_i92` (resposta individual do Questionário do Estudante (estado civil, cor ou raça, renda, trabalho, escola, família e outras)); `co_rs_i1` (resposta individual ao questionário de percepção da prova); `co_rs_i2` (resposta individual ao questionário de percepção da prova); `co_rs_i3` (resposta individual ao questionário de percepção da prova); `co_rs_i4` (resposta individual ao questionário de percepção da prova); `co_rs_i5` (resposta individual ao questionário de percepção da prova); `co_rs_i6` (resposta individual ao questionário de percepção da prova); `co_rs_i7` (resposta individual ao questionário de percepção da prova); `co_rs_i8` (resposta individual ao questionário de percepção da prova); `co_rs_i9` (resposta individual ao questionário de percepção da prova); `ano_fim_em` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `ano_in_grad` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `in_matut` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `in_vesper` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `in_noturno` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `co_turno_graduacao` (trajetória escolar do estudante (ano de conclusão do ensino médio, ingresso na graduação e turno)); `ds_vt_esc_ofg` (presença e desempenho individual do estudante na prova); `ds_vt_ace_ofg` (presença e desempenho individual do estudante na prova); `ds_vt_esc_oce` (presença e desempenho individual do estudante na prova); `ds_vt_ace_oce` (presença e desempenho individual do estudante na prova); `tp_pres` (presença e desempenho individual do estudante na prova); `tp_pr_ger` (presença e desempenho individual do estudante na prova); `tp_pr_ob_fg` (presença e desempenho individual do estudante na prova); `tp_pr_di_fg` (presença e desempenho individual do estudante na prova); `tp_pr_ob_ce` (presença e desempenho individual do estudante na prova); `tp_pr_di_ce` (presença e desempenho individual do estudante na prova); `tp_sfg_d1` (presença e desempenho individual do estudante na prova); `tp_sfg_d2` (presença e desempenho individual do estudante na prova); `tp_sce_d1` (presença e desempenho individual do estudante na prova); `tp_sce_d2` (presença e desempenho individual do estudante na prova); `tp_sce_d3` (presença e desempenho individual do estudante na prova); `nt_ger` (presença e desempenho individual do estudante na prova); `nt_fg` (presença e desempenho individual do estudante na prova); `nt_obj_fg` (presença e desempenho individual do estudante na prova); `nt_dis_fg` (presença e desempenho individual do estudante na prova); `nt_fg_d1` (presença e desempenho individual do estudante na prova); `nt_fg_d2` (presença e desempenho individual do estudante na prova); `nt_ce` (presença e desempenho individual do estudante na prova); `nt_obj_ce` (presença e desempenho individual do estudante na prova); `nt_dis_ce` (presença e desempenho individual do estudante na prova); `nt_ce_d1` (presença e desempenho individual do estudante na prova); `nt_ce_d2` (presença e desempenho individual do estudante na prova); `nt_ce_d3` (presença e desempenho individual do estudante na prova); `nt_fg_d1_pt` (presença e desempenho individual do estudante na prova); `nt_fg_d1_ct` (presença e desempenho individual do estudante na prova); `nt_fg_d2_pt` (presença e desempenho individual do estudante na prova); `nt_fg_d2_ct` (presença e desempenho individual do estudante na prova) |
| Eras | 2010: o exame passa a ser censitário para todos os estudantes habilitados; os dados chegam já separados em arquivos `arqN` (27 arquivos em 2010 a 2012); 2011: só os estudantes concluintes fazem a prova; os ingressantes são dispensados do exame; 2013: novo Questionário do Estudante (25 perguntas, 31 arquivos); a avaliação do processo formativo vai de QE_I26 a QE_I67; 2014: as edições com licenciaturas (2014, 2017 e 2021) trazem perguntas de licenciatura (QE_I69 a QE_I81) em arquivos próprios, e o Questionário do Estudante passa a ter 26 perguntas e QE_I27 a QE_I68 de avaliação do processo formativo; 2017: o turno deixa de vir em IN_MATUT, IN_VESPER e IN_NOTURNO e passa a vir agregado em CO_TURNO_GRADUACAO; em 2017 o Inep também registra a adequação dos microdados à LGPD e a exclusão de respostas de questionário quando há só um respondente no curso; 2021: questionário complementar da pandemia em arquivo próprio (QE_I82 a QE_I92 em 2021; QE_I69 a QE_I79 em 2022); 2022: o pacote vem em RAR, único formato desse tipo no catálogo do Inep; o dicionário é o único documento do pacote |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_enade_<ano>.zip` (2010, 2011, 2021, 2023), `microdados_enade_<ano>_LGPD.zip` (2012 a 2019) e `microdados_enade_2022_LGPD.rar` (2022), conforme o catálogo; o nome do arquivo na fonte não segue uma regra única.
- Não houve edição em 2020 (o catálogo registra que o exame não foi aplicado). A página oficial lista também as edições de 2004 a 2009, que o catálogo do fetcher não inclui, de modo que o lake começa em 2010.
- Cada ZIP tem a pasta `LEIA-ME` (manual do usuário, questionário do estudante, dicionário de arquivos e de variáveis; em 2014, 2017 e 2021 também o questionário de licenciatura e, em 2021, as questões complementares da pandemia) e a pasta `DADOS` com os `.txt`. O conversor lê só os `.txt` de `DADOS`.
- O manual diz que os arquivos usam ponto e vírgula, cabeçalho na primeira linha, decimal com ponto e valores faltantes como ponto nas variáveis numéricas e em branco nas de texto; `DS_VT_ACE_OFG` e `DS_VT_ACE_OCE` devem ser lidos como texto.
- Tamanhos descompactados do índice dos ZIP: `arq3` (prova e notas) é o maior, com 100 MB em 2010, 121 MB em 2021 e 92 MB em 2023; `arq1` tem 17,8 MB em 2023 e os arquivos de uma pergunta do questionário, 6,1 MB em 2023.
- O pacote de 2022 que o conversor lê traz só o dicionário em `LEIA-ME`, sem manual do usuário em PDF.

## Conteúdo

Os arquivos `microdados<ano>_arq1`, `arq2`, ... são colunas do mesmo exame repartidas por grupo de variáveis (Manual do usuário, seção 6 de cada edição; dicionário de arquivos). **Todos trazem `nu_ano` e `co_curso`**, e a linha de um arquivo não é a mesma pessoa da mesma linha de outro arquivo. O conteúdo de cada arquivo segue o dicionário:

| Arquivo | Conteúdo |
|---|---|
| `arq1` | caracterização do curso: código da IES, categoria administrativa, organização acadêmica, área de enquadramento no Enade (`co_grupo`), modalidade, município, UF e região do curso |
| `arq2` | informações acadêmicas do estudante: ano de término do ensino médio, ano de ingresso na graduação e turno (`in_matut`, `in_vesper`, `in_noturno` até 2016; `co_turno_graduacao` desde 2017) |
| `arq3` | a prova: número de itens válidos por seção, gabaritos e vetores de respostas, tipos de presença (`tp_pres`), situação das questões discursivas, notas de formação geral e componente específico (`nt_*`) e as respostas do questionário de percepção da prova (`co_rs_i1` a `co_rs_i9`) |
| `arq4` | avaliação do processo formativo pelo estudante (organização didático-pedagógica, infraestrutura e oportunidades de ampliação da formação): `qe_i22` a `qe_i54` em 2010 a 2012, `qe_i26` a `qe_i67` em 2013, `qe_i27` a `qe_i68` desde 2014 |
| `arq5` | sexo (`tp_sexo`) |
| `arq6` | idade do inscrito no dia da prova (`nu_idade`) |
| `arq7` em diante | perguntas do Questionário do Estudante, uma por arquivo: o arquivo `arq<6+n>` traz a pergunta QE`n` (`qe_i<n>`): estado civil (QE1), cor ou raça (QE2), nacionalidade, escolaridade dos pais, moradia, renda, trabalho, bolsas, ensino médio e razões de escolha do curso, entre outras |

Número de arquivos e perguntas por edição (dicionário de arquivos de cada edição):

| Edições | Arquivos | Perguntas do questionário e arquivos extras |
|---|---|---|
| 2010, 2011, 2012 | 27 | QE1 a QE21 em `arq7` a `arq27` |
| 2013 | 31 | QE1 a QE25 em `arq7` a `arq31` |
| 2015, 2016, 2018, 2019 | 32 | QE1 a QE26 em `arq7` a `arq32` |
| 2014, 2017 | 42 | QE1 a QE26 em `arq7` a `arq32`; perguntas de licenciatura QE69 a QE77 em `arq33` a `arq41`; `arq42` com as questões de licenciatura sobre o curso (`qe_i78` a `qe_i81`) |
| 2021 | 43 | como 2014 e 2017, mais `arq43` com o questionário complementar da pandemia (`qe_i82` a `qe_i92`) |
| 2022 | 33 | QE1 a QE26 em `arq7` a `arq32`; `arq33` com o questionário complementar da pandemia (`qe_i69` a `qe_i79`) |
| 2023 | 32 | QE1 a QE26 em `arq7` a `arq32`; o índice do dicionário ainda lista um `arq33` da pandemia que o ZIP não traz |

- O Enade avalia a cada edição os concluintes de um conjunto de áreas (por exemplo, em 2023, bacharelados como Agronomia, Medicina, Engenharias e tecnologias como Agronegócio e Radiologia, segundo o Manual); o conjunto de cursos muda entre edições.
- Os Manuais de 2021 e 2023 informam que os microdados trazem estudantes concluintes inscritos regularmente, e que resultados de curso com um só estudante com resultado válido (`tp_pres` = 555) e respostas de questionário de curso com um só respondente foram excluídos, em cumprimento ao art. 5º, § 9º, da Lei do Sinaes e à LGPD.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2010 | 27 arquivos, de 3 a 42 colunas |
| 2011 | 27 arquivos, de 3 a 42 colunas |
| 2012 | 27 arquivos, de 3 a 42 colunas |
| 2013 | 31 arquivos, de 3 a 46 colunas |
| 2014 | 42 arquivos, de 3 a 52 colunas |
| 2015 | 32 arquivos, de 3 a 52 colunas |
| 2016 | 32 arquivos, de 3 a 52 colunas |
| 2017 | 42 arquivos, de 3 a 52 colunas |
| 2018 | 32 arquivos, de 3 a 52 colunas |
| 2019 | 32 arquivos, de 3 a 52 colunas |
| 2021 | 43 arquivos, de 3 a 52 colunas |
| 2022 | 33 arquivos, de 3 a 52 colunas |
| 2023 | 32 arquivos, de 3 a 44 colunas |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx) de cada edição, lido edição a edição; a coluna descreve a edição mais recente em que aparece e, quando a pergunta muda, mostra o enunciado mais recente e o mais antigo.
As colunas `qe_iNN` **não têm o mesmo significado em todas as edições**: por exemplo, `qe_i04` é o número de pessoas da família que moram com o estudante em 2010 a 2012 e a escolaridade do pai em 2013 em diante, e `qe_i69` é pergunta de licenciatura em 2014, 2017 e 2021 e do questionário da pandemia em 2022. Confira o *Período* e o dicionário da edição.
A coluna *Arquivos* indica em quais arquivos do lake a coluna aparece (o nome do arquivo sem o ano, `microdados_arqN`).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `nu_ano` | `NU_ANO` | texto | Ano de realização do exame | — | todo | `microdados_arq1`, `microdados_arq10`, `microdados_arq11` e mais 40 |
| `co_curso` | `CO_CURSO` | texto | Código do curso no Enade | — | todo | `microdados_arq1`, `microdados_arq10`, `microdados_arq11` e mais 40 |
| `co_ies` | `CO_IES` | texto | Código da IES (e-MEC) | — | todo | `microdados_arq1` |
| `co_categad` | `CO_CATEGAD` | texto | Código da categoria administrativa da IES (1 = Pública Federal; 2 = Pública Estadual; 3 = Pública Municipal; 4 = Privada com fins lucrativos; 5 = Privada sem fins lucrativos; 7 = Especial; 8 = Comunitária/Confessional) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq1` |
| `co_orgacad` | `CO_ORGACAD` | texto | Código da organização acadêmica da IES (10019 = Centro Federal de Educação Tecnológica; 10020 = Centro Universitário; 10022 = Faculdade; 10026 = Instituto Federal de Educação, Ciência e Tecnologia; 10028 = Universidade) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq1` |
| `co_grupo` | `CO_GRUPO` | texto | Código da Área de enquadramento do curso no Enade (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq1` |
| `co_modalidade` | `CO_MODALIDADE` | texto | Código da Modalidade de Ensino (0 = EaD; 1 = Presencial) | — | todo | `microdados_arq1` |
| `co_munic_curso` | `CO_MUNIC_CURSO` | texto | Código do município de funcionamento do curso | — | todo | `microdados_arq1` |
| `co_uf_curso` | `CO_UF_CURSO` | texto | Código da UF de funcionamento do curso (lista de códigos no dicionário da fonte) | — | todo | `microdados_arq1` |
| `co_regiao_curso` | `CO_REGIAO_CURSO` | texto | Código da região de funcionamento do curso (1 = Região Norte (N); 2 = Região Nordeste (NE); 3 = Região Sudeste (SE); 4 = Região Sul (SUL); 5 = Região Centro-Oeste (CO)) | — | todo | `microdados_arq1` |
| `qe_i04` | `QE_I04` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Até que etapa de escolarização seu pai concluiu? Em 2010: Quantas pessoas, da sua família, moram com você na mesma casa? (Contando com seus pais, irmãos, cônjuge, filhos ou outros parentes que moram na mesma casa com você) | — | todo | `microdados_arq10` |
| `qe_i05` | `QE_I05` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Até que etapa de escolarização sua mãe concluiu? Em 2010: Somando a sua renda com a renda dos familiares que moram com você, quanto é, aproximadamente, a renda familiar? (Considere a renda de todos os seus familiares que moram… | — | todo | `microdados_arq11` |
| `qe_i06` | `QE_I06` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Onde e com quem você mora atualmente? Em 2010: Assinale a situação [financeira] abaixo que melhor descreve seu caso (incluindo bolsa). | — | todo | `microdados_arq12` |
| `qe_i07` | `QE_I07` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Quantas pessoas da sua família moram com você? Considere seus pais, irmãos, cônjuge, filhos e outros parentes que moram na mesma casa com você. Em 2010: Indique a resposta que melhor descreve sua atual situação de trabalho (Não contar estágio, bolsas de pesquisa ou monitoria). | — | todo | `microdados_arq13` |
| `qe_i08` | `QE_I08` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual a renda total de sua família, incluindo seus rendimentos? Em 2010: Durante o curso de graduação (responder somente no caso de ser concluinte): | — | todo | `microdados_arq14` |
| `qe_i09` | `QE_I09` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)? Em 2010: Você recebe ou recebeu algum tipo de bolsa de estudos ou financiamento para custear as mensalidades do curso? | — | todo | `microdados_arq15` |
| `qe_i10` | `QE_I10` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual alternativa a seguir melhor descreve sua situação de trabalho (exceto estágio ou bolsas)? Em 2010: Que tipo de bolsa de estudos ou financiamento você recebe ou recebeu para custear as mensalidades do curso? | — | todo | `microdados_arq16` |
| `qe_i11` | `QE_I11` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? No caso de haver mais de uma opção, marcar… Em 2010: Você recebe ou recebeu alguma bolsa para custear outras despesas do curso? | — | todo | `microdados_arq17` |
| `qe_i12` | `QE_I12` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Ao longo da sua trajetória acadêmica, você recebeu algum tipo de auxílio de permanência? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. Em 2010: Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa? | — | todo | `microdados_arq18` |
| `qe_i13` | `QE_I13` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Ao longo da sua trajetória acadêmica, você recebeu algum tipo de bolsa acadêmica? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. Em 2010: Até que nível seu pai estudou? | — | todo | `microdados_arq19` |
| `ano_fim_em` | `ANO_FIM_EM` | texto | Ano de conclusão do Ensino Médio | — | todo | `microdados_arq2` |
| `ano_in_grad` | `ANO_IN_GRAD` | texto | Ano de início da graduação | — | todo | `microdados_arq2` |
| `in_matut` | `IN_MATUT` | texto | Indicador de turno matutino (0 = Não; 1 = Sim) | — | 2010 a 2016 | `microdados_arq2` |
| `in_vesper` | `IN_VESPER` | texto | Indicador de turno vespertino (0 = Não; 1 = Sim) | — | 2010 a 2016 | `microdados_arq2` |
| `in_noturno` | `IN_NOTURNO` | texto | Indicador de turno noturno (0 = Não; 1 = Sim) | — | 2010 a 2016 | `microdados_arq2` |
| `qe_i14` | `QE_I14` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Durante o curso de graduação, você participou de programas e/ou atividades curriculares no exterior? Em 2010: Até que nível de ensino sua mãe estudou? | — | todo | `microdados_arq20` |
| `qe_i15` | `QE_I15` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social? Em 2010: Em que unidade da Federação você concluiu o ensino médio? | — | todo | `microdados_arq21` |
| `qe_i16` | `QE_I16` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Em que unidade da Federação você concluiu o ensino médio? Em 2010: Você mudou de cidade, estado ou país para realizar este curso? | — | todo | `microdados_arq22` |
| `qe_i17` | `QE_I17` | texto | Item do questionário; as alternativas de resposta mudam entre as edições (aqui, 2023): Em que tipo de escola você cursou o ensino médio? (A = Todo em escola pública; B = Todo em escola privada (particular); C = Todo no exterior; D = A maior parte em escola pública; E = A maior parte em escola privada (particular); F = Parte no Brasil e parte no exterior) | — | todo | `microdados_arq23` |
| `qe_i18` | `QE_I18` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual modalidade de ensino médio você concluiu? Em 2010: Que tipo de curso de ensino médio você concluiu? | — | todo | `microdados_arq24` |
| `qe_i19` | `QE_I19` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Quem lhe deu maior incentivo para cursar a graduação? Em 2010: Excetuando-se os livros indicados na bibliografia do seu curso, quantos livros você leu este ano? | — | todo | `microdados_arq25` |
| `qe_i20` | `QE_I20` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Algum dos grupos abaixo foi determinante para você enfrentar dificuldades durante seu curso superior e concluí-lo? Em 2010: Quantas horas por semana, aproximadamente, você dedica aos estudos, excetuando as horas de aula? | — | todo | `microdados_arq26` |
| `qe_i21` | `QE_I21` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Alguém em sua família concluiu um curso superior? Em 2010: Até o momento, qual turno concentrou a maior parte das disciplinas do seu curso? | — | todo | `microdados_arq27` |
| `nu_item_ofg` | `NU_ITEM_OFG` | texto | Número de itens da parte objetiva da Formação Geral | — | todo | `microdados_arq3` |
| `nu_item_oce` | `NU_ITEM_OCE` | texto | Número de itens da parte objetiva de Componente Específico | — | todo | `microdados_arq3` |
| `ds_vt_gab_ofg_fin` | `DS_VT_GAB_OFG_FIN` | texto | Vetor que representa o gabarito final de Formação Geral (1 letra por item (intervalo de A a E); Z = questão excluída devido à anulação; X = questão excluída devido ao coeficiente ponto-bisserial < 0,20) | — | todo | `microdados_arq3` |
| `ds_vt_gab_oce_fin` | `DS_VT_GAB_OCE_FIN` | texto | Vetor que representa o gabarito final de Componente Específico (1 letra por item (intervalo de A a E); 8 = questão excluída devido à anulação; 9 = questão excluída devido ao coeficiente ponto-bisserial < 0,20) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `ds_vt_esc_ofg` | `DS_VT_ESC_OFG` | texto | Vetor que representa a escolha de resposta da parte objetiva da Formação Geral | — | todo | `microdados_arq3` |
| `ds_vt_ace_ofg` | `DS_VT_ACE_OFG` | texto | Vetor que representa os acertos da parte objetiva na Formação Geral (0 = Errado; 1 = Certo; 8 = Anulada pela comissão; 9 = Anulada pelo índice de discriminação (correlação pontobisserial < 0,20)) | — | todo | `microdados_arq3` |
| `ds_vt_esc_oce` | `DS_VT_ESC_OCE` | texto | Vetor que representa a escolha de resposta da parte objetiva do Componente Específico | — | todo | `microdados_arq3` |
| `ds_vt_ace_oce` | `DS_VT_ACE_OCE` | texto | Vetor que representa os acertos da parte objetiva do Componente Específico (0 = Errado; 1 = Certo; 8 = Anulada pela comissão; 9 = Anulada pelo índice de discriminação) | — | todo | `microdados_arq3` |
| `tp_pres` | `TP_PRES` | texto | Tipo de presença no Enade (222 = Ausente; 334 = Eliminado por participação indevida; 444 = Ausente devido a dupla graduação; 555 = Presente com resultado válido; 565 = Dispensado da prova, por ausência de ensalamento; 585 = Dispensado da prova, por fenômenos da natureza; 888 = Presente na prova, com resultado desconsiderado pelo Inep) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_pr_ger` | `TP_PR_GER` | texto | Tipo de presença na prova (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_pr_ob_fg` | `TP_PR_OB_FG` | texto | Tipo de presença na parte objetiva na formação geral (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_pr_di_fg` | `TP_PR_DI_FG` | texto | Tipo de presença na parte discursiva na formação geral (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_pr_ob_ce` | `TP_PR_OB_CE` | texto | Tipo de presença na parte objetiva no componente específico (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_pr_di_ce` | `TP_PR_DI_CE` | texto | Tipo de presença na parte discursiva no componente específico (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_sfg_d1` | `TP_SFG_D1` | texto | Tipo de situação da questão 1 da parte discursiva da formação geral (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_sfg_d2` | `TP_SFG_D2` | texto | Tipo de situação da questão 2 da parte discursiva da formação geral (lista de códigos no dicionário da fonte) Códigos da edição 2022; podem mudar em edições anteriores. | — | 2010 a 2022 | `microdados_arq3` |
| `tp_sce_d1` | `TP_SCE_D1` | texto | Tipo de situação da questão 1 da parte discursiva do componente específico (lista de códigos no dicionário da fonte) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq3` |
| `tp_sce_d2` | `TP_SCE_D2` | texto | Tipo de situação da questão 2 da parte discursiva do componente específico (lista de códigos no dicionário da fonte) Códigos da edição 2022; podem mudar em edições anteriores. | — | 2010 a 2022 | `microdados_arq3` |
| `tp_sce_d3` | `TP_SCE_D3` | texto | Tipo de situação da questão 3 da parte discursiva do componente específico (lista de códigos no dicionário da fonte) Códigos da edição 2022; podem mudar em edições anteriores. | — | 2010 a 2022 | `microdados_arq3` |
| `nt_ger` | `NT_GER` | texto | Nota bruta da prova - Média ponderada da formação geral (25%) e componente específico (75%). (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_fg` | `NT_FG` | texto | Nota bruta na formação geral - Média ponderada da parte objetiva (60%) e discursiva (40%) na formação geral. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_obj_fg` | `NT_OBJ_FG` | texto | Nota bruta na parte objetiva da formação geral. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_dis_fg` | `NT_DIS_FG` | texto | Nota bruta na parte discursiva da formação geral. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_fg_d1` | `NT_FG_D1` | texto | Nota da questão 1 da parte discursiva da formação geral - Média ponderada da parte de Língua Portuguesa (20%) e Conteúdo (80%) da Questão 1 da parte discursiva (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_fg_d2` | `NT_FG_D2` | texto | Nota da questão 2 da parte discursiva na formação geral - Média ponderada da parte de Língua Portuguesa (20%) e Conteúdo (80%) da Questão 2 da parte discursiva. (valor de 0 a 100) | — | 2010 a 2022 | `microdados_arq3` |
| `nt_ce` | `NT_CE` | texto | Nota bruta no componente específico - Média ponderada da parte objetiva (85%) e discursiva (15%) no componente específico. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_obj_ce` | `NT_OBJ_CE` | texto | Nota bruta na parte objetiva do componente específico. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_dis_ce` | `NT_DIS_CE` | texto | Nota bruta na parte discursiva do componente específico. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_ce_d1` | `NT_CE_D1` | texto | Nota da questão 1 da parte discursiva do componente específico. (valor de 0 a 100) | — | todo | `microdados_arq3` |
| `nt_ce_d2` | `NT_CE_D2` | texto | Nota da questão 2 da parte discursiva do componente específico. (valor de 0 a 100) | — | 2010 a 2022 | `microdados_arq3` |
| `nt_ce_d3` | `NT_CE_D3` | texto | Nota da questão 3 da parte discursiva do componente específico. (valor de 0 a 100) | — | 2010 a 2022 | `microdados_arq3` |
| `co_rs_i1` | `CO_RS_I1` | texto | 1 - Qual o grau de dificuldade desta prova na parte de Formação Geral? (A = Muito fácil; B = Fácil; C = Médio; D = Difícil; E = Muito difícil; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i2` | `CO_RS_I2` | texto | 2 - Qual o grau de dificuldade desta prova na parte do Componente Específico? (A = Muito fácil; B = Fácil; C = Médio; D = Difícil; E = Muito difícil; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i3` | `CO_RS_I3` | texto | 3 - Considerando a extensão da prova, em relação ao tempo total, você considera que a prova foi: (A = Muito longa; B = Longa; C = Adequada; D = Curta; E = Muito curta; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i4` | `CO_RS_I4` | texto | 4 - Os enunciados das questões da prova na parte de Formação Geral estavam claros e objetivos? (A = Sim, todos; B = Sim, a maioria; C = Apenas cerca da metade; D = Poucos; E = Não, nenhum; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i5` | `CO_RS_I5` | texto | Item do questionário; as alternativas de resposta mudam entre as edições (aqui, 2023): 5 - Os enunciados das questões na parte do Componente Específico estavam claros e objetivos? (A = Sim, todos; B = Sim, a maioria; C = Apenas cerca da metade; D = Poucos se apresentam; E = Não, nenhum; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i6` | `CO_RS_I6` | texto | 6 - As informações/instruções fornecidas para a resolução das questões foram suficientes para resolvê-las? (A = Sim, até excessivas; B = Sim, em todas elas; C = Sim, na maioria delas; D = Sim, somente em algumas; E = Não, em nenhuma delas; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i7` | `CO_RS_I7` | texto | Item do questionário; as alternativas de resposta mudam entre as edições (aqui, 2023): 7 - Você se deparou com alguma dificuldade ao responder à prova. Qual? (A = Desconhecimento do conteúdo; B = Forma diferente de abordagem do conteúdo; C = Espaço insuficiente para responder às questões; D = Falta de motivação para fazer a prova; E = Não tive qualquer tipo de dificuldade para responder à prova; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i8` | `CO_RS_I8` | texto | 8 - Considerando apenas as questões objetivas da prova, você percebeu que: (A = Não estudou ainda a maioria desses conteúdos; B = Estudou alguns desses conteúdos, mas não os aprendeu; C = Estudou a maioria desses conteúdos, mas não os aprendeu; D = Estudou e aprendeu muitos desses conteúdos; E = Estudou e aprendeu todos esses conteúdos; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `co_rs_i9` | `CO_RS_I9` | texto | 9 - Qual foi o tempo gasto por você para concluir a prova? (A = Menos de uma hora; B = Entre uma e duas horas; C = Entre duas e três horas; D = Entre três e quatro horas; E = Quatro horas e não consegui terminar; * = Resposta anulada; . = Sem resposta; Valor em branco= Resposta não válida) | — | todo | `microdados_arq3` |
| `qe_i22` | `QE_I22` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Excetuando-se os livros indicados na bibliografia do seu curso, quantos livros você leu neste ano? Em 2010: As condições gerais das instalações físicas de salas de aula, bibliotecas e ambientes de trabalho e estudo para o funcionamento do curso são adequadas? (Se for estudante… | — | todo | `microdados_arq28`, `microdados_arq4` |
| `qe_i23` | `QE_I23` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula? Em 2010: As salas de aula são adequadas à quantidade de estudantes? (Se for estudante de EAD - Educação a distância, considere as condições do polo de apoio presencial e/ou sede). | — | todo | `microdados_arq29`, `microdados_arq4` |
| `qe_i24` | `QE_I24` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Você teve oportunidade de aprendizado de idioma estrangeiro na Instituição? Em 2010: As instalações de laboratórios, os equipamentos, os materiais e os serviços de apoio específicos do curso são adequados? (Se for estudante de EAD - Educação a distância… | — | todo | `microdados_arq30`, `microdados_arq4` |
| `qe_i25` | `QE_I25` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual o principal motivo para você ter escolhido este curso? Em 2010: Os ambientes para aulas práticas específicas do curso são adequados à quantidade de estudantes? (Se for estudante de EAD - Educação a distância, considere as condições… | — | todo | `microdados_arq31`, `microdados_arq4` |
| `qe_i26` | `QE_I26` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual a principal razão para você ter escolhido a sua instituição de educação superior? Em 2010: Os equipamentos e/ou materiais disponíveis nos ambientes para aulas práticas são suficientes para o número de estudantes? (Se for estudante de EAD - Educação a… | — | todo | `microdados_arq32`, `microdados_arq4` |
| `qe_i27` | `QE_I27` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As disciplinas cursadas contribuíram para sua formação integral, como cidadão e profissional. Em 2010: Como a sua instituição viabiliza o acesso dos estudantes de graduação à Internet para atender às necessidades do curso? | — | todo | `microdados_arq4` |
| `qe_i28` | `QE_I28` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os conteúdos abordados nas disciplinas do curso favoreceram sua atuação em estágios ou em atividades de iniciação profissional. Em 2010: Como você caracteriza o uso de recursos audiovisuais e tecnológicos no seu curso? | — | todo | `microdados_arq4` |
| `qe_i29` | `QE_I29` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As metodologias de ensino utilizadas no curso desafiaram você a aprofundar conhecimentos e desenvolver competências reflexivas e críticas. Em 2010: Com que frequência você normalmente utiliza a biblioteca de sua instituição? (Se for estudante de EAD – Educação a distância, considere as condições do polo de apoio… | — | todo | `microdados_arq4` |
| `qe_i30` | `QE_I30` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso propiciou experiências de aprendizagem inovadoras. Em 2010: Dentre as vezes em que precisou utilizar o acervo da biblioteca, você conseguiu? (Se for estudante de EAD – Educação a distância, considere as condições do polo de apoio… | — | todo | `microdados_arq4` |
| `qe_i31` | `QE_I31` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso contribuiu para o desenvolvimento da sua consciência ética para o exercício profissional. Em 2010: Como você avalia o acervo da biblioteca, quanto à atualização, em face das necessidades curriculares do seu curso? | — | todo | `microdados_arq4` |
| `qe_i32` | `QE_I32` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: No curso você teve oportunidade de aprender a trabalhar em equipe. Em 2010: Como você avalia o acervo de periódicos científicos/acadêmicos disponíveis na biblioteca quanto à atualização? | — | todo | `microdados_arq4` |
| `qe_i33` | `QE_I33` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso possibilitou aumentar sua capacidade de reflexão e argumentação. Em 2010: O horário de funcionamento da biblioteca atende às suas necessidades? (Se for estudante de EAD – Educação a distância, considere as condições do polo de apoio presencial… | — | todo | `microdados_arq4` |
| `qe_i34` | `QE_I34` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso promoveu o desenvolvimento da sua capacidade de pensar criticamente, analisar e refletir sobre soluções para problemas da sociedade. Em 2010: Na maioria das vezes, os planos de ensino apresentados pelos professores contêm os seguintes aspectos: objetivos, metodologias de ensino e critérios de avaliação… | — | todo | `microdados_arq4` |
| `qe_i35` | `QE_I35` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso contribuiu para você ampliar sua capacidade de comunicação nas formas oral e escrita. Em 2010: Os conteúdos trabalhados pela maioria dos professores são coerentes com os que foram apresentados nos respectivos planos de ensino? | — | todo | `microdados_arq4` |
| `qe_i36` | `QE_I36` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso contribuiu para o desenvolvimento da sua capacidade de aprender e atualizar-se permanentemente. Em 2010: Os professores solicitam em suas disciplinas a realização de atividades de pesquisa? | — | todo | `microdados_arq4` |
| `qe_i37` | `QE_I37` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As relações professor-aluno ao longo do curso estimularam você a estudar e aprender. Em 2010: Os professores indicam como material de estudo a utilização de livros-texto ? | — | todo | `microdados_arq4` |
| `qe_i38` | `QE_I38` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os planos de ensino apresentados pelos professores contribuíram para o desenvolvimento das atividades acadêmicas e para seus estudos. Em 2010: Os professores indicam como material de estudo a utilização de artigos de periódicos especializados (artigos científicos)? | — | todo | `microdados_arq4` |
| `qe_i39` | `QE_I39` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As referências bibliográficas indicadas pelos professores nos planos de ensino contribuíram para seus estudos e aprendizagens. Em 2010: Os professores indicam a utilização em suas disciplinas materiais elaborados por eles? | — | todo | `microdados_arq4` |
| `qe_i40` | `QE_I40` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Foram oferecidas oportunidades para os estudantes superarem dificuldades relacionadas ao processo de formação. Em 2010: As disciplinas do curso exigem domínio de língua estrangeira? | — | todo | `microdados_arq4` |
| `qe_i41` | `QE_I41` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A coordenação do curso esteve disponível para orientação acadêmica dos estudantes. Em 2010: Os professores têm disponibilidade para atendimento fora do período de aula? | — | todo | `microdados_arq4` |
| `qe_i42` | `QE_I42` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso exigiu de você organização e dedicação frequente aos estudos. Em 2010: Os professores demonstram domínio do conteúdo das disciplinas? | — | todo | `microdados_arq4` |
| `qe_i43` | `QE_I43` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Foram oferecidas oportunidades para os estudantes participarem de programas, projetos ou atividades de extensão universitária. Em 2010: O curso contextualiza o conhecimento da área (teorias, procedimentos, técnicas, instrumentos, etc.) com os temas gerais e situações do cotidiano da realidade brasileira? | — | todo | `microdados_arq4` |
| `qe_i44` | `QE_I44` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Foram oferecidas oportunidades para os estudantes participarem de projetos de iniciação científica e de atividades que estimularam a investigação acadêmica. Em 2010: Como você avalia o currículo do seu curso em relação à integração entre os conteúdos das diferentes disciplinas? | — | todo | `microdados_arq4` |
| `qe_i45` | `QE_I45` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso ofereceu condições para os estudantes participarem de eventos internos e/ou externos à instituição. Em 2010: Seu curso oferece atividades complementares? | — | todo | `microdados_arq4` |
| `qe_i46` | `QE_I46` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A instituição ofereceu oportunidades para os estudantes atuarem como representantes em órgãos colegiados. Em 2010: Você participou de programas de iniciação científica? Como foi a contribuição para a sua formação? | — | todo | `microdados_arq4` |
| `qe_i47` | `QE_I47` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso favoreceu a articulação do conhecimento teórico com atividades práticas. Em 2010: Você participou de programas de monitoria? Como foi a contribuição para a sua formação? | — | todo | `microdados_arq4` |
| `qe_i48` | `QE_I48` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As atividades práticas foram suficientes para relacionar os conteúdos do curso com a prática, contribuindo para sua formação profissional. Em 2010: Você participou de programas de extensão? Como foi a contribuição para a sua formação? | — | todo | `microdados_arq4` |
| `qe_i49` | `QE_I49` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso propiciou acesso a conhecimentos atualizados e/ou contemporâneos em sua área de formação. Em 2010: Sua IES apoia financeiramente a participação dos estudantes em eventos (congressos, encontros, seminários, visitas técnicas etc.)? | — | todo | `microdados_arq4` |
| `qe_i50` | `QE_I50` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O estágio supervisionado proporcionou experiências diversificadas para a sua formação. Em 2010: Como você avalia o nível de exigência do curso? | — | todo | `microdados_arq4` |
| `qe_i51` | `QE_I51` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As atividades realizadas durante seu trabalho de conclusão de curso contribuíram para qualificar sua formação profissional. Em 2010: Você considera que seu curso contribui para a aquisição de cultura geral? | — | todo | `microdados_arq4` |
| `qe_i52` | `QE_I52` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Foram oferecidas oportunidades para os estudantes realizarem intercâmbios e/ou estágios no país. Em 2010: Você considera que seu curso contribui para a aquisição de formação teórica na área? | — | todo | `microdados_arq4` |
| `qe_i53` | `QE_I53` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Foram oferecidas oportunidades para os estudantes realizarem intercâmbios e/ou estágios fora do país. Em 2010: Você considera que seu curso contribui na preparação para o exercício profissional? | — | todo | `microdados_arq4` |
| `qe_i54` | `QE_I54` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os estudantes participaram de avaliações periódicas do curso (disciplinas, atuação dos professores, infraestrutura). Em 2010: Como você avalia a contribuição do curso para a sua formação? | — | todo | `microdados_arq4` |
| `tp_sexo` | `TP_SEXO` | texto | Sexo (M = Masculino; F = Feminino; 9 = Indefinido) Códigos da edição 2023; podem mudar em edições anteriores. | — | todo | `microdados_arq5` |
| `nu_idade` | `NU_IDADE` | texto | Idade do inscrito no dia da prova | — | todo | `microdados_arq6` |
| `qe_i01` | `QE_I01` | texto | Item do questionário; as alternativas de resposta mudam entre as edições (aqui, 2023): Qual o seu estado civil? (A = Solteiro(a); B = Casado(a); C = Separado(a) judicialmente/divorciado(a); D = Viúvo(a); E = Outro) | — | todo | `microdados_arq7` |
| `qe_i02` | `QE_I02` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual é a sua cor ou raça? Em 2010: Como você se considera [raça/cor]? | — | todo | `microdados_arq8` |
| `qe_i03` | `QE_I03` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Qual a sua nacionalidade? Em 2010: Onde e com quem você mora atualmente? | — | todo | `microdados_arq9` |
| `nt_fg_d1_pt` | `NT_FG_D1_PT` | texto | Nota de Língua Portuguesa da questão 1 da parte discursiva da formação geral. (valor de 0 a 100) | — | 2013 a 2023 | `microdados_arq3` |
| `nt_fg_d1_ct` | `NT_FG_D1_CT` | texto | Nota de Conteúdo da questão 1 da parte discursiva da formação geral. (valor de 0 a 100) | — | 2013 a 2023 | `microdados_arq3` |
| `nt_fg_d2_pt` | `NT_FG_D2_PT` | texto | Nota de Língua Portuguesa da questão 2 da parte discursiva da formação geral. (valor de 0 a 100) | — | 2013 a 2022 | `microdados_arq3` |
| `nt_fg_d2_ct` | `NT_FG_D2_CT` | texto | Nota de Conteúdo da questão 2 da parte discursiva da formação geral. (valor de 0 a 100) | — | 2013 a 2022 | `microdados_arq3` |
| `qe_i55` | `QE_I55` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As avaliações de aprendizagem realizadas durante o curso foram compatíveis com os conteúdos ou temas trabalhados pelos professores. Em 2013: Os professores apresentaram disponibilidade para atender os estudantes. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i56` | `QE_I56` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os professores apresentaram disponibilidade para atender os estudantes fora do horário das aulas. Em 2013: Os professores demonstraram domínio do conteúdo das disciplinas que ministraram. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i57` | `QE_I57` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os professores demonstraram domínio dos conteúdos abordados nas disciplinas. Em 2013: Os professores utilizaram tecnologias de informação e comunicação (TICs) no processo de ensino‐aprendizagem. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i58` | `QE_I58` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os professores utilizaram tecnologias da informação e comunicação (TIC's) como estratégia de ensino (projetor, multimídia, laboratório de informática, ambiente virtual… Em 2013: A instituição dispôs de quantidade suficiente de funcionários para o apoio administrativo e acadêmico. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i59` | `QE_I59` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A instituição dispôs de quantidade suficiente de funcionários para o apoio administrativo e acadêmico. Em 2013: O curso disponibilizou monitores ou tutores para auxiliar os estudantes. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i60` | `QE_I60` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: O curso disponibilizou monitores ou tutores para auxiliar os estudantes. Em 2013: As condições de infraestrutura das salas de aula foram adequadas. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i61` | `QE_I61` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As condições de infraestrutura das salas de aula foram adequadas. Em 2013: Os equipamentos e materiais disponíveis para as aulas práticas foram adequados para a quantidade de estudantes. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i62` | `QE_I62` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os equipamentos e materiais disponíveis para as aulas práticas foram adequados para a quantidade de estudantes. Em 2013: Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i63` | `QE_I63` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso. Em 2013: A biblioteca dispôs das referências bibliográficas que os estudantes necessitaram. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i64` | `QE_I64` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A biblioteca dispôs das referências bibliográficas que os estudantes necessitaram. Em 2013: A instituição contou com biblioteca virtual ou conferiu acesso a obras disponíveis em acervos virtuais. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i65` | `QE_I65` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A instituição contou com biblioteca virtual ou conferiu acesso a obras disponíveis em acervos virtuais. Em 2013: O ambiente acadêmico favoreceu a reflexão e convivência social de forma a promover um clima de respeito à diversidade. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i66` | `QE_I66` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: As atividades acadêmicas desenvolvidas dentro e fora da sala de aula possibilitaram reflexão, convivência e respeito à diversidade. Em 2013: A instituição contou com espaços de cultura, de lazer, de convívio e interação social. | — | 2013 a 2023 | `microdados_arq4` |
| `qe_i67` | `QE_I67` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2023: A instituição promoveu atividades de cultura, de lazer e de interação social. Em 2013: A instituição dispôs de refeitório, cantina e banheiros em condições adequadas que atenderam as necessidades dos seus usuários. | — | 2013 a 2023 | `microdados_arq4` |
| `nu_item_ofg_z` | `NU_ITEM_OFG_Z` | texto | Número de itens da parte objetiva da Formação Geral que foram excluídos devido a anulação | — | 2014 a 2023 | `microdados_arq3` |
| `nu_item_ofg_x` | `NU_ITEM_OFG_X` | texto | Número de itens da parte objetiva da Formação Geral que foram excluídos devido ao coeficiente ponto-bisserial menor que 0,20 | — | 2014 a 2023 | `microdados_arq3` |
| `nu_item_ofg_n` | `NU_ITEM_OFG_N` | texto | Número de itens da parte objetiva da Formação Geral que não se aplicam ao grupo de curso | — | 2014 a 2023 | `microdados_arq3` |
| `nu_item_oce_z` | `NU_ITEM_OCE_Z` | texto | Número de itens da parte objetiva de Componente Específico que foram excluídos devido a anulação | — | 2014 a 2023 | `microdados_arq3` |
| `nu_item_oce_x` | `NU_ITEM_OCE_X` | texto | Número de itens da parte objetiva de Componente Específico que foram excluídos devido ao coeficiente ponto-bisserial menor que 0,20 | — | 2014 a 2023 | `microdados_arq3` |
| `nu_item_oce_n` | `NU_ITEM_OCE_N` | texto | Número de itens da parte objetiva de Componente Específico que não se aplicam ao grupo de curso | — | 2014 a 2023 | `microdados_arq3` |
| `qe_i69` | `QE_I69` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: Com o início da pandemia sua instituição passou rapidamente a ofertar aulas não presenciais. Em 2014: Você pretende exercer o magistério após o término do curso? | — | 2014 a 2022 | `microdados_arq33` |
| `qe_i70` | `QE_I70` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: Sua instituição ofereceu suporte para os estudantes superarem dificuldades tecnológicas de acesso às atividades não presenciais. Em 2014: Qual a principal razão para você ter escolhido a Licenciatura? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq34` |
| `qe_i71` | `QE_I71` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: As referências bibliográficas (livros, artigos, textos) necessárias às aulas continuaram acessíveis após o início da pandemia. Em 2014: Você já tem experiência profissional no magistério, qual a forma de contrato? Assinale a alternativa mais relevante para você. | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq35` |
| `qe_i72` | `QE_I72` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: As atividades de pesquisa e/ou extensão que você participava antes do início da pandemia continuaram sendo ofertadas. Em 2014: Se você tem experiência no magistério, em qual etapa/modalidade atuou? Assinale a alternativa mais relevante para você. | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq36` |
| `qe_i73` | `QE_I73` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: As atividades de estágio supervisionado puderam ser realizadas ao longo da pandemia Em 2014: Em que instituição você realizou seu estágio curricular obrigatório? Assinale a alternativa mais relevante para você. | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq37` |
| `qe_i74` | `QE_I74` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: Os professores demonstraram domínio dos recursos tecnológicos que passaram a ser utilizados nas aulas não presenciais. Em 2014: Em qual turno você realizou o estágio curricular obrigatório? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq38` |
| `qe_i75` | `QE_I75` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: A didática dos seus professores foi adequada para as aulas não presenciais. Em 2014: Em qual etapa/modalidade de ensino você realizou seu estágio curricular obrigatório? Assinale a alternativa mais relevante para você. | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq39` |
| `qe_i68` | `QE_I68` | texto | Item do questionário; as alternativas de resposta mudam entre as edições (aqui, 2023): A instituição dispôs de refeitório, cantina e banheiros em condições adequadas que atenderam as necessidades dos seus usuários. (1 = Discordo totalmente) | — | 2014 a 2023 | `microdados_arq4` |
| `qe_i76` | `QE_I76` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: Os recursos tecnológicos e o acesso à internet que você possuía no início da pandemia eram adequados para acompanhar as aulas não presenciais. Em 2014: Quantas horas de estágio curricular obrigatório você integralizou? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq40` |
| `qe_i77` | `QE_I77` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: Durante a pandemia, você desenvolveu a capacidade de aprender por meio do ensino não presencial. Em 2014: Onde você pretende atuar daqui a cinco anos? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq41` |
| `qe_i78` | `QE_I78` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: A implementação de aulas não presenciais e uso de tecnologias digitais decorrentes da pandemia prejudicaram seu processo formativo. Em 2014: A fundamentação teórica oferecida no curso de Licenciatura foi suficiente para sua compreensão sobre a educação escolar e sua preparação para o exercício da docência? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq42` |
| `qe_i79` | `QE_I79` | texto | Item do questionário cujo enunciado muda entre as edições. Em 2022: As dificuldades geradas pela pandemia para a continuidade dos estudos levaram você a pensar em trancar ou desistir do curso. Em 2014: Você vivenciou, durante o curso de graduação, experiências pedagógicas que gostaria de proporcionar aos seus futuros alunos? | — | 2014 a 2022 | `microdados_arq33`, `microdados_arq42` |
| `qe_i80` | `QE_I80` | texto | No decorrer do estágio curricular obrigatório, você teve suficiente orientação e supervisão de professores do seu curso? (A = Sim, durante todo o tempo; B = Sim, em grande parte do tempo; C = Apenas em algumas disciplinas/situações; D = Não) | — | 2014 a 2021 | `microdados_arq42` |
| `qe_i81` | `QE_I81` | texto | No decorrer do estágio curricular obrigatório, você teve adequado acompanhamento de um ou mais professores da instituição em que estagiou? (A = Sim, durante todo o tempo; B = Sim, em grande parte do tempo; C = Apenas em algumas disciplinas/situações; D = Não) | — | 2014 a 2021 | `microdados_arq42` |
| `co_turno_graduacao` | `CO_TURNO_GRADUACAO` | texto | Código do turno de graduação cursado pelo estudante (1 = Matutino; 2 = Vespertino; 3 = Integral; 4 = Noturno) | — | 2017 a 2023 | `microdados_arq2` |
| `qe_i82` | `QE_I82` | texto | Com o início da pandemia sua instituição passou rapidamente a ofertar aulas não presenciais. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i83` | `QE_I83` | texto | Sua instituição ofereceu suporte para os estudantes superarem dificuldades tecnológicas de acesso às atividades não presenciais. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i84` | `QE_I84` | texto | As referências bibliográficas (livros, artigos, textos) necessárias às aulas continuaram acessíveis após o início da pandemia. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i85` | `QE_I85` | texto | As atividades de pesquisa e/ou extensão que você participava antes do início da pandemia continuaram sendo ofertadas. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i86` | `QE_I86` | texto | As atividades de estágio supervisionado puderam ser realizadas ao longo da pandemia (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i87` | `QE_I87` | texto | Os professores demonstraram domínio dos recursos tecnológicos que passaram a ser utilizados nas aulas não presenciais. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i88` | `QE_I88` | texto | A didática dos seus professores foi adequada para as aulas não presenciais. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i89` | `QE_I89` | texto | Os recursos tecnológicos e o acesso à internet que você possuía no início da pandemia eram adequados para acompanhar as aulas não presenciais. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i90` | `QE_I90` | texto | Durante a pandemia, você desenvolveu a capacidade de aprender por meio do ensino não presencial. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i91` | `QE_I91` | texto | A implementação de aulas não presenciais e uso de tecnologias digitais decorrentes da pandemia prejudicaram seu processo formativo. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |
| `qe_i92` | `QE_I92` | texto | As dificuldades geradas pela pandemia para a continuidade dos estudos levaram você a pensar em trancar ou desistir do curso. (1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não se aplica; 8 = Não sei responder) | — | 2021 | `microdados_arq43` |

## No lake

- Dataset `inep/enade`, particionado por `ano`; um Parquet por `.txt` de `DADOS`, no padrão `enade-microdados_<ano>__microdados<ano>_arq<N>.parquet`. Não há arquivo único por edição, e os `arqN` não são intercambiáveis entre edições: consulte a tabela de conteúdo.
- Todas as colunas são texto: o DuckDB lê o arquivo sem inferir tipos, e os nomes saem normalizados (minúsculas).
- A coluna `ano` é a edição, tirada do nome do arquivo; `nu_ano` (do dicionário) é o ano dentro do dado.
- Campos em branco no `.txt` ficam vazios no Parquet. Onde o manual define o ponto como valor faltante, ele chega como texto (`.`), por exemplo em `co_rs_i1` e, por item, nos vetores `ds_vt_esc_ofg` (`........`).

## Cuidados de uso

- **Os arquivos só se juntam pelo curso, nunca pelo estudante.** O Manual (seção 2) diz que cada arquivo está ordenado por variáveis distintas e que a primeira linha de um arquivo não é o mesmo indivíduo da primeira linha de outro. Não use posição de linha nem `nu_ano` para casar `arq3` (nota) com `arq5` (sexo) ou `arq8` (cor ou raça). Só se pode agregar por `co_curso` (e `nu_ano`) e cruzar os agregados.
- **`co_curso` repete-se em todas as linhas de um curso.** Em `arq1` há uma linha por estudante com a caracterização do curso repetida; use `DISTINCT` antes de juntar com outro arquivo para não multiplicar linhas.
- **O mesmo nome de coluna muda de pergunta entre edições** (exemplos na seção Variáveis). Casar `qe_iNN` entre anos só vale depois de comparar os enunciados dos dicionários.
- **A numeração dos arquivos também muda.** No questionário geral a pergunta QE`n` está em `arq<6+n>` em todas as edições, mas o número de perguntas varia (21, 25 ou 26) e os arquivos extras de licenciatura e pandemia aparecem só em algumas, com números de arquivo diferentes.
- **A estrutura de colunas dos arquivos de prova e de turno muda.** `arq2` tem 7 colunas até 2016 (turnos em indicadores) e 5 desde 2017; `arq3` tem 42 colunas em 2010 a 2012, 46 em 2013, 52 de 2014 a 2022 e 44 em 2023.
- **Valores de `tp_pres` e de situação das questões mudam.** Os históricos dos manuais de 2017 e 2019 registram a criação do código 334 (eliminado por participação indevida) nos campos de situação da prova e a padronização, em 2022, das descrições dos tipos de presença; os códigos disponíveis variam por edição. Nas notas e vetores, filtre por `tp_pres = '555'` (presente com resultado válido) antes de calcular médias.
- **Exclusões.** Cursos com apenas um estudante com resultado válido e questionários de cursos com apenas um respondente foram retirados dos microdados (Manual 2021 e 2023); os números por curso podem ser menores que os da divulgação oficial. Inscrições indevidas atestadas pelas IES também ficam fora.
- **Formato numérico.** A nota usa ponto decimal (`10.7`), embora o dicionário de 2010 a 2012 mostre a faixa com vírgula. `nt_*` vai de 0 a 100 no dicionário; vetores como `ds_vt_ace_ofg` são texto e podem começar com dígitos, não os converta.
- **Anonimização.** Não há código nem nome do estudante. Mesmo assim sexo, idade, cor ou raça e renda aparecem em arquivos por estudante; use só agregados e respeite a regra de cursos com poucos respondentes.
- **O pacote de 2022 é RAR.** É o único do catálogo; o conversor o lê, mas sem manual do usuário na pasta `LEIA-ME`.
- **Edições de 2004 a 2009 ficam de fora.** A página oficial as lista, mas o fetcher não as coleta; o Manual diz que o exame é censitário desde 2010 e que só concluintes fazem a prova desde 2011, de modo que a edição de 2010 já é anterior a essa regra e as séries não são comparáveis sem cuidado.

## Exemplos

Número de estudantes e média da nota geral por tipo de presença na edição 2019 (`arq3`; colunas em texto, nota convertida para número):

```python
import duckdb

duckdb.sql("""
    SELECT tp_pres, count(*) AS estudantes,
           round(avg(try_cast(nt_ger AS DOUBLE)), 1) AS media_nt_ger
    FROM read_parquet('lake/inep/enade/ano=2019/*arq3.parquet')
    GROUP BY ALL
    ORDER BY tp_pres
""").show()
```

Nota média por categoria administrativa da IES juntando por curso (agrega `arq3` por `co_curso` e junta com a caracterização do curso de `arq1`):

```python
import duckdb

duckdb.sql("""
    WITH nota AS (
        SELECT co_curso, avg(try_cast(nt_ger AS DOUBLE)) AS media_nt_ger
        FROM read_parquet('lake/inep/enade/ano=2019/*arq3.parquet')
        WHERE tp_pres = '555'
        GROUP BY co_curso
    ), curso AS (
        SELECT DISTINCT co_curso, co_categad
        FROM read_parquet('lake/inep/enade/ano=2019/*arq1.parquet')
    )
    SELECT c.co_categad, count(*) AS cursos, round(avg(n.media_nt_ger), 1) AS media
    FROM nota n JOIN curso c USING (co_curso)
    GROUP BY ALL
    ORDER BY 1
""").show()
```

## Referências

- Microdados do Enade: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade
- Manual do usuário, questionário do estudante e dicionário de arquivos e de variáveis, dentro de cada pacote em https://download.inep.gov.br/microdados/
