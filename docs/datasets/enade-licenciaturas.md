---
dataset:
  id: enade-licenciaturas
  fonte: inep
  titulo: Enade das Licenciaturas 2025 — microdados
  resumo: 'Microdados do Enade das Licenciaturas 2025: resultados da avaliação teórica e respostas ao Questionário do Estudante dos concluintes de licenciaturas, em 28 arquivos por tema.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade-das-licenciaturas
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; a edição de 2025 é a primeira do Enade das Licenciaturas (a prova de 2025 foi aplicada em 26/10/2025 e reaplicada em 30/11/2025)
  cobertura:
    inicio: '2025'
    fim: '2025'
  unidade: um estudante concluinte de licenciatura inscrito regularmente no Enade 2025, em cada arquivo, sem ligação entre arquivos; na tabela de parâmetros, um item de prova por área
  granularidade:
    espacial: curso (código do curso no Enade), com IES, município, UF e região do curso
    temporal: ano da edição (2025)
  formato_bruto: ZIP com as pastas 1.LEIA-ME (manual do usuário, Questionário do Estudante, dicionário em xlsx e ods) e 2.DADOS (28 TXT com ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em xlsx e ods)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 115
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
    categoria: sexo do estudante
  - coluna: nu_idade
    categoria: idade do estudante (da base da Receita Federal)
  - coluna: qe_i01
    categoria: estado civil
  - coluna: qe_i02
    categoria: ter filhos
  - coluna: qe_i03
    categoria: cor ou raça declarada
  - coluna: qe_i04
    categoria: deficiência, transtorno global do desenvolvimento ou altas habilidades
  - coluna: qe_i05
    categoria: escolaridade da família
  - coluna: qe_i06
    categoria: escolaridade da família
  - coluna: qe_i07
    categoria: escolaridade da família
  - coluna: qe_i08
    categoria: situação financeira, renda familiar e situação de trabalho
  - coluna: qe_i09
    categoria: situação financeira, renda familiar e situação de trabalho
  - coluna: qe_i10
    categoria: situação financeira, renda familiar e situação de trabalho
  - coluna: qe_i11
    categoria: ingresso por ação afirmativa ou inclusão social
  - coluna: qe_i13
    categoria: bolsas e auxílios recebidos
  - coluna: qe_i15
    categoria: bolsas e auxílios recebidos
  - coluna: qe_i16
    categoria: bolsas e auxílios recebidos
  - coluna: ano_fim_em
    categoria: trajetória acadêmica do estudante
  - coluna: ano_in_grad
    categoria: trajetória acadêmica do estudante
  - coluna: co_turno_graduacao
    categoria: trajetória acadêmica do estudante
  - coluna: co_munic_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: co_uf_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: co_regiao_curso
    categoria: local de funcionamento do curso do estudante
  - coluna: ds_vt_gab_obj
    categoria: desempenho individual do estudante na prova
  - coluna: ds_vt_esc_obj
    categoria: desempenho individual do estudante na prova
  - coluna: ds_vt_ace_obj
    categoria: desempenho individual do estudante na prova
  - coluna: proficiencia
    categoria: desempenho individual do estudante na prova
  - coluna: nt_obj
    categoria: desempenho individual do estudante na prova
  - coluna: nt_dis
    categoria: desempenho individual do estudante na prova
  - coluna: nt_ger
    categoria: desempenho individual do estudante na prova
  - coluna: qt_acertos
    categoria: desempenho individual do estudante na prova
  eras:
  - desde: '2025'
    mudanca: primeira edição publicada do Enade das Licenciaturas (modalidade instituída em 2024 pela Portaria MEC nº 610); desde 2025 o instrumento da avaliação teórica é o mesmo da Prova Nacional Docente
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Enade das Licenciaturas 2025 — microdados

## Resumo

