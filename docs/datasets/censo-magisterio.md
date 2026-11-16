---
dataset:
  id: censo-magisterio
  fonte: inep
  titulo: Censo dos Profissionais do Magistério da Educação Básica 2003 — microdados
  resumo: 'Microdados do levantamento de 2003 com os profissionais do magistério da educação básica: perfil, vínculo, remuneração, formação e condições de trabalho; edição única.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-dos-profissionais-do-magisterio
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: edição única, 2003 (não se repetiu)
  cobertura:
    inicio: '2003'
    fim: '2003'
  unidade: um profissional do magistério da educação básica que respondeu ao questionário
  granularidade:
    espacial: profissional, com a escola em que leciona (máscara da escola, município, UF, região, rede, dependência administrativa e localização) e o município e a UF do endereço do profissional
    temporal: 2003; os vencimentos referem-se a setembro de 2003
  formato_bruto: ZIP com uma pasta de dados (um CSV com ponto e vírgula, não em UTF-8, lido como latin-1) e o Leia-me em PDF, que traz a nota técnica, o dicionário de variáveis e o questionário
  lake:
    estado: convertido
    particoes:
    - ano
    chave:
    - campo_chave
    colunas: 240
  unidades_de_medida:
    s_b_total: valor monetário bruto de setembro de 2003 (a fonte não informa a unidade monetária)
    c_h_total: horas (carga horária total do professor)
    q19: filhos (número)
    q25_a_2: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária)
    q25_b_2: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária)
    q25_c_2: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária)
    q25_d_2: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária)
    q35_a_3: horas semanais por fonte pagadora
    q25_b_3: horas semanais por fonte pagadora
    q25_c_3: horas semanais por fonte pagadora
    q25_d_3: horas semanais por fonte pagadora
    q3_dia: data de nascimento (dia, mês ou ano)
    q3_mes: data de nascimento (dia, mês ou ano)
    q3_ano: data de nascimento (dia, mês ou ano)
    q43_a_1: tempo (anos ou meses, conforme a descrição)
    q43_a_2: tempo (anos ou meses, conforme a descrição)
    q43_b_1: tempo (anos ou meses, conforme a descrição)
    q43_b_2: tempo (anos ou meses, conforme a descrição)
    q44_1: tempo (anos ou meses, conforme a descrição)
    q44_2: tempo (anos ou meses, conforme a descrição)
  dados_pessoais:
  - coluna: campo_chave
    categoria: identificador do profissional na base
  - coluna: q3_dia
    categoria: data de nascimento
  - coluna: q3_mes
    categoria: data de nascimento
  - coluna: q3_ano
    categoria: data de nascimento
  - coluna: q11
    categoria: município e UF do endereço do profissional
  - coluna: q12
    categoria: município e UF do endereço do profissional
  - coluna: q16
    categoria: sexo
  - coluna: q17
    categoria: cor ou raça declarada
  - coluna: q18
    categoria: estado civil e número de filhos
  - coluna: q19
    categoria: estado civil e número de filhos
  - coluna: q66
    categoria: endereço eletrônico do profissional
  - coluna: q25_a_2
    categoria: salário bruto e carga horária individuais
  - coluna: q35_a_3
    categoria: salário bruto e carga horária individuais
  - coluna: q25_b_2
    categoria: salário bruto e carga horária individuais
  - coluna: q25_b_3
    categoria: salário bruto e carga horária individuais
  - coluna: q25_c_2
    categoria: salário bruto e carga horária individuais
  - coluna: q25_c_3
    categoria: salário bruto e carga horária individuais
  - coluna: q25_d_2
    categoria: salário bruto e carga horária individuais
  - coluna: q25_d_3
    categoria: salário bruto e carga horária individuais
  - coluna: c_h_total
    categoria: salário bruto e carga horária individuais
  - coluna: s_b_total
    categoria: salário bruto e carga horária individuais
  - coluna: q62
    categoria: moradia, número de moradores e renda familiar
  - coluna: q63
    categoria: moradia, número de moradores e renda familiar
  - coluna: q64
    categoria: moradia, número de moradores e renda familiar
  eras:
  - desde: '2003'
    mudanca: edição única; o Leia-me tem a data de 2006 e a anotação de versão revisada em 2025
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Censo dos Profissionais do Magistério da Educação Básica 2003 — microdados

## Resumo

