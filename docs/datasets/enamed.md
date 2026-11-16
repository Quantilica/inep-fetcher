---
dataset:
  id: enamed
  fonte: inep
  titulo: Enamed 2025 — Exame Nacional de Avaliação da Formação Médica (microdados)
  resumo: 'Microdados do Enamed 2025: resultados e questionários dos concluintes de Medicina (via Enade) e dos demais participantes, em 36 arquivos por tema, mais a tabela de parâmetros dos itens.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enamed
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; a edição de 2025 é a primeira (prova aplicada em 19/10/2025, em 225 municípios)
  cobertura:
    inicio: '2025'
    fim: '2025'
  unidade: um participante do Enamed, em cada arquivo, sem ligação entre arquivos (concluinte de Medicina nos arquivos `microdados_enade_2025_*` e demais participantes nos `microdados_demais_part_2025_*`); na tabela de parâmetros, um item de prova
  granularidade:
    espacial: curso (concluintes), com IES, município, UF e região do curso; para os demais participantes, sem local
    temporal: ano da edição (2025)
  formato_bruto: ZIP com `1. LEIA-ME` (manual, três questionários em PDF, dicionário em xlsx e ods) e `DADOS` (pastas `Enade` com 23 TXT e `Demais Participantes` com 13 TXT, em UTF-8 com BOM, ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em TXT)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 118
  dados_pessoais:
  - coluna: tp_sexo
    categoria: sexo do participante
  - coluna: nu_idade
    categoria: idade do participante (da base da Receita Federal)
  - coluna: nu_questao_01
    categoria: estado civil
  - coluna: qe_i01
    categoria: estado civil
  - coluna: nu_questao_02
    categoria: ter filhos
  - coluna: qe_i02
    categoria: ter filhos
  - coluna: nu_questao_03
    categoria: cor ou raça declarada
  - coluna: qe_i03
    categoria: cor ou raça declarada
  - coluna: nu_questao_04
    categoria: deficiência, transtorno global do desenvolvimento ou altas habilidades
  - coluna: qe_i04
    categoria: deficiência, transtorno global do desenvolvimento ou altas habilidades
  - coluna: qe_i05
    categoria: escolaridade da família
  - coluna: qe_i06
    categoria: escolaridade da família
  - coluna: qe_i07
    categoria: escolaridade da família
  - coluna: nu_questao_05
    categoria: situação financeira, renda familiar e trabalho
  - coluna: qe_i08
    categoria: situação financeira, renda familiar e trabalho
  - coluna: qe_i09
    categoria: situação financeira, renda familiar e trabalho
  - coluna: qe_i10
    categoria: situação financeira, renda familiar e trabalho
  - coluna: qe_i11
    categoria: ingresso por ação afirmativa ou inclusão social
  - coluna: qe_i13
    categoria: bolsas e auxílios recebidos
  - coluna: qe_i15
    categoria: bolsas e auxílios recebidos
  - coluna: qe_i16
    categoria: bolsas e auxílios recebidos
  - coluna: nu_questao_07
    categoria: trajetória e atuação profissional do participante
  - coluna: nu_questao_08
    categoria: trajetória e atuação profissional do participante
  - coluna: nu_questao_09
    categoria: trajetória e atuação profissional do participante
  - coluna: nu_questao_10
    categoria: trajetória e atuação profissional do participante
  - coluna: nu_questao_06
    categoria: trajetória e atuação profissional do participante
  - coluna: ano_fim_em
    categoria: trajetória acadêmica do estudante
  - coluna: ano_in_grad
    categoria: trajetória acadêmica do estudante
  - coluna: co_turno_graduacao
    categoria: trajetória acadêmica do estudante
  - coluna: nu_ano_curso
    categoria: trajetória acadêmica do estudante
  - coluna: in_semestre_curso
    categoria: trajetória acadêmica do estudante
  - coluna: co_munic_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: co_uf_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: co_regiao_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: ds_vt_gab_obj
    categoria: desempenho individual do participante na prova
  - coluna: ds_vt_esc_obj
    categoria: desempenho individual do participante na prova
  - coluna: ds_vt_ace_obj
    categoria: desempenho individual do participante na prova
  - coluna: proficiencia
    categoria: desempenho individual do participante na prova
  - coluna: nt_ger
    categoria: desempenho individual do participante na prova
  - coluna: qt_acerto_area_1
    categoria: desempenho individual do participante na prova
  - coluna: qt_acerto_area_2
    categoria: desempenho individual do participante na prova
  - coluna: qt_acerto_area_3
    categoria: desempenho individual do participante na prova
  - coluna: qt_acerto_area_4
    categoria: desempenho individual do participante na prova
  - coluna: qt_acerto_area_5
    categoria: desempenho individual do participante na prova
  - coluna: per_acerto_enare
    categoria: desempenho individual do participante na prova
  - coluna: in_uso_enare
    categoria: desempenho individual do participante na prova
  eras:
  - desde: '2025'
    mudanca: primeira edição do Enamed, censitária para os concluintes de Medicina; versão corrigida do Inep de 28/04/2026 (a variável `TP_PR_GER` passou a se chamar `TP_PRES` e entraram `IN_USO_ENARE`, `NU_ANO_CURSO` e `IN_SEMESTRE_CURSO`)
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Enamed 2025 — Exame Nacional de Avaliação da Formação Médica (microdados)

## Resumo

