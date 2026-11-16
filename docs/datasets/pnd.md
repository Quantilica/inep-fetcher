---
dataset:
  id: pnd
  fonte: inep
  titulo: PND 2025 — Prova Nacional Docente (microdados)
  resumo: 'Microdados da Prova Nacional Docente 2025: resultados e questionário dos concluintes de licenciatura do Enade e dos demais participantes graduados em licenciatura, em 13 arquivos.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pnd
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; a edição de 2025 é a primeira (prova aplicada em 26/10/2025 e reaplicada em 30/11/2025)
  cobertura:
    inicio: '2025'
    fim: '2025'
  unidade: um participante inscrito na PND 2025, em cada arquivo, sem ligação entre arquivos; na tabela de parâmetros, um item de prova por área
  granularidade:
    espacial: área de avaliação (`co_grupo`), com município e UF do local de prova
    temporal: ano da edição (2025)
  formato_bruto: RAR (a URL do catálogo, com extensão .zip, não existe; a fonte publica .rar) com as pastas 1.LEIA-ME (manual, questionário contextual em PDF, dicionário em xlsx e ods) e 2.DADOS (13 TXT com ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em xlsx e ods)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 48
  unidades_de_medida:
    NU_ITEM_PROVA_1: número do item (sem unidade)
    NU_ITEM_PROVA_2: número do item (sem unidade)
    NU_ITEM_PROVA_3: número do item (sem unidade)
    NU_ITEM_PROVA_4: número do item (sem unidade)
    ITEM_MANTIDO: indicador 0 ou 1
    COR_BISSERIAL: correlação (de -1 a 1)
    PARAMETRO_B: parâmetro de dificuldade na escala da TRI
    INFIT: estatística de ajuste (sem unidade)
    OUTFIT: estatística de ajuste (sem unidade)
    CO_GRUPO: código da área (sem unidade)
  dados_pessoais:
  - coluna: tp_sexo
    categoria: sexo do participante
  - coluna: nu_idade
    categoria: idade do participante (da base da Receita Federal)
  - coluna: nu_questao_01
    categoria: estado civil
  - coluna: nu_questao_02
    categoria: cor ou raça declarada
  - coluna: nu_questao_03
    categoria: deficiência, transtorno global do desenvolvimento ou altas habilidades
  - coluna: nu_questao_04
    categoria: renda familiar
  - coluna: nu_questao_07
    categoria: escolaridade, trabalho e experiência como professor
  - coluna: nu_questao_08
    categoria: escolaridade, trabalho e experiência como professor
  - coluna: nu_questao_09
    categoria: escolaridade, trabalho e experiência como professor
  - coluna: nu_questao_05
    categoria: escolaridade, trabalho e experiência como professor
  - coluna: nu_questao_06
    categoria: escolaridade, trabalho e experiência como professor
  - coluna: co_municipio_prova
    categoria: local de prova do participante
  - coluna: sg_uf_municipio_prova
    categoria: local de prova do participante
  - coluna: ds_vt_gab_obj
    categoria: desempenho individual do participante na prova
  - coluna: ds_vt_esc_obj
    categoria: desempenho individual do participante na prova
  - coluna: ds_vt_ace_obj
    categoria: desempenho individual do participante na prova
  - coluna: proficiencia
    categoria: desempenho individual do participante na prova
  - coluna: nt_obj
    categoria: desempenho individual do participante na prova
  - coluna: nt_dis
    categoria: desempenho individual do participante na prova
  - coluna: nt_ger
    categoria: desempenho individual do participante na prova
  - coluna: qt_acertos
    categoria: desempenho individual do participante na prova
  eras:
  - desde: '2025'
    mudanca: primeira edição da PND; versão original dos microdados de 04/05/2026, com revisões do manual em 25/05/2026 e 09/09/2026
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# PND 2025 — Prova Nacional Docente (microdados)

## Resumo