Microdados do Censo dos Profissionais do Magistério da Educação Básica de 2003, realizado pelo Inep para atualizar os dados dos profissionais do magistério e orientar a implementação do Fundo de Manutenção e de Desenvolvimento do Ensino Fundamental e de Valorização do Magistério (Fundef). Cada registro é um profissional que respondeu ao questionário: identificação e perfil, situação contratual, vencimentos, níveis de atuação, formação e experiência, capacitação, uso de recursos, ocorrências na escola e condições de vida. O levantamento foi planejado como censo, mas não alcançou a cobertura prevista (ver Cuidados). É uma edição única; não há outros anos.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/censo-magisterio` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-dos-profissionais-do-magisterio |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | edição única, 2003 (não se repetiu) |
| Cobertura | 2003 a 2003 |
| Unidade (uma linha) | um profissional do magistério da educação básica que respondeu ao questionário |
| Granularidade | espacial: profissional, com a escola em que leciona (máscara da escola, município, UF, região, rede, dependência administrativa e localização) e o município e a UF do endereço do profissional; temporal: 2003; os vencimentos referem-se a setembro de 2003 |
| Formato bruto | ZIP com uma pasta de dados (um CSV com ponto e vírgula, não em UTF-8, lido como latin-1) e o Leia-me em PDF, que traz a nota técnica, o dicionário de variáveis e o questionário |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | `campo_chave` |
| Colunas | 240 |
| Unidades de medida | `s_b_total`: valor monetário bruto de setembro de 2003 (a fonte não informa a unidade monetária); `c_h_total`: horas (carga horária total do professor); `q19`: filhos (número); `q25_a_2`: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária); `q25_b_2`: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária); `q25_c_2`: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária); `q25_d_2`: valor monetário bruto de setembro de 2003 por fonte pagadora (a fonte não informa a unidade monetária); `q35_a_3`: horas semanais por fonte pagadora; `q25_b_3`: horas semanais por fonte pagadora; `q25_c_3`: horas semanais por fonte pagadora; `q25_d_3`: horas semanais por fonte pagadora; `q3_dia`: data de nascimento (dia, mês ou ano); `q3_mes`: data de nascimento (dia, mês ou ano); `q3_ano`: data de nascimento (dia, mês ou ano); `q43_a_1`: tempo (anos ou meses, conforme a descrição); `q43_a_2`: tempo (anos ou meses, conforme a descrição); `q43_b_1`: tempo (anos ou meses, conforme a descrição); `q43_b_2`: tempo (anos ou meses, conforme a descrição); `q44_1`: tempo (anos ou meses, conforme a descrição); `q44_2`: tempo (anos ou meses, conforme a descrição) |
| Dados pessoais | `campo_chave` (identificador do profissional na base); `q3_dia` (data de nascimento); `q3_mes` (data de nascimento); `q3_ano` (data de nascimento); `q11` (município e UF do endereço do profissional); `q12` (município e UF do endereço do profissional); `q16` (sexo); `q17` (cor ou raça declarada); `q18` (estado civil e número de filhos); `q19` (estado civil e número de filhos); `q66` (endereço eletrônico do profissional); `q25_a_2` (salário bruto e carga horária individuais); `q35_a_3` (salário bruto e carga horária individuais); `q25_b_2` (salário bruto e carga horária individuais); `q25_b_3` (salário bruto e carga horária individuais); `q25_c_2` (salário bruto e carga horária individuais); `q25_c_3` (salário bruto e carga horária individuais); `q25_d_2` (salário bruto e carga horária individuais); `q25_d_3` (salário bruto e carga horária individuais); `c_h_total` (salário bruto e carga horária individuais); `s_b_total` (salário bruto e carga horária individuais); `q62` (moradia, número de moradores e renda familiar); `q63` (moradia, número de moradores e renda familiar); `q64` (moradia, número de moradores e renda familiar) |
| Eras | 2003: edição única; o Leia-me tem a data de 2006 e a anotação de versão revisada em 2025 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_censo_profissionais_do_magisterio_2003.zip` (uma única edição).
- No bruto, o arquivo se chama `censo-magisterio/censo-magisterio-microdados_2003@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- O ZIP tem a pasta `dados` com `microdados_censo_professor_2003.csv` (807 MB descompactado, lido no índice do ZIP em 2026-11-15) e o arquivo de checksum, e a pasta `leia-me` com `LEIA-ME.pdf` (1,4 MB). O Leia-me tem a capa "Brasília, 2006" e a anotação "Versão revisada em 2025".
- O Leia-me é o único documento do ZIP: não há dicionário em planilha. As descrições do lake vêm do dicionário de variáveis dentro do Leia-me.

## Conteúdo

- Um único arquivo (`microdados_censo_professor_2003`), com uma linha por profissional respondente e 241 colunas (incluída a partição `ano`).
- **Controle da escola:** `campo_chave`, `mascara_esc`, `ano_mascara`, `codmunic_esc`, `uf_esc`, `sigla`, `mun_esc`, `reg`, `rede`, `dep`, `loc1`, `loc2`. A combinação `ano_mascara` + `mascara_esc`, informa o Leia-me, permite obter os dados da escola nos microdados do Censo Escolar.
- **Bloco I, identificação:** data de nascimento (quesito 3), município e UF do endereço (11 e 12), sexo, cor ou raça, estado civil e número de filhos (16 a 19); os demais quesitos do bloco não estão no CSV.
- **Bloco II, situação contratual, vencimentos e níveis de atuação:** regência de sala de aula, função, níveis e modalidades em que atua, disciplinas que ministra, vencimentos, fonte pagadora, carga horária semanal e situação contratual por rede (quesitos 20 a 27).
- **Bloco III do dicionário, formação acadêmica e experiência profissional (quesitos 28 a 58):** formação, cursos que frequenta, pós-graduação, tempo de magistério e na escola, turnos, capacitação continuada (quem promoveu, carga horária, avaliação, conteúdos), uso de recursos com os alunos e ocorrências na escola.
- **Bloco VI do dicionário, condições socioeconômicas (quesitos 59 a 66):** situação socioeconômica dos alunos, atividades fora do trabalho, objetos e moradia, número de moradores, renda familiar, satisfação profissional e endereço eletrônico.
- **Bloco VII, variáveis agregadas:** `c_h_total` (carga horária total do professor) e `s_b_total` (salário bruto total do professor); `autorizacao` registra a autorização para inscrição no Sistema Nacional de Certificação e Formação Continuada de Professores da Educação Básica.
- O CSV não traz nome, número de identidade, órgão expedidor, endereço (rua, número, complemento e bairro), CEP, DDD nem telefone, que constam do questionário (quesitos 2, 4 a 10 e 13 a 15); a fonte não os lista no dicionário.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2003 | `microdados_censo_professor` (240) |

## Variáveis

As descrições vêm do dicionário de variáveis do Leia-me (PDF). Os nomes das colunas seguem o número do quesito do questionário (`q23_a_1` é o quesito 23, item a, opção 1); o texto da pergunta está na descrição e os códigos das respostas estão no Leia-me.
Nos quesitos de marcação múltipla (`q23_*`, `q24_*`), o dicionário lista 1 = atua ou ministra e 0 = não marcou; nos de escolha única, 0 = não marcou. Os códigos que cabem em poucas palavras estão entre parênteses na descrição; as demais listas de categorias estão no Leia-me.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `campo_chave` | `CAMPO_CHAVE` | texto | Identifica o profissional do magistério da educação básica | — | todo |
| `mascara_esc` | `MASCARA_ESC` | texto | possível obter os dados estatísticos da escola a partir dos microdados do Censo da | — | todo |
| `ano_mascara` | `ANO_MASCARA` | texto | Ano da máscara da escola em que o profissional leciona | — | todo |
| `codmunic_esc` | `CODMUNIC_ESC` | texto | 3º e 4º dígitos: mesoregião; | — | todo |
| `uf_esc` | `UF_ESC` | texto | Nome da Unidade da Federação da escola | — | todo |
| `sigla` | `SIGLA` | texto | Sigla da UF da escola | — | todo |
| `mun_esc` | `MUN_ESC` | texto | Nome do município da escola em que leciona | — | todo |
| `reg` | `REG` | texto | Região da escola leciona | — | todo |
| `rede` | `REDE` | texto | Rede (1 = pública; 2 = privada) | — | todo |
| `dep` | `DEP` | texto | Dependencia administrativa da escola em que leciona (1 = federal; 2 = estadual; 3 = municipal; 4 = privada) | — | todo |
| `loc1` | `LOC1` | texto | Localização da escola em que leciona(Rural e Urbana) (1 = rural; 2 = urbana) | — | todo |
| `loc2` | `LOC2` | texto | Localização da escola em que leciona (Capital e Interior) (1 = capital; 2 = interior) | — | todo |
| `q3_dia` | `Q3_DIA` | texto | Data de nascimento - dia | — | todo |
| `q3_mes` | `Q3_MES` | texto | Data de nascimento - mês | — | todo |
| `q3_ano` | `Q3_ANO` | texto | Data de nascimento - ano | — | todo |
| `q11` | `Q11` | texto | Município (quesito 11 do questionário, logo após o endereço do profissional) | — | todo |
| `q12` | `Q12` | texto | UF (quesito 12 do questionário, logo após o município do endereço do profissional) | — | todo |
| `q16` | `Q16` | texto | Sexo (M = masculino; F = feminino) | — | todo |
| `q17` | `Q17` | texto | Em relação à cor ou à raça, como você se considera (0 = não marcou; 1 = branco(a); 2 = pardo(a); 3 = preto(a); 4 = amarelo(a); 5 = indígena) | — | todo |
| `q18` | `Q18` | texto | Estado Civil (0 = não marcou; 1 = solteiro; 2 = casado ou com companheiro(a); 3 = divorciado, desquitado ou separado; 4 = viúvo(a)) | — | todo |
| `q19` | `Q19` | texto | Número de Filhos | — | todo |
| `q20` | `Q20` | texto | Está em regência de sala de aula (S = sim; N = não) | — | todo |
| `q21` | `Q21` | texto | Está readaptado (S = sim; N = não) | — | todo |
| `q22` | `Q22` | texto | Função principal que exerce nesta escola (0 = não marcou; 1 = coordenador(a) pedagógico; 2 = diretor(a); 3 = outra função pedagógica; 4 = função administrativa; 5 = especialista; 6 = outra função na escola) | — | todo |
| `q23_a_1` | `Q23_A_1` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Creche (1 = atua; 0 = não marcou) | — | todo |
| `q23_a_2` | `Q23_A_2` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Pré-escola (1 = atua; 0 = não marcou) | — | todo |
| `q23_a_3` | `Q23_A_3` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Classe de Alfabetização (1 = atua; 0 = não marcou) | — | todo |
| `q23_a_4` | `Q23_A_4` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Fundamental 1ª a 4ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_a_5` | `Q23_A_5` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Fundamental 5ª a 8ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_a_6` | `Q23_A_6` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Regular - Médio (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_1` | `Q23_B_1` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Creche (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_2` | `Q23_B_2` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Pré- escola (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_3` | `Q23_B_3` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Classe de Alfabetização (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_4` | `Q23_B_4` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Fundamental 1ª a 4ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_5` | `Q23_B_5` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Fundamental 5ª a 8ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_b_6` | `Q23_B_6` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Especial - Médio (1 = atua; 0 = não marcou) | — | todo |
| `q23_c_1` | `Q23_C_1` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação de Jovens e Adultos - Alfabetização (1 = atua; 0 = não marcou) | — | todo |
| `q23_c_2` | `Q23_C_2` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação de Jovens e Adultos - Fundamental 1ª a 4ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_c_3` | `Q23_C_3` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação de Jovens e Adultos - Fundamental 5ª a 8ª série (1 = atua; 0 = não marcou) | — | todo |
| `q23_c_4` | `Q23_C_4` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação de Jovens e Adultos - Médio (1 = atua; 0 = não marcou) | — | todo |
| `q23_d_1` | `Q23_D_1` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Profissional - Nível básico (1 = atua; 0 = não marcou) | — | todo |
| `q23_d_2` | `Q23_D_2` | texto | Níveis e/ou modalidades de ensino em que atua nesta escola - Educação Profissional - Nível técnico (1 = atua; 0 = não marcou) | — | todo |
| `q24_1` | `Q24_1` | texto | Informe as disciplinas que ministra - Química (1 = ministra; 0 = não marcou) | — | todo |
| `q24_2` | `Q24_2` | texto | Informe as disciplinas que ministra - Física (1 = ministra; 0 = não marcou) | — | todo |
| `q24_3` | `Q24_3` | texto | Informe as disciplinas que ministra - Biologia (1 = ministra; 0 = não marcou) | — | todo |
| `q24_4` | `Q24_4` | texto | Informe as disciplinas que ministra - Matemática (1 = ministra; 0 = não marcou) | — | todo |
| `q24_5` | `Q24_5` | texto | Informe as disciplinas que ministra - Ciências (1 = ministra; 0 = não marcou) | — | todo |
| `q24_6` | `Q24_6` | texto | Informe as disciplinas que ministra - Língua Inglesa (1 = ministra; 0 = não marcou) | — | todo |
| `q24_7` | `Q24_7` | texto | Informe as disciplinas que ministra - Língua Espanhola (1 = ministra; 0 = não marcou) | — | todo |
| `q24_8` | `Q24_8` | texto | Informe as disciplinas que ministra - Língua Francesa (1 = ministra; 0 = não marcou) | — | todo |
| `q24_9` | `Q24_9` | texto | Informe as disciplinas que ministra - Outra língua estrangeira (1 = ministra; 0 = não marcou) | — | todo |
| `q24_10` | `Q24_10` | texto | Informe as disciplinas que ministra - Artes (1 = ministra; 0 = não marcou) | — | todo |
| `q24_11` | `Q24_11` | texto | Informe as disciplinas que ministra - Psicologia (1 = ministra; 0 = não marcou) | — | todo |
| `q24_12` | `Q24_12` | texto | Informe as disciplinas que ministra - Didática (1 = ministra; 0 = não marcou) | — | todo |
| `q24_13` | `Q24_13` | texto | Informe as disciplinas que ministra - Educação Física (1 = ministra; 0 = não marcou) | — | todo |
| `q24_14` | `Q24_14` | texto | Informe as disciplinas que ministra - História (1 = ministra; 0 = não marcou) | — | todo |
| `q24_15` | `Q24_15` | texto | Informe as disciplinas que ministra - Geografia (1 = ministra; 0 = não marcou) | — | todo |
| `q24_16` | `Q24_16` | texto | Informe as disciplinas que ministra - Filosofia (1 = ministra; 0 = não marcou) | — | todo |
| `q24_17` | `Q24_17` | texto | Informe as disciplinas que ministra - Educação Religiosa (1 = ministra; 0 = não marcou) | — | todo |
| `q24_18` | `Q24_18` | texto | Informe as disciplinas que ministra - Sociologia (1 = ministra; 0 = não marcou) | — | todo |
| `q24_19` | `Q24_19` | texto | Informe as disciplinas que ministra - Estudos Sociais (1 = ministra; 0 = não marcou) | — | todo |
| `q24_20` | `Q24_20` | texto | Informe as disciplinas que ministra - Língua Indígena (1 = ministra; 0 = não marcou) | — | todo |
| `q24_21` | `Q24_21` | texto | Informe as disciplinas que ministra - Outra disciplina (1 = ministra; 0 = não marcou) | — | todo |
| `q24_22` | `Q24_22` | texto | Informe as disciplinas que ministra - Língua Portuguesa ou Literatura de Língua Portuguesa (1 = ministra; 0 = não marcou) | — | todo |
| `q24_23` | `Q24_23` | texto | Informe as disciplinas que ministra - Outras (1 = ministra; 0 = não marcou) | — | todo |
| `q25_a_1` | `Q25_A_1` | texto | Fonte pagadora (Rede Federal) | — | todo |
| `q25_a_2` | `Q25_A_2` | texto | Salário Bruto (Rede Federal) | — | todo |
| `q35_a_3` | `Q35_A_3` | texto | Carga Horária Semanal (Rede Federal) (nome como aparece no cabeçalho do CSV e no dicionário, na posição de Q25_a_3) | — | todo |
| `q25_a_4` | `Q25_A_4` | texto | Situação contratual ou de vínculo (Rede Federal) | — | todo |
| `q25_b_1` | `Q25_B_1` | texto | Fonte pagadora (Rede Estadual) | — | todo |
| `q25_b_2` | `Q25_B_2` | texto | Salário Bruto (Rede Estadual) | — | todo |
| `q25_b_3` | `Q25_B_3` | texto | Carga Horária Semanal (Rede Estadual) | — | todo |
| `q25_b_4` | `Q25_B_4` | texto | Situação contratual ou de vínculo (Rede Estadual) | — | todo |
| `q25_c_1` | `Q25_C_1` | texto | Fonte pagadora (Rede Municipal) | — | todo |
| `q25_c_2` | `Q25_C_2` | texto | Salário Bruto (Rede Municipal) | — | todo |
| `q25_c_3` | `Q25_C_3` | texto | Carga Horária Semanal (Rede Municipal) | — | todo |
| `q25_c_4` | `Q25_C_4` | texto | Situação contratual ou de vínculo (Rede Municipal) | — | todo |
| `q25_d_1` | `Q25_D_1` | texto | Fonte pagadora (Rede Privada) | — | todo |
| `q25_d_2` | `Q25_D_2` | texto | Salário Bruto (Rede Privada) | — | todo |
| `q25_d_3` | `Q25_D_3` | texto | Carga Horária Semanal (Rede Privada) | — | todo |
| `q25_d_4` | `Q25_D_4` | texto | Situação contratual ou de vínculo (Rede Privada) | — | todo |
| `q26` | `Q26` | texto | Você tem outra atividade assalariada fora do magistério (quesito 26 do questionário) | — | todo |
| `q27` | `Q27` | texto | A atividade assalariada fora do magistério é mais rendosa | — | todo |
| `q28` | `Q28` | texto | Qual o grau de formação abaixo representa o seu nível de escolaridade | — | todo |
| `q29_a` | `Q29_A` | texto | Possui formação de conteúdo de Educação Especial - em Nível Médio | — | todo |
| `q29_b` | `Q29_B` | texto | Possui formação de conteúdo de Educação Especial - em Nível Superior | — | todo |
| `q30` | `Q30` | texto | Atualmente freqüenta algum curso de Nível Médio | — | todo |
| `q31` | `Q31` | texto | O curso que freqüenta é na Modalidade Normal | — | todo |
| `q32` | `Q32` | texto | O curso que freqüenta é em escola indígena | — | todo |
| `q33_a_1` | `Q33_A_1` | texto | Código do Curso de formação acadêmica | — | todo |
| `q33_b_1` | `Q33_B_1` | texto | Código do Curso de formação acadêmica | — | todo |
| `q34_a` | `Q34_A` | texto | Ano de Conclusão do Curso de formação acadêmica | — | todo |
| `q34_b` | `Q34_B` | texto | Ano de Conclusão do Curso de formação acadêmica | — | todo |
| `q35_a` | `Q35_A` | texto | Dependência Administrativa da Instituição de formação acadêmica | — | todo |
| `q35_b` | `Q35_B` | texto | Dependência Administrativa da Instituição de formação acadêmica | — | todo |
| `q36` | `Q36` | texto | Atualmente freqüenta algum curso superior de graduação | — | todo |
| `q37` | `Q37` | texto | O curso de graduação que freqüenta é de licenciatura | — | todo |
| `q38` | `Q38` | texto | Qual a dependência administrativa da instituição em que freqüenta o curso de graduação | — | todo |
| `q39` | `Q39` | texto | Código do Curso de graduação que freqüenta | — | todo |
| `q40` | `Q40` | texto | Entre as modalidades de cursos de pós-graduação abaixo, marque a opção que corresponde ao curso de mais alta titulação que você possui | — | todo |
| `q41` | `Q41` | texto | Qual o ano de conclusão do curso de pós-graduação | — | todo |
| `q42` | `Q42` | texto | Qual a dependência administrativa da instituição em que fez o curso de pós-graduação | — | todo |
| `q43_a_1` | `Q43_A_1` | texto | Alguma função do magistério da Educação Básica - Anos | — | todo |
| `q43_a_2` | `Q43_A_2` | texto | Alguma função do magistério da Educação Básica - Meses | — | todo |
| `q43_b_1` | `Q43_B_1` | texto | A função atual - Anos | — | todo |
| `q43_b_2` | `Q43_B_2` | texto | A função atual - Meses | — | todo |
| `q44_1` | `Q44_1` | texto | Há quantos anos você trabalha nesta escola - Anos | — | todo |
| `q44_2` | `Q44_2` | texto | Há quantos anos você trabalha nesta escola - Meses | — | todo |
| `q45` | `Q45` | texto | Em quantas escolas você trabalha | — | todo |
| `q46_1` | `Q46_1` | texto | Em quais turnos você trabalha no exercício da atividade docente - Manhã | — | todo |
| `q46_2` | `Q46_2` | texto | Em quais turnos você trabalha no exercício da atividade docente - Tarde | — | todo |
| `q46_3` | `Q46_3` | texto | Em quais turnos você trabalha no exercício da atividade docente - Noite | — | todo |
| `q46_4` | `Q46_4` | texto | Em quais turnos você trabalha no exercício da atividade docente - Intermediário | — | todo |
| `q47` | `Q47` | texto | Considerando sua jornada de trabalho semanal nesta escola, quantas horas são dedicadas exclusivamente a atividades em sala de aula | — | todo |
| `q48` | `Q48` | texto | Você participa ou participou de alguma atividade ou curso de formação continuada nos últimos 2 anos | — | todo |
| `q49_1` | `Q49_1` | texto | Esta capacitação foi - Presencial | — | todo |
| `q49_2` | `Q49_2` | texto | Esta capacitação foi - A Distância | — | todo |
| `q49_3` | `Q49_3` | texto | Esta capacitação foi - Semipresencial | — | todo |
| `q50_1` | `Q50_1` | texto | Qual a carga horária total dessa capacitação - horas (Presencial) | — | todo |
| `q50_2` | `Q50_2` | texto | Qual a carga horária total dessa capacitação - horas (à distancia) | — | todo |
| `q50_3` | `Q50_3` | texto | Qual a carga horária total dessa capacitação - horas (semipresencial) | — | todo |
| `q51_1` | `Q51_1` | texto | Quem promoveu a capacitação - MEC | — | todo |
| `q51_2` | `Q51_2` | texto | Quem promoveu a capacitação - Secretaria Municipal de Educação | — | todo |
| `q51_3` | `Q51_3` | texto | Quem promoveu a capacitação - Secretaria Estadual de Educação | — | todo |
| `q51_4` | `Q51_4` | texto | Quem promoveu a capacitação - A própria escola | — | todo |
| `q51_5` | `Q51_5` | texto | Quem promoveu a capacitação - Instituição de Ensino Superior Privada | — | todo |
| `q51_6` | `Q51_6` | texto | Quem promoveu a capacitação - Instituição de Ensino Superior Pública | — | todo |
| `q51_7` | `Q51_7` | texto | Quem promoveu a capacitação - ONG | — | todo |
| `q51_8` | `Q51_8` | texto | Quem promoveu a capacitação - Sindicatos | — | todo |
| `q52` | `Q52` | texto | Qual a sua avaliação sobre a qualidade dessa capacitação | — | todo |
| `q53` | `Q53` | texto | Qual a sua avaliação dessa formação para melhoria da sua prática pedagógica | — | todo |
| `q54_1` | `Q54_1` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Sexualidade, direitos reprodutivos, gênero, prevenção DST/AIDS | — | todo |
| `q54_2` | `Q54_2` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Língua Indígena | — | todo |
| `q54_3` | `Q54_3` | texto | você participou: Educação para a paz e não-discriminatória, prevenção da violência e do | — | todo |
| `q54_4` | `Q54_4` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Princípios da Avaliação | — | todo |
| `q54_5` | `Q54_5` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Nova metodologias de ensino | — | todo |
| `q54_6` | `Q54_6` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Conteúdo das disciplinas que você leciona | — | todo |
| `q54_7` | `Q54_7` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Planejamento/Projeto de trabalho | — | todo |
| `q54_8` | `Q54_8` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Mediação de conflitos | — | todo |
| `q54_9` | `Q54_9` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Aspectos da Gestão Escolar | — | todo |
| `q54_10` | `Q54_10` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: E.C.A | — | todo |
| `q54_11` | `Q54_11` | texto | Esse conteúdo relacionado foi o que melhor representou o curso de capacitação que você participou: Alfabetização | — | todo |
| `q55_a` | `Q55_A` | texto | Você participou de capacitação para o uso das seguintes tecnologias - TV e Vídeo | — | todo |
| `q55_b` | `Q55_B` | texto | Você participou de capacitação para o uso das seguintes tecnologias - Computador | — | todo |
| `q55_c` | `Q55_C` | texto | Você participou de capacitação para o uso das seguintes tecnologias - Internet | — | todo |
| `q55_d` | `Q55_D` | texto | Você participou de capacitação para o uso das seguintes tecnologias - Rádio | — | todo |
| `q56_a` | `Q56_A` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Quadro magnético/quadro branco | — | todo |
| `q56_b` | `Q56_B` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Livro didático | — | todo |
| `q56_c` | `Q56_C` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Biblioteca | — | todo |
| `q56_d` | `Q56_D` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Jornais e/ou Revistas | — | todo |
| `q56_e` | `Q56_E` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - TV/Vídeo | — | todo |
| `q56_f` | `Q56_F` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Retroprojetor | — | todo |
| `q56_g` | `Q56_G` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - DataShow | — | todo |
| `q56_h` | `Q56_H` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Computador | — | todo |
| `q56_i` | `Q56_I` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Internet | — | todo |
| `q56_j` | `Q56_J` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Laboratório de Informática | — | todo |
| `q56_k` | `Q56_K` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Laboratório de Ciências/Física/Química/Biologia | — | todo |
| `q56_l` | `Q56_L` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Material esportivo | — | todo |
| `q56_m` | `Q56_M` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Instrumentos musicais | — | todo |
| `q56_n` | `Q56_N` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Copiadora/Mimeógrafo | — | todo |
| `q56_o` | `Q56_O` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Brinquedos | — | todo |
| `q56_p` | `Q56_P` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Materiais para artes | — | todo |
| `q56_q` | `Q56_Q` | texto | Com que freqüência você usa os seguintes recursos com seus alunos - Plataforma PROINFO de Ensino a Distância | — | todo |
| `q57_1` | `Q57_1` | texto | Quais os programas de TV/Vídeo que mais utiliza - Programas da TV Escola | — | todo |
| `q57_2` | `Q57_2` | texto | Quais os programas de TV/Vídeo que mais utiliza - Programas do Salto para o Futuro | — | todo |
| `q57_3` | `Q57_3` | texto | Quais os programas de TV/Vídeo que mais utiliza - Programas da TV Educativa | — | todo |
| `q57_4` | `Q57_4` | texto | Quais os programas de TV/Vídeo que mais utiliza - Programas do canal Futura | — | todo |
| `q57_5` | `Q57_5` | texto | Quais os programas de TV/Vídeo que mais utiliza - Programas de TV comercial | — | todo |
| `q57_6` | `Q57_6` | texto | Quais os programas de TV/Vídeo que mais utiliza - Fitas alugadas ou cedidas | — | todo |
| `q57_7` | `Q57_7` | texto | Quais os programas de TV/Vídeo que mais utiliza - Não utilizo | — | todo |
| `q57_8` | `Q57_8` | texto | Quais os programas de TV/Vídeo que mais utiliza - Outros | — | todo |
| `q58_a` | `Q58_A` | texto | Ocorreu na Escola - Insuficiência de recursos financeiros e materiais | — | todo |
| `q58_b` | `Q58_B` | texto | Ocorreu na Escola - Falta de professores para alguma disciplina | — | todo |
| `q58_c` | `Q58_C` | texto | Ocorreu na Escola - Carência de pessoal de apoio pedagógico | — | todo |
| `q58_d` | `Q58_D` | texto | Ocorreu na Escola - Falta de recursos pedagógicos | — | todo |
| `q58_e` | `Q58_E` | texto | Ocorreu na Escola - Interrupção das atividades escolares | — | todo |
| `q58_f` | `Q58_F` | texto | Ocorreu na Escola - Muitas faltas por parte dos alunos | — | todo |
| `q58_g` | `Q58_G` | texto | Ocorreu na Escola - Muitas faltas por parte dos professores | — | todo |
| `q58_h` | `Q58_H` | texto | Ocorreu na Escola - Rotatividade do corpo docente | — | todo |
| `q58_i` | `Q58_I` | texto | Ocorreu na Escola - Agressão física de professores/funcionários contra alunos | — | todo |
| `q58_j` | `Q58_J` | texto | Ocorreu na Escola - Agressão física entre alunos | — | todo |
| `q58_k` | `Q58_K` | texto | Ocorreu na Escola - Agressão física de alunos contra professores/funcionários | — | todo |
| `q58_l` | `Q58_L` | texto | Ocorreu na Escola - Agressão física contra alunos/professores/funcionários por pessoas de fora | — | todo |
| `q58_m` | `Q58_M` | texto | Ocorreu na Escola - Depredação da escola por pessoas de dentro da escola | — | todo |
| `q58_n` | `Q58_N` | texto | Ocorreu na Escola - Depredação da escola por estranhos | — | todo |
| `q58_o` | `Q58_O` | texto | Ocorreu na Escola - Roubos/furtos por pessoas de dentro da escola | — | todo |
| `q58_p` | `Q58_P` | texto | Ocorreu na Escola - Roubos/furtos por pessoas de fora | — | todo |
| `q58_q` | `Q58_Q` | texto | Ocorreu na Escola - Alunos sobre efeitos de drogas ilícitas | — | todo |
| `q58_r` | `Q58_R` | texto | Ocorreu na Escola - Tráfico de drogas nas dependências da escola | — | todo |
| `q58_s` | `Q58_S` | texto | Ocorreu na Escola - Situações de preconceitos/discriminação de gênero/raça | — | todo |
| `q58_t` | `Q58_T` | texto | Ocorreu na Escola - Porte de armas de fogo por alunos nas dependências da escola | — | todo |
| `q58_u` | `Q58_U` | texto | Ocorreu na Escola - Porte de armas brancas por alunos nas dependências da escola | — | todo |
| `q58_v` | `Q58_V` | texto | Ocorreu na Escola - Alunos alcoolizados | — | todo |
| `q59` | `Q59` | texto | É possível, na sua avaliação, caracterizar a situação socioeconômica da maioria dos alunos desta escola | — | todo |
| `q60_1` | `Q60_1` | texto | Atividades que freqüenta fora do ambiente de trabalho - Leitura de livros | — | todo |
| `q60_2` | `Q60_2` | texto | Atividades que freqüenta fora do ambiente de trabalho - Leitura de jornais e/ou revistas | — | todo |
| `q60_3` | `Q60_3` | texto | Atividades que freqüenta fora do ambiente de trabalho - Participa de atividades religiosas/Igreja | — | todo |
| `q60_4` | `Q60_4` | texto | Atividades que freqüenta fora do ambiente de trabalho - Vai a shows/festas | — | todo |
| `q60_5` | `Q60_5` | texto | Atividades que freqüenta fora do ambiente de trabalho - Assiste a filmes em cinema | — | todo |
| `q60_6` | `Q60_6` | texto | Atividades que freqüenta fora do ambiente de trabalho - Navega na Internet | — | todo |
| `q60_7` | `Q60_7` | texto | Atividades que freqüenta fora do ambiente de trabalho - Pratica atividades físicas, desportiva ou recreativa | — | todo |
| `q60_8` | `Q60_8` | texto | Atividades que freqüenta fora do ambiente de trabalho - Assiste a programas em TV comercial | — | todo |
| `q60_9` | `Q60_9` | texto | Atividades que freqüenta fora do ambiente de trabalho - Assiste a peças teatrais | — | todo |
| `q60_10` | `Q60_10` | texto | Atividades que freqüenta fora do ambiente de trabalho - Assiste a filmes e/ou programas de TV a cabo | — | todo |
| `q60_11` | `Q60_11` | texto | Atividades que freqüenta fora do ambiente de trabalho - Assiste a filmes em casa | — | todo |
| `q60_12` | `Q60_12` | texto | Atividades que freqüenta fora do ambiente de trabalho - Participa de atividades político e partidárias | — | todo |
| `q60_13` | `Q60_13` | texto | Atividades que freqüenta fora do ambiente de trabalho - Freqüenta clube | — | todo |
| `q60_14` | `Q60_14` | texto | Atividades que freqüenta fora do ambiente de trabalho - Participa de atividades comunitárias | — | todo |
| `q60_15` | `Q60_15` | texto | Atividades que freqüenta fora do ambiente de trabalho - Participa de atividades sindicais | — | todo |
| `q60_16` | `Q60_16` | texto | Atividades que freqüenta fora do ambiente de trabalho - Atua em ONG's | — | todo |
| `q60_17` | `Q60_17` | texto | Atividades que freqüenta fora do ambiente de trabalho - Participa de outras atividades | — | todo |
| `q61_a` | `Q61_A` | texto | Na sua casa existem estes objetos - Aparelho de TV | — | todo |
| `q61_b` | `Q61_B` | texto | Na sua casa existem estes objetos - Aparelho de DVD | — | todo |
| `q61_c` | `Q61_C` | texto | Na sua casa existem estes objetos - Secadora de roupa | — | todo |
| `q61_d` | `Q61_D` | texto | Na sua casa existem estes objetos - Máquina de lavar roupa | — | todo |
| `q61_e` | `Q61_E` | texto | Na sua casa existem estes objetos - Telefone celular | — | todo |
| `q61_f` | `Q61_F` | texto | Na sua casa existem estes objetos - Videocassete | — | todo |
| `q61_g` | `Q61_G` | texto | Na sua casa existem estes objetos - Fogão a gás | — | todo |
| `q61_h` | `Q61_H` | texto | Na sua casa existem estes objetos - Rádio | — | todo |
| `q61_i` | `Q61_I` | texto | Na sua casa existem estes objetos - Forno de microondas | — | todo |
| `q61_j` | `Q61_J` | texto | Na sua casa existem estes objetos - Microcomputador | — | todo |
| `q61_k` | `Q61_K` | texto | Na sua casa existem estes objetos - Motocicleta | — | todo |
| `q61_l` | `Q61_L` | texto | Na sua casa existem estes objetos - Automóvel | — | todo |
| `q61_m` | `Q61_M` | texto | Na sua casa existem estes objetos - Máquina de lavar louça | — | todo |
| `q61_n` | `Q61_N` | texto | Na sua casa existem estes objetos - Aspirador de pó | — | todo |
| `q61_o` | `Q61_O` | texto | Na sua casa existem estes objetos - Geladeira | — | todo |
| `q61_p` | `Q61_P` | texto | Na sua casa existem estes objetos - Freezer | — | todo |
| `q61_q` | `Q61_Q` | texto | Na sua casa existem estes objetos - Telefone fixo | — | todo |
| `q61_r` | `Q61_R` | texto | Na sua casa existem estes objetos - Aparelho de som | — | todo |
| `q61_s` | `Q61_S` | texto | Na sua casa existem estes objetos - Bicicleta | — | todo |
| `q61_t` | `Q61_T` | texto | Na sua casa existem estes objetos - Ar-condicionado | — | todo |
| `q61_u` | `Q61_U` | texto | Na sua casa existem estes objetos - Aquecedor | — | todo |
| `q62` | `Q62` | texto | Você mora em casa | — | todo |
| `q63` | `Q63` | texto | Quantas pessoas moram com você | — | todo |
| `q64` | `Q64` | texto | aproximadamente a renda familiar da casa | — | todo |
| `q65` | `Q65` | texto | Considerando sua situação atual, como você se considerea no exercício profissional | — | todo |
| `q66` | `Q66` | texto | Endereço eletrônico | — | todo |
| `autorizacao` | `AUTORIZACAO` | texto | Autoriza a inscrição no Sistema Nacional de Certificação e Formação Continuada de Professores da Educação Básica (S = sim; N = não) | — | todo |
| `c_h_total` | `C_H_TOTAL` | texto | Carga horária total do professor (variável agregada) | — | todo |
| `s_b_total` | `S_B_TOTAL` | texto | Salário bruto total do professor (variável agregada) | — | todo |

## No lake

- Dataset `inep/censo-magisterio`, particionado por `ano` (só `ano=2003`); um Parquet, `censo-magisterio-microdados_2003__microdados_censo_professor_2003.parquet`.
- Todas as colunas são texto: o DuckDB lê o CSV sem inferir tipos, e os nomes saem normalizados (minúsculas). Valores decimais usam ponto (por exemplo, `935.00`).
- A coluna `ano` é a edição, tirada do nome do arquivo; `ano_mascara` é o ano da máscara da escola.
- O arquivo de checksum (`md5_*.txt`) é ignorado.

## Cuidados de uso

- **Não é um censo completo nem uma amostra planejada.** A Nota Técnica do Leia-me informa que o levantamento, planejado como censitário, não alcançou esse objetivo por problemas operacionais: responderam 164.780 dos 211.933 estabelecimentos do Censo Escolar 2003 (77,8%) e 1.542.878 profissionais, 61,8% das 2.497.918 funções docentes do Censo Escolar (36,1% na rede federal, 64,8% na estadual, 71,7% na municipal e 36,7% na particular). Distrito Federal (41%) e Rio de Janeiro (48,8%) têm as menores taxas entre as UF; Tocantins (87,4%) e Rio Grande do Norte (80,1%), as maiores.
- **Respondentes voluntários.** O Inep adverte que, sem delineamento amostral prévio, não é possível calcular o erro das estimativas, que médias salariais e de carga horária podem estar super ou subestimadas e que, quanto mais desagregados os dados, menos confiáveis; por isso prefere medianas.
- **Salário respondido por 89,9% dos profissionais.** O quesito de salário teve 1.386.418 respostas entre 1.542.878 respondentes (Tabela 4 da Nota Técnica); `s_b_total` fica vazio para os demais. Na amostra convertida, 1.329 das 1.500 linhas têm `s_b_total`.
- **Duplicidade possível.** O questionário (quesito 1) pergunta se o profissional já respondeu em outra escola; o Leia-me não informa como respostas repetidas de um mesmo profissional foram tratadas.
- **Dados pessoais publicados.** O arquivo traz data de nascimento, sexo, cor ou raça, estado civil, número de filhos, município e UF do endereço, remuneração, renda familiar e, em `q66`, endereço eletrônico informado pelo profissional (preenchido em 502 das 1.500 primeiras linhas). Trate o conjunto como dado pessoal, não o republique linha a linha e não use `q66` para contato.
- **Nome de coluna fora do padrão.** Entre `q25_a_2` e `q25_a_4` o cabeçalho do CSV traz `q35_a_3` (carga horária semanal na rede federal, descrita no dicionário com esse nome) onde se esperaria `q25_a_3`; não há coluna `q25_a_3`. Existem também `q35_a` e `q35_b` (dependência administrativa da instituição de formação), que são outros quesitos.
- **A máscara da escola vale só para 2003.** O Leia-me informa que a mesma `mascara_esc` em anos diferentes não identifica a mesma escola; ligue com o Censo Escolar usando `ano_mascara` e `mascara_esc` e só com os microdados de 2003.
- **Descrições com a pergunta, sem as categorias.** Muitos quesitos de escala (por exemplo `q56_*`, frequência de uso de recursos, ou `q58_*`, ocorrências na escola) têm listas de resposta que estão apenas no Leia-me.
- **Quesitos que não se aplicam a todos.** Segundo o questionário, `q22` não precisa ser respondido por regentes de sala de aula, `q23_*` vale só para professores regentes e `q24_*` só para regentes do ensino fundamental, médio e educação profissional; a ausência de marcação nesses quesitos não é, por si, um zero informativo.

## Exemplos

Número de profissionais e mediana do salário bruto total por sexo (`q16`: M = masculino, F = feminino), com o texto convertido para número; a fonte recomenda medianas e cautela com recortes (ver Cuidados). A consulta usa a amostra do lake; no arquivo completo os números são outros:

```python
import duckdb

duckdb.sql("""
    SELECT q16 AS sexo,
           count(*) AS profissionais,
           count(try_cast(s_b_total AS DOUBLE)) AS com_salario,
           round(median(try_cast(s_b_total AS DOUBLE)), 2) AS mediana_salario_bruto
    FROM read_parquet('lake/inep/censo-magisterio/ano=2003/*.parquet')
    GROUP BY ALL
    ORDER BY sexo
""").show()
```

## Referências

- Microdados do Censo dos Profissionais do Magistério: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-dos-profissionais-do-magisterio
- Leia-me (apresentação, nota técnica, dicionário e questionário), dentro do ZIP em https://download.inep.gov.br/microdados/
