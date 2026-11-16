---
dataset:
  id: ana
  fonte: inep
  titulo: ANA — Avaliação Nacional da Alfabetização
  resumo: 'Microdados da Avaliação Nacional da Alfabetização (ANA) de 2014 e 2016: proficiência e respostas dos alunos do 3º ano do ensino fundamental, resultados por escola e parâmetros dos itens.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/ana
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'sem periodicidade regular: duas edições com microdados (2014 e 2016)'
  cobertura:
    inicio: '2014'
    fim: '2016'
  unidade: um aluno do 3º ano do ensino fundamental (arquivo `ts_aluno`); uma escola (arquivo `ts_escola`); um item de prova com seus parâmetros (arquivo `ts_item`)
  granularidade:
    espacial: aluno e escola, com região, UF e área (capital ou interior); os códigos de escola e de município são máscaras (códigos fictícios iniciados em 6)
    temporal: ano da edição
  formato_bruto: ZIP por edição com as pastas DADOS (três CSV com ponto e vírgula), DICIONÁRIO (xlsx e ods), INPUTS (SAS, SPSS e R), LEIA-ME e PLANILHAS DE RESULTADOS; o ZIP de 2014 traz também relatórios técnicos em PDF
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 136
  unidades_de_medida:
    proficiencia_lpo_ana: pontos na escala única da ANA (média 500 e desvio 100)
    desvio_padrao_lpo_ana: pontos na escala única da ANA (média 500 e desvio 100)
    proficiencia_lpd_ana: pontos na escala única da ANA (média 500 e desvio 100)
    desvio_padrao_lpd_ana: pontos na escala única da ANA (média 500 e desvio 100)
    proficiencia_mt_ana: pontos na escala única da ANA (média 500 e desvio 100)
    desvio_padrao_mt_ana: pontos na escala única da ANA (média 500 e desvio 100)
    erro_padrao_lpo_ana: pontos na escala única da ANA (média 500 e desvio 100)
    erro_padrao_lpd_ana: pontos na escala única da ANA (média 500 e desvio 100)
    erro_padrao_mt_ana: pontos na escala única da ANA (média 500 e desvio 100)
    proficiencia_lpo: escala única da ANA com média 0 e desvio 1 na população de referência
    desvio_padrao_lpo: escala única da ANA com média 0 e desvio 1 na população de referência
    proficiencia_lpd: escala única da ANA com média 0 e desvio 1 na população de referência
    desvio_padrao_lpd: escala única da ANA com média 0 e desvio 1 na população de referência
    proficiencia_mt: escala única da ANA com média 0 e desvio 1 na população de referência
    desvio_padrao_mt: escala única da ANA com média 0 e desvio 1 na população de referência
    erro_padrao_lpo: escala única da ANA com média 0 e desvio 1 na população de referência
    erro_padrao_lpd: escala única da ANA com média 0 e desvio 1 na população de referência
    erro_padrao_mt: escala única da ANA com média 0 e desvio 1 na população de referência
    media_lpo: pontos na escala da ANA
    media_lpd: pontos na escala da ANA
    media_mt: pontos na escala da ANA
    pc_formacao_docente: percentual
    taxa_participacao_lp: percentual
    nivel_1_lpo: percentual
    nivel_2_lpo: percentual
    nivel_3_lpo: percentual
    nivel_4_lpo: percentual
    esc_sim_n1_lpo: percentual
    esc_sim_n2_lpo: percentual
    esc_sim_n3_lpo: percentual
    esc_sim_n4_lpo: percentual
    nivel_1_lpd: percentual
    nivel_2_lpd: percentual
    nivel_3_lpd: percentual
    nivel_4_lpd: percentual
    nivel_5_lpd: percentual
    esc_sim_n1_lpd: percentual
    esc_sim_n2_lpd: percentual
    esc_sim_n3_lpd: percentual
    esc_sim_n4_lpd: percentual
    esc_sim_n5_lpd: percentual
    taxa_participacao_mt: percentual
    nivel_1_mt: percentual
    nivel_2_mt: percentual
    nivel_3_mt: percentual
    nivel_4_mt: percentual
    esc_sim_n1_mt: percentual
    esc_sim_n2_mt: percentual
    esc_sim_n3_mt: percentual
    esc_sim_n4_mt: percentual
    nu_matriculados_censo: alunos
    nu_presentes_lp: alunos
    nu_validos_lp: alunos
    nu_presentes_mt: alunos
    nu_validos_mt: alunos
    a: 'parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso)'
    b: 'parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso)'
    c: 'parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso)'
  dados_pessoais:
  - coluna: id_aluno
    categoria: código do aluno na ANA (identificador de estudante; sem nome ou CPF)
  - coluna: in_sala_separada_lp
    categoria: atendimento em sala exclusiva para aluno com necessidade especial
  - coluna: in_sala_separada_mt
    categoria: atendimento em sala exclusiva para aluno com necessidade especial
  - coluna: in_rec_esc1
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc2
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc3
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc5
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc6
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc12
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc13
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc14
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc15
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc16
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc17
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc18
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc19
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_esc20
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep1
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep2
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep3
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep4
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep5
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep6
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep7
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep8
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep9
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep10
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: in_rec_inep11
    categoria: recursos de acessibilidade solicitados (indicam necessidade especial do aluno)
  - coluna: tx_resposta_lp
    categoria: desempenho individual do aluno
  - coluna: tx_resposta_mt
    categoria: desempenho individual do aluno
  - coluna: conceito_q1
    categoria: desempenho individual do aluno
  - coluna: conceito_q2
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_ortografia
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_coesao
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_segmentacao
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_pontuacao
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_progressao_tematica
    categoria: desempenho individual do aluno
  - coluna: conceito_q3_elementos_narrativa
    categoria: desempenho individual do aluno
  - coluna: nivel_lpo
    categoria: desempenho individual do aluno
  - coluna: proficiencia_lpo
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_lpo
    categoria: desempenho individual do aluno
  - coluna: proficiencia_lpo_ana
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_lpo_ana
    categoria: desempenho individual do aluno
  - coluna: nivel_lpd
    categoria: desempenho individual do aluno
  - coluna: proficiencia_lpd
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_lpd
    categoria: desempenho individual do aluno
  - coluna: proficiencia_lpd_ana
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_lpd_ana
    categoria: desempenho individual do aluno
  - coluna: nivel_mt
    categoria: desempenho individual do aluno
  - coluna: proficiencia_mt
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_mt
    categoria: desempenho individual do aluno
  - coluna: proficiencia_mt_ana
    categoria: desempenho individual do aluno
  - coluna: desvio_padrao_mt_ana
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_lpo
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_lpo_ana
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_lpd
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_lpd_ana
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_mt
    categoria: desempenho individual do aluno
  - coluna: erro_padrao_mt_ana
    categoria: desempenho individual do aluno
  eras:
  - desde: '2016'
    mudanca: TS_ALUNO separa leitura e escrita de língua portuguesa (cadernos e pesos próprios) e traz situação de presença, sala separada e recursos de acessibilidade; "desvio padrão" da proficiência passa a "erro padrão"; os códigos de CO_QUESITO mudam (9 a 14 em 2014; 16 a 21 em 2016); TS_ITEM ganha IN_ITEM_ADAPTADO e TP_ADAPTACAO
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# ANA — Avaliação Nacional da Alfabetização