Microdados do Exame Nacional de Avaliação da Formação Médica (Enamed), instituído pela Portaria MEC nº 330, de 23/04/2025, como modalidade do Enade para os cursos de Medicina, conduzido pelo Inep com a Ebserh e que unifica as matrizes do Enade de Medicina e a prova objetiva de acesso direto do Exame Nacional de Residência (Enare). Os dados da edição de 2025 cobrem dois públicos: os concluintes de Medicina inscritos no Enade (que podem usar a nota no Enare) e os demais participantes, profissionais graduados em Medicina inscritos só para o Enare. Por exigência da LGPD, os dados vêm em arquivos temáticos ordenados por variáveis diferentes (23 para os concluintes e 13 para os demais participantes), de modo que não é possível ligar as informações de um mesmo participante.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/enamed` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enamed |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; a edição de 2025 é a primeira (prova aplicada em 19/10/2025, em 225 municípios) |
| Cobertura | 2025 a 2025 |
| Unidade (uma linha) | um participante do Enamed, em cada arquivo, sem ligação entre arquivos (concluinte de Medicina nos arquivos `microdados_enade_2025_*` e demais participantes nos `microdados_demais_part_2025_*`); na tabela de parâmetros, um item de prova |
| Granularidade | espacial: curso (concluintes), com IES, município, UF e região do curso; para os demais participantes, sem local; temporal: ano da edição (2025) |
| Formato bruto | ZIP com `1. LEIA-ME` (manual, três questionários em PDF, dicionário em xlsx e ods) e `DADOS` (pastas `Enade` com 23 TXT e `Demais Participantes` com 13 TXT, em UTF-8 com BOM, ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em TXT) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 118 |
| Unidades de medida | — |
| Dados pessoais | `tp_sexo` (sexo do participante); `nu_idade` (idade do participante (da base da Receita Federal)); `nu_questao_01` (estado civil); `qe_i01` (estado civil); `nu_questao_02` (ter filhos); `qe_i02` (ter filhos); `nu_questao_03` (cor ou raça declarada); `qe_i03` (cor ou raça declarada); `nu_questao_04` (deficiência, transtorno global do desenvolvimento ou altas habilidades); `qe_i04` (deficiência, transtorno global do desenvolvimento ou altas habilidades); `qe_i05` (escolaridade da família); `qe_i06` (escolaridade da família); `qe_i07` (escolaridade da família); `nu_questao_05` (situação financeira, renda familiar e trabalho); `qe_i08` (situação financeira, renda familiar e trabalho); `qe_i09` (situação financeira, renda familiar e trabalho); `qe_i10` (situação financeira, renda familiar e trabalho); `qe_i11` (ingresso por ação afirmativa ou inclusão social); `qe_i13` (bolsas e auxílios recebidos); `qe_i15` (bolsas e auxílios recebidos); `qe_i16` (bolsas e auxílios recebidos); `nu_questao_07` (trajetória e atuação profissional do participante); `nu_questao_08` (trajetória e atuação profissional do participante); `nu_questao_09` (trajetória e atuação profissional do participante); `nu_questao_10` (trajetória e atuação profissional do participante); `nu_questao_06` (trajetória e atuação profissional do participante); `ano_fim_em` (trajetória acadêmica do estudante); `ano_in_grad` (trajetória acadêmica do estudante); `co_turno_graduacao` (trajetória acadêmica do estudante); `nu_ano_curso` (trajetória acadêmica do estudante); `in_semestre_curso` (trajetória acadêmica do estudante); `co_munic_curso` (local de funcionamento do curso do estudante); `co_uf_curso` (local de funcionamento do curso do estudante); `co_regiao_curso` (local de funcionamento do curso do estudante); `ds_vt_gab_obj` (desempenho individual do participante na prova); `ds_vt_esc_obj` (desempenho individual do participante na prova); `ds_vt_ace_obj` (desempenho individual do participante na prova); `proficiencia` (desempenho individual do participante na prova); `nt_ger` (desempenho individual do participante na prova); `qt_acerto_area_1` (desempenho individual do participante na prova); `qt_acerto_area_2` (desempenho individual do participante na prova); `qt_acerto_area_3` (desempenho individual do participante na prova); `qt_acerto_area_4` (desempenho individual do participante na prova); `qt_acerto_area_5` (desempenho individual do participante na prova); `per_acerto_enare` (desempenho individual do participante na prova); `in_uso_enare` (desempenho individual do participante na prova) |
| Eras | 2025: primeira edição do Enamed, censitária para os concluintes de Medicina; versão corrigida do Inep de 28/04/2026 (a variável `TP_PR_GER` passou a se chamar `TP_PRES` e entraram `IN_USO_ENARE`, `NU_ANO_CURSO` e `IN_SEMESTRE_CURSO`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_enamed_2025.zip` (9.255.524 bytes; última modificação na fonte em 2026-05-14, lido em 2026-11-15). A página oficial lista só a edição de 2025, com a nota "Atualizado em 14/05/2025", ano que difere do cabeçalho HTTP do arquivo e das datas do manual (2026).
- No bruto, o arquivo se chama `enamed/enamed-microdados_2025@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- O ZIP tem `microdados_enamed_2025/1. LEIA-ME` (manual do usuário, Questionário do Estudante, Questionário Contextual e Questionário de Percepção de Prova em PDF, dicionário em xlsx e ods e um arquivo temporário do Excel, `~$Dicionário_arquivos_variáveis_microdados_Enamed_2025.xlsx`, de 165 bytes, que não é planilha) e `DADOS` com `Enade` (`microdados_enade_2025_arq1.txt` a `arq23.txt`), `Demais Participantes` (`microdados_demais_part_2025_arq1.txt` a `arq13.txt`) e `microdados2025_parametros_itens.txt` (3.891 bytes).
- Linhas de dados conferidas na fonte em 2026-11-15: cada um dos 23 arquivos dos concluintes tem 39.794 linhas, cada um dos 13 dos demais participantes tem 56.833 e a tabela de parâmetros tem 93. O arquivo de caracterização dos concluintes (`arq1`) traz 351 cursos, de 295 IES, em 27 UF.
- O manual registra duas versões: a original, de 16/01/2026, e uma de 28/04/2026, que alterou a categorização de `TP_INSCRICAO`, renomeou `TP_PR_GER` para `TP_PRES`, incluiu `IN_USO_ENARE`, `NU_ANO_CURSO` e `IN_SEMESTRE_CURSO`, atualizou notas e acertos por área (áreas 2 e 3), excluiu participantes com inscrição indevida e incluiu um participante de curso com apenas um concluinte.

## Conteúdo

- **Dois públicos, dois conjuntos de arquivos.** Os arquivos `microdados_enade_2025_arq<N>` trazem os concluintes de Medicina inscritos no Enade (`tp_inscricao` 1), que responderam ao Questionário do Estudante e puderam optar por usar a nota no Enare (`in_uso_enare`). Os arquivos `microdados_demais_part_2025_arq<N>` trazem os demais participantes (`tp_inscricao` 2), graduados em Medicina inscritos só para o Enare, que responderam ao Questionário Contextual (variáveis `nu_questao_01` a `nu_questao_10`).
- **A prova.** Cem questões objetivas de múltipla escolha com quatro alternativas, em dois cadernos (`co_caderno` 1 e 2) com rotação de itens; a nota e a proficiência vêm da Teoria de Resposta ao Item combinada com o método de Angoff modificado, e os acertos por área foram reclassificados em cinco grandes áreas (Clínica Médica, Cirurgia Geral, Pediatria, Ginecologia e Obstetrícia e Medicina da Família e Comunidade) para o Enare.
- **Por que tantos arquivos.** Para atender à LGPD, os microdados foram divididos em arquivos temáticos ordenados por variáveis diferentes: a primeira linha de um arquivo não é o mesmo participante da primeira linha de outro. Entre os concluintes só se pode agrupar os arquivos por `co_curso`; para os demais participantes, só por `nu_ano`, ou seja, não se junta nada em nível de participante.
- **Concluintes do Enade (23 arquivos):**

| Arquivo | Conteúdo (do dicionário de arquivos do Inep) | Colunas |
|---|---|---|
| `microdados_enade_2025_arq1` | caracterização do curso | `inu_ano` (`NU_ANO`), `tp_inscricao`, `co_curso`, `co_ies`, `co_categad`, `co_orgacad`, `co_grupo`, `co_munic_curso`, `co_uf_curso`, `co_regiao_curso` |
| `arq2` | informações acadêmicas: ano de conclusão do ensino médio, ano de início da graduação e turno | `ano_fim_em`, `ano_in_grad`, `co_turno_graduacao` |
| `arq3` | prova e resultados: caderno, número de itens válidos, anulados e desconsiderados, vetores, tipo de presença, proficiência, nota, acertos por área, percentual de acertos para o Enare, respostas do Questionário de Percepção de Prova e, a partir de 28/04/2026, opção de uso no Enare e ano e semestre de conclusão do curso | `co_caderno` a `in_semestre_curso` (28 colunas) |
| `arq4` | avaliação dos estudantes sobre o processo formativo, em escala de concordância de 1 a 6, e itens de recomendação | `qe_i18` a `qe_i58` |
| `arq5`, `arq6` | sexo; idade no dia da prova | `tp_sexo`; `nu_idade` |
| `arq7` a `arq23` | uma questão do Questionário do Estudante por arquivo, em ordem (`arq7` é `qe_i01`, `arq8` é `qe_i02` e assim até `arq23`, que é `qe_i17`) | `qe_i01` a `qe_i17` |

- **Demais participantes (13 arquivos):**

| Arquivo | Conteúdo (do dicionário de arquivos do Inep) | Colunas |
|---|---|---|
| `microdados_demais_part_2025_arq1` | prova e resultados: caderno, itens válidos, anulados e desconsiderados, vetores, presença, proficiência, nota, acertos por área, percentual de acertos para o Enare e respostas do Questionário de Percepção de Prova | `inu_ano` (`NU_ANO`), `tp_inscricao`, `co_caderno` a `co_rs_i9` (27 colunas no arquivo) |
| `arq2`, `arq3` | sexo; idade no dia da prova | `tp_sexo`; `nu_idade` |
| `arq4` a `arq13` | uma questão do Questionário Contextual por arquivo, na ordem (`arq4` é `nu_questao_01`, até `arq13`, que é `nu_questao_10`): estado civil, filhos, cor ou raça, deficiência, renda, tempo desde a conclusão do curso, trabalho atual, tempo como médico, carga horária semanal e esferas de atuação pretendidas | `nu_questao_01` a `nu_questao_10` |

- **Tabela de parâmetros.** `microdados2025_parametros_itens` traz, por item, o número do item em cada uma das duas provas (`nu_item_prova_1` e `nu_item_prova_2`), se foi mantido no cálculo, o parâmetro de dificuldade, a correlação bisserial e as estatísticas INFIT e OUTFIT; serve para reordenar os itens entre os cadernos.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2025 | 37 arquivos, de 2 a 43 colunas |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx), com as abas `DICIONÁRIO DE VARIÁVEIS - ENADE`, `DICIONÁRIO DE VARIÁVEIS - DP` e `DICIONÁRIO - PARÂMETROS`. Quando uma coluna existe nos dois públicos com descrição diferente, a descrição junta as duas versões.
A coluna *Arquivos* indica em quais arquivos do lake a coluna aparece (o nome do arquivo sem o ano); a coluna `inu_ano` está em todos os arquivos de dados. Os códigos de resposta do Questionário do Estudante são letras (A, B, …); `.` marca "sem resposta" nas respostas de texto e nos números.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `nu_item_prova_1` | `NU_ITEM_PROVA_1` | texto | Número do item na prova 1 (1 a 100) | — | todo | `microdados_parametros_itens` |
| `nu_item_prova_2` | `NU_ITEM_PROVA_2` | texto | Número do item na prova 2 (1 a 100) | — | todo | `microdados_parametros_itens` |
| `item_mantido` | `ITEM_MANTIDO` | texto | Indica se o item foi mantido no cálculo | 1 = Sim; 0 = Não | todo | `microdados_parametros_itens` |
| `parametro_b` | `PARAMETRO_B` | texto | Parâmetro de dificuldade (Min = - 9,9999; Max = 9,9999) | — | todo | `microdados_parametros_itens` |
| `cor_bisserial` | `COR_BISSERIAL` | texto | Correlação Bisserial (Min = - 1; Max = 1) | — | todo | `microdados_parametros_itens` |
| `infit` | `INFIT` | texto | Estatística de Ajuste INFIT na TRI (Min = - 9,9999; Max = 9,9999) | — | todo | `microdados_parametros_itens` |
| `outfit` | `OUTFIT` | texto | Estatística de Ajuste OUTFIT na TRI (Min = - 9,9999; Max = 9,9999) | — | todo | `microdados_parametros_itens` |
| `inu_ano` | `INU_ANO` | texto | Ano de realização do exame (2025). Na fonte a coluna se chama `NU_ANO`; o arquivo começa com a marca de ordem de bytes UTF-8 (BOM), que o conversor leu como parte do nome, e a coluna ficou `inu_ano` em todos os arquivos de dados | — | todo | `microdados_demais_part_arq1`, `microdados_demais_part_arq10`, `microdados_demais_part_arq11` e mais 33 |
| `tp_inscricao` | `TP_INSCRICAO` | texto | Tipo de inscrição | 1 = Concluinte do Enade; 2 = Demais Participantes | todo | `microdados_demais_part_arq1`, `microdados_enade_arq1` |
| `co_caderno` | `CO_CADERNO` | texto | Código do caderno respondido pelo participante (1 e 2) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `nu_item` | `NU_ITEM` | texto | Número de itens válidos. (90 itens) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `nu_item_z` | `NU_ITEM_Z` | texto | Número de itens que foram anulados pela Comissão Assessora de Área ou administrativamente pelo Inep (7 itens) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `nu_item_x` | `NU_ITEM_X` | texto | Número de itens que foram desconsiderdos devido à correlação bisserial menor ou igual a 0. (3 itens) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `ds_vt_gab_obj` | `DS_VT_GAB_OBJ` | texto | Vetor que representa o gabarito final da prova. (1 letra por item (intervalo de A a D)) | 6 = Questão anulada pela Comissão Assessora de Área ou administrativamente pelo Inep | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `ds_vt_esc_obj` | `DS_VT_ESC_OBJ` | texto | Vetor que representa a escolha de resposta da prova. (1 letra por item (intervalo de A a D)) | . = em branco; * = múltiplo | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `ds_vt_ace_obj` | `DS_VT_ACE_OBJ` | texto | Vetor que representa os acertos da prova. | 0 = Errado; 1 = Certo; 6 = Questão anulada pela Comissão Assessora de Área ou administrativamente pelo Inep; 4 = Eliminado; 8 = Questão desconsiderada pela TRI; 9 = Ausente | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `tp_pres` | `TP_PRES` | texto | Tipo de presença na prova | 222 = Ausente; 334 = Eliminado por participação indevida; 555 = Presente com resultado válido | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `proficiencia` | `PROFICIENCIA` | texto | Proficiência da TRI na prova objetiva (valor de theta) (Min = -9,999; Max = 9,999; Se TP_PR_GER = 222 ou 334, então = .) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `nt_ger` | `NT_GER` | texto | Nota da prova objetiva (Min = 0,0; Max = 100,0; Se TP_PR_GER = 222 ou 334, então = .) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `qt_acerto_area_1` | `QT_ACERTO_AREA_1` | texto | Número de acertos na Área 1 (Clínica Médica) (Min = 0; Max = 20) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `qt_acerto_area_2` | `QT_ACERTO_AREA_2` | texto | Número de acertos na Área 2 (Pediatria) (Min = 0; Max = 20) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `qt_acerto_area_3` | `QT_ACERTO_AREA_3` | texto | Número de acertos na Área 3 (Cirurgia Geral) (Min = 0; Max = 20) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `qt_acerto_area_4` | `QT_ACERTO_AREA_4` | texto | Número de acertos na Área 4 (Ginecologia e Obstetrícia) (Min = 0; Max = 20) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `qt_acerto_area_5` | `QT_ACERTO_AREA_5` | texto | Número de acertos na Área 5 (Medicina da Família e Comunidade/Saúde Coletiva) (Min = 0; Max = 20) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `per_acerto_enare` | `PER_ACERTO_ENARE` | texto | Percentual de acertos para fins do Enare, calculado a partir do número de acertos somados ao número de questões anuladas/desconsideradas. (Min = 0; Max = 100) | — | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i1` | `CO_RS_I1` | texto | Qual o grau de dificuldade das questões? (. = Sem resposta) | A = Muito fácil; B = Fácil; C = Médio; D = Difícil; E = Muito difícil; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i2` | `CO_RS_I2` | texto | Qual foi o tempo gasto por você para concluir a prova? (. = Sem resposta) | A = Menos de uma hora; B = Entre uma e duas horas; C = Entre três e quatro horas; D = Entre quatro e cinco horas; E = Cinco horas, e não consegui terminar; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i3` | `CO_RS_I3` | texto | Em relação ao tempo total de aplicação, você considera que a prova foi (. = Sem resposta) | A = Muito longa; B = Longa; C = Adequada; D = Curta; E = Muito curta; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i4` | `CO_RS_I4` | texto | Os enunciados das questões estavam claros e objetivos? (. = Sem resposta) | A = Sim, todos; B = Sim, a maioria; C = Apenas cerca da metade; D = Poucos; E = Não, nenhum; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i5` | `CO_RS_I5` | texto | As informações/instruções fornecidas para a resolução das questões foram suficientes para resolvê-las? (. = Sem resposta) | A = Sim, até excessivas; B = Sim, em todas elas; C = Sim, na maioria delas; D = Sim, somente em algumas; E = Não, em nenhuma delas; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i6` | `CO_RS_I6` | texto | Você se deparou com alguma dificuldade ao responder à prova? Qual? (. = Sem resposta) | A = Desconhecimento do conteúdo; B = Forma diferente de abordagem do conteúdo; C = Espaço insuficiente para responder às questões; D = Falta de motivação para fazer a prova; E = Não tive qualquer tipo de dificuldade para responder à prova; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i7` | `CO_RS_I7` | texto | Considerando as questões da prova, você percebeu que (. = Sem resposta) | A = Não estudou ainda a maioria desses conteúdos; B = Estudou alguns desses conteúdos, mas não os aprendeu; C = Estudou a maioria desses conteúdos, mas não os aprendeu; D = Estudou e aprendeu muitos desses conteúdos; … (lista completa no dicionário da fonte) | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i8` | `CO_RS_I8` | texto | Como você avalia a sequência das questões na prova? (. = Sem resposta) | A = A sequência não interferiu nas minhas respostas; B = Preferiria a sequência por área; C = Preferiria a sequência por grau de dificuldade; D = A sequência dificultou meu raciocínio durante a prova; … (lista completa no dicionário da fonte) | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `co_rs_i9` | `CO_RS_I9` | texto | As atividades práticas desenvolvidas ao longo do seu curso contribuíram para a resolução das questões dessa prova? (. = Sem resposta) | A = Sim; B = Não; * = Resposta anulada | todo | `microdados_demais_part_arq1`, `microdados_enade_arq3` |
| `nu_questao_07` | `NU_QUESTAO_07` | texto | Você está trabalhando atualmente? (. = Sem resposta) | A = Não; B = Sim, mas não na minha área de formação; C = Sim, na minha área de formação | todo | `microdados_demais_part_arq10` |
| `nu_questao_08` | `NU_QUESTAO_08` | texto | Há quanto tempo você atua profissionalmente como médico? (. = Sem resposta) | A = Nunca atuei como médico; B = Menos de 1 ano; C = Entre 1 e 2 anos; D = Entre 3 e 5 anos; E = Entre 6 e 10 anos; F = Mais de 10 anos | todo | `microdados_demais_part_arq11` |
| `nu_questao_09` | `NU_QUESTAO_09` | texto | Qual sua carga horária atual de trabalho semanal como médico? (. = Sem resposta) | A = Não estou trabalhando atualmente como médico; B = 20 horas semanais ou menos; C = 30 horas semanais; D = 40 horas semanais; E = Mais de 40 horas semanais | todo | `microdados_demais_part_arq12` |
| `nu_questao_10` | `NU_QUESTAO_10` | texto | A partir da obtenção de especialidade médico-profissional, por meio de Residência Médica, você pretende inserir-se em quais esferas profissionais listadas a seguir: (. = Sem resposta) | A = Prestação de serviço no Sistema único de Saúde (SUS); B = Prestação de serviço na rede hospitalar privada; C = Pesquisa aplicada no setor privado; D = Pesquisa e Ensino na área da formação médica; E = Outras | todo | `microdados_demais_part_arq13` |
| `tp_sexo` | `TP_SEXO` | texto | Sexo | M = Masculino; F = Feminino; 9 = Indefinido | todo | `microdados_demais_part_arq2`, `microdados_enade_arq5` |
| `nu_idade` | `NU_IDADE` | texto | Idade do inscrito em 19/10/2025 (Dados provenientes da base da Receita Federal) | — | todo | `microdados_demais_part_arq3`, `microdados_enade_arq6` |
| `nu_questao_01` | `NU_QUESTAO_01` | texto | Qual o seu estado civil? (. = Sem resposta) | A = Solteiro(a); B = Casado (a) ou vivendo em união estável; C = Separado(a) judicialmente/divorciado(a); D = Viúvo(a); E = Outro | todo | `microdados_demais_part_arq4` |
| `nu_questao_02` | `NU_QUESTAO_02` | texto | Você tem filhos? (. = Sem resposta) | A = Não; B = Sim, 1 filho; C = Sim, 2 filhos; D = Sim, 3 filhos ou mais | todo | `microdados_demais_part_arq5` |
| `nu_questao_03` | `NU_QUESTAO_03` | texto | Qual é a sua cor ou raça? (. = Sem resposta) | A = Branca; B = Preta; C = Amarela; D = Parda; E = Indígena; F = Não quero declarar | todo | `microdados_demais_part_arq6` |
| `nu_questao_04` | `NU_QUESTAO_04` | texto | Você tem alguma deficiência, transtorno global do desenvolvimento ou altas habilidades? (Você pode marcar quantas alternativas considerar necessárias). (. = Sem resposta) | A = Não possuo; B = Cegueira; C = Baixa Visão; D = Surdez; E = Deficiência Auditiva; F = Deficiência Física; G = Transtorno do Espectro Autista (TEA); H = Altas habilidades/superdotação; I = Deficiência Intelectual; … (lista completa no dicionário da fonte) | todo | `microdados_demais_part_arq7` |
| `nu_questao_05` | `NU_QUESTAO_05` | texto | Qual a renda total de sua família, incluindo seus rendimentos? (considere como família a sua unidade de origem composta por pessoas que possuem vínculos consanguíneos e/ou de parentesco, todas moradoras do mesmo domicílio). (. = Sem resposta) | A = Até 1,5 salário mínimo (até R$ 2.277,00); B = De 1,5 a 3 salários mínimos (R$ 2.277,00 a R$ 4.554,00); C = De 3 a 4,5 salários mínimos (R$ 4.554,00 a R$ 6.831,00); D = De 4,5 a 6 salários mínimos (R$ 6.831,00 a R$ 9.108,00); … (lista completa no dicionário da fonte) | todo | `microdados_demais_part_arq8` |
| `nu_questao_06` | `NU_QUESTAO_06` | texto | Há quanto tempo você concluiu o curso de medicina? (. = Sem resposta) | A = Menos de 1 ano; B = Entre 1 e 2 anos; C = Entre 3 e 5 anos; D = Entre 6 e 10 anos; E = Mais de 10 anos; F = Não concluí | todo | `microdados_demais_part_arq9` |
| `co_curso` | `CO_CURSO` | texto | Código do curso no Enade (Entre 12 e 5001466) | — | todo | `microdados_enade_arq1`, `microdados_enade_arq10`, `microdados_enade_arq11` e mais 20 |
| `co_ies` | `CO_IES` | texto | Código da IES (e-MEC) (Entre 1 e 29118) | — | todo | `microdados_enade_arq1` |
| `co_categad` | `CO_CATEGAD` | texto | Código da categoria administrativa da IES | 1 = Pública Federal; 2 = Pública Estadual; 3 = Pública Municipal; 4 = Privada com fins lucrativos; 5 = Privada sem fins lucrativos; 7 = Especial; 8 = Comunitária/Confessional | todo | `microdados_enade_arq1` |
| `co_orgacad` | `CO_ORGACAD` | texto | Código da organização acadêmica da IES | 10020 = Centro Universitário; 10022 = Faculdade; 10028 = Universidade | todo | `microdados_enade_arq1` |
| `co_grupo` | `CO_GRUPO` | texto | Código da Área de enquadramento do curso no Enade | 12 = MEDICINA | todo | `microdados_enade_arq1` |
| `co_munic_curso` | `CO_MUNIC_CURSO` | texto | Código do município de funcionamento do curso (Entre 1100049 e 5300108 (Identificação do Município conforme IBGE - Ir para Planilha MUNICÍPIOS)) | — | todo | `microdados_enade_arq1` |
| `co_uf_curso` | `CO_UF_CURSO` | texto | Código da UF de funcionamento do curso (Conforme código do IBGE) | 11 = Rondônia (RO); 12 = Acre (AC); 13 = Amazonas (AM); 14 = Roraima (RR); 15 = Pará (PA); 16 = Amapa (AP); 17 = Tocantins (TO); 21 = Maranhão (MA); 22 = Piauí (PI); 23 = Ceará (CE); 24 = Rio Grande do Norte (RN); 25 = Paraíba (PB); 26 = Pernambuco (PE); … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq1` |
| `co_regiao_curso` | `CO_REGIAO_CURSO` | texto | Código da região de funcionamento do curso | 1 = Região Norte (N); 2 = Região Nordeste (NE); 3 = Região Sudeste (SE); 4 = Região Sul (SUL); 5 = Região Centro-Oeste (CO) | todo | `microdados_enade_arq1` |
| `qe_i04` | `QE_I04` | texto | Você tem alguma deficiência, transtorno global do desenvolvimento ou altas habilidades? (Você pode marcar quantas alternativas considerar necessárias). (. = Sem resposta) | A = Não possuo; B = Cegueira; C = Baixa Visão; D = Surdez; E = Deficiência Auditiva; F = Deficiência Física; G = Transtorno do Espectro Autista (TEA); H = Altas habilidades/superdotação; I = Deficiência Intelectual; … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq10` |
| `qe_i05` | `QE_I05` | texto | Alguém em sua família concluiu um curso superior? (. = Sem resposta) | A = Sim; B = Não; C = Não sei responder | todo | `microdados_enade_arq11` |
| `qe_i06` | `QE_I06` | texto | Até que etapa de escolarização sua mãe concluiu? (. = Sem resposta) | A = Nenhuma; B = Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série); C = Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série); D = Ensino Médio; E = Ensino Superior - Graduação; F = Pós-graduação (Especialização); G = Pós-Graduação (Mestrado ou Doutorado); … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq12` |
| `qe_i07` | `QE_I07` | texto | Até que etapa de escolarização seu pai concluiu? (. = Sem resposta) | A = Nenhuma; B = Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série); C = Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série); D = Ensino Médio; E = Ensino Superior - Graduação; F = Pós-graduação (Especialização); G = Pós-Graduação (Mestrado ou Doutorado); … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq13` |
| `qe_i08` | `QE_I08` | texto | Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)? (. = Sem resposta) | A = Não tenho renda e meus gastos são financiados por programas governamentais; B = Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas; … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq14` |
| `qe_i09` | `QE_I09` | texto | Qual a renda total de sua família, incluindo seus rendimentos? (considere como família a sua unidade de origem composta por pessoas que possuem vínculos consanguíneos e/ou de parentesco, todas moradoras do mesmo domicílio). (. = Sem resposta) | A = Até 1,5 salário mínimo (até R$ 2277,00); B = De 1,5 a 3 salários mínimos (R$ 2277,00 a R$ 4554,00); C = De 3 a 4,5 salários mínimos (R$ 4554,00 a R$ 6831,00); D = De 4,5 a 6 salários mínimos (R$ 6831,00 a R$ 9108,00); … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq15` |
| `qe_i10` | `QE_I10` | texto | Qual alternativa melhor descreve a sua situação de trabalho durante a maior parte do curso? (Excluindo trabalhos acadêmicos e bolsas). (. = Sem resposta) | A = Não trabalhei durante o curso; B = Trabalhei 20 horas semanais; C = Trabalhei 30 horas semanais; D = Trabalhei 40 horas semanais; E = Trabalhei com jornada de trabalho flexível de horários | todo | `microdados_enade_arq16` |
| `qe_i11` | `QE_I11` | texto | Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social? (Exemplos de políticas de ação afirmativa ou inclusão social são as Cotas e o Prouni.) (. = Sem resposta) | A = Não; B = Sim, por critério étnico-racial; C = Sim, por critério de renda; D = Sim, por ter estudado em escola pública ou particular com bolsa de estudos; E = Sim, por sistema que combina dois ou mais critérios anteriores; … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq17` |
| `qe_i12` | `QE_I12` | texto | Qual a principal razão para você ter escolhido a sua instituição de educação superior? (. = Sem resposta) | A = Gratuidade; B = Preço da mensalidade; C = Proximidade da minha residência; D = Proximidade do meu trabalho; E = Facilidade de acesso; F = Qualidade/reputação; G = Foi a única onde tive aprovação; H = Possibilidade de ter bolsa de estudo; I = Outro motivo | todo | `microdados_enade_arq18` |
| `qe_i13` | `QE_I13` | texto | Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. (. = Sem resposta) | A = Nenhum, pois meu curso é gratuito; B = Nenhum, embora meu curso não seja gratuito; C = ProUni integral; D = ProUni parcial, apenas; E = FIES, apenas; F = ProUni Parcial e FIES; G = Bolsa oferecida por governo estadual, distrital ou municipal; … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq19` |
| `ano_fim_em` | `ANO_FIM_EM` | texto | Ano de conclusão do Ensino Médio (AAAA, conforme lançado pelo estudante) | — | todo | `microdados_enade_arq2` |
| `ano_in_grad` | `ANO_IN_GRAD` | texto | Ano de início da graduação (AAAA, conforme lançado pelo estudante) | — | todo | `microdados_enade_arq2` |
| `co_turno_graduacao` | `CO_TURNO_GRADUACAO` | texto | Código do turno de graduação cursado pelo estudante | 1 = Matutino; 2 = Vespertino; 3 = Integral; 4 = Noturno | todo | `microdados_enade_arq2` |
| `qe_i14` | `QE_I14` | texto | Algum fator dificultou sua permanência no ensino superior? (. = Sem resposta) | A = Não tive dificuldades; B = Falta de recursos financeiros para pagar mensalidades; C = Falta de recursos financeiros para se manter estudando; D = Falta de recursos financeiros para comprar material e/ou equipamentos requeridos pelo curso; … (lista completa no dicionário da fonte) | todo | `microdados_enade_arq20` |
| `qe_i15` | `QE_I15` | texto | Ao longo da sua trajetória acadêmica, você recebeu algum tipo de auxílio permanência? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. (. = Sem resposta) | A = Nenhum; B = Auxílio moradia; C = Auxílio alimentação; D = Auxílio moradia e alimentação; E = Auxílio permanência; F = Outro tipo de auxílio | todo | `microdados_enade_arq21` |
| `qe_i16` | `QE_I16` | texto | Ao longo da sua trajetória acadêmica, você recebeu algum tipo de bolsa acadêmica? (Você pode marcar quantas alternativas considerar necessário). (. = Sem resposta) | A = Nenhum; B = Bolsa de iniciação científica; C = Bolsa de extensão; D = Bolsa de monitoria/tutoria; E = Bolsa PET; F = Bolsa PIBID; G = Bolsa Residência Pedagógica; H = Outro tipo de bolsa acadêmica | todo | `microdados_enade_arq22` |
| `qe_i17` | `QE_I17` | texto | Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula? (. = Sem resposta) | A = Nenhuma, apenas assisto às aulas; B = De uma a três; C = De quatro a sete; D = De oito a doze; E = Mais de doze | todo | `microdados_enade_arq23` |
| `in_uso_enare` | `IN_USO_ENARE` | texto | Opção por utilizar os resultados no Enamed para fins do Enare | 0 = Não; 1 = Sim | todo | `microdados_enade_arq3` |
| `nu_ano_curso` | `NU_ANO_CURSO` | texto | Ano de conclusão do curso (AAAA, conforme lançado pelo coordenador do curso) | — | todo | `microdados_enade_arq3` |
| `in_semestre_curso` | `IN_SEMESTRE_CURSO` | texto | Semestre de conclusão do curso (A, conforme lançado pelo coordenador do curso) | — | todo | `microdados_enade_arq3` |
| `qe_i18` | `QE_I18` | texto | Foram oferecidas oportunidades para os estudantes participarem de programas, projetos ou atividades de extensão universitária. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i19` | `QE_I19` | texto | Foram oferecidas oportunidades para os estudantes participarem de projetos de iniciação científica e/ou de atividades que estimularam a investigação acadêmica. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i20` | `QE_I20` | texto | As atividades realizadas durante seu trabalho de conclusão de curso contribuíram para qualificar sua formação profissional. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i21` | `QE_I21` | texto | As relações professor-aluno ao longo do curso foram positivas, estimulando os estudantes a estudar e aprender. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i22` | `QE_I22` | texto | Os professores apresentaram e discutiram os planos de ensino/curso das disciplinas com os estudantes. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i23` | `QE_I23` | texto | As referências bibliográficas indicadas pelos professores contribuíram para seus estudos e aprendizagens.. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i24` | `QE_I24` | texto | As avaliações da aprendizagem realizadas durante o curso foram compatíveis com os conteúdos ou temas trabalhados pelos professores. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i25` | `QE_I25` | texto | Os professores demonstraram domínio dos conteúdos abordados nas disciplinas. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i26` | `QE_I26` | texto | Os professores utilizaram estratégias e instrumentos de avaliação diversificados (provas, seminários, trabalhos em grupo, portfólio, autoavaliação etc.) (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i27` | `QE_I27` | texto | Os professores ofereceram devolutivas das avaliações (comentários, explicações, sugestões para melhoria) que auxiliaram os estudantes a avançar em suas aprendizagens. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i28` | `QE_I28` | texto | Os professores estimularam a participação ativa dos estudantes durante as aulas (por meio de atividades em grupo, discussões, seminários etc.) não se limitando às aulas expositivas. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i29` | `QE_I29` | texto | O curso disponibilizou quantidade suficiente de professores e preceptores para auxiliar os estudantes. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i30` | `QE_I30` | texto | As atividades práticas de ensino contemplaram a quantidade adequada de equipamentos em relação aos estudantes. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i31` | `QE_I31` | texto | Foram oferecidas oportunidades para os estudantes superarem dificuldades relacionadas ao processo de formação. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i32` | `QE_I32` | texto | A coordenação do curso esteve disponível para orientação acadêmica dos estudantes. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i33` | `QE_I33` | texto | O curso favoreceu a articulação do conhecimento teórico com atividades práticas. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i34` | `QE_I34` | texto | O curso propiciou acesso a conhecimentos atualizados e/ou contemporâneos em sua área de formação. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i35` | `QE_I35` | texto | As disciplinas cursadas contribuíram para sua formação como profissional. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i36` | `QE_I36` | texto | As metodologias de ensino utilizadas no curso desafiaram você a se posicionar mais criticamente diante do conhecimento. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i37` | `QE_I37` | texto | Os estudantes participaram de avaliações periódicas das condições de formação (disciplinas, atuação dos professores, infraestrutura). (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i38` | `QE_I38` | texto | O curso proporcionou condições de acesso adequado às bibliografias indicadas nas disciplinas, de forma física ou virtual. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i39` | `QE_I39` | texto | As salas de aula apresentaram tamanho, mobiliário e recursos tecnológicos adequados. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i40` | `QE_I40` | texto | Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso e à quantidade de estudantes. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i41` | `QE_I41` | texto | Os laboratórios de habilidades e simulação de atividade assistencial permitiram a capacitação dos estudantes nas diversas competências desenvolvidas nas diferentes fases do curso. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i42` | `QE_I42` | texto | Foram realizadas simulações de alta fidelidade em diferentes etapas do curso. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i43` | `QE_I43` | texto | A integração do curso com o sistema de saúde viabilizou a formação do estudante em serviço, conforme necessidades locais e regionais. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i44` | `QE_I44` | texto | Integrar conhecimentos básicos e clínicos na atenção integral à saúde de indivíduos e comunidades, considerando os princípios do SUS. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i45` | `QE_I45` | texto | Realizar o cuidado em saúde com base em práticas éticas, humanizadas e orientadas para a promoção, prevenção, recuperação e reabilitação da saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i46` | `QE_I46` | texto | Utilizar evidências científicas para fundamentar a tomada de decisão clínica e terapêutica, em diferentes níveis de atenção à saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i47` | `QE_I47` | texto | Vivenciar a formação a partir de metodologias ativas, como aprendizagem baseada em problemas (PBL) e simulação. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i48` | `QE_I48` | texto | Praticar medicina por meio de estágios supervisionados em diferentes níveis de atenção à saúde (primária, secundária e terciária), articulados às redes públicas de saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i49` | `QE_I49` | texto | Praticar medicina por meio de estágios supervisionados em diferentes níveis de atenção à saúde (primária, secundária e terciária), articulados às redes privadas de saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i50` | `QE_I50` | texto | Estabelecer comunicação efetiva com usuários do sistema de saúde, familiares, equipes de saúde e a comunidade, respeitando aspectos éticos e culturais. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i51` | `QE_I51` | texto | Atuar em equipes multiprofissionais de saúde de forma colaborativa, por meio de vivências em educação interprofissional (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i52` | `QE_I52` | texto | Utilizar recursos tecnológicos e de informação em saúde de maneira crítica, ética e segura. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i53` | `QE_I53` | texto | Desenvolver habilidades de liderança, resolução de conflitos e gestão de processos de trabalho em saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i54` | `QE_I54` | texto | Refletir continuamente sobre a minha formação, buscando atualização permanente e compromisso com a qualidade do cuidado em saúde. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i55` | `QE_I55` | texto | Relacionar as atividades práticas de ensino ao contexto de saúde e bem-estar local e regional. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i56` | `QE_I56` | texto | Desenvolver competências práticas relacionadas a ações de atenção à saúde e ao bem-estar social, em uma perspectiva de integralidade, tanto individual quanto coletiva. (. = Sem resposta) | 1 = Discordo totalmente; 2 = Discordo; 3 = Discordo parcialmente; 4 = Concordo parcialmente; 5 = Concordo; 6 = Concordo totalmente; 7 = Não sei responder; 8 = Não se aplica | todo | `microdados_enade_arq4` |
| `qe_i57` | `QE_I57` | texto | Em uma escala de 0 a 10, o quanto você recomendaria o seu curso para um amigo ou colega? (1 a 10; . = Sem resposta) | — | todo | `microdados_enade_arq4` |
| `qe_i58` | `QE_I58` | texto | Em uma escala de 0 a 10, o quanto você recomendaria a sua Instituição de Educação Superior para um amigo ou colega? (1 a 10; . = Sem resposta) | — | todo | `microdados_enade_arq4` |
| `qe_i01` | `QE_I01` | texto | Qual o seu estado civil? (. = Sem resposta) | A = Solteiro(a); B = Casado(a) ou vivendo em união estável; C = Separado(a) judicialmente/divorciado(a); D = Viúvo(a); E = Outro | todo | `microdados_enade_arq7` |
| `qe_i02` | `QE_I02` | texto | Você tem filhos? (. = Sem resposta) | A = Não; B = Sim, 1 filho; C = Sim, 2 filhos; D = Sim, 3 filhos ou mais | todo | `microdados_enade_arq8` |
| `qe_i03` | `QE_I03` | texto | Qual é a sua cor ou raça? (. = Sem resposta) | A = Branca; B = Preta; C = Amarela; D = Parda; E = Indígena; F = Não quero declarar | todo | `microdados_enade_arq9` |

## No lake

- Dataset `inep/enamed`, particionado por `ano` (única partição: 2025); um Parquet por TXT, no padrão `enamed-microdados_2025__microdados_enade_2025_arq<N>.parquet`, `enamed-microdados_2025__microdados_demais_part_2025_arq<N>.parquet` e `enamed-microdados_2025__microdados2025_parametros_itens.parquet`.
- Todas as colunas são texto, com os nomes normalizados (minúsculas). Em todos os arquivos de dados a coluna `NU_ANO` aparece como `inu_ano` (veja Cuidados de uso).
- A coluna `ano` é a edição, tirada do nome do arquivo.

## Cuidados de uso

- **A coluna de ano se chama `inu_ano`.** Os 36 TXT de dados começam com a marca de ordem de bytes UTF-8 (BOM), que o conversor lê como latin-1 e junta ao primeiro nome de coluna; `NU_ANO` vira `inu_ano` em todos os arquivos, e não existe coluna `nu_ano` no lake. Use `ano` (a partição) ou `inu_ano`; o dicionário da fonte não conhece esse nome.
- **Não há ligação entre arquivos por participante, e a chave do dataset fica vazia.** Entre os concluintes, só `co_curso` liga os arquivos (e cada linha de um casa com várias do outro no mesmo curso: agregue por curso antes de juntar). Entre os demais participantes só há `inu_ano`, igual para todos, e nada liga os arquivos.
- **Presença e notas.** `tp_pres` na fonte: concluintes, 555 (presente com resultado válido) em 39.257 linhas, 222 (ausente) em 517 e 334 (eliminado) em 20; demais participantes, 555 em 49.783, 222 em 7.021 e 334 em 29. O manual diz que `proficiencia` e `nt_ger` ficam em branco para ausentes e eliminados. Filtre `tp_pres` = 555 antes de calcular desempenho.
- **Dois públicos nas mesmas colunas.** `co_caderno`, `tp_pres`, `proficiencia`, `nt_ger`, `tp_sexo` e `nu_idade` existem nos dois conjuntos de arquivos (a coluna *Arquivos* mostra a origem); some só dentro de cada público. Cuidado com `tp_inscricao` (1 concluinte, 2 demais participantes) ao empilhar `arq3` dos concluintes e `arq1` dos demais participantes.
- **Decimais com ponto e vazios de dois tipos.** Ao contrário do Enade das Licenciaturas e da PND, o Enamed usa ponto decimal (por exemplo, `2.900` e `-3.655`). O manual manda ler os valores faltantes numéricos como `.` e os de caractere como vazio.
- **Questionário de percepção de prova e acertos por área.** `qt_acerto_area_1` a `5` e `per_acerto_enare` têm a classificação em cinco áreas do Enare, não as áreas da matriz do Enamed. `ds_vt_ace_obj` deve ser lido como texto (vetor de 100 posições).
- **Dados pessoais.** Os arquivos trazem sexo, idade, cor ou raça, deficiência, estado civil, filhos, renda e escolaridade da família, ações afirmativas e bolsas (concluintes) e, para os demais participantes, também a trajetória profissional (tempo de formado, trabalho, carga horária e esferas de atuação pretendidas), sem nome ou identificador. Cursos com menos de dois estudantes com resultado válido ou menos de dois respondentes dos questionários foram excluídos pelo Inep. Evite recortes com poucos casos.
- **Arquivo temporário no ZIP.** O ZIP traz o arquivo de bloqueio `~$Dicionário_arquivos_variáveis_microdados_Enamed_2025.xlsx` (165 bytes), que não é uma planilha válida e não foi convertido para o lake.
- **Uma edição só.** O lake tem apenas 2025.

## Exemplos

Número de concluintes de Medicina por tipo de presença (`tp_pres`) no arquivo de prova e resultados, com a média de acertos na área 1 (Clínica Médica) dos presentes. Na amostra do lake, o arquivo tem só as primeiras 1.500 linhas:

```python
import duckdb

duckdb.sql("""
    SELECT tp_pres, count(*) AS participantes,
           round(avg(try_cast(qt_acerto_area_1 AS DOUBLE)), 1) AS media_acertos_clinica_medica
    FROM read_parquet('lake/inep/enamed/ano=2025/*microdados_enade_2025_arq3.parquet')
    GROUP BY tp_pres
    ORDER BY tp_pres
""").show()
```

## Referências

- Microdados do Enamed: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enamed
- Manual do usuário, questionários e dicionário de arquivos e variáveis, dentro do ZIP em https://download.inep.gov.br/microdados/microdados_enamed_2025.zip