Microdados da Prova Nacional Docente (PND), exame anual do Ministério da Educação e do Inep, instituído em 2025 como um dos eixos do Programa Mais Professores (Decreto nº 12.358, de 14/01/2025), para auxiliar estados e municípios a selecionar professores para as suas redes. A PND de 2025 usou as matrizes e os instrumentos da avaliação teórica do Enade das Licenciaturas, em 17 áreas, e tem dois públicos: os concluintes de licenciatura participantes do Enade das Licenciaturas e os demais participantes, graduados em licenciatura. Por exigência da LGPD, os dados vêm em 13 arquivos ordenados por variáveis diferentes, ligados só pela área (`co_grupo`); o desempenho e as respostas ao Questionário Contextual de um mesmo participante não podem ser ligados.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/pnd` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pnd |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; a edição de 2025 é a primeira (prova aplicada em 26/10/2025 e reaplicada em 30/11/2025) |
| Cobertura | 2025 a 2025 |
| Unidade (uma linha) | um participante inscrito na PND 2025, em cada arquivo, sem ligação entre arquivos; na tabela de parâmetros, um item de prova por área |
| Granularidade | espacial: área de avaliação (`co_grupo`), com município e UF do local de prova; temporal: ano da edição (2025) |
| Formato bruto | RAR (a URL do catálogo, com extensão .zip, não existe; a fonte publica .rar) com as pastas 1.LEIA-ME (manual, questionário contextual em PDF, dicionário em xlsx e ods) e 2.DADOS (13 TXT com ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em xlsx e ods) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 48 |
| Unidades de medida | `NU_ITEM_PROVA_1`: número do item (sem unidade); `NU_ITEM_PROVA_2`: número do item (sem unidade); `NU_ITEM_PROVA_3`: número do item (sem unidade); `NU_ITEM_PROVA_4`: número do item (sem unidade); `ITEM_MANTIDO`: indicador 0 ou 1; `COR_BISSERIAL`: correlação (de -1 a 1); `PARAMETRO_B`: parâmetro de dificuldade na escala da TRI; `INFIT`: estatística de ajuste (sem unidade); `OUTFIT`: estatística de ajuste (sem unidade); `CO_GRUPO`: código da área (sem unidade) |
| Dados pessoais | `tp_sexo` (sexo do participante); `nu_idade` (idade do participante (da base da Receita Federal)); `nu_questao_01` (estado civil); `nu_questao_02` (cor ou raça declarada); `nu_questao_03` (deficiência, transtorno global do desenvolvimento ou altas habilidades); `nu_questao_04` (renda familiar); `nu_questao_07` (escolaridade, trabalho e experiência como professor); `nu_questao_08` (escolaridade, trabalho e experiência como professor); `nu_questao_09` (escolaridade, trabalho e experiência como professor); `nu_questao_05` (escolaridade, trabalho e experiência como professor); `nu_questao_06` (escolaridade, trabalho e experiência como professor); `co_municipio_prova` (local de prova do participante); `sg_uf_municipio_prova` (local de prova do participante); `ds_vt_gab_obj` (desempenho individual do participante na prova); `ds_vt_esc_obj` (desempenho individual do participante na prova); `ds_vt_ace_obj` (desempenho individual do participante na prova); `proficiencia` (desempenho individual do participante na prova); `nt_obj` (desempenho individual do participante na prova); `nt_dis` (desempenho individual do participante na prova); `nt_ger` (desempenho individual do participante na prova); `qt_acertos` (desempenho individual do participante na prova) |
| Eras | 2025: primeira edição da PND; versão original dos microdados de 04/05/2026, com revisões do manual em 25/05/2026 e 09/09/2026 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- **O catálogo do fetcher tem a URL errada.** O catálogo pede `https://download.inep.gov.br/microdados/microdados_pnd_2025.zip`, que responde 404 (conferido em 2026-11-15). A página oficial publica `https://download.inep.gov.br/microdados/microdados_pnd_2025.rar` (RAR, 44.084.875 bytes; última modificação na fonte em 2026-09-09; a página diz "Arquivo atualizado em 09/09/2026"), que responde 200. A amostra do lake desta documentação foi obtida desse RAR.
- No bruto, o arquivo se chamaria `pnd/pnd-microdados_2025@AAAAMMDD.<extensão>`, em que o sufixo é a data de modificação na fonte; como o fetcher parte da URL .zip, o download previsto hoje não se completa.
- O RAR tem `Microdados_PND_2025/1.LEIA-ME` (manual do usuário de 09/09/2026, `QUESTIONARIO_CONTEXTUAL_PND.pdf` e o dicionário de arquivos e variáveis em xlsx e ods, cujo nome traz a data "09-09-2029", provável erro de ano) e `2.DADOS` com `microdados2025_pnd_arq1.txt` a `arq13.txt` e `microdados2025_parametros_itens` em xlsx e ods. O arquivo `arq1` tem 371.539.465 bytes descompactado; os demais, entre 15,0 e 16,1 MB.
- Cada um dos 13 TXT tem 1.087.359 linhas de dados (conferido na fonte em 2026-11-15).
- O histórico de alterações do manual registra a versão original de 04/05/2026; em 25/05/2026, a padronização do texto das categorias de `DS_VT_GAB_OBJ` e `DS_VT_ACE_OBJ` e a correção da descrição das categorias de `NU_QUESTAO_04` e `TP_INSCRICAO_PND`; e, em 09/09/2026, a descrição da estrutura de `DS_VT_ACE_OBJ`.