## Resumo

Microdados da Avaliação Nacional da Alfabetização (ANA), aplicada pelo Inep ao final do ciclo de alfabetização (3º ano do ensino fundamental) das escolas públicas com ao menos 10 estudantes matriculados. A ANA mede leitura e escrita em língua portuguesa e matemática. Cada edição traz três arquivos: alunos (respostas, conceitos de escrita e proficiência), escolas (médias, distribuição por nível de proficiência e indicadores contextuais) e itens (gabarito, descritor e parâmetros da Teoria de Resposta ao Item). O lake cobre as duas edições com microdados publicadas (2014 e 2016); o piloto de 2013 não tem microdados na página oficial.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/ana` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/ana |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | sem periodicidade regular: duas edições com microdados (2014 e 2016) |
| Cobertura | 2014 a 2016 |
| Unidade (uma linha) | um aluno do 3º ano do ensino fundamental (arquivo `ts_aluno`); uma escola (arquivo `ts_escola`); um item de prova com seus parâmetros (arquivo `ts_item`) |
| Granularidade | espacial: aluno e escola, com região, UF e área (capital ou interior); os códigos de escola e de município são máscaras (códigos fictícios iniciados em 6); temporal: ano da edição |
| Formato bruto | ZIP por edição com as pastas DADOS (três CSV com ponto e vírgula), DICIONÁRIO (xlsx e ods), INPUTS (SAS, SPSS e R), LEIA-ME e PLANILHAS DE RESULTADOS; o ZIP de 2014 traz também relatórios técnicos em PDF |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 136 |
| Unidades de medida | `proficiencia_lpo_ana`: pontos na escala única da ANA (média 500 e desvio 100); `desvio_padrao_lpo_ana`: pontos na escala única da ANA (média 500 e desvio 100); `proficiencia_lpd_ana`: pontos na escala única da ANA (média 500 e desvio 100); `desvio_padrao_lpd_ana`: pontos na escala única da ANA (média 500 e desvio 100); `proficiencia_mt_ana`: pontos na escala única da ANA (média 500 e desvio 100); `desvio_padrao_mt_ana`: pontos na escala única da ANA (média 500 e desvio 100); `erro_padrao_lpo_ana`: pontos na escala única da ANA (média 500 e desvio 100); `erro_padrao_lpd_ana`: pontos na escala única da ANA (média 500 e desvio 100); `erro_padrao_mt_ana`: pontos na escala única da ANA (média 500 e desvio 100); `proficiencia_lpo`: escala única da ANA com média 0 e desvio 1 na população de referência; `desvio_padrao_lpo`: escala única da ANA com média 0 e desvio 1 na população de referência; `proficiencia_lpd`: escala única da ANA com média 0 e desvio 1 na população de referência; `desvio_padrao_lpd`: escala única da ANA com média 0 e desvio 1 na população de referência; `proficiencia_mt`: escala única da ANA com média 0 e desvio 1 na população de referência; `desvio_padrao_mt`: escala única da ANA com média 0 e desvio 1 na população de referência; `erro_padrao_lpo`: escala única da ANA com média 0 e desvio 1 na população de referência; `erro_padrao_lpd`: escala única da ANA com média 0 e desvio 1 na população de referência; `erro_padrao_mt`: escala única da ANA com média 0 e desvio 1 na população de referência; `media_lpo`: pontos na escala da ANA; `media_lpd`: pontos na escala da ANA; `media_mt`: pontos na escala da ANA; `pc_formacao_docente`: percentual; `taxa_participacao_lp`: percentual; `nivel_1_lpo`: percentual; `nivel_2_lpo`: percentual; `nivel_3_lpo`: percentual; `nivel_4_lpo`: percentual; `esc_sim_n1_lpo`: percentual; `esc_sim_n2_lpo`: percentual; `esc_sim_n3_lpo`: percentual; `esc_sim_n4_lpo`: percentual; `nivel_1_lpd`: percentual; `nivel_2_lpd`: percentual; `nivel_3_lpd`: percentual; `nivel_4_lpd`: percentual; `nivel_5_lpd`: percentual; `esc_sim_n1_lpd`: percentual; `esc_sim_n2_lpd`: percentual; `esc_sim_n3_lpd`: percentual; `esc_sim_n4_lpd`: percentual; `esc_sim_n5_lpd`: percentual; `taxa_participacao_mt`: percentual; `nivel_1_mt`: percentual; `nivel_2_mt`: percentual; `nivel_3_mt`: percentual; `nivel_4_mt`: percentual; `esc_sim_n1_mt`: percentual; `esc_sim_n2_mt`: percentual; `esc_sim_n3_mt`: percentual; `esc_sim_n4_mt`: percentual; `nu_matriculados_censo`: alunos; `nu_presentes_lp`: alunos; `nu_validos_lp`: alunos; `nu_presentes_mt`: alunos; `nu_validos_mt`: alunos; `a`: parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso); `b`: parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso); `c`: parâmetro do item na Teoria de Resposta ao Item (a: discriminação, b: dificuldade, c: acerto ao acaso) |
| Dados pessoais | `id_aluno` (código do aluno na ANA (identificador de estudante; sem nome ou CPF)); `in_sala_separada_lp` (atendimento em sala exclusiva para aluno com necessidade especial); `in_sala_separada_mt` (atendimento em sala exclusiva para aluno com necessidade especial); `in_rec_esc1` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc2` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc3` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc5` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc6` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc12` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc13` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc14` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc15` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc16` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc17` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc18` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc19` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_esc20` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep1` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep2` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep3` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep4` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep5` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep6` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep7` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep8` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep9` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep10` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `in_rec_inep11` (recursos de acessibilidade solicitados (indicam necessidade especial do aluno)); `tx_resposta_lp` (desempenho individual do aluno); `tx_resposta_mt` (desempenho individual do aluno); `conceito_q1` (desempenho individual do aluno); `conceito_q2` (desempenho individual do aluno); `conceito_q3_ortografia` (desempenho individual do aluno); `conceito_q3_coesao` (desempenho individual do aluno); `conceito_q3_segmentacao` (desempenho individual do aluno); `conceito_q3_pontuacao` (desempenho individual do aluno); `conceito_q3_progressao_tematica` (desempenho individual do aluno); `conceito_q3_elementos_narrativa` (desempenho individual do aluno); `nivel_lpo` (desempenho individual do aluno); `proficiencia_lpo` (desempenho individual do aluno); `desvio_padrao_lpo` (desempenho individual do aluno); `proficiencia_lpo_ana` (desempenho individual do aluno); `desvio_padrao_lpo_ana` (desempenho individual do aluno); `nivel_lpd` (desempenho individual do aluno); `proficiencia_lpd` (desempenho individual do aluno); `desvio_padrao_lpd` (desempenho individual do aluno); `proficiencia_lpd_ana` (desempenho individual do aluno); `desvio_padrao_lpd_ana` (desempenho individual do aluno); `nivel_mt` (desempenho individual do aluno); `proficiencia_mt` (desempenho individual do aluno); `desvio_padrao_mt` (desempenho individual do aluno); `proficiencia_mt_ana` (desempenho individual do aluno); `desvio_padrao_mt_ana` (desempenho individual do aluno); `erro_padrao_lpo` (desempenho individual do aluno); `erro_padrao_lpo_ana` (desempenho individual do aluno); `erro_padrao_lpd` (desempenho individual do aluno); `erro_padrao_lpd_ana` (desempenho individual do aluno); `erro_padrao_mt` (desempenho individual do aluno); `erro_padrao_mt_ana` (desempenho individual do aluno) |
| Eras | 2016: TS_ALUNO separa leitura e escrita de língua portuguesa (cadernos e pesos próprios) e traz situação de presença, sala separada e recursos de acessibilidade; "desvio padrão" da proficiência passa a "erro padrão"; os códigos de CO_QUESITO mudam (9 a 14 em 2014; 16 a 21 em 2016); TS_ITEM ganha IN_ITEM_ADAPTADO e TP_ADAPTACAO |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_ana_<ano>.zip` para 2014 e 2016, as duas edições listadas na página oficial dos microdados da ANA (conferido em 2026-11-15).
- A ANA foi criada em 2013 como edição piloto e a segunda edição foi a de 2014 (Leia-me da edição 2014); não há microdados do piloto de 2013 na página oficial.
- Cada ZIP tem as pastas `DADOS`, `DICIONÁRIO`, `INPUTS`, `LEIA-ME` (em 2014, `LEIA-ME E DOCUMENTOS TÉCNICOS`) e `PLANILHAS DE RESULTADOS`. O conversor lê só os CSV de `DADOS`; as planilhas de resultados por município, UF, região e Brasil (xlsx e ods) não viram arquivos do lake.
- Tamanhos descompactados no índice dos ZIP: `TS_ALUNO.csv` com 639 MB em 2014 e 804 MB em 2016; `TS_ESCOLA.csv` com 10,5 MB e 10,3 MB; `TS_ITEM.csv` com 14,9 KB e 17,2 KB.
- Os Leia-me das duas edições levam a data de junho de 2023 e já descrevem o modelo de microdados da LGPD (ver Cuidados de uso).

## Conteúdo

- **`ts_aluno`:** uma linha por aluno do 3º ano. Traz localização e escola (com códigos mascarados), indicadores de presença e de preenchimento, caderno de prova, respostas aos testes objetivos (`tx_resposta_lp`, `tx_resposta_mt`), conceitos obtidos nas questões de escrita de palavras e de produção textual, pesos de expansão, nível e proficiência em leitura (`lpo`), escrita (`lpd`) e matemática (`mt`). Em 2014 a leitura e a escrita compartilham caderno e peso (`_lp`).
- **`ts_escola`:** uma linha por escola. Traz o nível socioeconômico, a adequação da formação docente, o número de matriculados no Censo Escolar, presentes e válidos, a taxa de participação, a média de cada área e o percentual de alunos em cada nível de proficiência, inclusive o do "Perfil de Escola Similar" (`esc_sim_*`).
- **`ts_item`:** uma linha por item e gabarito. Traz disciplina, bloco, posição, código do item, descritor, tipo, modelo de resposta ao item e os parâmetros `a`, `b` e `c`. Itens de escrita têm mais de uma linha por item, uma por categoria de resposta (por exemplo, gabaritos `B/A` e `A` com parâmetro `b` diferente).
- As notas das áreas têm duas escalas: a proficiência "bruta" (média 0 e desvio 1 na população de referência) e a transformada `_ana` (média 500 e desvio 100). Os níveis de proficiência de leitura e matemática vão de 1 a 4 e os de escrita, de 1 a 5.
- A ANA é censitária para o público-alvo: estudantes do 3º ano de escolas públicas com ao menos 10 matriculados (Censo Escolar até o fim de julho de cada edição).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2014 | `ts_aluno` (45); `ts_escola` (46); `ts_item` (14) |
| 2016 | `ts_aluno` (76); `ts_escola` (46); `ts_item` (16) |

## Variáveis

As descrições e os códigos vêm dos dicionários de variáveis (xlsx) de cada edição; vale a edição mais recente que traz a variável (2016). Todas as colunas do lake são texto, mesmo as numéricas; o tipo declarado nos dicionários é `Num` ou `Char`.
Os dicionários descrevem `ID_DEPENDENCIA_ADM` em `TS_ESCOLA` (2014 e 2016) e em `TS_ALUNO` (2014), mas os CSV trazem `IN_PUBLICA` (0 = privada, 1 = pública), como o Leia-me diz. A coluna `id_turno` também consta no dicionário de 2014 e não nos dados.
A coluna *Arquivos* indica em quais arquivos do lake a coluna aparece (o nome do arquivo sem o ano).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `id_exame_ana` | `ID_EXAME_ANA` | texto | Ano da ANA | — | todo | `ts_aluno`, `ts_escola`, `ts_item` |
| `id_regiao` | `ID_REGIAO` | texto | Código da Região (1 = Norte; 2 = Nordeste; 3 = Sudeste; 4 = Sul; 5 = Centro-Oeste) | — | todo | `ts_aluno`, `ts_escola` |
| `id_uf` | `ID_UF` | texto | Código da Unidade da Federação (código IBGE da UF, de 11 = RO a 53 = DF) | — | todo | `ts_aluno`, `ts_escola` |
| `id_municipio` | `ID_MUNICIPIO` | texto | Código do Município | — | todo | `ts_aluno`, `ts_escola` |
| `id_area` | `ID_AREA` | texto | Área (1 = capital; 2 = interior) | — | todo | `ts_aluno`, `ts_escola` |
| `id_escola` | `ID_ESCOLA` | texto | Código da Escola | — | todo | `ts_aluno`, `ts_escola` |
| `in_publica` | `IN_PUBLICA` | texto | Dependência administrativa reduzida a indicador de escola pública (0 = privada; 1 = pública), em lugar da dependência detalhada (Leia-me) | — | todo | `ts_aluno`, `ts_escola` |
| `id_localizacao` | `ID_LOCALIZACAO` | texto | Localização (1 = urbana; 2 = rural) | — | todo | `ts_aluno`, `ts_escola` |
| `id_turma` | `ID_TURMA` | texto | Código da turma na ANA | — | todo | `ts_aluno` |
| `id_serie` | `ID_SERIE` | texto | Série (3 = 3º ano do ensino fundamental) | — | todo | `ts_aluno`, `ts_item` |
| `id_aluno` | `ID_ALUNO` | texto | Código do aluno na ANA | — | todo | `ts_aluno` |
| `in_situacao_censo` | `IN_SITUACAO_CENSO` | texto | Indicador de consistência com o Censo Escolar do ano da edição (0 = não consistente; 1 = consistente) | — | todo | `ts_aluno` |
| `in_presenca_lp` | `IN_PRESENCA_LP` | texto | Indicador de presença no dia dos testes de Língua Portuguesa (Leitura e Escrita) (0 = aluno ausente; 1 = aluno presente) | — | todo | `ts_aluno` |
| `in_presenca_mt` | `IN_PRESENCA_MT` | texto | Indicador de presença no dia dos testes de Matemática (0 = aluno ausente; 1 = aluno presente) | — | todo | `ts_aluno` |
| `in_preenchimento_lp` | `IN_PREENCHIMENTO_LP` | texto | Indicador de preenchimento dos testes de Língua Portuguesa (Leitura e Escrita) (0 = prova não preenchida; 1 = prova preenchida) | — | todo | `ts_aluno` |
| `in_preenchimento_mt` | `IN_PREENCHIMENTO_MT` | texto | Indicador de preenchimento dos testes de Matemática (0 = prova não preenchida; 1 = prova preenchida) | — | todo | `ts_aluno` |
| `co_caderno_prova_lp` | `CO_CADERNO_PROVA_LP` | texto | Código do Caderno de Provas do Teste de Língua Portuguesa (Leitura e Escrita) (0 = caderno não identificado; 1 a 16 = prova regular; 17 = macrotipo) | — | 2014 | `ts_aluno` |
| `co_caderno_prova_mt` | `CO_CADERNO_PROVA_MT` | texto | Código do Caderno de Provas do Teste de Matemática (0 = caderno não identificado; 1 a 16 = prova regular; 17 = macrotipo; 18 = surdos e 19 = ledor ou braille, só em 2016) | — | todo | `ts_aluno` |
| `tx_resposta_lp` | `TX_RESPOSTA_LP` | texto | Resposta do Aluno ao Teste de Leitura em Língua Portuguesa (A, B, C, D; `.` = em branco; `*` = nulo) | — | todo | `ts_aluno` |
| `tx_resposta_mt` | `TX_RESPOSTA_MT` | texto | Resposta do Aluno ao Teste de Matemática (A, B, C, D; `.` = em branco; `*` = nulo) | — | todo | `ts_aluno` |
| `conceito_q1` | `CONCEITO_Q1` | texto | Conceito obtido na questão 1 do teste de Escrita em Língua portuguesa (escrita de palavras) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu) | — | todo | `ts_aluno` |
| `conceito_q2` | `CONCEITO_Q2` | texto | Conceito obtido na questão 2 do teste de Escrita em Língua portuguesa (escrita de palavras) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu) | — | todo | `ts_aluno` |
| `conceito_q3_ortografia` | `CONCEITO_Q3_ORTOGRAFIA` | texto | Conceito obtido para ortografia na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `conceito_q3_coesao` | `CONCEITO_Q3_COESAO` | texto | Conceito obtido para coesão na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `conceito_q3_segmentacao` | `CONCEITO_Q3_SEGMENTACAO` | texto | Conceito obtido para segmentação na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `conceito_q3_pontuacao` | `CONCEITO_Q3_PONTUACAO` | texto | Conceito obtido para pontuação na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `conceito_q3_progressao_tematica` | `CONCEITO_Q3_PROGRESSAO_TEMATICA` | texto | Conceito obtido para progressão temática na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `conceito_q3_elementos_narrativa` | `CONCEITO_Q3_ELEMENTOS_NARRATIVA` | texto | Conceito obtido para elementos da narrativa na questão 3 do teste de Escrita em Língua portuguesa (produção de textos) (A, B ou C; BR = em branco; NL = nulo; NR = não respondeu; TI = texto incipiente) | — | todo | `ts_aluno` |
| `peso_aluno_lp` | `PESO_ALUNO_LP` | texto | Peso do Aluno em Língua Portuguesa (Leitura e Escrita) | — | 2014 | `ts_aluno` |
| `nivel_lpo` | `NIVEL_LPO` | texto | Posicionamento do aluno na escala de proficiência em Leitura em Língua Portuguesa (1 a 4) | — | todo | `ts_aluno` |
| `proficiencia_lpo` | `PROFICIENCIA_LPO` | texto | Proficiência do aluno em Leitura em Língua Portuguesa calculada na escala única da ANA, com média = 0 e desvio = 1 na população de referência | — | todo | `ts_aluno` |
| `desvio_padrao_lpo` | `DESVIO_PADRAO_LPO` | texto | Desvio padrão da proficiência em Leitura em Língua Portuguesa | — | 2014 | `ts_aluno` |
| `proficiencia_lpo_ana` | `PROFICIENCIA_LPO_ANA` | texto | Proficiência em Leitura em Língua Portuguesa transformada na escala única da ANA, com média = 500, desvio = 100 | — | todo | `ts_aluno` |
| `desvio_padrao_lpo_ana` | `DESVIO_PADRAO_LPO_ANA` | texto | Desvio padrão da proficiência transformada em Leitura em Língua Portuguesa | — | 2014 | `ts_aluno` |
| `nivel_lpd` | `NIVEL_LPD` | texto | Posicionamento do aluno na escala de proficiência em Escrita em Língua Portuguesa (1 a 5) | — | todo | `ts_aluno` |
| `proficiencia_lpd` | `PROFICIENCIA_LPD` | texto | Proficiência do aluno em Escrita em Língua Portuguesa calculada na escala única da ANA, com média = 0 e desvio = 1 na população de referência | — | todo | `ts_aluno` |
| `desvio_padrao_lpd` | `DESVIO_PADRAO_LPD` | texto | Desvio padrão da proficiência em Escrita em Língua Portuguesa | — | 2014 | `ts_aluno` |
| `proficiencia_lpd_ana` | `PROFICIENCIA_LPD_ANA` | texto | Proficiência em Escrita em Língua Portuguesa transformada na escala única da ANA, com média = 500, desvio = 100 | — | todo | `ts_aluno` |
| `desvio_padrao_lpd_ana` | `DESVIO_PADRAO_LPD_ANA` | texto | Desvio padrão da proficiência transformada em Escrita em Língua Portuguesa | — | 2014 | `ts_aluno` |
| `peso_aluno_mt` | `PESO_ALUNO_MT` | texto | Peso do Aluno em Matemática | — | todo | `ts_aluno` |
| `nivel_mt` | `NIVEL_MT` | texto | Posicionamento do aluno na escala de proficiência em Matemática (1 a 4) | — | todo | `ts_aluno` |
| `proficiencia_mt` | `PROFICIENCIA_MT` | texto | Proficiência do aluno em Matemática calculada na escala única da ANA, com média = 0 e desvio = 1 na população de referência | — | todo | `ts_aluno` |
| `desvio_padrao_mt` | `DESVIO_PADRAO_MT` | texto | Desvio padrão da proficiência em Matemática | — | 2014 | `ts_aluno` |
| `proficiencia_mt_ana` | `PROFICIENCIA_MT_ANA` | texto | Proficiência do aluno em Matemática transformada na escala única da ANA, com média = 500, desvio = 100 | — | todo | `ts_aluno` |
| `desvio_padrao_mt_ana` | `DESVIO_PADRAO_MT_ANA` | texto | Desvio padrão da proficiência transformada em Matemática | — | 2014 | `ts_aluno` |
| `pc_formacao_docente` | `PC_FORMACAO_DOCENTE` | texto | Indicador de Adequação da Formação Docente (Informação referente ao Grupo 1, para os Anos Iniciais do EF) | — | todo | `ts_escola` |
| `nivel_socio_economico` | `NIVEL_SOCIO_ECONOMICO` | texto | Nível socioecônomico da escola (2014: 8 = muito baixo a 14 = muito alto; 2016: 15 = muito baixo a 21 = muito alto) | — | todo | `ts_escola` |
| `nu_matriculados_censo` | `NU_MATRICULADOS_CENSO` | texto | Número de alunos matriculados no 3º ano do ensino fundamental de 9 anos no censo 2016 | — | todo | `ts_escola` |
| `nu_presentes_lp` | `NU_PRESENTES_LP` | texto | Número de alunos, que estavam presentes no dia da aplicação dos testes de Língua Portuguesa (Leitura e Escrita) da ANA | — | todo | `ts_escola` |
| `nu_validos_lp` | `NU_VALIDOS_LP` | texto | Número de alunos do no 3º ano, que responderam a três ou mais questões dos testes de Língua Portuguesa (Leitura) da ANA | — | todo | `ts_escola` |
| `taxa_participacao_lp` | `TAXA_PARTICIPACAO_LP` | texto | Taxa de participação nos testes de Língua Portuguesa: alunos presentes (`nu_presentes_lp`) sobre matriculados no 3º ano pelo Censo Escolar (`nu_matriculados_censo`); o dicionário diz "Matemática" por engano | — | todo | `ts_escola` |
| `media_lpo` | `MEDIA_LPO` | texto | Média em Leitura em Língua Portuguesa | — | todo | `ts_escola` |
| `nivel_1_lpo` | `NIVEL_1_LPO` | texto | Percentual de estudantes com proficiência menor ou igual a 425 pontos | — | todo | `ts_escola` |
| `nivel_2_lpo` | `NIVEL_2_LPO` | texto | Percentual de estudantes com proficiencia maior que 425 e menor ou igual a 525 pontos | — | todo | `ts_escola` |
| `nivel_3_lpo` | `NIVEL_3_LPO` | texto | Percentual de estudantes com proficiencia maior que 525 e menor ou igual a 625 pontos | — | todo | `ts_escola` |
| `nivel_4_lpo` | `NIVEL_4_LPO` | texto | Percentual de estudantes com proficiencia maior que 625 pontos | — | todo | `ts_escola` |
| `esc_sim_n1_lpo` | `ESC_SIM_N1_LPO` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência menor ou igual a 425 pontos | — | todo | `ts_escola` |
| `esc_sim_n2_lpo` | `ESC_SIM_N2_LPO` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiencia maior que 425 e menor ou igual a 525 pontos | — | todo | `ts_escola` |
| `esc_sim_n3_lpo` | `ESC_SIM_N3_LPO` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiencia maior que 525 e menor ou igual a 625 pontos | — | todo | `ts_escola` |
| `esc_sim_n4_lpo` | `ESC_SIM_N4_LPO` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiencia maior que 625 pontos | — | todo | `ts_escola` |
| `media_lpd` | `MEDIA_LPD` | texto | Média em Escrita em Língua Portuguesa | — | todo | `ts_escola` |
| `nivel_1_lpd` | `NIVEL_1_LPD` | texto | Percentual de estudantes com proficiência menor que 350 pontos | — | todo | `ts_escola` |
| `nivel_2_lpd` | `NIVEL_2_LPD` | texto | Percentual de estudantes com proficiência maior ou igual a 350 e menor que 450 pontos | — | todo | `ts_escola` |
| `nivel_3_lpd` | `NIVEL_3_LPD` | texto | Percentual de estudantes com proficiência maior ou igual a 450 e menor que 500 pontos | — | todo | `ts_escola` |
| `nivel_4_lpd` | `NIVEL_4_LPD` | texto | Percentual de estudantes com proficiência maior ou igual a 500 e menor que 600 pontos | — | todo | `ts_escola` |
| `nivel_5_lpd` | `NIVEL_5_LPD` | texto | Percentual de estudantes com proficiência maior ou igual a 600 pontos | — | todo | `ts_escola` |
| `esc_sim_n1_lpd` | `ESC_SIM_N1_LPD` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência menor que 350 pontos | — | todo | `ts_escola` |
| `esc_sim_n2_lpd` | `ESC_SIM_N2_LPD` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior ou igual a 350 e menor que 450 pontos | — | todo | `ts_escola` |
| `esc_sim_n3_lpd` | `ESC_SIM_N3_LPD` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior ou igual a 450 e menor que 500 pontos | — | todo | `ts_escola` |
| `esc_sim_n4_lpd` | `ESC_SIM_N4_LPD` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior ou igual a 500 e menor que 600 pontos | — | todo | `ts_escola` |
| `esc_sim_n5_lpd` | `ESC_SIM_N5_LPD` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior ou igual a 600 pontos | — | todo | `ts_escola` |
| `nu_presentes_mt` | `NU_PRESENTES_MT` | texto | Número de alunos do no 3º ano, que estavam presentes no dia da aplicação dos testes de Matemática da ANA | — | todo | `ts_escola` |
| `nu_validos_mt` | `NU_VALIDOS_MT` | texto | Número de alunos do no 3º ano, que responderam a três ou mais questões dos testes de Matemática da ANA | — | todo | `ts_escola` |
| `taxa_participacao_mt` | `TAXA_PARTICIPACAO_MT` | texto | Taxa de participação nos testes de Matemática calculada pela razão entre o total de alunos presentes na ANA (QT_ALUNO_PRESENTE_MT) e o total de alunos cadastrados no Censo Escolar que são público alvo da ANA (NU_MATRICULADOS_CENSO) | — | todo | `ts_escola` |
| `media_mt` | `MEDIA_MT` | texto | Média em Matemática | — | todo | `ts_escola` |
| `nivel_1_mt` | `NIVEL_1_MT` | texto | Percentual de estudantes com proficiência menor ou igual a 425 pontos | — | todo | `ts_escola` |
| `nivel_2_mt` | `NIVEL_2_MT` | texto | Percentual de estudantes com proficiência maior que 425 e menor ou igual a 525 pontos | — | todo | `ts_escola` |
| `nivel_3_mt` | `NIVEL_3_MT` | texto | Percentual de estudantes com proficiência maior que 525 e menor ou igual a 575 pontos | — | todo | `ts_escola` |
| `nivel_4_mt` | `NIVEL_4_MT` | texto | Percentual de estudantes com proficiência maior que 575 pontos | — | todo | `ts_escola` |
| `esc_sim_n1_mt` | `ESC_SIM_N1_MT` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência menor ou igual a 425 pontos | — | todo | `ts_escola` |
| `esc_sim_n2_mt` | `ESC_SIM_N2_MT` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior que 425 e menor ou igual a 525 pontos | — | todo | `ts_escola` |
| `esc_sim_n3_mt` | `ESC_SIM_N3_MT` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior que 525 e menor ou igual a 575 pontos | — | todo | `ts_escola` |
| `esc_sim_n4_mt` | `ESC_SIM_N4_MT` | texto | Percentual de estudantes do Perfil de Escola Similar com proficiência maior que 575 pontos | — | todo | `ts_escola` |
| `disciplina` | `DISCIPLINA` | texto | Área de conhecimento do item (LC = Linguagens e Códigos; MT = Matemática) | — | todo | `ts_item` |
| `bloco` | `BLOCO` | texto | Identificador do bloco | De 1 a 8 = 1 | todo | `ts_item` |
| `posicao` | `POSICAO` | texto | Identificador da posição do item no bloco | De 1 a 10 = 3 | todo | `ts_item` |
| `id_item` | `ID_ITEM` | texto | Código do item | — | todo | `ts_item` |
| `co_quesito` | `CO_QUESITO` | texto | Quesito avaliado no item de produção textual (2014: 9 = ortografia, 10 = coesão, 11 = segmentação, 12 = pontuação, 13 = sequência narrativa, 14 = elementos da narrativa; 2016: 16 a 21, na mesma ordem) | — | todo | `ts_item` |
| `nu_descritor_habilidade` | `NU_DESCRITOR_HABILIDADE` | texto | Identificador do descritor do item | — | todo | `ts_item` |
| `gabarito` | `GABARITO` | texto | Gabarito do item (A a D; X = anulado) ou conceito dos itens de escrita de palavras e de produção textual; itens com acerto parcial trazem a sequência dos conceitos (por exemplo `B/A`) | — | todo | `ts_item` |
| `tipo_item` | `TIPO_ITEM` | texto | Tipo de resposta esperada para o item (Escrita de Palavras, Produção Textual ou Resposta Objetiva); o texto acentuado sai corrompido no lake | — | todo | `ts_item` |
| `item_modelo` | `ITEM_MODELO` | texto | Modelo da Teoria de Resposta ao Item (M3PL = logístico de 3 parâmetros; MRG = resposta gradual) | — | todo | `ts_item` |
| `a` | `A` | texto | Parâmetro de discriminação do item: poder do item de diferenciar quem domina de quem não domina a habilidade avaliada | — | todo | `ts_item` |
| `b` | `B` | texto | Parâmetro de dificuldade do item: quanto maior, mais difícil o item | — | todo | `ts_item` |
| `c` | `C` | texto | Parâmetro de acerto ao acaso: probabilidade de acertar sem dominar a habilidade (vazio nos itens de modelo gradual `MRG`) | — | todo | `ts_item` |
| `tp_situacao_presenca_lp` | `TP_SITUACAO_PRESENCA_LP` | texto | Tipo da situação de presença na aplicação dos testes de Língua Portuguesa (Leitura e Escrita). Informação contida na Lista de Presença. (0 = aluno regular; 1 = inserido; 2 = transferido; 3 = instrumento não retornou) | — | 2016 | `ts_aluno` |
| `tp_situacao_presenca_mt` | `TP_SITUACAO_PRESENCA_MT` | texto | Tipo da situação de presença na aplicação do teste de Matemática (Leitura e Escrita). Informação contida na Lista de Presença. (0 = aluno regular; 1 = inserido; 2 = transferido; 3 = instrumento não retornou) | — | 2016 | `ts_aluno` |
| `in_sala_separada_lp` | `IN_SALA_SEPARADA_LP` | texto | Indicador de atendimento em sala exclusiva para candidatos com necessidades especiais que realizaram testes de Língua Portuguesa (Leitura e Escrita) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_sala_separada_mt` | `IN_SALA_SEPARADA_MT` | texto | Indicador de atendimento em sala exclusiva para candidatos com necessidades especiais que realizaram testes de Matemática (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc1` | `IN_REC_ESC1` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Auxílio para leitura (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc2` | `IN_REC_ESC2` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Auxílio para transcrição (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc3` | `IN_REC_ESC3` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Intérprete de libras (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc5` | `IN_REC_ESC5` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Guia intérprete (para surdocegueira) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc6` | `IN_REC_ESC6` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Nenhum (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc12` | `IN_REC_ESC12` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA:Aparelho de CD (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc13` | `IN_REC_ESC13` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA:Aparelho de DVD (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc14` | `IN_REC_ESC14` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA:Computador (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc15` | `IN_REC_ESC15` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Máquina de escrever (perkins) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc16` | `IN_REC_ESC16` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Monitor/televisão (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc17` | `IN_REC_ESC17` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA: Punção (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc18` | `IN_REC_ESC18` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA:Reglete (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc19` | `IN_REC_ESC19` | texto | Indicador de solicitação de recurso - ESCOLA: Sorabam (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_esc20` | `IN_REC_ESC20` | texto | Indicador de solicitação de recurso disponibilizado pela ESCOLA:Software de tela (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep1` | `IN_REC_INEP1` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Auxílio para leitura (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep2` | `IN_REC_INEP2` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Auxílio para transcrição (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep3` | `IN_REC_INEP3` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Intérprete de libras (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep4` | `IN_REC_INEP4` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Leitor labial (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep5` | `IN_REC_INEP5` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Guia intérprete (para surdocegueira) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep6` | `IN_REC_INEP6` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Nenhum (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep7` | `IN_REC_INEP7` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Aplicador extra (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep8` | `IN_REC_INEP8` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Prova adaptada para surdos (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep9` | `IN_REC_INEP9` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Prova ampliada (fonte 18) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep10` | `IN_REC_INEP10` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Prova superampliada (fonte 24) (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `in_rec_inep11` | `IN_REC_INEP11` | texto | Indicador de solicitação de recurso disponibilizado pelo Inep: Prova em braille (0 = não; 1 = sim) | — | 2016 | `ts_aluno` |
| `co_caderno_prova_lpo` | `CO_CADERNO_PROVA_LPO` | texto | Código do Caderno de Provas do Teste de Língua Portuguesa (Leitura) (0 = caderno não identificado; 1 a 16 = prova regular; 17 = macrotipo; 18 = surdos e 19 = ledor ou braille, só em 2016) | — | 2016 | `ts_aluno` |
| `co_caderno_prova_lpd` | `CO_CADERNO_PROVA_LPD` | texto | Código do Caderno de Provas do Teste de Língua Portuguesa (Escrita) (1 a 4) | — | 2016 | `ts_aluno` |
| `peso_aluno_lpo` | `PESO_ALUNO_LPO` | texto | Peso do Aluno em Língua Portuguesa (Leitura) | — | 2016 | `ts_aluno` |
| `erro_padrao_lpo` | `ERRO_PADRAO_LPO` | texto | Erro padrão da proficiência em Leitura em Língua Portuguesa | — | 2016 | `ts_aluno` |
| `erro_padrao_lpo_ana` | `ERRO_PADRAO_LPO_ANA` | texto | Erro padrão da proficiência transformada em Leitura em Língua Portuguesa | — | 2016 | `ts_aluno` |
| `peso_aluno_lpd` | `PESO_ALUNO_LPD` | texto | Peso do Aluno em Língua Portuguesa (Escrita) | — | 2016 | `ts_aluno` |
| `erro_padrao_lpd` | `ERRO_PADRAO_LPD` | texto | Erro padrão da proficiência em Escrita em Língua Portuguesa | — | 2016 | `ts_aluno` |
| `erro_padrao_lpd_ana` | `ERRO_PADRAO_LPD_ANA` | texto | Erro padrão da proficiência transformada em Escrita em Língua Portuguesa | — | 2016 | `ts_aluno` |
| `erro_padrao_mt` | `ERRO_PADRAO_MT` | texto | Erro padrão da proficiência em Matemática | — | 2016 | `ts_aluno` |
| `erro_padrao_mt_ana` | `ERRO_PADRAO_MT_ANA` | texto | Erro padrão da proficiência transformada em Matemática | — | 2016 | `ts_aluno` |
| `in_item_adaptado` | `IN_ITEM_ADAPTADO` | texto | Indicador de adaptação do item para acessibilidade (0 = não; 1 = sim) | — | 2016 | `ts_item` |
| `tp_adaptacao` | `TP_ADAPTACAO` | texto | Público para o qual o item foi adaptado (nos dados de 2016: LP-SURDOS ou MT-SURDOS) | — | 2016 | `ts_item` |

## No lake

- Dataset `inep/ana`, particionado por `ano`; um Parquet por CSV de `DADOS`, no padrão `ana-microdados_<ano>__ts_aluno.parquet` (também `ts_escola` e `ts_item`).
- Todas as colunas são texto: o DuckDB lê o CSV sem inferir tipos, e os nomes saem normalizados (minúsculas, sem acento).
- A coluna `ano` é a edição, tirada do nome do arquivo; `id_exame_ana` é o ano dentro do dado.
- Campos vazios no CSV (por exemplo, proficiência de aluno ausente) ficam vazios no Parquet.

## Cuidados de uso

- **Os arquivos não se juntam por chave sem cuidado.** `ts_aluno`, `ts_escola` e `ts_item` são entidades diferentes. Aluno e escola se ligam por `id_escola` (código mascarado, igual em todas as bases da edição, segundo o Leia-me) e por `ano`.
- **Esquema muda entre as edições.** Em 2014 `ts_aluno` tem 45 colunas de dados e em 2016, 76; as colunas de leitura e escrita passam a ter caderno e peso separados e `desvio_padrao_*` vira `erro_padrao_*`. Confira a coluna *Período*.
- **Códigos mudam entre as edições.** Em `ts_item`, `co_quesito` usa 9 a 14 em 2014 e 16 a 21 em 2016 para os mesmos seis quesitos da produção textual (ortografia, coesão, segmentação, pontuação, sequência narrativa e elementos da narrativa).
- **O código do nível socioeconômico da escola muda de faixa.** `nivel_socio_economico` usa 8 (muito baixo) a 14 (muito alto) em 2014 e 15 a 21 em 2016, segundo os dicionários; o valor 12 de 2014 e o 19 de 2016 são o mesmo nível (médio alto).
- **Separador do gabarito.** Em `ts_item.gabarito`, itens com acerto parcial vêm como `B,A` e `TI,C,B,A` em 2014 e como `B/A` e `FT/TI/C/B/A` em 2016 (nos dados; o dicionário de 2014 diz `B/A`).
- **Formato numérico de `ts_item` em 2014.** Os parâmetros `a`, `b` e `c` vêm com vírgula decimal (`0,79479`) e `id_item` vem com sufixo `.0` (`64396.0`); em 2016 usam ponto e inteiro. Troque a vírgula e converta antes de calcular.
- **Acentuação quebrada em `ts_item.tipo_item`.** O CSV da fonte é UTF-8, mas o lake o lê como latin-1: o valor "Produção Textual" aparece como `ProduÃ§Ã£o Textual`. Filtre por `LIKE 'Produ%'` ou corrija o texto ao ler.
- **Proteção de dados (LGPD).** Os códigos de escola e de município são máscaras (códigos fictícios iniciados em 6, os mesmos em todas as bases) e a dependência administrativa foi trocada por `in_publica`. Não há nome, CPF ou data de nascimento; ainda assim o aluno tem código próprio na ANA e há indicadores de necessidade especial.
- **Peso de expansão.** Para estimar resultados da população use `peso_aluno_*` e considere só alunos com proficiência calculada; sem peso ficam alunos inconsistentes com o Censo Escolar, com menos de três questões respondidas, sem caderno identificado ou em escola que não atingiu o mínimo para validar a aplicação (Leia-me).
- **Divulgação mínima.** O Leia-me diz que a divulgação oficial dos resultados de uma escola exige ao menos 10 presentes e 80% de participação (em 2016, também 4 respondentes válidos) e a de um município, 10 presentes e 50% de participação; esses critérios foram usados no mascaramento dos dados, e o Leia-me não informa quais escolas ficam de fora.
- **Taxa de participação de língua portuguesa.** O dicionário descreve `taxa_participacao_lp` como taxa dos "testes de Matemática"; pela conferência (`nu_presentes_lp` dividido por `nu_matriculados_censo`) a taxa é a de língua portuguesa.

## Exemplos

Média da proficiência em matemática por região na edição 2016, ponderada pelos alunos válidos (arquivo `ts_escola`, texto convertido para número):

```python
import duckdb

duckdb.sql("""
    SELECT id_regiao,
           count(*) AS escolas,
           round(sum(try_cast(media_mt AS DOUBLE) * try_cast(nu_validos_mt AS DOUBLE))
                 / sum(try_cast(nu_validos_mt AS DOUBLE)), 1) AS media_mt
    FROM read_parquet('lake/inep/ana/ano=2016/*ts_escola.parquet')
    GROUP BY ALL
    ORDER BY id_regiao
""").show()
```

## Referências

- Microdados da ANA: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/ana
- Leia-me e dicionário de variáveis de cada edição, dentro de cada ZIP em https://download.inep.gov.br/microdados/