Microdados do Enade das Licenciaturas, modalidade do Exame Nacional de Desempenho de Estudantes instituída em 2024 para avaliar os concluintes dos cursos de licenciatura; a edição de 2025 é a primeira publicada. Reúnem os resultados da avaliação teórica e as respostas do Questionário do Estudante e do Questionário de Percepção de Prova dos concluintes inscritos regularmente em 17 áreas de licenciatura, mais as características dos cursos e a tabela de parâmetros dos itens. Por exigência da LGPD, os dados vêm separados em 28 arquivos (`arq1` a `arq28`), cada um ordenado por uma variável diferente: só é possível agrupar os arquivos pelo código do curso, nunca ligar as informações de um mesmo estudante.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/enade-licenciaturas` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade-das-licenciaturas |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; a edição de 2025 é a primeira do Enade das Licenciaturas (a prova de 2025 foi aplicada em 26/10/2025 e reaplicada em 30/11/2025) |
| Cobertura | 2025 a 2025 |
| Unidade (uma linha) | um estudante concluinte de licenciatura inscrito regularmente no Enade 2025, em cada arquivo, sem ligação entre arquivos; na tabela de parâmetros, um item de prova por área |
| Granularidade | espacial: curso (código do curso no Enade), com IES, município, UF e região do curso; temporal: ano da edição (2025) |
| Formato bruto | ZIP com as pastas 1.LEIA-ME (manual do usuário, Questionário do Estudante, dicionário em xlsx e ods) e 2.DADOS (28 TXT com ponto e vírgula e CRLF, mais a tabela de parâmetros dos itens em xlsx e ods) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 115 |
| Unidades de medida | `NU_ITEM_PROVA_1`: número do item (sem unidade); `NU_ITEM_PROVA_2`: número do item (sem unidade); `NU_ITEM_PROVA_3`: número do item (sem unidade); `NU_ITEM_PROVA_4`: número do item (sem unidade); `ITEM_MANTIDO`: indicador 0 ou 1; `COR_BISSERIAL`: correlação (de -1 a 1); `PARAMETRO_B`: parâmetro de dificuldade na escala da TRI; `INFIT`: estatística de ajuste (sem unidade); `OUTFIT`: estatística de ajuste (sem unidade); `CO_GRUPO`: código da área (sem unidade) |
| Dados pessoais | `tp_sexo` (sexo do estudante); `nu_idade` (idade do estudante (da base da Receita Federal)); `qe_i01` (estado civil); `qe_i02` (ter filhos); `qe_i03` (cor ou raça declarada); `qe_i04` (deficiência, transtorno global do desenvolvimento ou altas habilidades); `qe_i05` (escolaridade da família); `qe_i06` (escolaridade da família); `qe_i07` (escolaridade da família); `qe_i08` (situação financeira, renda familiar e situação de trabalho); `qe_i09` (situação financeira, renda familiar e situação de trabalho); `qe_i10` (situação financeira, renda familiar e situação de trabalho); `qe_i11` (ingresso por ação afirmativa ou inclusão social); `qe_i13` (bolsas e auxílios recebidos); `qe_i15` (bolsas e auxílios recebidos); `qe_i16` (bolsas e auxílios recebidos); `ano_fim_em` (trajetória acadêmica do estudante); `ano_in_grad` (trajetória acadêmica do estudante); `co_turno_graduacao` (trajetória acadêmica do estudante); `co_munic_curso` (local de funcionamento do curso do estudante); `co_uf_curso` (local de funcionamento do curso do estudante); `co_regiao_curso` (local de funcionamento do curso do estudante); `ds_vt_gab_obj` (desempenho individual do estudante na prova); `ds_vt_esc_obj` (desempenho individual do estudante na prova); `ds_vt_ace_obj` (desempenho individual do estudante na prova); `proficiencia` (desempenho individual do estudante na prova); `nt_obj` (desempenho individual do estudante na prova); `nt_dis` (desempenho individual do estudante na prova); `nt_ger` (desempenho individual do estudante na prova); `qt_acertos` (desempenho individual do estudante na prova) |
| Eras | 2025: primeira edição publicada do Enade das Licenciaturas (modalidade instituída em 2024 pela Portaria MEC nº 610); desde 2025 o instrumento da avaliação teórica é o mesmo da Prova Nacional Docente |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_enade_licenciaturas_2025.zip` (25.731.801 bytes; última modificação na fonte em 2026-09-09, lido em 2026-11-15). A página oficial lista só a edição de 2025 ("Arquivo atualizado em 09/09/2026").
- No bruto, o arquivo se chama `enade-licenciaturas/enade-licenciaturas-microdados_2025@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- O ZIP tem `Microdados_Enade_Licenciaturas_2025/1.LEIA-ME` (manual do usuário de 09/09/2026, Questionário do Estudante em PDF e o dicionário de arquivos e variáveis em xlsx e ods) e `2.DADOS` com 28 arquivos `microdados2025_arq1.txt` a `arq28.txt` e a tabela `microdados2025_parametros_itens` em xlsx e ods. O maior arquivo é `arq3` (93.756.019 bytes descompactado), seguido de `arq4` (31.394.979) e `arq1` (13.312.075); os demais ficam entre 4,5 e 7,4 MB.
- Cada um dos 28 TXT tem 293.082 linhas de dados (conferido na fonte em 2026-11-15), uma por inscrito regular que o Inep manteve nos microdados. O arquivo `arq1` traz 4.948 cursos, de 840 IES, em 17 áreas.
- O histórico de alterações do manual registra a versão original de 04/05/2026 e, em 09/09/2026, a complementação da descrição de `DS_VT_ACE_OBJ`.

## Conteúdo

- **Estudantes cobertos.** Concluintes de cursos de licenciatura inscritos regularmente (pela IES ou, administrativamente, pelo Inep) no Enade das Licenciaturas 2025, nas áreas Artes Visuais, Ciências Biológicas, Ciência da Computação, Ciências Sociais, Educação Física, Filosofia, Física, Geografia, História, Letras (Português, Português e Espanhol, Português e Inglês, Inglês), Matemática, Música, Pedagogia e Química. Os resultados de cursos com um único estudante com resultado válido (`tp_pres` 555) e as respostas dos questionários de cursos com um único respondente foram excluídos.
- **Por que há 28 arquivos.** Para atender à LGPD, o Inep dividiu os microdados em arquivos temáticos, cada um com `nu_ano` e `co_curso` mais um grupo de variáveis, e cada um ordenado por uma variável diferente. A primeira linha de um arquivo não é o mesmo estudante da primeira linha de outro: não existe ligação por estudante. O manual diz que a junção de arquivos só é possível pelo código do curso (`co_curso`), e que nessa junção os estudantes ficam distribuídos de forma aleatória dentro de cada curso.
- **O que é cada `arqN`:**

| Arquivo | Conteúdo (do dicionário de arquivos do Inep) | Colunas |
|---|---|---|
| `arq1` | caracterização do curso: IES, categoria administrativa, organização acadêmica, área, modalidade, município, UF e região do curso | `nu_ano`, `co_curso`, `co_ies`, `co_categad`, `co_orgacad`, `co_grupo`, `co_modalidade`, `co_munic_curso`, `co_uf_curso`, `co_regiao_curso` |
| `arq2` | informações acadêmicas dos estudantes: ano de conclusão do ensino médio, ano de início da graduação e turno | `ano_fim_em`, `ano_in_grad`, `co_turno_graduacao` |
| `arq3` | prova: caderno, reaplicação, vetores de gabarito, escolha e acertos, tipo de presença, situação na parte discursiva, proficiência, notas, quantidade de acertos e respostas do Questionário de Percepção de Prova | `co_caderno` a `co_rs_i9` (21 colunas) |
| `arq4` | avaliação dos estudantes sobre o processo formativo (organização didático-pedagógica, infraestrutura e oportunidades de ampliação da formação) | `qe_i20` a `qe_i66` |
| `arq5` | sexo | `tp_sexo` |
| `arq6` | idade do inscrito no dia da prova | `nu_idade` |
| `arq7` a `arq25` | uma questão do Questionário do Estudante por arquivo, na ordem das questões 1 a 19 (`arq7` é `qe_i01`, `arq8` é `qe_i02` e assim até `arq25`, que é `qe_i19`) | `qe_i01` a `qe_i19` |
| `arq26`, `arq27` | recomendação do curso (`qe_i68`) e da instituição (`qe_i69`) a um amigo ou colega | `qe_i68`, `qe_i69` |
| `arq28` | interesse em participar da Prova Nacional Docente 2025 | `qe_i70` |
| `parametros_itens` | tabela de parâmetros dos itens por área (`CO_GRUPO`): número do item em cada caderno, se foi mantido, correlação bisserial, parâmetro de dificuldade e ajustes INFIT e OUTFIT | colunas em maiúsculas |

- A pesquisa individualizada, com identificação do estudante, só é possível pelo Serviço de Acesso a Dados Protegidos (Sedap) do Inep, segundo o manual.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2025 | 29 arquivos, de 3 a 49 colunas |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx), aba `DICIONÁRIO DE VARIÁVEIS`; a tabela de parâmetros dos itens não tem dicionário próprio nesta edição (as descrições de suas colunas são as do dicionário do Enamed, que traz a mesma tabela, e as colunas estão em maiúsculas no lake).
A coluna *Arquivos* indica em qual arquivo `arqN` do lake a coluna aparece; `nu_ano` e `co_curso` estão em todos os arquivos de `arq1` a `arq28`.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `nu_ano` | `NU_ANO` | texto | Ano de realização do exame (2025) | — | todo | `microdados_arq1`, `microdados_arq10`, `microdados_arq11` e mais 25 |
| `co_curso` | `CO_CURSO` | texto | Código do curso no Enade (Entre 6 e 5001385) | — | todo | `microdados_arq1`, `microdados_arq10`, `microdados_arq11` e mais 25 |
| `co_ies` | `CO_IES` | texto | Código da IES (e-MEC) (Entre 1 e 29118) | — | todo | `microdados_arq1` |
| `co_categad` | `CO_CATEGAD` | texto | Código da categoria administrativa da IES | 1 = Pública Federal; 2 = Pública Estadual; 3 = Pública Municipal; 4 = Privada com fins lucrativos; 5 = Privada sem fins lucrativos; 7 = Especial; 8 = Comunitária/Confessional | todo | `microdados_arq1` |
| `co_orgacad` | `CO_ORGACAD` | texto | Código da organização acadêmica da IES | 10019 = Centro Federal de Educação Tecnológica; 10020 = Centro Universitário; 10022 = Faculdade; 10026 = Instituto Federal de Educação, Ciência e Tecnologia; 10028 = Universidade | todo | `microdados_arq1` |
| `co_grupo` | `CO_GRUPO` | texto | Código da Área de enquadramento do curso no Enade | 702 = MATEMÁTICA (LICENCIATURA); 904 = LETRAS - PORTUGUÊS (LICENCIATURA); 905 = LETRAS -PORTUGUÊS E INGLÊS (LICENCIATURA); 906 = LETRAS - PORTUGUÊS E ESPANHOL (LICENCIATURA); 1402 = FÍSICA (LICENCIATURA); 1502 = QUÍMICA (LICENCIATURA); … (lista completa no dicionário da fonte) | todo | `microdados_arq1` |
| `co_modalidade` | `CO_MODALIDADE` | texto | Código da Modalidade de Ensino | 0 = EaD; 1 = Presencial | todo | `microdados_arq1` |
| `co_munic_curso` | `CO_MUNIC_CURSO` | texto | Código do município de funcionamento do curso (Entre 1100015 e 5300108 (Identificação do Município conforme IBGE - Ir para Planilha MUNICÍPIOS)) | — | todo | `microdados_arq1` |
| `co_uf_curso` | `CO_UF_CURSO` | texto | Código da UF de funcionamento do curso (Conforme código do IBGE) | 11 = Rondônia (RO); 12 = Acre (AC); 13 = Amazonas (AM); 14 = Roraima (RR); 15 = Pará (PA); 16 = Amapa (AP); 17 = Tocantins (TO); 21 = Maranhão (MA); 22 = Piauí (PI); 23 = Ceará (CE); 24 = Rio Grande do Norte (RN); 25 = Paraíba (PB); 26 = Pernambuco (PE); … (lista completa no dicionário da fonte) | todo | `microdados_arq1` |
| `co_regiao_curso` | `CO_REGIAO_CURSO` | texto | Código da região de funcionamento do curso | 1 = Região Norte (N); 2 = Região Nordeste (NE); 3 = Região Sudeste (SE); 4 = Região Sul (SUL); 5 = Região Centro-Oeste (CO) | todo | `microdados_arq1` |
| `qe_i04` | `QE_I04` | texto | Você tem alguma deficiência, transtorno global do desenvolvimento ou altas habilidades? (Você pode marcar quantas alternativas considerar necessárias). | A = Não possuo.; B = Cegueira.; C = Baixa Visão.; D = Surdez.; E = Deficiência Auditiva.; F = Deficiência Física.; G = Transtorno do Espectro Autista (TEA).; H = Altas habilidades/superdotação.; I = Deficiência Intelectual.; … (lista completa no dicionário da fonte) | todo | `microdados_arq10` |
| `qe_i05` | `QE_I05` | texto | Alguém em sua família concluiu um curso superior? | A = Sim.; B = Não.; C = Não sei responder. | todo | `microdados_arq11` |
| `qe_i06` | `QE_I06` | texto | Até que etapa de escolarização sua mãe concluiu? | A = Nenhuma.; B = Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série).; C = Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série).; D = Ensino Médio.; E = Ensino Superior - Graduação.; F = Pós-graduação (Especialização).; G = Pós-Graduação (Mestrado ou Doutorado).; … (lista completa no dicionário da fonte) | todo | `microdados_arq12` |
| `qe_i07` | `QE_I07` | texto | Até que etapa de escolarização seu pai concluiu? | A = Nenhuma.; B = Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série).; C = Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série).; D = Ensino Médio.; E = Ensino Superior - Graduação.; F = Pós-graduação (Especialização).; G = Pós-Graduação (Mestrado ou Doutorado).; … (lista completa no dicionário da fonte) | todo | `microdados_arq13` |
| `qe_i08` | `QE_I08` | texto | Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)? | A = Não tenho renda e meus gastos são financiados por programas governamentais.; B = Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas.; … (lista completa no dicionário da fonte) | todo | `microdados_arq14` |
| `qe_i09` | `QE_I09` | texto | Qual a renda total de sua família, incluindo seus rendimentos? (considere como família a sua unidade de origem composta por pessoas que possuem vínculos consanguíneos e/ou de parentesco, todas moradoras do mesmo domicílio). | A = Até 1,5 salário mínimo (até R$ 2.277,00).; B = De 1,5 a 3 salários mínimos (R$ 2.277,00 a R$ 4.554,00).; C = De 3 a 4,5 salários mínimos (R$ 4.554,00 a R$ 6.831,00).; D = De 4,5 a 6 salários mínimos (R$ 6.831,00 a R$ 9.108,00).; … (lista completa no dicionário da fonte) | todo | `microdados_arq15` |
| `qe_i10` | `QE_I10` | texto | Qual alternativa melhor descreve a sua situação de trabalho durante a maior parte do curso? (Excluindo trabalhos acadêmicos e bolsas). | A = Não trabalhei durante o curso.; B = Trabalhei 20 horas semanais.; C = Trabalhei 30 horas semanais.; D = Trabalhei 40 horas semanais.; E = Trabalhei com jornada de trabalho flexível de horários. | todo | `microdados_arq16` |
| `qe_i11` | `QE_I11` | texto | Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social? (Exemplos de políticas de ação afirmativa ou inclusão social são as Cotas e o Prouni.) | A = Não.; B = Sim, por critério étnico-racial.; C = Sim, por critério de renda.; D = Sim, por ter estudado em escola pública ou particular com bolsa de estudos.; E = Sim, por sistema que combina dois ou mais critérios anteriores.; … (lista completa no dicionário da fonte) | todo | `microdados_arq17` |
| `qe_i12` | `QE_I12` | texto | Qual a principal razão para você ter escolhido a sua instituição de educação superior? | A = Gratuidade.; B = Preço da mensalidade.; C = Proximidade da minha residência.; D = Proximidade do meu trabalho.; E = Facilidade de acesso.; F = Qualidade/reputação.; G = Foi a única onde tive aprovação.; H = Possibilidade de ter bolsa de estudo.; … (lista completa no dicionário da fonte) | todo | `microdados_arq18` |
| `qe_i13` | `QE_I13` | texto | Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. | A = Nenhum, pois meu curso é gratuito.; B = Nenhum, embora meu curso não seja gratuito.; C = ProUni integral.; D = ProUni parcial, apenas.; E = FIES, apenas.; F = ProUni Parcial e FIES.; G = Bolsa oferecida por governo estadual, distrital ou municipal.; … (lista completa no dicionário da fonte) | todo | `microdados_arq19` |
| `ano_fim_em` | `ANO_FIM_EM` | texto | Ano de conclusão do Ensino Médio (AAAA, conforme lançado pelo estudante) | — | todo | `microdados_arq2` |
| `ano_in_grad` | `ANO_IN_GRAD` | texto | Ano de início da graduação (AAAA, conforme lançado pelo estudante) | — | todo | `microdados_arq2` |
| `co_turno_graduacao` | `CO_TURNO_GRADUACAO` | texto | Código do turno de graduação cursado pelo estudante | 1 = Matutino; 2 = Vespertino; 3 = Integral; 4 = Noturno | todo | `microdados_arq2` |
| `qe_i14` | `QE_I14` | texto | Algum fator dificultou sua permanência no ensino superior? | A = Não tive dificuldades.; B = Falta de recursos financeiros para pagar mensalidades.; C = Falta de recursos financeiros para se manter estudando.; D = Falta de recursos financeiros para comprar material e/ou equipamentos requeridos pelo curso.; … (lista completa no dicionário da fonte) | todo | `microdados_arq20` |
| `qe_i15` | `QE_I15` | texto | Ao longo da sua trajetória acadêmica, você recebeu algum tipo de auxílio permanência? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração. | A = Nenhum.; B = Auxílio moradia.; C = Auxílio alimentação.; D = Auxílio moradia e alimentação.; E = Auxílio permanência.; F = Outro tipo de auxílio. | todo | `microdados_arq21` |
| `qe_i16` | `QE_I16` | texto | Ao longo da sua trajetória acadêmica, você recebeu algum tipo de bolsa acadêmica? (Você pode marcar quantas alternativas considerar necessário). | A = Nenhum.; B = Bolsa de iniciação científica.; C = Bolsa de extensão.; D = Bolsa de monitoria/tutoria.; E = Bolsa PET.; F = Bolsa PIBID.; G = Bolsa Residência Pedagógica.; H = Outro tipo de bolsa acadêmica. | todo | `microdados_arq22` |
| `qe_i17` | `QE_I17` | texto | Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula? | A = Nenhuma, apenas assisto às aulas.; B = De uma a três.; C = De quatro a sete.; D = De oito a doze.; E = Mais de doze. | todo | `microdados_arq23` |
| `qe_i18` | `QE_I18` | texto | Você pretende exercer o magistério após o término do curso? | A = Sim, como atuação profissional principal.; B = Sim, mas esta não será a minha atuação profissional principal.; C = Não.; D = Ainda não decidi. | todo | `microdados_arq24` |
| `qe_i19` | `QE_I19` | texto | Onde você pretende atuar daqui a cinco anos? | A = Em escola pública, como professor.; B = Em escola privada, como professor.; C = Em escola/instituição pública, na gestão educacional.; D = Em escola/instituição privada, na gestão educacional.; … (lista completa no dicionário da fonte) | todo | `microdados_arq25` |
| `qe_i68` | `QE_I68` | texto | Em uma escala de 0 a 10, o quanto você recomendaria o seu curso para um amigo ou colega? | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq26` |
| `qe_i69` | `QE_I69` | texto | Em uma escala de 0 a 10, o quanto você recomendaria a sua Instituição de Educação Superior para um amigo ou colega? | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq27` |
| `qe_i70` | `QE_I70` | texto | Qual o seu interesse em participar da Prova Nacional Docente – 2025? | A = Quero ser professor da rede pública.; B = Sou professor da rede pública e quero ampliar a carga horária na mesma rede de ensino.; C = Sou professor da rede pública e quero complementar a carga horária de trabalho em outra rede de ensino.; … (lista completa no dicionário da fonte) | todo | `microdados_arq28` |
| `co_caderno` | `CO_CADERNO` | texto | Código do caderno (Códigos dos cadernos 1 a 4 referentes a aplicação e código do caderno 5 à reaplicação) | 1 = Caderno 1; 2 = Caderno 2; 3 = Caderno 3; 4 = Caderno 4; 5 = Caderno 5; . = Estudante que escolheu fazer a prova na área distinta da área do Enade | todo | `microdados_arq3` |
| `in_reaplicacao` | `IN_REAPLICACAO` | texto | Indicação da prova válida para o inscrito: aplicação ou reaplicação | 0 = Participante que fez a prova no dia da aplicação - 26/10/2025; 1 = Participante que fez a prova no dia da reaplicação - 30/11/2025 | todo | `microdados_arq3` |
| `ds_vt_gab_obj` | `DS_VT_GAB_OBJ` | texto | Vetor que representa o gabarito final das questões objetivas (Uma letra por item (intervalo de A a D)) | 6 = Questão anulada pela Comissão Assessora de Área ou administrativamente pelo Inep | todo | `microdados_arq3` |
| `ds_vt_esc_obj` | `DS_VT_ESC_OBJ` | texto | Vetor que representa a escolha de resposta das questões objetivas (Escolha de resposta no Item = Uma letra por item (intervalo de A a D); Códigos possíveis:; A; B; C; D) | . = em branco; * = múltiplas escolhas | todo | `microdados_arq3` |
| `ds_vt_ace_obj` | `DS_VT_ACE_OBJ` | texto | Vetor que representa os acertos da prova, a variável representa o vetor de acertos rotacionados, tendo como base a sequência das questões do Caderno 1. (Indica o resultado do Item.) | 0 = Errada - escolha da alternativa diferente do gabarito; 1 = Correta - escolha da alternativa igual ao gabarito; 4 = Eliminado; 6 = Questão anulada pela Comissão Assessora de Área ou administrativamente pelo Inep; 8 = Questão desconsiderada pela TRI; … (lista completa no dicionário da fonte) | todo | `microdados_arq3` |
| `tp_pres` | `TP_PRES` | texto | Tipo de presença na prova | 222 = Ausente; 334 = Eliminado; 444 = Ausente devido a múltiplas inscrições; 555 = Presente com resultado válido; 888 = Presente na prova, com resultado desconsiderado pelo Inep; . = Estudante que escolheu fazer a prova na área distinta da área do Enade | todo | `microdados_arq3` |
| `tp_sit_disc` | `TP_SIT_DISC` | texto | Tipo de situação na parte discursiva (Nota: (*) resultado considerado para o cálculo da nota do estudante;; (**) resultado desconsiderado para o cálculo da nota do estudante.) | 222 = Não se aplica (estudante ausente)**; 333 = Questão em branco - estudante presente (nota=zero)*; 335 = Questão zerada por motivo de resposta nula (nota=zero)*; 336 = Questão com resposta divergente da temática (nota=zero)*; … (lista completa no dicionário da fonte) | todo | `microdados_arq3` |
| `proficiencia` | `PROFICIENCIA` | texto | Proficiência da TRI na prova objetiva (valor de theta) (Min = -4,00000; Max = 4,00000) | — | todo | `microdados_arq3` |
| `nt_obj` | `NT_OBJ` | texto | Nota da prova objetiva (valor de 0 a 100) (Min = 0,000; Max = 100,000) | — | todo | `microdados_arq3` |
| `nt_dis` | `NT_DIS` | texto | Nota da questão discursiva (valor de 0 a 20) (Min = 0,000; Max = 20,000) | — | todo | `microdados_arq3` |
| `nt_ger` | `NT_GER` | texto | Nota geral da prova - Média ponderada considerando a nota da prova objetiva (80%) e a nota da questão discursiva (20%). (valor de 0 a 100) (Min = 0,000; Max = 100,000) | — | todo | `microdados_arq3` |
| `qt_acertos` | `QT_ACERTOS` | texto | Quatidade de acertos na prova objetiva (Min = 0; Max = 80) | — | todo | `microdados_arq3` |
| `co_rs_i1` | `CO_RS_I1` | texto | 1 - Qual o grau de dificuldade desta prova na parte de Formação Geral? (. = Sem resposta) | A = Muito fácil.; B = Fácil.; C = Médio.; D = Difícil.; E = Muito difícil.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i2` | `CO_RS_I2` | texto | 2 - Qual o grau de dificuldade desta prova na parte do Componente Específico? (. = Sem resposta) | A = Muito fácil.; B = Fácil.; C = Médio.; D = Difícil.; E = Muito difícil.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i3` | `CO_RS_I3` | texto | 3 - Considerando a extensão da prova, em relação ao tempo total, você considera que a prova foi: (. = Sem resposta) | A = Muito longa.; B = Longa.; C = Adequada.; D = Curta.; E = Muito curta.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i4` | `CO_RS_I4` | texto | 4 - Os enunciados das questões da prova na parte de Formação Geral estavam claros e objetivos? (. = Sem resposta) | A = Sim, todos.; B = Sim, a maioria.; C = Apenas cerca da metade.; D = Poucos.; E = Não, nenhum.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i5` | `CO_RS_I5` | texto | 5 - Os enunciados das questões na parte do Componente Específico estavam claros e objetivos? (. = Sem resposta) | A = Sim, todos.; B = Sim, a maioria.; C = Apenas cerca da metade.; D = Poucos se apresentam.; E = Não, nenhum.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i6` | `CO_RS_I6` | texto | 6 - As informações/instruções fornecidas para a resolução das questões foram suficientes para resolvê-las? (. = Sem resposta) | A = Sim, até excessivas.; B = Sim, em todas elas.; C = Sim, na maioria delas.; D = Sim, somente em algumas.; E = Não, em nenhuma delas.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `co_rs_i7` | `CO_RS_I7` | texto | 7 - Você se deparou com alguma dificuldade ao responder à prova. Qual? (. = Sem resposta) | A = Desconhecimento do conteúdo.; B = Forma diferente de abordagem do conteúdo.; C = Espaço insuficiente para responder às questões.; D = Falta de motivação para fazer a prova.; E = Não tive qualquer tipo de dificuldade para responder à prova.; … (lista completa no dicionário da fonte) | todo | `microdados_arq3` |
| `co_rs_i8` | `CO_RS_I8` | texto | 8 - Considerando apenas as questões objetivas da prova, você percebeu que: (. = Sem resposta) | A = Não estudou ainda a maioria desses conteúdos.; B = Estudou alguns desses conteúdos, mas não os aprendeu.; C = Estudou a maioria desses conteúdos, mas não os aprendeu.; D = Estudou e aprendeu muitos desses conteúdos.; … (lista completa no dicionário da fonte) | todo | `microdados_arq3` |
| `co_rs_i9` | `CO_RS_I9` | texto | 9 - Qual foi o tempo gasto por você para concluir a prova? (. = Sem resposta) | A = Menos de uma hora.; B = Entre uma e duas horas.; C = Entre duas e três horas.; D = Entre três e quatro horas.; E = Quatro horas e não consegui terminar.; * = Resposta anulada; Valor em branco = Resposta não válida | todo | `microdados_arq3` |
| `qe_i20` | `QE_I20` | texto | Foram oferecidas oportunidades para os estudantes participarem de programas, projetos ou atividades de extensão universitária. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i21` | `QE_I21` | texto | Foram oferecidas oportunidades para os estudantes participarem de projetos de iniciação científica e/ou de atividades que estimularam a investigação acadêmica. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i22` | `QE_I22` | texto | As atividades realizadas durante seu trabalho de conclusão de curso contribuíram para qualificar sua formação profissional. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i23` | `QE_I23` | texto | As relações professor-aluno ao longo do curso foram positivas, estimulando os estudantes a estudar e aprender. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i24` | `QE_I24` | texto | Os professores apresentaram e discutiram os planos de ensino/curso das disciplinas com os estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i25` | `QE_I25` | texto | As referências bibliográficas indicadas pelos professores contribuíram para seus estudos e aprendizagens. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i26` | `QE_I26` | texto | As avaliações da aprendizagem realizadas durante o curso foram compatíveis com os conteúdos ou temas trabalhados pelos professores. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i27` | `QE_I27` | texto | Os professores demonstraram domínio dos conteúdos abordados nas disciplinas. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i28` | `QE_I28` | texto | Os professores utilizaram estratégias e instrumentos de avaliação diversificados (provas, seminários, trabalhos em grupo, portfólio, autoavaliação, etc) | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i29` | `QE_I29` | texto | Os professores ofereceram devolutivas das avaliações (comentários, explicações, sugestões para melhoria) que auxiliaram os estudantes a avançar em suas aprendizagens. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i30` | `QE_I30` | texto | Os professores estimularam a participação ativa dos estudantes durante as aulas (por meio de atividades em grupo, discussões, seminários, etc) não se limitando às aulas expositivas. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i31` | `QE_I31` | texto | O curso disponibilizou quantidade suficiente de professores ou tutores para auxiliar os estudantes nas disciplinas a distância. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i32` | `QE_I32` | texto | Nas disciplinas a distância, houve interação ao vivo (presencial ou síncrona, mediada por tecnologia) entre os estudantes e o professor. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i33` | `QE_I33` | texto | Foram oferecidas oportunidades para os estudantes superarem dificuldades relacionadas ao processo de formação. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i34` | `QE_I34` | texto | A coordenação do curso esteve disponível para orientação acadêmica dos estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i35` | `QE_I35` | texto | O curso favoreceu a articulação do conhecimento teórico com atividades práticas. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i36` | `QE_I36` | texto | O curso propiciou acesso a conhecimentos atualizados e/ou contemporâneos em sua área de formação. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i37` | `QE_I37` | texto | As disciplinas cursadas contribuíram para sua formação como profissional. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i38` | `QE_I38` | texto | As metodologias de ensino utilizadas no curso desafiaram você a se posicionar mais criticamente diante do conhecimento. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i39` | `QE_I39` | texto | Os estudantes participaram de avaliações periódicas das condições de formação (disciplinas, atuação dos professores, infraestrutura). | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i40` | `QE_I40` | texto | O Ambiente Virtual de Aprendizagem - AVA (Moodle, Google Classroom, etc.) apresentou materiais, recursos e tecnologias apropriados para o desenvolvimento das disciplinas. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i41` | `QE_I41` | texto | O curso proporcionou condições de acesso adequado às bibliografias indicadas nas disciplinas, de forma física ou virtual. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i42` | `QE_I42` | texto | As salas de aula apresentaram tamanho, mobiliário e recursos tecnológicos adequados. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i43` | `QE_I43` | texto | As condições de infraestrutura dos polos foram adequadas para os encontros presenciais (não se aplica para cursos presenciais). | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i44` | `QE_I44` | texto | Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso e à quantidade de estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i45` | `QE_I45` | texto | Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso e à quantidade de estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i46` | `QE_I46` | texto | Planejar o ensino considerando a proposta curricular, os conhecimentos prévios, as origens culturais, as experiências de vida e os interesses de todos os estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i47` | `QE_I47` | texto | Propor objetivos de aprendizagem desafiadores aos estudantes, considerando os diferentes níveis cognitivos e dimensões do conhecimento. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i48` | `QE_I48` | texto | Planejar sequências didáticas, articulando diferentes estratégias de ensino, recursos e formas de avaliação coerentes com os objetivos de aprendizagem e objetos de conhecimento. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i49` | `QE_I49` | texto | Utilizar estratégias e recursos diversificados das Tecnologias da Informação e Comunicação (TICs), de maneira apropriada e contextualizada ao processo de ensino e aprendizagem. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i50` | `QE_I50` | texto | Dominar os conhecimentos específicos da minha área de formação e saber como ensiná-los. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i51` | `QE_I51` | texto | Analisar como os estudantes aprendem, em cada faixa etária e etapa de ensino, utilizando estratégias, recursos e materiais adequados e contextualizados a todos os estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i52` | `QE_I52` | texto | Utilizar diferentes estratégias e recursos para a aprendizagem dos estudantes do público da educação especial (alunos com deficiência, alunos com transtornos globais do desenvolvimento, alunos com altas habilidades/superdotação). | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i53` | `QE_I53` | texto | Dominar as informações sobre a estrutura e organização do sistema educacional brasileiro, incluindo suas etapas, modalidades e as políticas a elas associadas. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i54` | `QE_I54` | texto | Conhecer o aluno surdo, sua cultura, identidade e a utilizar os princípios básicos da Língua Brasileira de Sinais (LIBRAS). | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i55` | `QE_I55` | texto | Trabalhar com o tema das relações étnico-raciais e o ensino de história e cultura afro-brasileira, africana e indígena. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i56` | `QE_I56` | texto | Realizar a gestão da sala de aula, considerando diferentes aspectos como a organização de espaços físicos, o aproveitamento do tempo, a seleção de materiais e recursos pedagógicos. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i57` | `QE_I57` | texto | Identificar e desenvolver estratégias pedagógicas preventivas e corretivas para lidar com fenômenos como a indisciplina, o bullying e as diferentes formas de violência escolar. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i58` | `QE_I58` | texto | Desenvolver estratégias de gestão de sala de aula que busquem manter os alunos interessados e engajados nas atividades pedagógicas, criando um ambiente seguro, organizado e respeitoso. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i59` | `QE_I59` | texto | Monitorar o processo de aprendizagem dos estudantes, por meio de diferentes estratégias, para identificar avanços e necessidades. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i60` | `QE_I60` | texto | Utilizar estratégias e instrumentos de avaliação diversificados, considerando a heterogeneidade dos estudantes (provas, seminários, trabalhos em grupo, portfólio, autoavaliação, etc). | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i61` | `QE_I61` | texto | Oferecer devolutivas das avaliações compreensíveis aos estudantes, com comentários, explicações e sugestões que os auxiliem a avançar em suas aprendizagens. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i62` | `QE_I62` | texto | Dominar as informações sobre as avaliações externas, sabendo integrá-las ao planejamento das ações didático-pedagógicas da escola. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i63` | `QE_I63` | texto | Trabalhar em equipe dialogando sobre minhas práticas pedagógicas, de modo colaborativo e solidário. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i64` | `QE_I64` | texto | Refletir permanentemente sobre a minha prática pedagógica, revisando-a e readequando-a sempre que necessário. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i65` | `QE_I65` | texto | Reconhecer a importância de participar da comunidade escolar de maneira propositiva, respeitando as decisões tomadas nas instâncias colegiadas, colaborando para a melhoria da escola como um todo. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `qe_i66` | `QE_I66` | texto | Interagir com as famílias, respeitando as suas culturas e múltiplas formas de organização, visando a melhoria da aprendizagem de todos os estudantes. | 1 = Discordo totalmente.; 2 = Discordo.; 3 = Discordo parcialmente.; 4 = Concordo parcialmente.; 5 = Concordo.; 6 = Concordo totalmente.; 7 = Não sei responder.; 8 = Não se aplica. | todo | `microdados_arq4` |
| `tp_sexo` | `TP_SEXO` | texto | Sexo | M = Masculino; F = Feminino; 9 = Indefinido | todo | `microdados_arq5` |
| `nu_idade` | `NU_IDADE` | texto | Idade do inscrito em 26/10/2025 ( aplicação) Idade do inscrito em 30/11/2025 (reaplicação) (Dados provenientes da base da Receita Federal) | — | todo | `microdados_arq6` |
| `qe_i01` | `QE_I01` | texto | Qual o seu estado civil? | A = Solteiro(a).; B = Casado(a) ou vivendo em união estável.; C = Separado(a) judicialmente/divorciado(a).; D = Viúvo(a).; E = Outro. | todo | `microdados_arq7` |
| `qe_i02` | `QE_I02` | texto | Você tem filhos? | A = Não.; B = Sim, 1 filho.; C = Sim, 2 filhos.; D = Sim, 3 filhos ou mais. | todo | `microdados_arq8` |
| `qe_i03` | `QE_I03` | texto | Qual é a sua cor ou raça? | A = Branca.; B = Preta.; C = Amarela.; D = Parda.; E = Indígena.; F = Não quero declarar. | todo | `microdados_arq9` |
| `CO_GRUPO` | `CO_GRUPO` | inteiro | Código da área de enquadramento do curso no Enade, na tabela de parâmetros dos itens (coluna em maiúsculas, distinta de `co_grupo`); não consta do dicionário desta edição | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_1` | `NU_ITEM_PROVA_1` | inteiro | Número do item na prova 1 (caderno 1) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_2` | `NU_ITEM_PROVA_2` | inteiro | Número do item na prova 2 (caderno 2) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_3` | `NU_ITEM_PROVA_3` | inteiro | Número do item na prova 3 (caderno 3); a numeração dos cadernos segue a coluna de mesmo nome (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `NU_ITEM_PROVA_4` | `NU_ITEM_PROVA_4` | inteiro | Número do item na prova 4 (caderno 4); a numeração dos cadernos segue a coluna de mesmo nome (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `ITEM_MANTIDO` | `ITEM_MANTIDO` | inteiro | Indica se o item foi mantido no cálculo (1 = sim, 0 = não) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `COR_BISSERIAL` | `COR_BISSERIAL` | decimal | Correlação bisserial do item (de -1 a 1) (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `PARAMETRO_B` | `PARAMETRO_B` | decimal | Parâmetro de dificuldade do item na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `INFIT` | `INFIT` | decimal | Estatística de ajuste INFIT na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |
| `OUTFIT` | `OUTFIT` | decimal | Estatística de ajuste OUTFIT na TRI (descrição do dicionário do Enamed para a coluna de mesmo nome; o dicionário do Enade das Licenciaturas não descreve a tabela de parâmetros) | — | todo | `microdados_parametros_itens` |

## No lake

- Dataset `inep/enade-licenciaturas`, particionado por `ano` (única partição: 2025); um Parquet por TXT, no padrão `enade-licenciaturas-microdados_2025__microdados2025_arq<N>.parquet`, mais `enade-licenciaturas-microdados_2025__microdados2025_parametros_itens.parquet`.
- Nos arquivos `arq1` a `arq28` as colunas são texto, com os nomes normalizados (minúsculas). A tabela de parâmetros dos itens é a exceção: o conversor a lê da planilha, mantém os nomes em maiúsculas (`CO_GRUPO`, `NU_ITEM_PROVA_1` a `4`, `ITEM_MANTIDO`, `COR_BISSERIAL`, `PARAMETRO_B`, `INFIT`, `OUTFIT`) e grava inteiros e decimais.
- A coluna `ano` é a edição, tirada do nome do arquivo; `nu_ano` é o ano dentro do dado.

## Cuidados de uso

- **Não há ligação entre arquivos por estudante, e a chave do dataset fica vazia.** `co_curso` é a única coluna comum útil: ela permite montar o perfil e os resultados do curso, mas, ao juntar `arqN` por `co_curso`, cada linha de um arquivo casa com todas as linhas do outro para o mesmo curso (um produto cartesiano por curso, sem sentido por estudante). Agregue cada arquivo por curso antes de juntar.
- **Decimais com vírgula, apesar do manual.** O manual manda importar os decimais com ponto, mas `proficiencia`, `nt_obj`, `nt_dis` e `nt_ger` vêm com vírgula nos TXT (por exemplo, `-2,72395` e `0,24`); troque a vírgula por ponto antes de converter.
- **Códigos de ausência.** `.` marca "sem resposta" nas perguntas do questionário (em `qe_i03`, 57.737 linhas na fonte; vazio em 1.552); nas respostas do Questionário de Percepção de Prova (`co_rs_i1` a `co_rs_i9`), `.` é sem resposta, `*` é resposta anulada e valor em branco é resposta não válida; em `co_caderno`, `tp_pres` e `tp_sit_disc`, o dicionário usa `.` para o estudante que escolheu fazer a prova em área distinta da do Enade (`tp_pres` está vazio em 10.469 linhas). `tp_sexo` tem o código 9 ("indefinido") em 25 linhas.
- **Presença.** `tp_pres` na fonte: 555 (presente com resultado válido) em 196.059 linhas, 222 (ausente) em 84.999, 444 (ausente por múltiplas inscrições) em 1.187, 334 (eliminado) em 356 e 888 (presença com resultado desconsiderado pelo Inep) em 12. As linhas de ausentes e eliminados fazem parte do arquivo; filtre `tp_pres` = 555 antes de calcular médias de desempenho.
- **Vetores.** `ds_vt_ace_obj` é o vetor de acertos reordenado pela sequência das questões do caderno 1; use a tabela de parâmetros dos itens para voltar à ordem original do caderno. Importe as colunas `ds_vt_gab_obj`, `ds_vt_esc_obj` e `ds_vt_ace_obj` como texto.
- **A tabela de parâmetros tem outros problemas.** O xlsx da fonte tem duas abas (aplicação, com 10 colunas, e reaplicação, com 4 colunas e `NU_ITEM_PROVA_5`), e o lake guarda só a primeira. Os nomes das colunas ficam em maiúsculas, e a coluna `CO_GRUPO` difere de `co_grupo` dos outros arquivos só pela caixa: ao unir os arquivos em um motor sem distinção de maiúsculas, as duas colidem.
- **Escala do dicionário.** O dicionário lista, para `qe_i68` e `qe_i69` ("em uma escala de 0 a 10"), as categorias de concordância de 1 a 8 das demais afirmações; na fonte, as duas colunas assumem valores de 0 a 10 (por exemplo, `qe_i68` vale 10 em 126.881 linhas e fica vazio em 59.323). Use a escala de 0 a 10.
- **Dados pessoais.** Os arquivos trazem sexo, idade, cor ou raça, deficiência, estado civil, filhos, renda, escolaridade da família, ações afirmativas e bolsas, sem nome ou identificador do estudante, em arquivos ordenados de forma diferente. Mesmo assim, evite recortes com poucos casos (cursos pequenos).
- **Uma edição só.** O lake tem apenas 2025; comparar com o Enade regular (dataset `enade`) exige atenção, porque a estrutura de arquivos e as áreas são outras.

## Exemplos

Número de inscritos por área (`co_grupo`) e sexo, juntando por curso o arquivo de sexo (agregado por curso antes de juntar, para não multiplicar linhas) ao de caracterização dos cursos. Na amostra do lake, cada arquivo tem só as primeiras 1.500 linhas, ordenadas de forma diferente, de modo que poucos cursos aparecem nos dois:

```python
import duckdb

duckdb.sql("""
    WITH sexo AS (
        SELECT co_curso, count(*) FILTER (WHERE tp_sexo = 'F') AS mulheres, count(*) FILTER (WHERE tp_sexo = 'M') AS homens
        FROM read_parquet('lake/inep/enade-licenciaturas/ano=2025/*arq5.parquet')
        GROUP BY co_curso
    ), curso AS (
        SELECT DISTINCT co_curso, co_grupo
        FROM read_parquet('lake/inep/enade-licenciaturas/ano=2025/*arq1.parquet')
    )
    SELECT c.co_grupo, sum(s.mulheres) AS mulheres, sum(s.homens) AS homens
    FROM sexo s JOIN curso c USING (co_curso)
    GROUP BY c.co_grupo
    ORDER BY c.co_grupo
""").show()
```

## Referências

- Microdados do Enade das Licenciaturas: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade-das-licenciaturas
- Manual do usuário, Questionário do Estudante e dicionário de arquivos e variáveis, dentro do ZIP em https://download.inep.gov.br/microdados/microdados_enade_licenciaturas_2025.zip