## Conteúdo

- **Dois públicos.** Segundo o manual, a PND é composta por dois públicos: os estudantes concluintes que fizeram a avaliação teórica do Enade das Licenciaturas e os demais participantes, graduados em licenciatura. A coluna `tp_inscricao_pnd` diz o perfil: 1 = concluinte do Enade, 2 = demais participantes e 3 = concluinte do Enade que optou por fazer a prova em outra área. Contagens na fonte: 283.015 concluintes (1), 794.251 demais participantes (2) e 10.093 concluintes que mudaram de área (3).
- **Questionários.** Os concluintes respondem ao Questionário do Estudante, cujas respostas estão nos microdados do Enade das Licenciaturas, não aqui. Os demais participantes respondem ao Questionário Contextual (perfil socioeconômico, experiência docente e interesse na PND), cujas respostas estão nestes microdados (`nu_questao_01` a `nu_questao_10`). Todos podem responder ao Questionário de Percepção de Prova (`co_rs_i1` a `co_rs_i9`).
- **Áreas.** 17 áreas, como as do Enade das Licenciaturas: Artes Visuais, Ciências Biológicas, Ciência da Computação, Ciências Sociais, Educação Física, Filosofia, Física, Geografia, História, Letras (Português, Português e Espanhol, Português e Inglês, Inglês), Matemática, Música, Pedagogia e Química.
- **Por que há 13 arquivos.** Para atender à LGPD, os dados vêm em arquivos distintos, ordenados por variáveis diferentes; só é possível agrupá-los por `co_grupo`, e não por participante. Os resultados de concluintes de cursos com um único participante com presença válida foram excluídos (também dos microdados do Enade das Licenciaturas).
- **O que é cada `arqN`:**

| Arquivo | Conteúdo (do dicionário de arquivos do Inep) | Colunas |
|---|---|---|
| `microdados2025_pnd_arq1` | área, município e UF do local de prova, perfil do participante, reaplicação, caderno, vetores, presença, situação na parte discursiva, proficiência, notas, acertos e respostas do Questionário de Percepção de Prova | `nu_ano`, `co_grupo`, `co_municipio_prova`, `sg_uf_municipio_prova`, `tp_inscricao_pnd`, `in_reaplicacao`, `co_caderno` a `co_rs_i9` (26 colunas) |
| `arq2` | sexo | `tp_sexo` |
| `arq3` | idade no dia da prova | `nu_idade` |
| `arq4` a `arq13` | uma questão do Questionário Contextual por arquivo, na ordem (`arq4` é `nu_questao_01`, `arq5` é `nu_questao_02` e assim até `arq13`, que é `nu_questao_10`): estado civil, cor ou raça, deficiência, renda, tempo desde a conclusão da licenciatura, escolaridade, trabalho atual, experiência como professor, carga horária semanal e interesse em participar da PND | `nu_questao_01` a `nu_questao_10` |
| `parametros_itens` | tabela de parâmetros dos itens por área (`CO_GRUPO`): número do item em cada caderno, se foi mantido, correlação bisserial, parâmetro de dificuldade e ajustes INFIT e OUTFIT | colunas em maiúsculas |

- A pesquisa individualizada só é possível pelo Serviço de Acesso a Dados Protegidos (Sedap) do Inep, segundo o manual.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2025 | 14 arquivos, de 3 a 26 colunas |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx), aba `DICIONÁRIO_DE_VARIAVÉIS`; a tabela de parâmetros dos itens não tem dicionário nesta edição (as descrições de suas colunas são as do dicionário do Enamed, que traz a mesma tabela, e as colunas estão em maiúsculas no lake).
A coluna *Arquivos* indica em qual arquivo `arqN` do lake a coluna aparece; `nu_ano` e `co_grupo` estão em todos os arquivos de `arq1` a `arq13`. As respostas do Questionário Contextual são letras (A, B, …); `.` marca "sem resposta".

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `CO_GRUPO` | `CO_GRUPO` | inteiro | Código da área de enquadramento na PND, na tabela de parâmetros dos itens (coluna em maiúsculas, distinta de `co_grupo`); não consta do dicionário desta edição | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_1` | `NU_ITEM_PROVA_1` | inteiro | Número do item na prova 1 (caderno 1) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_2` | `NU_ITEM_PROVA_2` | inteiro | Número do item na prova 2 (caderno 2) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_3` | `NU_ITEM_PROVA_3` | inteiro | Número do item na prova 3 (caderno 3); a numeração dos cadernos segue a coluna de mesmo nome (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_4` | `NU_ITEM_PROVA_4` | inteiro | Número do item na prova 4 (caderno 4); a numeração dos cadernos segue a coluna de mesmo nome (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `ITEM_MANTIDO` | `ITEM_MANTIDO` | inteiro | Indica se o item foi mantido no cálculo (1 = sim, 0 = não) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `COR_BISSERIAL` | `COR_BISSERIAL` | decimal | Correlação bisserial do item (de -1 a 1) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `PARAMETRO_B` | `PARAMETRO_B` | decimal | Parâmetro de dificuldade do item na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `INFIT` | `INFIT` | decimal | Estatística de ajuste INFIT na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `OUTFIT` | `OUTFIT` | decimal | Estatística de ajuste OUTFIT na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário da PND não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `nu_ano` | `NU_ANO` | texto | Ano de realização do exame (2025) | — | todo | `microdados_pnd_arq1`, `microdados_pnd_arq10`, `microdados_pnd_arq11` e mais 10 |
| `co_grupo` | `CO_GRUPO` | texto | Código da Área da prova de enquadramento do curso no Enade | 702 = MATEMÁTICA (LICENCIATURA); 904 = LETRAS - PORTUGUÊS (LICENCIATURA); 905 = LETRAS -PORTUGUÊS E INGLÊS (LICENCIATURA); 906 = LETRAS - PORTUGUÊS E ESPANHOL (LICENCIATURA); 1402 = FÍSICA (LICENCIATURA); 1502 = QUÍMICA (LICENCIATURA); … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq1`, `microdados_pnd_arq10`, `microdados_pnd_arq11` e mais 10 |
| `co_municipio_prova` | `CO_MUNICIPIO_PROVA` | texto | Código do município do local de prova (Entre 1100015 e 5300108 (Identificação do Município conforme IBGE - Ir para Planilha MUNICÍPIOS)) | — | todo | `microdados_pnd_arq1` |
| `sg_uf_municipio_prova` | `SG_UF_MUNICIPIO_PROVA` | texto | Sigla da UF do município do local de prova (Conforme código do IBGE; Rondônia (RO); Acre (AC); Amazonas (AM); Roraima (RR); Pará (PA); Amapa (AP); Tocantins (TO); Maranhão (MA); Piauí (PI); Ceará (CE); Rio Grande do Norte (RN); Paraíba (PB); Pernambuco (PE); Alagoas (AL); Sergipe (SE); Bahia (BA); Minas gerais (MG); Espírito Santo (ES); Rio de Janeiro (RJ); São Paulo (SP); Paraná (PR); Santa Catarina (SC); Rio Grande do Sul (RS); Mato Grosso do Sul (MS); Mato Grosso (MT); Goiás (GO); Distrito federal (DF)) | — | todo | `microdados_pnd_arq1` |
| `tp_inscricao_pnd` | `TP_INSCRICAO_PND` | texto | Perfil de participante na PND (Identifica a origem da inscrição do estudante no PROVA_DOCENTE.Valores possíveis:) | 1 = Concluinte Enade; 2 = Demais Participantes; 3 = Concluinte Enade que optou por realizar a prova em outra área, diferente da inscrição no Enade. | todo | `microdados_pnd_arq1` |
| `in_reaplicacao` | `IN_REAPLICACAO` | texto | Indicação da prova válida para o inscrito: aplicação ou reaplicação | 0 = Participante que fez a prova no dia da aplicação - 26/10/2025; 1 = Participante que fez a prova no dia da reaplicação - 30/11/2025 | todo | `microdados_pnd_arq1` |
| `co_caderno` | `CO_CADERNO` | texto | Código do caderno (Códigos dos cadernos 1 a 4 referentes a aplicação e código do caderno 5 à reaplicação) | 1 = Caderno 1; 2 = Caderno 2; 3 = Caderno 3; 4 = Caderno 4; 5 = Caderno 5 | todo | `microdados_pnd_arq1` |
| `ds_vt_gab_obj` | `DS_VT_GAB_OBJ` | texto | Vetor que representa o gabarito final da prova. (1 letra por item (intervalo de A a D)) | 6 = Questão anulada pela Comissão Assessora de Área | todo | `microdados_pnd_arq1` |
| `ds_vt_esc_obj` | `DS_VT_ESC_OBJ` | texto | Vetor que representa a escolha de resposta da prova. A ordem das questões está de acordo ordem de caderno, consultar variável CO_CADERNO. (1 letra por item (intervalo de A a D)) | . = em branco; * = múltiplo | todo | `microdados_pnd_arq1` |
| `ds_vt_ace_obj` | `DS_VT_ACE_OBJ` | texto | Vetor que representa os acertos da prova, a variável representa o vetor de acertos rotacionados, tendo como base a sequência das questões do Caderno 1. | 0 = Errado; 1 = Certo; 4 = Eliminado; 6 = Questão anulada pela Comissão Assessora de Área; 8 = Questão desconsiderada estatísticamente; 9 = Ausente | todo | `microdados_pnd_arq1` |
| `tp_pres` | `TP_PRES` | texto | Tipo de presença na prova | 222 = Ausente; 334 = Eliminado por participação indevida; 444 = Ausente devido a múltiplas inscrições; 555 = Presente com resultado válido; 888 = Presente na prova, com resultado desconsiderado pelo Inep | todo | `microdados_pnd_arq1` |
| `tp_sit_disc` | `TP_SIT_DISC` | texto | Tipo de situação na parte discursiva (Nota: (*) resultado considerado para o cálculo da nota do estudante;; (**) resultado desconsiderado para o cálculo da nota do estudante.) | 222 = Não se aplica (estudante ausente)**; 333 = Questão em branco - estudante presente (nota=zero)*; 335 = Questão zerada por motivo de resposta nula (nota=zero)*; 336 = Questão com resposta divergente da temática (nota=zero)*; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq1` |
| `proficiencia` | `PROFICIENCIA` | texto | Proficiência da TRI na prova objetiva (valor de theta) (Min = -9,999; Max = 9,999; Se TP_PRES = 222 ou 334, então = .) | — | todo | `microdados_pnd_arq1` |
| `nt_obj` | `NT_OBJ` | texto | Nota da prova objetiva (Min = 0,00; Max = 100,00; Se TP_PRES = 222 ou 334, então = .) | — | todo | `microdados_pnd_arq1` |
| `nt_dis` | `NT_DIS` | texto | Nota final da questão discursiva (Min = 0,00; Max = 10,00; Se TP_PRES = 222 ou 334, então = .) | — | todo | `microdados_pnd_arq1` |
| `nt_ger` | `NT_GER` | texto | Nota Geral na PND (objetiva x 0,8 + 2x discursiva) (Min = 0,0; Max = 100,0; Se TP_PRES = 222 ou 334, então = .) | — | todo | `microdados_pnd_arq1` |
| `qt_acertos` | `QT_ACERTOS` | texto | Quatidade de acertos na prova objetiva (Min = 0; Max = 80) | — | todo | `microdados_pnd_arq1` |
| `co_rs_i1` | `CO_RS_I1` | texto | Qual o grau de dificuldade das questões? (. = Sem resposta) | A = Muito fácil; B = Fácil; C = Médio; D = Difícil; E = Muito difícil; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i2` | `CO_RS_I2` | texto | Qual foi o tempo gasto por você para concluir a prova? (. = Sem resposta) | A = Menos de uma hora; B = Entre uma e duas horas; C = Entre três e quatro horas; D = Entre quatro e cinco horas; E = Cinco horas, e não consegui terminar; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i3` | `CO_RS_I3` | texto | Em relação ao tempo total de aplicação, você considera que a prova foi (. = Sem resposta) | A = Muito longa; B = Longa; C = Adequada; D = Curta; E = Muito curta; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i4` | `CO_RS_I4` | texto | Os enunciados das questões estavam claros e objetivos? (. = Sem resposta) | A = Sim, todos; B = Sim, a maioria; C = Apenas cerca da metade; D = Poucos; E = Não, nenhum; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i5` | `CO_RS_I5` | texto | As informações/instruções fornecidas para a resolução das questões foram suficientes para resolvê-las? (. = Sem resposta) | A = Sim, até excessivas; B = Sim, em todas elas; C = Sim, na maioria delas; D = Sim, somente em algumas; E = Não, em nenhuma delas; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i6` | `CO_RS_I6` | texto | Você se deparou com alguma dificuldade ao responder à prova? Qual? (. = Sem resposta) | A = Desconhecimento do conteúdo; B = Forma diferente de abordagem do conteúdo; C = Espaço insuficiente para responder às questões; D = Falta de motivação para fazer a prova; E = Não tive qualquer tipo de dificuldade para responder à prova; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `co_rs_i7` | `CO_RS_I7` | texto | Considerando as questões da prova, você percebeu que (. = Sem resposta) | A = Não estudou ainda a maioria desses conteúdos; B = Estudou alguns desses conteúdos, mas não os aprendeu; C = Estudou a maioria desses conteúdos, mas não os aprendeu; D = Estudou e aprendeu muitos desses conteúdos; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq1` |
| `co_rs_i8` | `CO_RS_I8` | texto | Como você avalia a sequência das questões na prova? (. = Sem resposta) | A = A sequência não interferiu nas minhas respostas; B = Preferiria a sequência por área; C = Preferiria a sequência por grau de dificuldade; D = A sequência dificultou meu raciocínio durante a prova; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq1` |
| `co_rs_i9` | `CO_RS_I9` | texto | As atividades práticas desenvolvidas ao longo do seu curso contribuíram para a resolução das questões dessa prova? (. = Sem resposta) | A = Sim; B = Não; * = Resposta anulada | todo | `microdados_pnd_arq1` |
| `nu_questao_07` | `NU_QUESTAO_07` | texto | Você está trabalhando atualmente? (. = Sem resposta) | A = Não; B = Sim, mas não na minha área de formação; C = Sim, na minha área de formação | todo | `microdados_pnd_arq10` |
| `nu_questao_08` | `NU_QUESTAO_08` | texto | Quanto tempo de experiência como professor(a) você possui? (. = Sem resposta) | A = Entre 1 e 2 anos; B = Entre 3 e 5 anos; C = Entre 6 e 10 anos; D = Mais de 10 anos; E = Menos de 1 ano; F = Nunca atuei como médico | todo | `microdados_pnd_arq11` |
| `nu_questao_09` | `NU_QUESTAO_09` | texto | Qual sua carga horária de trabalho semanal atualmente? (. = Sem resposta) | A = 20 horas semanais ou menos; B = 30 horas semanais; C = 40 horas semanais; D = Jornada de trabalho flexível de horários; E = Não estou trabalhando atualmente | todo | `microdados_pnd_arq12` |
| `nu_questao_10` | `NU_QUESTAO_10` | texto | Qual o seu interesse em participar da PND - 2025? (. = Sem resposta) | A = Quero ser professor da rede pública; B = Sou professor da rede pública e quero ampliar a carga horária na mesma rede de ensino; C = Sou professor da rede pública e quero atuar em rede de ensino de outro estado/município; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq13` |
| `tp_sexo` | `TP_SEXO` | texto | Sexo | M = Masculino; F = Feminino; 9 = Indefinido | todo | `microdados_pnd_arq2` |
| `nu_idade` | `NU_IDADE` | texto | Idade do inscrito em 26/10/2025 ( aplicação) Idade do inscrito em 30/11/2025 (reaplicação) (Dados provenientes da base da Receita Federal) | — | todo | `microdados_pnd_arq3` |
| `nu_questao_01` | `NU_QUESTAO_01` | texto | Qual o seu estado civil? (. = Sem resposta) | A = Casado (a) ou vivendo em união estável; B = Outro; C = Separado(a) judicialmente/divorciado(a); D = Solteiro(a); E = Viúvo(a) | todo | `microdados_pnd_arq4` |
| `nu_questao_02` | `NU_QUESTAO_02` | texto | Qual é a sua cor ou raça? (. = Sem resposta) | A = Amarela; B = Branca; C = Indígena; D = Não quero declarar; E = Parda; F = Preta | todo | `microdados_pnd_arq5` |
| `nu_questao_03` | `NU_QUESTAO_03` | texto | Você tem alguma deficiência, transtorno global do desenvolvimento ou altas habilidades? (Você pode marcar quantas alternativas considerar necessárias). (. = Sem resposta) | A = Altas habilidades/superdotação; B = Baixa Visão; C = Cegueira; D = Deficiência Auditiva; E = Deficiência Física; F = Deficiência Intelectual; G = Dislexia; H = Não possuo; I = Não quero declarar; J = Outras/outros; K = Surdez; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq6` |
| `nu_questao_04` | `NU_QUESTAO_04` | texto | Qual a renda total de sua família, incluindo seus rendimentos? (considere como família a sua unidade de origem composta por pessoas que possuem vínculos consanguíneos e/ou de parentesco, todas moradoras do mesmo domicílio). (. = Sem resposta) | A = Acima de 30 salários-mínimos (mais de R$ 45.540,00); B = Até 1,5 salário mínimo (até R$ 2.277,00); C = De 1,5 a 3 salários mínimos (R$ 2.277,00 a R$ 4.554,00); D = De 10 a 30 salários mínimos (R$ 15.180,00 a R$ 45.540,00); … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq7` |
| `nu_questao_05` | `NU_QUESTAO_05` | texto | Há quanto tempo você concluiu o curso de licenciatura? (. = Sem resposta) | A = Entre 1 e 2 anos; B = Entre 3 e 5 anos; C = Entre 6 e 10 anos; D = Mais de 10 anos; E = Menos de 1 ano | todo | `microdados_pnd_arq8` |
| `nu_questao_06` | `NU_QUESTAO_06` | texto | Qual é o mais alto nível de escolaridade que você concluiu? (. = Sem resposta) | A = Bacharelado em área específica; B = Doutorado; C = Ensino Médio - Magistério/Normal; D = Ensino médio Completo; E = Licenciatura em área específica; F = Licenciatura em área Pedagogia; G = Mestrado; H = Normal Superior; I = Pós-graduação lato sensu; … (lista completa no dicionário da fonte) | todo | `microdados_pnd_arq9` |

## No lake

- Dataset `inep/pnd`, particionado por `ano` (única partição: 2025); um Parquet por TXT, no padrão `pnd-microdados_2025__microdados2025_pnd_arq<N>.parquet`, mais `pnd-microdados_2025__microdados2025_parametros_itens.parquet`.
- Nos arquivos `arq1` a `arq13` as colunas são texto, com os nomes normalizados (minúsculas). A tabela de parâmetros dos itens é a exceção: o conversor a lê da planilha, mantém os nomes em maiúsculas e grava inteiros e decimais.
- A coluna `ano` é a edição, tirada do nome do arquivo; `nu_ano` é o ano dentro do dado.

## Cuidados de uso

- **A URL do catálogo não baixa.** `microdados_pnd_2025.zip` dá 404 na fonte, que publica `microdados_pnd_2025.rar` (RAR). Um leitor de ZIP não abre o RAR.
- **Não há ligação entre arquivos por participante, e a chave do dataset fica vazia.** A única coluna comum útil é `co_grupo` (a área); juntar dois `arqN` por ela multiplica as linhas por área (um produto cartesiano por área, sem sentido por participante). Agregue cada arquivo por área, e por `tp_inscricao_pnd` quando for o caso, antes de juntar.
- **Decimais com vírgula e `NA`.** O manual manda importar decimais com ponto e valores ausentes como aspas duplas, mas `proficiencia`, `nt_obj`, `nt_dis` e `nt_ger` vêm com vírgula nos TXT (por exemplo, `-2,46117`) e, para os ausentes, com o texto `NA`. Troque a vírgula por ponto e trate `NA` como nulo antes de converter.
- **Presença.** `tp_pres` na fonte: 555 (presente com resultado válido) em 760.106 linhas, 222 (ausente) em 325.879, 334 (eliminado por participação indevida) em 1.268, 444 (ausente por múltiplas inscrições) em 94 e 888 (presença com resultado desconsiderado pelo Inep) em 12. Os ausentes fazem parte do arquivo; filtre `tp_pres` = 555 antes de calcular desempenho.
- **Aplicação e reaplicação.** `in_reaplicacao` 1 marca quem fez a prova na reaplicação de 30/11/2025 (7.944 linhas) e `co_caderno` 5 é o caderno da reaplicação. O xlsx da tabela de parâmetros tem duas abas (aplicação, com 10 colunas, e reaplicação, com 4 colunas e `NU_ITEM_PROVA_5`), e o lake guarda só a primeira.
- **Nome das colunas da tabela de parâmetros.** Ficam em maiúsculas, e `CO_GRUPO` difere de `co_grupo` dos outros arquivos só pela caixa: ao unir os arquivos em um motor sem distinção de maiúsculas, as duas colidem.
- **Nota geral.** O dicionário descreve `nt_ger` como "objetiva x 0,8 + 2x discursiva"; o Enade das Licenciaturas, que usa o mesmo instrumento, descreve a nota como 80% da objetiva e 20% da discursiva. Confira antes de reproduzir a nota.
- **Dados pessoais.** Os arquivos trazem sexo, idade, cor ou raça, deficiência, estado civil, renda, escolaridade e experiência como professor, com município e UF do local de prova, sem nome ou identificador, em arquivos ordenados de forma diferente. Os concluintes do Enade só entram com as informações do Questionário do Estudante nos microdados do Enade das Licenciaturas. Evite recortes com poucos casos.
- **Uma edição só.** O lake tem apenas 2025.

## Exemplos

Número de participantes presentes com resultado válido (`tp_pres` 555) e nota geral média por perfil (`tp_inscricao_pnd`), no arquivo principal, com a vírgula decimal trocada por ponto. Na amostra do lake, o arquivo tem só as primeiras 1.500 linhas:

```python
import duckdb

duckdb.sql("""
    SELECT tp_inscricao_pnd AS perfil, count(*) AS participantes,
           round(avg(try_cast(replace(nt_ger, ',', '.') AS DOUBLE)), 1) AS nota_geral_media
    FROM read_parquet('lake/inep/pnd/ano=2025/*pnd_arq1.parquet')
    WHERE tp_pres = '555'
    GROUP BY ALL
    ORDER BY perfil
""").show()
```

## Referências

- Microdados da Prova Nacional Docente: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pnd
- Manual do usuário, questionário contextual e dicionário de arquivos e variáveis, dentro do RAR em https://download.inep.gov.br/microdados/microdados_pnd_2025.rar
