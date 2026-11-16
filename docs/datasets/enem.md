---
dataset:
  id: enem
  fonte: inep
  titulo: Enem — microdados
  resumo: 'Microdados do Exame Nacional do Ensino Médio: participantes, questionário socioeconômico, notas e itens das provas, de 1998 em diante.'
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano, publicada depois da aplicação
  cobertura:
    inicio: '1998'
    fim: '2025'
  unidade: um participante do Enem numa edição (arquivos de participantes e resultados); um item de prova (arquivo de itens)
  granularidade:
    espacial: participante, com escola e UF de aplicação conforme a edição; sem município de residência desde 2024
    temporal: ano da edição
  formato_bruto: ZIP anual com pastas DADOS, DICIONÁRIO, INPUTS e documentos; os dados vêm em CSV com ponto e vírgula (latin-1); o ZIP de 2025 usa compressão Deflate64
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 793
  unidades_de_medida:
    nu_nota_comp1: pontos
    nu_nota_comp2: pontos
    nu_nota_comp3: pontos
    nu_nota_comp4: pontos
    nu_nota_comp5: pontos
    nu_nota_redacao: pontos
    nu_nota_cn: pontos
    nu_nota_ch: pontos
    nu_nota_lc: pontos
    nu_nota_mt: pontos
  dados_pessoais:
  - coluna: nu_inscricao
    categoria: identificador do participante (a fonte o substitui por uma máscara sequencial)
  - coluna: tp_sexo
    categoria: sexo do participante
  - coluna: tp_cor_raca
    categoria: cor ou raça declarada
  - coluna: tp_estado_civil
    categoria: estado civil
  - coluna: tp_faixa_etaria
    categoria: idade ou faixa etária
  - coluna: co_municipio_residencia
    categoria: local de nascimento ou residência
  - coluna: no_municipio_residencia
    categoria: local de nascimento ou residência
  - coluna: co_uf_residencia
    categoria: local de nascimento ou residência
  - coluna: sg_uf_residencia
    categoria: local de nascimento ou residência
  eras:
  - desde: '2009'
    mudanca: 'reformulação do exame: 180 questões objetivas em quatro áreas e redação, em dois dias; surge o arquivo de itens da prova'
  - desde: '2020'
    mudanca: 'modelo simplificado de microdados (LGPD): saem variáveis que facilitavam a identificação do participante'
  - desde: '2024'
    mudanca: o ZIP passa a ter PARTICIPANTES e RESULTADOS, sem chave em comum; NU_IDADE vira TP_FAIXA_ETARIA; saem os municípios de nascimento e de residência; volta o código da escola de conclusão
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Enem — microdados

## Resumo

Microdados anuais do Exame Nacional do Ensino Médio (Enem), publicados pelo Inep. Cada edição traz, por participante, as características informadas na inscrição, as respostas ao questionário socioeconômico e as notas das provas objetivas e da redação; a partir de 2009 traz também um arquivo com os itens das provas. O Inep os descreve como o menor nível de desagregação dos dados do exame.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/enem` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano, publicada depois da aplicação |
| Cobertura | 1998 a 2025 |
| Unidade (uma linha) | um participante do Enem numa edição (arquivos de participantes e resultados); um item de prova (arquivo de itens) |
| Granularidade | espacial: participante, com escola e UF de aplicação conforme a edição; sem município de residência desde 2024; temporal: ano da edição |
| Formato bruto | ZIP anual com pastas DADOS, DICIONÁRIO, INPUTS e documentos; os dados vêm em CSV com ponto e vírgula (latin-1); o ZIP de 2025 usa compressão Deflate64 |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 793 |
| Unidades de medida | `nu_nota_comp1`: pontos; `nu_nota_comp2`: pontos; `nu_nota_comp3`: pontos; `nu_nota_comp4`: pontos; `nu_nota_comp5`: pontos; `nu_nota_redacao`: pontos; `nu_nota_cn`: pontos; `nu_nota_ch`: pontos; `nu_nota_lc`: pontos; `nu_nota_mt`: pontos |
| Dados pessoais | `nu_inscricao` (identificador do participante (a fonte o substitui por uma máscara sequencial)); `tp_sexo` (sexo do participante); `tp_cor_raca` (cor ou raça declarada); `tp_estado_civil` (estado civil); `tp_faixa_etaria` (idade ou faixa etária); `co_municipio_residencia` (local de nascimento ou residência); `no_municipio_residencia` (local de nascimento ou residência); `co_uf_residencia` (local de nascimento ou residência); `sg_uf_residencia` (local de nascimento ou residência) |
| Eras | 2009: reformulação do exame: 180 questões objetivas em quatro áreas e redação, em dois dias; surge o arquivo de itens da prova; 2020: modelo simplificado de microdados (LGPD): saem variáveis que facilitavam a identificação do participante; 2024: o ZIP passa a ter PARTICIPANTES e RESULTADOS, sem chave em comum; NU_IDADE vira TP_FAIXA_ETARIA; saem os municípios de nascimento e de residência; volta o código da escola de conclusão |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_enem_<ano>.zip` para os anos de 1998 a 2025 (padrão de URL sem exceções no catálogo).
- No bruto, o arquivo se chama `enem/enem-microdados_<ano>@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- Cada ZIP tem as pastas `DADOS` (CSV), `DICIONÁRIO` (xlsx e ods), `INPUTS` (leitura em SAS, SPSS e R), `LEIA-ME E DOCUMENTOS TÉCNICOS` e, desde as edições recentes, `PROVAS E GABARITOS`. O conversor lê só o que está em `DADOS`; as provas em texto para leitor de tela ficam de fora.
- O ZIP de 2023 tem `MICRODADOS_ENEM_2023.csv` com 1,78 GB descompactado; o de 2025, `RESULTADOS_2025.csv` com 2,1 GB e `PARTICIPANTES_2025.csv` com 513 MB (tamanhos lidos no índice do ZIP em 2026-11-15).

## Conteúdo

- **Até 2008:** um arquivo por edição (`microdados_enem_<ano>`), com a prova única de 63 questões interdisciplinares e o questionário socioeconômico.
- **2009 a 2023:** `microdados_enem_<ano>` (participante, questionário, escola, notas) e `itens_prova_<ano>` (um item por linha, com área, posição, gabarito e parâmetros). Em 2022 o ZIP traz também `quest_hab_estudo`, um questionário de hábitos de estudo.
- **2024 e 2025:** três arquivos: `participantes` (caracterização e questionário socioeconômico), `resultados` (escola de conclusão, provas, gabaritos e notas) e `itens_prova`. O Inep informa que `participantes` e `resultados` não têm chave de ligação em comum, de propósito, para preservar o anonimato.
- As notas das provas objetivas vêm da Teoria de Resposta ao Item (TRI); o Inep publica os procedimentos de cálculo nos documentos técnicos de cada edição.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 1998 | `microdados_enem` (163) |
| 1999 | `microdados_enem` (156) |
| 2000 | `microdados_enem` (154) |
| 2001 | `microdados_enem` (276) |
| 2002 | `microdados_enem` (252) |
| 2003 | `microdados_enem` (222) |
| 2004 | `microdados_enem` (239) |
| 2005 | `microdados_enem` (257) |
| 2006 | `microdados_enem` (258) |
| 2007 | `microdados_enem` (258) |
| 2008 | `microdados_enem` (258) |
| 2009 | `itens_prova` (12); `microdados_enem` (339) |
| 2010 | `itens_prova` (13); `microdados_enem` (105) |
| 2011 | `itens_prova` (13); `microdados_enem` (128) |
| 2012 | `itens_prova` (13); `microdados_enem` (115) |
| 2013 | `itens_prova` (14); `microdados_enem` (130) |
| 2014 | `itens_prova` (14); `microdados_enem` (130) |
| 2015 | `itens_prova` (14); `microdados_enem` (105) |
| 2016 | `itens_prova` (14); `microdados_enem` (105) |
| 2017 | `itens_prova` (14); `microdados_enem` (78) |
| 2018 | `itens_prova` (14); `microdados_enem` (78) |
| 2019 | `itens_prova` (14); `microdados_enem` (76) |
| 2020 | `itens_prova` (15); `microdados_enem` (76) |
| 2021 | `itens_prova` (14); `microdados_enem` (76) |
| 2022 | `itens_prova` (14); `microdados_enem` (76); `quest_hab_estudo` (86) |
| 2023 | `itens_prova` (14); `microdados_enem` (76) |
| 2024 | `itens_prova` (14); `participantes` (38); `resultados` (42) |
| 2025 | `itens_prova` (14); `participantes` (38); `resultados` (70) |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx) que cada ZIP traz; vale a edição mais recente que traz a variável. Colunas de edições antigas sem dicionário legível por máquina ficam sem descrição.
A coluna *Arquivos* indica em quais arquivos do lake a coluna aparece (o nome do arquivo sem o ano). Como o conjunto muda entre edições, veja também a coluna *Período*.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `nu_inscricao` | `NU_INSCRICAO` | texto | Número de inscrição1 | — | todo | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `nu_ano` | `NU_ANO` | texto | Ano do Enem | — | todo | `microdados_enem`, `participantes`, `resultados` |
| `tp_faixa_etaria` | `TP_FAIXA_ETARIA` | texto | Faixa etária2 | 1 = Menor de 17 anos; 2 = 17 anos; 3 = 18 anos; 4 = 19 anos; 5 = 20 anos; 6 = 21 anos; 7 = 22 anos; 8 = 23 anos; 9 = 24 anos; 10 = 25 anos; 11 = Entre 26 e 30 anos; 12 = Entre 31 e 35 anos; 13 = Entre 36 e 40 anos; 14 = Entre 41 e 45 anos; … (lista completa no dicionário da fonte) | todo | `microdados_enem`, `participantes` |
| `tp_sexo` | `TP_SEXO` | texto | Sexo | M = Masculino; F = Feminino | todo | `microdados_enem`, `participantes` |
| `co_municipio_residencia` | `CO_MUNICIPIO_RESIDENCIA` | texto | Código do Município em que o inscrito mora: | — | 1998 a 2007 | `microdados_enem` |
| `no_municipio_residencia` | `NO_MUNICIPIO_RESIDENCIA` | texto | Nome do município em que o inscrito mora | — | 1998 a 2007 | `microdados_enem` |
| `co_uf_residencia` | `CO_UF_RESIDENCIA` | texto | Código da Unidade da Federação da residência do inscrito | — | 1998 a 2007 | `microdados_enem` |
| `sg_uf_residencia` | `SG_UF_RESIDENCIA` | texto | Sigla da Unidade da Federação da residência do inscrito | — | 1998 a 2007 | `microdados_enem` |
| `tp_presenca` | `TP_PRESENCA` | texto | Presença a prova objetiva | 0 = Faltou à prova; 1 = Presente à prova | 1998 a 2008 | `microdados_enem` |
| `co_prova` | `CO_PROVA` | texto | Código identificador da prova | — | todo | `itens_prova`, `microdados_enem` |
| `vl_perc_comp1` | `VL_PERC_COMP1` | texto | Nota da competência 1 | — | 1998 a 2008 | `microdados_enem` |
| `vl_perc_comp2` | `VL_PERC_COMP2` | texto | Nota da competência 2 | — | 1998 a 2008 | `microdados_enem` |
| `vl_perc_comp3` | `VL_PERC_COMP3` | texto | Nota da competência 3 | — | 1998 a 2008 | `microdados_enem` |
| `vl_perc_comp4` | `VL_PERC_COMP4` | texto | Nota da competência 4 | — | 1998 a 2008 | `microdados_enem` |
| `vl_perc_comp5` | `VL_PERC_COMP5` | texto | Nota da competência 5 | — | 1998 a 2008 | `microdados_enem` |
| `nu_nota_objetiva` | `NU_NOTA_OBJETIVA` | texto | Nota da prova objetiva | — | 1998 a 2008 | `microdados_enem` |
| `tx_respostas_objetiva` | `TX_RESPOSTAS_OBJETIVA` | texto | Vetor com as respostas da parte objetiva da prova4 | — | 1998 a 2008 | `microdados_enem` |
| `tx_gabarito_objetiva` | `TX_GABARITO_OBJETIVA` | texto | Vetor com o gabarito da parte objetiva da prova | — | 1998 a 2008 | `microdados_enem` |
| `tp_status_redacao` | `TP_STATUS_REDACAO` | texto | Situação da redação do participante | 1 = Sem problemas; 2 = Anulada; 3 = Cópia Texto Motivador; 4 = Em Branco; 6 = Fuga ao tema; 7 = Não atendimento ao tipo textual; 8 = Texto insuficiente; 9 = Parte desconectada | todo | `microdados_enem`, `resultados` |
| `nu_nota_comp1` | `NU_NOTA_COMP1` | texto | Nota média da competência 1 obtida a partir dos avaliadores considerados válidos para o cálculo (conforme regras do edital) – Demonstrar domínio da modalidade escrita formal da Língua Portuguesa | — | todo | `microdados_enem`, `resultados` |
| `nu_nota_comp2` | `NU_NOTA_COMP2` | texto | Nota média da competência 2 obtida a partir dos avaliadores considerados válidos para o cálculo (conforme regras do edital) - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa | — | todo | `microdados_enem`, `resultados` |
| `nu_nota_comp3` | `NU_NOTA_COMP3` | texto | Nota média da competência 3 obtida a partir dos avaliadores considerados válidos para o cálculo (conforme regras do edital) - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista | — | todo | `microdados_enem`, `resultados` |
| `nu_nota_comp4` | `NU_NOTA_COMP4` | texto | Nota média da competência 4 obtida a partir dos avaliadores considerados válidos para o cálculo (conforme regras do edital) - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação | — | todo | `microdados_enem`, `resultados` |
| `nu_nota_comp5` | `NU_NOTA_COMP5` | texto | Nota média da competência 5 obtida a partir dos avaliadores considerados válidos para o cálculo (conforme regras do edital) - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos | — | todo | `microdados_enem`, `resultados` |
| `nu_nota_redacao` | `NU_NOTA_REDACAO` | texto | Nota final da prova de redação | — | todo | `microdados_enem`, `resultados` |
| `in_qse` | `IN_QSE` | texto | Resposta ao Questionário Socioeconômico | 1 = Respondeu o questionário socioecômico; 0 = Não respondeu o questionário socioecômico | 1998 a 2009 | `microdados_enem` |
| `q1` | `Q1` | texto | Até quando seu pai estudou? | A = Não estudou;; B = Da 1ª à 4ª série do Ensino Fundamental (antigo primário);; C = Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio);; D = Ensino Médio (antigo 2º grau) incompleto;; E = Ensino Médio (antigo 2º grau);; F = Ensino Superior incompleto;; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q2` | `Q2` | texto | Até quando sua mãe estudou? | A = Não estudou;; B = Da 1ª à 4ª série do Ensino Fundamental (antigo primário);; C = Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio);; D = Ensino Médio (antigo 2º grau) incompleto;; E = Ensino Médio (antigo 2º grau);; F = Ensino Superior incompleto;; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q3` | `Q3` | texto | Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.) | A = Nenhuma renda;; B = Até um salário mínimo (até R$622,00);; C = Mais de 1 até 1,5 (de R$ 622,01 até R$ 933,00).; D = Mais de 1,5 até 2 (de R$ 933,01 até R$ 1244,00).; E = Mais de 2 até 2,5 (de R$ 1244,01 até R$ 1555,00).; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q4` | `Q4` | texto | Quantas pessoas moram em sua casa (incluindo você)? | 1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5; 6 = 6; 7 = 7; 8 = 8; 9 = 9; 10 = 10; 11 = 11; 12 = 12; 13 = 13; 14 = 14; 15 = 15; 16 = 16; 17 = 17; 18 = 18; 19 = 19; 20 = 20 ou mais | 1998 a 2009 | `microdados_enem` |
| `q5` | `Q5` | texto | A residência de sua família é? | A = Própria e quitada; B = Própria e em pagamento (financiada); C = Alugada; D = Cedida; E = Outra situação (loteamento não regularizado, ocupação, etc) | 1998 a 2009 | `microdados_enem` |
| `q6` | `Q6` | texto | A residência de sua família está localizada em? | A = Zona rural.; B = Zona urbana; C = Comunidade indígena.; D = Comunidade quilombola. | 1998 a 2009 | `microdados_enem` |
| `q7` | `Q7` | texto | Você tem em sua casa? TV em cores | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2009 | `microdados_enem` |
| `q8` | `Q8` | texto | Você tem em sua casa? Videocassete e/ou DVD | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2009 | `microdados_enem` |
| `q9` | `Q9` | texto | Você tem em sua casa? Rádio | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2009 | `microdados_enem` |
| `q10` | `Q10` | texto | Você tem em sua casa? Microcomputador | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q11` | `Q11` | texto | Você tem em sua casa? Automóvel | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q12` | `Q12` | texto | Você tem em sua casa? Máquina de lavar roupa | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q13` | `Q13` | texto | Você tem em sua casa? Geladeira | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q14` | `Q14` | texto | Você tem em sua casa? Freezer (aparelho independente ou parte da geladeira duplex) | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q15` | `Q15` | texto | Você tem em sua casa? Telefone fixo | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q16` | `Q16` | texto | Você tem em sua casa? Telefone celular | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q17` | `Q17` | texto | Você tem em sua casa? Acesso à Internet | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q18` | `Q18` | texto | Você tem em sua casa? TV por assinatura | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q19` | `Q19` | texto | Você tem em sua casa? Aspirador de pó | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q20` | `Q20` | texto | Você tem em sua casa? Empregada mensalista | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q21` | `Q21` | texto | Você tem em sua casa? Banheiro | A = 1; B = 2; C = 3 ou mais; D = Não tenho | 1998 a 2010 | `microdados_enem` |
| `q22` | `Q22` | texto | Você exerce ou já exerceu atividade remunerada? | A = Sim, estou trabalhando; B = Sim, já trabalhei, mas não estou trabalhando; C = Não, nunca trabalhei | 1998 a 2010 | `microdados_enem` |
| `q23` | `Q23` | texto | Indique os motivos que levaram você a participar do ENEM: Testar meus conhecimentos | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q24` | `Q24` | texto | Indique os motivos que levaram você a participar do ENEM: Aumentar a possibilidade de conseguir um emprego | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q25` | `Q25` | texto | Indique os motivos que levaram você a participar do ENEM: Progredir no meu emprego atual | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q26` | `Q26` | texto | Indique os motivos que levaram você a participar do ENEM: Ingressar na Educação Superior Pública | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q27` | `Q27` | texto | Indique os motivos que levaram você a participar do ENEM: Ingressar na Educação Superior Privada | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q28` | `Q28` | texto | Indique os motivos que levaram você a participar do ENEM: Conseguir uma bolsa de estudos (ProUni, outras) | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q29` | `Q29` | texto | Indique os motivos que levaram você a participar do ENEM: Participar do Programa de Financiamento Estudantil - FIES | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 1998 a 2010 | `microdados_enem` |
| `q30` | `Q30` | texto | Quantos anos você levou para concluir o Ensino Fundamental? | A = Menos de 8 anos.; B = 8 anos.; C = 9 anos.; D = 10 anos.; E = 11 anos.; F = Mais de 11 anos.; G = Não conclui.; H = Não cursei. (Passe para a pergunta 33) | 1998 a 2010 | `microdados_enem` |
| `q31` | `Q31` | texto | Você deixou de estudar durante o Ensino Fundamental? | A = Não.; B = Sim, por um ano.; C = Sim, por dois anos.; D = Sim, por três anos.; E = Sim, por quatro anos ou mais. | 1998 a 2010 | `microdados_enem` |
| `q32` | `Q32` | texto | Em que tipo de escola você cursou o Ensino Fundamental? | A = Somente em escola pública;; B = Maior parte em escola pública;; C = Somente em escola particular;; D = Maior parte em escola particular;; E = Somente em escola indígena;; F = Maior parte em escola indígena;; … (lista completa no dicionário da fonte) | 1998 a 2010 | `microdados_enem` |
| `q33` | `Q33` | texto | Quantos anos você levou para concluir o Ensino Médio? | A = Menos de 3 anos; B = 3 anos; C = 4 anos; D = 5 anos; E = 6 anos ou mais; F = Não conclui.; G = Não cursei. (Passe para a pergunta 36) | 1998 a 2010 | `microdados_enem` |
| `q34` | `Q34` | texto | Você deixou de estudar durante o Ensino Médio? | A = Não.; B = Sim, por um ano.; C = Sim, por dois anos.; D = Sim, por três anos.; E = Sim, por quatro anos ou mais. | 1998 a 2010 | `microdados_enem` |
| `q35` | `Q35` | texto | Em que tipo de escola você cursou o Ensino Médio? | A = Somente em escola pública;; B = Maior parte em escola pública;; C = Somente em escola particular;; D = Maior parte em escola particular;; E = Somente em escola indígena;; F = Maior parte em escola indígena;; … (lista completa no dicionário da fonte) | 1998 a 2010 | `microdados_enem` |
| `q36` | `Q36` | texto | Caso você ingresse no Ensino Superior privado pretende recorrer aos auxílios abaixo para custeio das mensalidades? Pró-Uni (Programa Universidade para Todos) | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q37` | `Q37` | texto | Caso você ingresse no Ensino Superior privado pretende recorrer aos auxílios abaixo para custeio das mensalidades? Bolsa de estudos da própria Instituição de Ensino Superior | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q38` | `Q38` | texto | Caso você ingresse no Ensino Superior privado pretende recorrer aos auxílios abaixo para custeio das mensalidades? Bolsa de estudos da empresa onde trabalho. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q39` | `Q39` | texto | Caso você ingresse no Ensino Superior privado pretende recorrer aos auxílios abaixo para custeio das mensalidades? Auxílio do Programa de Financiamento Estudantil - FIES | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q40` | `Q40` | texto | Você cursa ou já cursou a Educação de Jovens e Adultos – EJA? | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q41` | `Q41` | texto | Como é ou era o principal curso de EJA que você frequenta ou frequentou? | A = Curso presencial em escola pública.; B = Curso presencial em escola privada.; C = Curso presencial na empresa em que trabalhei, instituição filantrópica ou religiosa.; D = Curso a distância (via rádio, televisão, internet, correio, com apostilas).; … (lista completa no dicionário da fonte) | 1998 a 2010 | `microdados_enem` |
| `q42` | `Q42` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Trabalhava, não tinha tempo de estudar. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q43` | `Q43` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Estudava no curso da empresa e foi interrompido. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q44` | `Q44` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Ocorreram problemas de saúde ou acidentes comigo ou familiares | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q45` | `Q45` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Mudei de bairro, cidade ou município. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q46` | `Q46` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Por motivos pessoais, casamento, filhos, etc. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q47` | `Q47` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Faltava-me interesse, desisti. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q48` | `Q48` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Senti-me discriminado(a). | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q49` | `Q49` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Temi/Sofri violência. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q50` | `Q50` | texto | Você já frequentou o ensino regular? | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q51` | `Q51` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de vaga em escola pública. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q52` | `Q52` | texto | Indique o que levou você a deixar de cursar o ensino regular: Ausência de escola perto de casa. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q53` | `Q53` | texto | Indique o que levou você a deixar de cursar o ensino regular: Dificuldades após reprovação. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q54` | `Q54` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de interesse em estudar. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q55` | `Q55` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de condições adequadas na escola. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q56` | `Q56` | texto | Indique o que levou você a deixar de cursar o ensino regular: Trabalho, falta de tempo para estudar. | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q57` | `Q57` | texto | Indique o que levou você a deixar de cursar o ensino regular: Motivos pessoais, casamento / filhos, etc | A = Sim; B = Não | 1998 a 2010 | `microdados_enem` |
| `q58` | `Q58` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de apoio familiar. | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q59` | `Q59` | texto | Indique o que levou você a deixar de cursar o ensino regular: Problemas de saúde ou acidente comigo ou familiares. | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q60` | `Q60` | texto | Indique o que levou você a deixar de cursar o ensino regular: Discriminação / Preconceitos (sexo, raça, idade, classe etc.) | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q61` | `Q61` | texto | Indique o que levou você a deixar de cursar o ensino regular: Medo de sofrer violência. | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q62` | `Q62` | texto | Quantos anos você tinha quando deixou de frequentar o ensino regular? | A = Menos de 10 anos.; B = Entre 10 e 14 anos.; C = Entre 15 e 18 anos.; D = Entre 19 e 24 anos.; E = Entre 25 e 30 anos.; F = Mais de 30 anos.; G = Não deixei de frequentar. | 1998 a 2009 | `microdados_enem` |
| `q63` | `Q63` | texto | Como prova de consideração por parte da escola pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha fornecimento de refeição aos (às) alunos(as) | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q64` | `Q64` | texto | A escola deve oferecer horário flexível para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q65` | `Q65` | texto | A escola deve oferecer menor carga de trabalho ou de tarefas extraclasse para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q66` | `Q66` | texto | A escola deve oferecer programa de recuperação de notas para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q67` | `Q67` | texto | A escola deve oferecer abono de faltas para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q68` | `Q68` | texto | A escola deve oferecer aulas mais dinâmicas, com didática diferenciada para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q69` | `Q69` | texto | A escola deve oferecer aulas de revisão da matéria aos alunos interessados que trabalham | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q70` | `Q70` | texto | A escola deve oferecer atendimento extraclasse aos alunos que trabalham | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q71` | `Q71` | texto | A escola deve oferecer fornecimento de refeição para o aluno que trabalha | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q72` | `Q72` | texto | Anos que levou para concluir o ensino fundamental (1º grau) | A = Menos de 8 anos; B = 8 anos; C = 9 anos; D = 10 anos; E = 11 anos; F = Mais de 11 anos; G = Não cursei | 1998 a 2009 | `microdados_enem` |
| `q73` | `Q73` | texto | Em que tipo de escola cursou o ensino fundamental (1ª grau) | A = Somente em escola pública; B = Parte em escola pública e parte em escola particular; C = Somente em escola particular; D = Somente em escola indígena ou em escola situada em comunidade quilombola; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q74` | `Q74` | texto | Em que ano concluiu ou concluirá o ensino médio (2º grau) | A = Vai concluir após 2009; B = Vai concluir no segundo semestre de 2009; C = No primeiro semestre de 2009; D = Em 2008; E = Em 2007; F = Em 2006; G = Em 2005; H = Em 2004; I = Entre 2003 e 2002; J = Antes de 2002; K = Não cursei o ensino médio | 1998 a 2009 | `microdados_enem` |
| `q75` | `Q75` | texto | Quantos anos levou para cursar o ensino médio (2º grau) | A = Menos de 3 anos; B = 3 anos; C = 4 anos; D = 5 anos; E = 6 anos; F = Mais de 6 anos | 1998 a 2009 | `microdados_enem` |
| `q76` | `Q76` | texto | Em que turno cursou ou esta cursando o ensino médio | A = Somente no turno diurno; B = Maior parte no turno diurno; C = Somente no turno noturno; D = Maior parte no turno noturno | 1998 a 2009 | `microdados_enem` |
| `q77` | `Q77` | texto | Em que tipo de escola cursou ou está cursando o ensino médio (2º grau) | A = Somente em escola pública; B = Maior parte em escola pública; C = Somente em escola particular; D = Maior parte em escola particular; E = Somente em escola indígena; F = Maior parte em escola não-indígena; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q78` | `Q78` | texto | Em que modalidade de ensino concluiu ou vai concluir o ensino médio (2º grau) | A = Ensino regular; B = Educação para jovens e adultos (antigo supletivo); C = Ensino técnico / ensino profissional | 1998 a 2009 | `microdados_enem` |
| `q79` | `Q79` | texto | Fez curso de língua estrangeira | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q80` | `Q80` | texto | Fez curso de computação ou informática | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q81` | `Q81` | texto | Fez curso preparatório para o vestibular (cursinho) | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q82` | `Q82` | texto | Fez outros cursos | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q83` | `Q83` | texto | Com que frequência lê jornais | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q84` | `Q84` | texto | Com que frequência lê revistas de informação geral (Carta Capital, Veja, Istoé, Época, Exame, Caros Amigos, Piauí, Forum, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q85` | `Q85` | texto | Com que frequência lê revistas de divulgação científica, tecnológica, filosófica ou artística (Ciência Hoje, Geo, Galileu, Mente & Cérebro, Linux Magazine, PC Magazine, Filosofia, Cult, Nossa História, História Viva, Entrelivros, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q86` | `Q86` | texto | Com que frequência lê revistas de humor, quadrinhos ou jogos (Casseta & Planeta, Turma da Mônica, PC Gamer, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q87` | `Q87` | texto | Com que frequência lê revistas para adolescentes ou sobre TV, cinema, música, celebridades (Viração, TPM, Set, Rolling Stones, Capricho, Contigo, Caras, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q88` | `Q88` | texto | Com que frequência lê revistas sobre comportamento, moda, estilo e decoração (Cláudia, Maire Claire, Pais & Filhos, Casa & Jardim, Bons Fluidos, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q89` | `Q89` | texto | Com que frequência lê revistas sobre automóveis, esporte e lazer (Quatro Rodas, Duas Rodas, Placar, Pesca & Cia, Náutica, Revista do Volei, Viagem & Turismo, Terra, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q90` | `Q90` | texto | Com que frequência lê revistas sobre saúde (Boa Saúde, Saúde, Vida Simples, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q91` | `Q91` | texto | Com que frequência lê revistas sobre religião (Sophia, Revista das Religiões, Missões, Gospel, Orixás, Delfos, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q92` | `Q92` | texto | Com que frequência lê revistas sobre educação e estudos (Educação, Guia do Estudante, Almanaque Abril, Sociologia, Lígua Portuguesa, Speak up, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q93` | `Q93` | texto | Com que frequência lê livros de ficção (romances, contos, poesias, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q94` | `Q94` | texto | Com que frequência lê livros de não ficção e biografias (reportagens, livros científicos, filosóficos, históricos, documentários, etc.) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q95` | `Q95` | texto | Com que frequência lê dicionários, enciclopédias e manuais | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q96` | `Q96` | texto | Com que frequência lê sites e matérias na Internet | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 1998 a 2009 | `microdados_enem` |
| `q97` | `Q97` | texto | Avaliação da escola em que fez o ensino médio quanto ao conhecimento que os(as) professores(as) têm das matérias e a maneira de transmiti-lo | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q98` | `Q98` | texto | Avaliação da escola em que fez o ensino médio quanto à dedicação dos(as) professores(as) para preparar aulas e atender aos alunos | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q99` | `Q99` | texto | Avaliação da escola em que fez o ensino médio quanto às iniciativas da escola para realizar excursões, passeios culturais, estudos do meio ambiente | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q100` | `Q100` | texto | Avaliação da escola em que fez o ensino médio quanto à biblioteca | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q101` | `Q101` | texto | Avaliação da escola em que fez o ensino médio quanto às condições das salas de aula | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q102` | `Q102` | texto | Avaliação da escola em que fez o ensino médio quanto às condições dos laboratórios | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q103` | `Q103` | texto | Avaliação da escola em que fez o ensino médio quanto ao acesso a computadores e outros recursos de informática | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q104` | `Q104` | texto | Avaliação da escola em que fez o ensino médio quanto ao ensino de língua estrangeira | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q105` | `Q105` | texto | Avaliação da escola em que fez o ensino médio quanto ao interesse dos(as) alunos(as) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q106` | `Q106` | texto | Avaliação da escola em que fez o ensino médio quanto ao trabalho de grupo | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q107` | `Q107` | texto | Avaliação da escola em que fez o ensino médio quanto às práticas de esportes | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q108` | `Q108` | texto | Avaliação da escola em que fez o ensino médio quanto à atenção e respeito dos(as) funcionários(as) e dos(as) professores(as) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q109` | `Q109` | texto | Avaliação da escola em que fez o ensino médio quanto à direção | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q110` | `Q110` | texto | Avaliação da escola em que fez o ensino médio quanto à organização dos horários de aulas | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q111` | `Q111` | texto | Avaliação da escola em que fez o ensino médio quanto à localização | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q112` | `Q112` | texto | Avaliação da escola em que fez o ensino médio quanto à segurança (iluminação, policiamento, etc.) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q113` | `Q113` | texto | Avaliação da escola em que fez o ensino médio quanto ao respeito à diversidade | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q114` | `Q114` | texto | Avaliação da escola em que fez o ensino médio quanto a acessibilidade física e os recursos e os materiais para estudantes com deficiência (rampas, corrimãos, lupas, etc.) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q115` | `Q115` | texto | Avaliação da escola em que fez o ensino médio quanto a atenção às questões ambientais | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q116` | `Q116` | texto | A escola em que estuda ou estudou realiza palestras / debates | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q117` | `Q117` | texto | A escola em que estuda ou estudou realiza jogos / esportes / campeonatos | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q118` | `Q118` | texto | A escola em que estuda ou estudou realiza dança/música/coral/teatro | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q119` | `Q119` | texto | A escola em que estuda ou estudou realiza estudos do meio ambiente / passeios | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q120` | `Q120` | texto | A escola em que estuda ou estudou realiza feira de ciências / feira cultural | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q121` | `Q121` | texto | A escola em que estuda ou estudou realiza festas/gincanas | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q122` | `Q122` | texto | Atendimento educacional extraclasse | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q123` | `Q123` | texto | De acordo com os ensinamentos no ensino médio, como considera o preparo para conseguir um emprego, exercer alguma atividade profissional | A = Eu me considero preparado(a) para entrar no mercado de trabalho; B = Apesar de ter frequentado uma boa escola, eu me considero despreparado(a), pois não aprendi o suficiente para conseguir um emprego; … (lista completa no dicionário da fonte) | 1998 a 2009 | `microdados_enem` |
| `q124` | `Q124` | texto | Os(as) professores(as) têm autoridade, firmeza | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q125` | `Q125` | texto | Os(as) professores(as) são distantes, têm pouco envolvimento | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q126` | `Q126` | texto | Os(as) professores(as) têm respeito pelos estudantes | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q127` | `Q127` | texto | Os(as) professores(as) são indiferentes, ignoram sua existência | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q128` | `Q128` | texto | Os(as) professores(as) são preocupados(as) e dedicados(as) | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q129` | `Q129` | texto | Os(as) professores(as) são autoritários(as), rígidos(as), abusam do poder | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q130` | `Q130` | texto | Os(as) professores(as) valorizam as diferenças e ensinam a respeitá-las | A = Sim; B = Não | 1998 a 2009 | `microdados_enem` |
| `q131` | `Q131` | texto | Avaliação sobre a escola quanto à liberdade de expressar as ideias | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q132` | `Q132` | texto | Avaliação sobre a escola quanto ao respeito aos estudantes, sem discriminá-los | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q133` | `Q133` | texto | Avaliação sobre a escola quanto à amizade e respeito entre alunos(as) e trabalhadores da escola (funcionários(as), professores(as)) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q134` | `Q134` | texto | Avaliação sobre a escola quanto a levar em conta suas opiniões | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q135` | `Q135` | texto | Avaliação sobre a escola quanto à discussão dos problemas da atualidade nas aulas | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q136` | `Q136` | texto | Avaliação sobre a escola quanto à convivência entre estudantes | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `q137` | `Q137` | texto | Avaliação sobre a escola quanto à organização para apoiar a resolução de problemas de relacionamento entre estudantes | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 1998 a 2009 | `microdados_enem` |
| `tp_st_conclusao` | `TP_ST_CONCLUSAO` | texto | Situação de conclusão do Ensino Médio | 1 = Já concluí o Ensino Médio; 2 = Estou cursando e concluirei o Ensino Médio em 2025; 3 = Estou cursando e concluirei o Ensino Médio após 2025; 4 = Não concluí e não estou cursando o Ensino Médio | 1999 a 2025 | `microdados_enem`, `participantes` |
| `co_municipio_esc` | `CO_MUNICIPIO_ESC` | texto | Código do município da escola | — | 2001 a 2025 | `microdados_enem`, `resultados` |
| `no_municipio_esc` | `NO_MUNICIPIO_ESC` | texto | Nome do município da escola | — | 2001 a 2025 | `microdados_enem`, `resultados` |
| `co_uf_esc` | `CO_UF_ESC` | texto | Código da Unidade da Federação da escola | 11 = Rondônia; 12 = Acre; 13 = Amazonas; 14 = Roraima; 15 = Pará; 16 = Amapá; 17 = Tocantins; 21 = Maranhão; 22 = Piauí; 23 = Ceará; 24 = Rio Grande do Norte; 25 = Paraíba; 26 = Pernambuco; 27 = Alagoas; 28 = Sergipe; 29 = Bahia; 31 = Minas Gerais; … (lista completa no dicionário da fonte) | 2001 a 2025 | `microdados_enem`, `resultados` |
| `sg_uf_esc` | `SG_UF_ESC` | texto | Sigla da Unidade da Federação da escola | AC = Acre; AL = Alagoas; AM = Amazonas; AP = Amapá; BA = Bahia; CE = Ceará; DF = Distrito Federal; ES = Espírito Santo; GO = Goiás; MA = Maranhão; MG = Minas Gerais; MS = Mato Grosso do Sul; MT = Mato Grosso; PA = Pará; PB = Paraíba; PE = Pernambuco; … (lista completa no dicionário da fonte) | 2001 a 2025 | `microdados_enem`, `resultados` |
| `tp_dependencia_adm_esc` | `TP_DEPENDENCIA_ADM_ESC` | texto | Dependência administrativa (Escola) | 1 = Federal; 2 = Estadual; 3 = Municipal; 4 = Privada | 2001 a 2025 | `microdados_enem`, `resultados` |
| `tp_localizacao_esc` | `TP_LOCALIZACAO_ESC` | texto | Localização (Escola) | 1 = Urbana; 2 = Rural | 2001 a 2025 | `microdados_enem`, `resultados` |
| `tp_sit_func_esc` | `TP_SIT_FUNC_ESC` | texto | Situação de funcionamento (Escola) | 1 = Em atividade; 2 = Paralisada; 3 = Extinta; 4 = Escola extinta em anos anteriores. | 2001 a 2025 | `microdados_enem`, `resultados` |
| `q6_1` | `Q6_1` | texto | Mora sozinho(a) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_2` | `Q6_2` | texto | Mora com o pai | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_3` | `Q6_3` | texto | Mora com a mãe | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_4` | `Q6_4` | texto | Mora com esposa / marido / companheiro(a) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_5` | `Q6_5` | texto | Mora com filho(s) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_6` | `Q6_6` | texto | Mora com irmão(s) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_7` | `Q6_7` | texto | Mora com outro(s) parente(s) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q6_8` | `Q6_8` | texto | Mora com amigo(s) ou colega(s) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q16_1` | `Q16_1` | texto | Tem TV em cores e quantas | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_2` | `Q16_2` | texto | Tem Videocassete e/ou DVD e quantos | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_3` | `Q16_3` | texto | Tem Rádio e quantos | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_4` | `Q16_4` | texto | Tem Microcomputador e quantos | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_5` | `Q16_5` | texto | Tem Automóvel e quantos | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_6` | `Q16_6` | texto | Tem Máquina de lavar roupa e quantos | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_7` | `Q16_7` | texto | Aspirador de pó | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_8` | `Q16_8` | texto | Geladeira | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_9` | `Q16_9` | texto | Freezer | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q16_10` | `Q16_10` | texto | Telefone fixo | A = 1; B = 2; C = 3; D = 4; E = 5 ou +; F = Não há. | 2001 a 2002 | `microdados_enem` |
| `q17_1` | `Q17_1` | texto | Tem casa própria | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q17_2` | `Q17_2` | texto | Se a casa é em rua calçada ou asfaltada | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q17_3` | `Q17_3` | texto | Se a casa tem água corrente de torneira | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q17_4` | `Q17_4` | texto | Se a casa tem eletricidade | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q17_5` | `Q17_5` | texto | Tem empregada doméstica | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q30_1` | `Q30_1` | texto | Os conhecimentos no ensino médio foram adequados ao que o mercado de trabalho solicita | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q30_2` | `Q30_2` | texto | Os conhecimentos no ensino médio tiveram relação com a profissão que escolheu / que exerce | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q30_3` | `Q30_3` | texto | Os conhecimentos no ensino médio foram bem desenvolvidos, com aulas práticas, laboratórios, etc | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q30_4` | `Q30_4` | texto | Os conhecimentos no ensino médio proporcionaram cultura e conhecimento | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_1` | `Q33_1` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha o horário flexível | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_2` | `Q33_2` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha menor carga de trabalho ou de tarefas extraclasse | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_3` | `Q33_3` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha programa de recuperação de notas | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_4` | `Q33_4` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha abono de faltas | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_5` | `Q33_5` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha aulas mais dinâmicas, com didática diferenciada | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_6` | `Q33_6` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha aulas de revisão da matéria aos interessados | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q33_7` | `Q33_7` | texto | Como prova de consideração por parte da escola em consideração pelo aluno trabalhar e estudar ao mesmo tempo, a escola tinha fornecimento de refeição aos alunos | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_1` | `Q34_1` | texto | A escola deve oferecer horário flexível para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_2` | `Q34_2` | texto | A escola deve oferecer menor carga de trabalho ou de tarefas extraclasse para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_3` | `Q34_3` | texto | A escola deve oferecer programa de recuperação de notas para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_4` | `Q34_4` | texto | A escola deve oferecer abono de faltas para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_5` | `Q34_5` | texto | A escola deve oferecer aulas mais dinâmicas, com didática diferenciada para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_6` | `Q34_6` | texto | A escola deve oferecer aulas de revisão da matéria aos alunos que interessados que trabalham | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q34_7` | `Q34_7` | texto | A escola deve oferecer fornecimento de refeição para o aluno que trabalha | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q42_1` | `Q42_1` | texto | Fez curso de língua estrangeira fora da escola durante o ensino médio (2º grau) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q42_2` | `Q42_2` | texto | Fez curso de computação ou informática fora da escola durante o ensino médio (2º grau) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q42_3` | `Q42_3` | texto | Fez curso preparatório para o vestibular (cursinho) fora da escola durante o ensino médio (2º grau) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q42_4` | `Q42_4` | texto | Fez artes plásticas ou atividades artísticas em geral fora da escola durante o ensino médio (2º grau) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q42_5` | `Q42_5` | texto | Fez esportes, atividades físicas fora da escola durante o ensino médio (2º grau) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q43_1` | `Q43_1` | texto | Com que freqüência lê jornais | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 2001 a 2002 | `microdados_enem` |
| `q43_2` | `Q43_2` | texto | Com que freqüência lê revistas de informação geral (Veja, Isto é, Época, etc) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 2001 a 2002 | `microdados_enem` |
| `q43_3` | `Q43_3` | texto | Com que freqüência lê revistas de humor / quadrinhos | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 2001 a 2002 | `microdados_enem` |
| `q43_4` | `Q43_4` | texto | Com que freqüência lê revistas de divulgação científica (Ciência Hoje, Galileu, etc) | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 2001 a 2002 | `microdados_enem` |
| `q43_5` | `Q43_5` | texto | Com que freqüência lê romances, livros de ficção | A = Frequentemente (todo dia ou quase todo dia); B = Às vezes; C = Nunca | 2001 a 2002 | `microdados_enem` |
| `q44_1` | `Q44_1` | texto | Avaliação da escola que fez o ensino médio quanto o conhecimento que os(as) professores(as) têm das matérias e a maneira de transmiti-lo | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_2` | `Q44_2` | texto | Avaliação da escola que fez o ensino médio quanto a dedicação dos professores para preparar aulas e atender aos alunos | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_3` | `Q44_3` | texto | Avaliação da escola que fez o ensino médio quanto as iniciativas da escola para realizar excursões, estudos do meio | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_4` | `Q44_4` | texto | Avaliação da escola que fez o ensino médio quanto a biblioteca da escola | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_5` | `Q44_5` | texto | Avaliação da escola que fez o ensino médio quanto as condições das salas de aula | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_6` | `Q44_6` | texto | Avaliação da escola que fez o ensino médio quanto as condições dos laboratórios | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_7` | `Q44_7` | texto | Avaliação da escola que fez o ensino médio quanto o acesso a computadores e outros recursos de informática | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_8` | `Q44_8` | texto | Avaliação da escola que fez o ensino médio quanto o ensino de língua estrangeira | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_9` | `Q44_9` | texto | Avaliação da escola que fez o ensino médio quanto o interesse dos alunos | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_10` | `Q44_10` | texto | Avaliação da escola que fez o ensino médio quanto o trabalho de grupo | 1 2 3 4 5 6 7 8 9 10 = Notas | 2001 a 2002 | `microdados_enem` |
| `q44_11` | `Q44_11` | texto | Avaliação da escola que fez o ensino médio quanto a práticas de esportes | 1 2 3 4 5 6 7 8 9 10 = Notas | 2001 a 2002 | `microdados_enem` |
| `q44_12` | `Q44_12` | texto | Avaliação da escola que fez o ensino médio quanto a atenção e o respeito dos funcionários | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_13` | `Q44_13` | texto | Avaliação da escola que fez o ensino médio quanto a direção dela | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_14` | `Q44_14` | texto | Avaliação da escola que fez o ensino médio quanto a organização dos horários de aulas | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_15` | `Q44_15` | texto | Avaliação da escola que fez o ensino médio quanto a localização dela | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q44_16` | `Q44_16` | texto | Avaliação da escola que fez o ensino médio quanto a segurança (iluminação, policiamento, etc) | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q45_1` | `Q45_1` | texto | A escola em que estuda ou estudou realiza palestras / debates | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_2` | `Q45_2` | texto | A escola em que estuda ou estudou realiza jogos / esportes / campeonatos | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_3` | `Q45_3` | texto | A escola em que estuda ou estudou realiza teatro | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_4` | `Q45_4` | texto | A escola em que estuda ou estudou realiza coral | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_5` | `Q45_5` | texto | A escola em que estuda ou estudou realiza dança / música | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_6` | `Q45_6` | texto | A escola em que estuda ou estudou realiza estudos do meio / passeios | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_7` | `Q45_7` | texto | A escola em que estuda ou estudou realiza feira de ciências / feira cultural | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q45_8` | `Q45_8` | texto | A escola em que estuda ou estudou realiza festas / gincanas | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_1` | `Q47_1` | texto | Sua reação é de amizade | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_2` | `Q47_2` | texto | Os(as) professores(as) têm autoridade, firmeza | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_3` | `Q47_3` | texto | Os(as) professores(as) são distantes, têm pouco envolvimento | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_4` | `Q47_4` | texto | Os(as) professores(as) têm respeito | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_5` | `Q47_5` | texto | Os(as) professores(as) são indiferentes, ignoram sua existência | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_6` | `Q47_6` | texto | Os(as) professores(as) são preocupados(as) e dedicados(as) | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q47_7` | `Q47_7` | texto | Os(as) professores(as) são autoritários(as), rígidos(as), abusam do poder | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q48_1` | `Q48_1` | texto | Avaliação sobre a escola quanto a liberdade de expressar a idéias | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q48_2` | `Q48_2` | texto | Avaliação sobre a escola quanto o respeito aos alunos | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q48_3` | `Q48_3` | texto | Avaliação sobre a escola quanto a amizade e respeito entre alunos(as) e funcionários(as) | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q48_4` | `Q48_4` | texto | Avaliação sobre a escola quanto a levar em conta suas opiniões | 1 2 3 4 5 6 7 8 9 10 = Nota | 2001 a 2002 | `microdados_enem` |
| `q50_1` | `Q50_1` | texto | Avaliação sobre a escola quanto a liberdade de expressar a idéias | 1 = Nota | 2001 | `microdados_enem` |
| `q50_2` | `Q50_2` | texto | Avaliação sobre a escola em realação entre alunos e professores | 1 = Nota | 2001 | `microdados_enem` |
| `q50_3` | `Q50_3` | texto | Avaliação sobre a escola quanto o respeito aos alunos | 1 = Nota | 2001 | `microdados_enem` |
| `q50_4` | `Q50_4` | texto | Avaliação sobre a escola quanto a amizade e respeito entre alunos(as) e funcionários(as) | 1 = Nota | 2001 | `microdados_enem` |
| `q50_5` | `Q50_5` | texto | Avaliação sobre a escola quanto a levar em conta suas opiniões | 1 = Nota | 2001 | `microdados_enem` |
| `q50_6` | `Q50_6` | texto | Avaliação sobre a escola quanto a discussão dos problemas da atualidade nas aulas | 1 = Nota | 2001 | `microdados_enem` |
| `q50_7` | `Q50_7` | texto | Avaliação sobre a escola quanto a convivência entre alunos | 1 = Nota | 2001 | `microdados_enem` |
| `q50_8` | `Q50_8` | texto | Avaliação sobre a escola quanto ao uso de drogas entre os alunos | 1 = Nota | 2001 | `microdados_enem` |
| `q50_9` | `Q50_9` | texto | Avaliação sobre a escola quanto a organização para apoiar a resolução de problemas de relacionamento entre alunos | 1 = Nota | 2001 | `microdados_enem` |
| `q50_10` | `Q50_10` | texto | Avaliação sobre a escola quanto a iniciativa para apoiar a resolução de problemas de relacionamento entre alunos e professores | 1 = Nota | 2001 | `microdados_enem` |
| `q50_11` | `Q50_11` | texto | Avaliação sobre a escola quanto a levar em conta seus problemas pessoais e familiares | 1 = Nota | 2001 | `microdados_enem` |
| `q50_12` | `Q50_12` | texto | Avaliação sobre a escola quanto a realização de Programas e Palestras contra drogas | 1 = Nota | 2001 | `microdados_enem` |
| `q50_13` | `Q50_13` | texto | Avaliação sobre a escola quanto a capacidade relacionar os conteúdos das matérias com o cotidiano | 1 = Nota | 2001 | `microdados_enem` |
| `q50_14` | `Q50_14` | texto | Avaliação sobre a escola quanto a capacidade de a escola avaliar conhecimento, o que aprendeu | 1 = Nota | 2001 | `microdados_enem` |
| `q56_1` | `Q56_1` | texto | O candidato já procurou pela família para resolver seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_2` | `Q56_2` | texto | O candidato já procurou cartomante para resolver seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_3` | `Q56_3` | texto | O candidato já consultou o jogo de búzios para resolver os seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_4` | `Q56_4` | texto | O candidato foi à Igreja/procurou padre/pastor para resolver seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_5` | `Q56_5` | texto | O candidato buscou ajuda profissional (psicólogo, médico,etc) para resolver seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_6` | `Q56_6` | texto | O candidato consultou horóscopo para resolver os seus problemas pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_7` | `Q56_7` | texto | O candidato já procurou pelos amigos para resolver | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q56_8` | `Q56_8` | texto | O candidato buscou orientação em livros e revistas para resolver dados pessoais | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q59_1` | `Q59_1` | texto | Qual dos pontos o candidato valoriza em 1º lugar no momento | A = Amizade; B = Sinceridade; C = Honestidade; D = Igualdade; E = Solidariedade | 2001 a 2002 | `microdados_enem` |
| `q59_2` | `Q59_2` | texto | Qual dos pontos o candidato valoriza em 2º lugar no momento | A = Amizade; B = Sinceridade; C = Honestidade; D = Igualdade; E = Solidariedade | 2001 a 2002 | `microdados_enem` |
| `q59_3` | `Q59_3` | texto | Participa de um Grupo de bairro ou associação comunitária | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q59_4` | `Q59_4` | texto | Participa de uma Igreja ou grupo religioso | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q59_5` | `Q59_5` | texto | Participa de um partido político | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q59_6` | `Q59_6` | texto | Participa de uma Ong ou movimento social | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q59_7` | `Q59_7` | texto | Participa de um clube recreativo ou associação esportiva | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q60_1` | `Q60_1` | texto | Qual dos pontos o candidato valoriza em 1º lugar no momento | A = Lealdade; B = Ética; C = Liberdade; D = Independência; E = Justiça; F = Deus/minha religião | 2001 a 2002 | `microdados_enem` |
| `q60_2` | `Q60_2` | texto | Qual dos pontos o candidato valoriza em 2º lugar no momento | A = Lealdade; B = Ética; C = Liberdade; D = Independência; E = Justiça; F = Deus/minha religião | 2001 a 2002 | `microdados_enem` |
| `q60_3` | `Q60_3` | texto | O quanto você se interessa pela economia nacional, a questão da inflação, o plano real | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_4` | `Q60_4` | texto | O quanto você se interessa a política da sua cidade, o prefeito, os vereadores | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_5` | `Q60_5` | texto | O quanto você se interessa por esportes | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_6` | `Q60_6` | texto | O quanto você se interessa pelas questões sobre o meio ambiente, poluição, etc | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_7` | `Q60_7` | texto | O quanto você se interessa pelas questões sociais como a desigualdade, a pobreza, o desemprego, a miséria | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_8` | `Q60_8` | texto | O quanto você se interessa pelas questões sobre artes, teatro, cinema | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_9` | `Q60_9` | texto | O quanto você se interessa sobre a questão das drogas e suas conseqüências | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q60_10` | `Q60_10` | texto | O quanto você se interessa sobre assuntos sobre seu ídolo (cantor/a, artista, ou conjunto musical) | A = Muito; B = Pouco; C = Não me interesso | 2001 | `microdados_enem` |
| `q61_1` | `Q61_1` | texto | Qual dos pontos o candidato valoriza em 1º lugar no momento | A = Trabalho / profissão; B = Família; C = Estudos / aprender coisas novas / ter cultura; D = Diversão / tempo livre; E = Namorado(a) / companheiro(a); F = Dinheiro; G = Segurança material | 2001 a 2002 | `microdados_enem` |
| `q61_2` | `Q61_2` | texto | Qual dos pontos o candidato valoriza em 2º lugar no momento | A = Trabalho / profissão; B = Família; C = Estudos / aprender coisas novas / ter cultura; D = Diversão / tempo livre; E = Namorado(a) / companheiro(a); F = Dinheiro; G = Segurança material | 2001 a 2002 | `microdados_enem` |
| `q62_1` | `Q62_1` | texto | O que mais preocupa o candidato em 1º lugar no momento | A = Conseguir trabalho / emprego; B = Meu futuro em geral; C = Terminar meus estudos / os exames / provas; D = Dinheiro; E = Estar bem com meus amigos; F = Conseguir entrar na faculdade / universidade; G = A falta de liberdade, a dependência de minha família; … (lista completa no dicionário da fonte) | 2001 a 2002 | `microdados_enem` |
| `q62_2` | `Q62_2` | texto | O que mais preocupa o candidato em 2º lugar no momento | A = Conseguir trabalho / emprego; B = Meu futuro em geral; C = Terminar meus estudos / os exames / provas; D = Dinheiro; E = Estar bem com meus amigos; F = Conseguir entrar na faculdade / universidade; G = A falta de liberdade, a dependência de minha família; … (lista completa no dicionário da fonte) | 2001 a 2002 | `microdados_enem` |
| `q63_1` | `Q63_1` | texto | O que mais preocupa o candidato em 1º lugar no momento | A = O meio ambiente; B = A Aids e as doenças perigosas e sem cura; C = O racismo e o desrespeito às pessoas de outra raça ou religião; D = A pobreza, as favelas, os meninos de rua; E = As drogas e a violência; F = A situação do país | 2001 a 2002 | `microdados_enem` |
| `q63_2` | `Q63_2` | texto | O que mais preocupa o candidato em 2º lugar no momento | A = O meio ambiente; B = A Aids e as doenças perigosas e sem cura; C = O racismo e o desrespeito às pessoas de outra raça ou religião; D = A pobreza, as favelas, os meninos de rua; E = As drogas e a violência; F = A situação do país | 2001 a 2002 | `microdados_enem` |
| `q64_1` | `Q64_1` | texto | Para se conseguir alguma coisa na vida é preciso ter sorte. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_2` | `Q64_2` | texto | É importante ser honesto e trabalhador, mas não se consegue nada na vida. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_3` | `Q64_3` | texto | Só se realiza quem cursa uma faculdade e consegue um diploma superior. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_4` | `Q64_4` | texto | Quando se é perseverante se consegue tudo. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_5` | `Q64_5` | texto | È bom ter amigos influentes, pois está cada vez mais difícil conseguir o que se quer. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_6` | `Q64_6` | texto | O sucesso só vale a pena se for obtido com honestidade e trabalho. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_7` | `Q64_7` | texto | È a competência de cada um que leva ao sucesso profissional. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_8` | `Q64_8` | texto | É preciso ter fé para conseguir as coisas. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_9` | `Q64_9` | texto | Não tem nada de mais fumar maconha. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_10` | `Q64_10` | texto | Cada vez mais a sociedade valoriza quem estuda. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_11` | `Q64_11` | texto | Existe pobreza e miséria no país porque não há vontade de trabalhar. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_12` | `Q64_12` | texto | Vale tudo para conseguir meus objetivos. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q64_13` | `Q64_13` | texto | O uso de drogas e do álcool são duas das piores coisas do mundo de hoje. | A = Concorda; B = Discorda | 2001 a 2002 | `microdados_enem` |
| `q65_1` | `Q65_1` | texto | É a primeira mais importante contribuição que obteve ao realizar o ensino médio(2º grau) | A = Obtenção de um certificado de conclusão de curso/ obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2001 a 2002 | `microdados_enem` |
| `q65_2` | `Q65_2` | texto | É a segunda mais importante contribuição que obteve ao realizar o ensino médio(2º grau) | A = Obtenção de um certificado de conclusão de curso/ obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2001 a 2002 | `microdados_enem` |
| `q65_3` | `Q65_3` | texto | É a terceira mais importante contribuição que obteve ao realizar o ensino médio(2º grau) | A = Obtenção de um certificado de conclusão de curso/ obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2001 a 2002 | `microdados_enem` |
| `q65_4` | `Q65_4` | texto | Importância dada pelo candidato do ENEM com relação a conviver com a família | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_5` | `Q65_5` | texto | Importância dada pelo candidato do ENEM com relação a ter um envolvimento amoroso, namorar | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_6` | `Q65_6` | texto | Importância dada pelo candidato do ENEM com relação a realizar programas culturais, ir ao teatro, ao cinema, etc | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_7` | `Q65_7` | texto | Importância dada pelo candidato do ENEM com relação escutar rádio, assistir a programas de TV | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_8` | `Q65_8` | texto | Importância dada pelo candidato do ENEM com relação ler obras de ficção, romances | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_9` | `Q65_9` | texto | Importância dada pelo candidato do ENEM com relação a fazer algum trabalho vonluntário para a comunidade, ajudar as pessoas | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_10` | `Q65_10` | texto | Importância dada pelo candidato do ENEM com relação a praticar esportes, fazer ginástica, cuidar do físico | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_11` | `Q65_11` | texto | Importância dada pelo candidato do ENEM com relação a ter uma atividade política, participar de Ongs, sindicatos, grêmio estudantil | 1 = Classificação | 2001 | `microdados_enem` |
| `q65_12` | `Q65_12` | texto | Importância dada pelo candidato do ENEM com relação ir a Igreja, participar de atividades por ela promovidas | 1 = Classificação | 2001 | `microdados_enem` |
| `q66_1` | `Q66_1` | texto | O ensino médio contriu para obtenção de um certificado de conclusão de curso/ obtenção de um diploma. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_2` | `Q66_2` | texto | O ensino médio contriu para formação básica necessária para obter um emprego melhor. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_3` | `Q66_3` | texto | O ensino médio contriu para condições de melhorar minha posição no emprego atual. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_4` | `Q66_4` | texto | O ensino médio contriu para obtenção de cultura geral/ampliação de minha formação pessoal. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_5` | `Q66_5` | texto | O ensino médio contriu para formação básica necessária para continuar os estudos em uma universidade/faculdade. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_6` | `Q66_6` | texto | O ensino médio contriu para fazer muitos amigos/conhecer várias pessoas. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q66_7` | `Q66_7` | texto | O ensino médio contriu para atender à expectativa de meus pais sobre meus estudos. | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q70_1` | `Q70_1` | texto | Meus pais ajudaram a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_2` | `Q70_2` | texto | A escola ajudou a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_3` | `Q70_3` | texto | Meus amigos ajudaram a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_4` | `Q70_4` | texto | Informações gerais, revistas, jornais, TV ajudaram a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_5` | `Q70_5` | texto | Meu trabalho ajudou a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_6` | `Q70_6` | texto | Estímulo financeiro ajudou a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_7` | `Q70_7` | texto | Facilidade de obter emprego ajudou a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q70_8` | `Q70_8` | texto | Minha identificação com a profissão me ajudou a tomar minha decisão sobre minha profissão | 1 = Classificação | 2001 | `microdados_enem` |
| `q71_1` | `Q71_1` | texto | Está freqüentando um curso profissionalizante | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q71_2` | `Q71_2` | texto | Está freqüentando um curso preparatório para vestibular | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q71_3` | `Q71_3` | texto | Está freqüentando um curso superior | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q71_4` | `Q71_4` | texto | Está freqüentando um curso de língua estrangeira | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_1` | `Q73_1` | texto | O curso profissionalizante fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_2` | `Q73_2` | texto | O curso preparatório para vestibular fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_3` | `Q73_3` | texto | O curso superior fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_4` | `Q73_4` | texto | O curso de língua estrangeira fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_5` | `Q73_5` | texto | O curso de computação ou informática fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q73_6` | `Q73_6` | texto | Outro curso fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 a 2002 | `microdados_enem` |
| `q74_1` | `Q74_1` | texto | Concluiu curso profissionalizante | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_2` | `Q74_2` | texto | Concluiu curso preparatório para vestibular, mas não ingressei no curso superior | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_3` | `Q74_3` | texto | Concluiu curso superior | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_4` | `Q74_4` | texto | Fiz curso superior mas não me formei | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_5` | `Q74_5` | texto | Concluiu curso de língua estrangeira | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_6` | `Q74_6` | texto | Concluiu curso de computação ou informática | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q74_7` | `Q74_7` | texto | Concluiu outro curso | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_1` | `Q75_1` | texto | O curso profissionalizante fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_2` | `Q75_2` | texto | O curso preparatório para vestibular fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_3` | `Q75_3` | texto | O curso superior fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_4` | `Q75_4` | texto | O curso de língua estrangeira fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_5` | `Q75_5` | texto | O curso de computação ou informática fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q75_6` | `Q75_6` | texto | Outro curso fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2001 | `microdados_enem` |
| `q48_5` | `Q48_5` | texto | Avaliação sobre a escola quanto a discussão dos problemas da atualidade nas aulas | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_6` | `Q48_6` | texto | Avaliação sobre a escola quanto a convivência entre alunos | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_7` | `Q48_7` | texto | Avaliação sobre a escola quanto a organização para apoiar a resolução de problemas de relacionamento entre alunos | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_8` | `Q48_8` | texto | Avaliação sobre a escola quanto a iniciativa para apoiar a resolução de problemas de relacionamento entre alunos e professores | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_9` | `Q48_9` | texto | Avaliação sobre a escola quanto a levar em conta seus problemas pessoais e familiares | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_10` | `Q48_10` | texto | Avaliação sobre a escola quanto a realização de Programas e Palestras contra drogas | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_11` | `Q48_11` | texto | Avaliação sobre a escola quanto a capacidade relacionar os conteúdos das matérias com o cotidiano | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q48_12` | `Q48_12` | texto | Avaliação sobre a escola quanto a capacidade de a escola avaliar conhecimento, o que aprendeu | 1 2 3 4 5 6 7 8 9 10 = Nota | 2002 | `microdados_enem` |
| `q54_1` | `Q54_1` | texto | O candidato já procurou pela família para resolver seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_2` | `Q54_2` | texto | O candidato já procurou cartomante para resolver seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_3` | `Q54_3` | texto | O candidato já consultou o jogo de búzios para resolver os seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_4` | `Q54_4` | texto | O candidato foi à Igreja/procurou padre/pastor para resolver seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_5` | `Q54_5` | texto | O candidato buscou ajuda profissional (psicólogo, médico,etc) para resolver seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_6` | `Q54_6` | texto | O candidato consultou horóscopo para resolver os seus problemas pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_7` | `Q54_7` | texto | O candidato já procurou pelos amigos para resolver | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q54_8` | `Q54_8` | texto | O candidato buscou orientação em livros e revistas para resolver dados pessoais | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_1` | `Q57_1` | texto | Participa de um Grêmio estudantil | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_2` | `Q57_2` | texto | Participa de um Sindicato ou Associação Profissional | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_3` | `Q57_3` | texto | Participa de um Grupo de bairro ou associação comunitária | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_4` | `Q57_4` | texto | Participa de uma Igreja ou grupo religioso | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_5` | `Q57_5` | texto | Participa de um partido político | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_6` | `Q57_6` | texto | Participa de uma Ong ou movimento social | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q57_7` | `Q57_7` | texto | Participa de um clube recreativo ou associação esportiva | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q58_1` | `Q58_1` | texto | O quanto você se interessa pela política nacional, o papel dos(as) deputados(as) e senadores(as), o Presidente da República, etc | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_2` | `Q58_2` | texto | O quanto você se interessa pela política dos outros países | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_3` | `Q58_3` | texto | O quanto você se interessa pela economia nacional, a questão da inflação, o plano real | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_4` | `Q58_4` | texto | O quanto você se interessa a política da sua cidade, o prefeito, os vereadores | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_5` | `Q58_5` | texto | O quanto você se interessa por esportes | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_6` | `Q58_6` | texto | O quanto você se interessa pelas questões sobre o meio ambiente, poluição, etc | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_7` | `Q58_7` | texto | O quanto você se interessa pelas questões sociais como a desigualdade, a pobreza, o desemprego, a miséria | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_8` | `Q58_8` | texto | O quanto você se interessa pelas questões sobre artes, teatro, cinema | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_9` | `Q58_9` | texto | O quanto você se interessa sobre a questão das drogas e suas conseqüências | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q58_10` | `Q58_10` | texto | O quanto você se interessa sobre assuntos sobre seu ídolo (cantor/a, artista, ou conjunto musical) | A = Muito; B = Pouco; C = Não me interesso | 2002 | `microdados_enem` |
| `q69_1` | `Q69_1` | texto | Meus pais ajudaram a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_2` | `Q69_2` | texto | A escola ajudou a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_3` | `Q69_3` | texto | Meus amigos ajudaram a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_4` | `Q69_4` | texto | Informações gerais, revistas, jornais, TV ajudaram a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_5` | `Q69_5` | texto | Meu trabalho ajudou a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_6` | `Q69_6` | texto | Estímulo financeiro ajudou a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_7` | `Q69_7` | texto | Facilidade de obter emprego ajudou a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q69_8` | `Q69_8` | texto | Minha identificação com a profissão me ajudou a tomar minha decisão sobre minha profissão | 1 2 3 4 5 6 7 8 = Classificação | 2002 | `microdados_enem` |
| `q71_5` | `Q71_5` | texto | Está freqüentando um curso de computação ou informática | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q71_6` | `Q71_6` | texto | Está freqüentando outro curso | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_1` | `Q72_1` | texto | Concluiu curso profissionalizante | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_2` | `Q72_2` | texto | Concluiu curso preparatório para vestibular, mas não ingressei no curso superior | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_3` | `Q72_3` | texto | Concluiu curso superior | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_4` | `Q72_4` | texto | Fiz curso superior mas não me formei | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_5` | `Q72_5` | texto | Concluiu curso de língua estrangeira | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_6` | `Q72_6` | texto | Concluiu curso de computação ou informática | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q72_7` | `Q72_7` | texto | Concluiu outro curso | A = Sim; B = Não | 2002 | `microdados_enem` |
| `q138` | `Q138` | texto | Avaliação sobre a escola quanto à iniciativa para apoiar a resolução de problemas de relacionamento entre estudantes e professores(as) | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q139` | `Q139` | texto | Avaliação sobre a escola quanto à levar em conta seus problemas pessoais e familiares | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q140` | `Q140` | texto | Avaliação sobre a escola quanto à realização de Projetos e Palestras contra drogas | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q141` | `Q141` | texto | Avaliação sobre a escola quanto à realização de projetos e palestras sobre promoção da saúde e prevenção a Aids e a doenças sexualmente transmissíveis | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q142` | `Q142` | texto | Avaliação da escola quanto à realização de projetos e palestras sobre direitos humanos e violência | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q143` | `Q143` | texto | Avaliação da escola quanto à adoção de medidas para garantir a acessibilidade a estudantes com deficiências físicas ou mentais | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q144` | `Q144` | texto | Avaliação sobre a escola quanto à capacidade de relacionar os conteúdos das matérias com o cotidiano | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q145` | `Q145` | texto | Avaliação sobre a escola quanto ao reconhecimento e valorização da identidade étnica dos estudantes | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q146` | `Q146` | texto | Avaliação da escola quanto à levar em conta a opinião/participação dos pais | A = Insuficiente a regular; B = Regular a bom; C = Bom a excelente | 2003 a 2009 | `microdados_enem` |
| `q147` | `Q147` | texto | Nota para a formação que obteve no ensino médio | A = 0; B = 1; C = 2; D = 3; E = 4; F = 5; G = 6; H = 7; I = 8; J = 9; K = 10; L = Não sei; M = Não cursei | 2003 a 2009 | `microdados_enem` |
| `q148` | `Q148` | texto | Considera-se racista | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q149` | `Q149` | texto | Parentes racistas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q150` | `Q150` | texto | Amigos(as) ou colegas de escola e/ou trabalho racistas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q151` | `Q151` | texto | Vizinhos e/ou conhecidos racistas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q152` | `Q152` | texto | Professores(as) ou funcionários da escola | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q153` | `Q153` | texto | Pessoas em geral (nas ruas, nos ambientes públicos, etc.) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q154` | `Q154` | texto | Acredita possuir algum preconceito contra pessoas mais pobres / participantes de programas sociais do governo (Bolsa família, etc.) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q155` | `Q155` | texto | Acredita possuir algum preconceito contra negros(as), indígenas, orientais, ciganos(as), ou de outras etnias | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q156` | `Q156` | texto | Acredita possuir algum preconceito contra mulheres | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q157` | `Q157` | texto | Acredita possuir algum preconceito contra homossexuais ou gays, lésbicas, bissexuais, travestis, transexuais | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q158` | `Q158` | texto | Acredita possuir algum preconceito contra pessoas muito religiosas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q159` | `Q159` | texto | Acredita possuir algum preconceito contra pessoas de outra religião | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q160` | `Q160` | texto | Acredita possuir algum preconceito contra pessoas sem religião | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q161` | `Q161` | texto | Acredita possuir algum preconceito contra pessoas de outras cidades, do interior, da zona rural ou de outras regiões do país ou do exterior | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q162` | `Q162` | texto | Acredita possuir algum preconceito contra pessoas idosas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q163` | `Q163` | texto | Acredita possuir algum preconceito contra pessoas com deficiência física ou mental | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q164` | `Q164` | texto | Acredita possuir algum preconceito contra pessoas muito gordas ou muito magras | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q165` | `Q165` | texto | Acredita possuir algum preconceito contra moradores(as) de favela ou de periferia | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q166` | `Q166` | texto | Acredita possuir algum preconceito contra meninos(as) em situação de rua | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q167` | `Q167` | texto | Acredita possuir algum preconceito contra jovens infratores(as) / jovens em conflito com a lei | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q168` | `Q168` | texto | Acredita possuir algum preconceito contra usuários(as) de drogas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q169` | `Q169` | texto | Já sofreu discriminação econômica | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q170` | `Q170` | texto | Já sofreu discriminação étnica, racial ou de cor | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q171` | `Q171` | texto | Já sofreu discriminação de gênero (ou por ser mulher ou por ser homem) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q172` | `Q172` | texto | Já sofreu discriminação por ser ou ter sido identificado como homossexual (gay, lésbica, bissexual, travesti ou transexual | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q173` | `Q173` | texto | Já sofreu discriminação religiosa | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q174` | `Q174` | texto | Já sofreu discriminação por não ter religião | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q175` | `Q175` | texto | Já sofreu discriminação por causa do local de seu nascimento (em outra cidade, no interior, em outra região, no exterior, etc.) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q176` | `Q176` | texto | Já sofreu discriminação por causa da idade | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q177` | `Q177` | texto | Já sofreu discriminação por ser pessoa com deficiência física ou mental | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q178` | `Q178` | texto | Já sofreu discriminação por causa de sua aparência física (gordo/a, magro/a, alto/a, baixo/a, etc.) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q179` | `Q179` | texto | Já sofreu discriminação por causa do lugar de sua moradia | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q180` | `Q180` | texto | Já presenciou discriminação econômica | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q181` | `Q181` | texto | Já presenciou discriminação étnica, racial ou de cor | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q182` | `Q182` | texto | Já presenciou discriminação contra mulheres | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q183` | `Q183` | texto | Já presenciou discriminação contra homossexuais (gay, lésbica, bissexual, travesti ou transexual) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q184` | `Q184` | texto | Já presenciou discriminação religiosa | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q185` | `Q185` | texto | Já presenciou discriminação por causa do local de seu nascimento (em outra cidade, no interior, em outra região, no exterior, etc.) | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q186` | `Q186` | texto | Já presenciou discriminação contra jovens menores de 18 anos | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q187` | `Q187` | texto | Já presenciou discriminação contra pessoas idosas | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q188` | `Q188` | texto | Já presenciou discriminação por ser pessoa com deficiência | A = Sim; B = Não | 2003 a 2009 | `microdados_enem` |
| `q189` | `Q189` | texto | Já presenciou discriminação por causa de sua aparência física | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q190` | `Q190` | texto | Já presenciou discriminação por causa do lugar de sua moradia | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q191` | `Q191` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa de outra classe social | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q192` | `Q192` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa de outra cor ou etnia | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q193` | `Q193` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa de outra religião | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q194` | `Q194` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa com posições políticas diferentes da sua | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q195` | `Q195` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa de outra origem geográfica | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q196` | `Q196` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa homossexual (gay, lésbica, bissexual, travesti ou transexual) | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q197` | `Q197` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa muito mais nova ou mais velha | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q198` | `Q198` | texto | Se incomodaria se tivesse como parente ou colega de escola uma pessoa com deficiência física ou mental | A = Sim; B = Não | 2004 a 2009 | `microdados_enem` |
| `q199` | `Q199` | texto | O quanto você se interessa pela política | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q200` | `Q200` | texto | O quanto você se interessa pela globalização | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q201` | `Q201` | texto | O quanto você se interessa por esportes | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q202` | `Q202` | texto | O quanto você se interessa por religião | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q203` | `Q203` | texto | O quanto você se interessa pelas questões do meio ambiente, poluição | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q204` | `Q204` | texto | O quanto você se interessa pelas questões sobre desigualdade social, pobreza, desemprego, miséria | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q205` | `Q205` | texto | O quanto você se interessa pelas questões sobre artes, teatro, cinema | A = Muito; B = Pouco; C = Não me interesso | 2004 a 2009 | `microdados_enem` |
| `q206` | `Q206` | texto | O quanto você se interessa sobre a questão das drogas | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q207` | `Q207` | texto | O quanto você se interessa sobre a questão do acesso e qualidade dos serviços públicos de saúde e educação | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q208` | `Q208` | texto | O quanto você se interessa pelas questões sobre sexualidade (prazer, sexo seguro, gravidez, doenças sexualmente transmissíveis, etc.) | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q209` | `Q209` | texto | O quanto você se interessa pelas questões sobre racismo contra negros, indígenas, orientais, ciganos, judeus, etc. | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q210` | `Q210` | texto | O quanto você se interessa pelas questões sobre discriminação e violência contra mulheres | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q211` | `Q211` | texto | O quanto você se interessa pelas questões sobre discriminação e violência contra homossexuais (gay, lésbica, bissexual, travesti ou transexual) | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q212` | `Q212` | texto | O quanto você se interessa pelas questões sobre discriminação e violência contra crianças e adolescentes | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q213` | `Q213` | texto | O quanto você se interessa pelas questões sobre discriminação e violência contra pessoas idosas | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q214` | `Q214` | texto | O quanto você se interessa pelas questões sobre discriminação e violência contra pessoas com deficiência | A = Muito; B = Pouco; C = Não me interesso | 2005 a 2009 | `microdados_enem` |
| `q215` | `Q215` | texto | A primeira contribuição para a sua vida pessoal que obteve ao realizar o Ensino Médio foi | A = Obtenção de um certificado de conclusão de curso / obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q216` | `Q216` | texto | A segunda contribuição para a sua vida pessoal que obteve ao realizar o Ensino Médio foi | A = Obtenção de um certificado de conclusão de curso / obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q217` | `Q217` | texto | A terceira contribuição para a sua vida pessoal que obteve ao realizar o Ensino Médio foi | A = Obtenção de um certificado de conclusão de curso / obtenção de um diploma; B = Formação básica necessária para obter um emprego melhor; C = Condições de melhorar minha posição no emprego atual; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q218` | `Q218` | texto | A principal decisão que vai tomar quando concluir ou obter a certificação do ensino médio (2º grau) | A = Já conclui o ensino médio; B = Prestar vestibular e continuar os estudos no ensino superior; C = Procurar um emprego; D = Prestar vestibular e continuar a trabalhar; E = Fazer curso(s) profissionalizante(s) e me preparar para o trabalho; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q219` | `Q219` | texto | E a médio prazo, daqui a uns 4 ou 5 anos já planejou o que gostaria que acontecesse | A = Gostaria de ter um diploma universitário para conseguir um bom emprego; B = Gostaria de prestar um concurso e trabalhar no setor público; C = Gostaria de ganhar dinheiro em meu próprio negócio; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q220` | `Q220` | texto | Que profissão escolheu seguir | A = Ainda não escolhi; B = Profissão ligada às Engenharias / Ciências Tecnológicas / Matemáticas; C = Profissão ligada às Ciências Humanas; D = Profissão ligada às Artes; E = Profissão ligadas às Ciências Biológicas e de Saúde; … (lista completa no dicionário da fonte) | 2005 a 2009 | `microdados_enem` |
| `q221` | `Q221` | texto | Meus pais ajudaram a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2005 a 2009 | `microdados_enem` |
| `q222` | `Q222` | texto | A escola ajudou a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2005 a 2009 | `microdados_enem` |
| `q223` | `Q223` | texto | Meus amigos ajudaram a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2005 a 2009 | `microdados_enem` |
| `tp_ensino` | `TP_ENSINO` | texto | Tipo de instituição que concluiu ou concluirá o Ensino Médio | 1 = Ensino Regular; 2 = Educação Especial - Modalidade Substitutiva | 2006 a 2025 | `microdados_enem`, `participantes` |
| `co_municipio_prova` | `CO_MUNICIPIO_PROVA` | texto | Código do município da aplicação da prova | — | 2008 a 2025 | `microdados_enem`, `participantes`, `resultados` |
| `no_municipio_prova` | `NO_MUNICIPIO_PROVA` | texto | Nome do município da aplicação da prova | — | 2008 a 2025 | `microdados_enem`, `participantes`, `resultados` |
| `co_uf_prova` | `CO_UF_PROVA` | texto | Código da Unidade da Federação da aplicação da prova | 11 = Rondônia; 12 = Acre; 13 = Amazonas; 14 = Roraima; 15 = Pará; 16 = Amapá; 17 = Tocantins; 21 = Maranhão; 22 = Piauí; 23 = Ceará; 24 = Rio Grande do Norte; 25 = Paraíba; 26 = Pernambuco; 27 = Alagoas; 28 = Sergipe; 29 = Bahia; 31 = Minas Gerais; … (lista completa no dicionário da fonte) | 2008 a 2025 | `microdados_enem`, `participantes`, `resultados` |
| `sg_uf_prova` | `SG_UF_PROVA` | texto | Sigla da Unidade da Federação da aplicação da prova | RO = Rondônia; AC = Acre; AM = Amazonas; RR = Roraima; PA = Pará; AP = Amapá; TO = Tocantins; MA = Maranhão; PI = Piauí; CE = Ceará; RN = Rio Grande do Norte; PB = Paraíba; PE = Pernambuco; AL = Alagoas; SE = Sergipe; BA = Bahia; MG = Minas Gerais; … (lista completa no dicionário da fonte) | 2008 a 2025 | `microdados_enem`, `participantes`, `resultados` |
| `co_posicao` | `CO_POSICAO` | texto | Posição do item na prova | — | 2009 a 2025 | `itens_prova` |
| `sg_area` | `SG_AREA` | texto | Sigla da área de conhecimento do item | CH = Ciências Humanas; CN = Ciências da Natureza; LC = Linguagens e Códigos; MT = Matemática | 2009 a 2025 | `itens_prova` |
| `co_item` | `CO_ITEM` | texto | Código do item | — | 2009 a 2025 | `itens_prova` |
| `tx_gabarito` | `TX_GABARITO` | texto | Gabarito do item¹ | — | 2009 a 2025 | `itens_prova` |
| `co_habilidade` | `CO_HABILIDADE` | texto | Habilidade do item | — | 2009 a 2025 | `itens_prova` |
| `in_item_aban` | `IN_ITEM_ABAN` | texto | Indicador de item abandonado | 0 = Não; 1 = Sim | 2009 a 2025 | `itens_prova` |
| `tx_motivo_aban` | `TX_MOTIVO_ABAN` | texto | Motivo para o abandono do item | — | 2009 a 2025 | `itens_prova` |
| `nu_param_a` | `NU_PARAM_A` | texto | Parâmetro de discriminação: é o poder de discriminação do item para diferenciar os participantes que dominam dos participantes que não dominam a habilidade avaliada. | — | 2009 a 2025 | `itens_prova` |
| `nu_param_b` | `NU_PARAM_B` | texto | Parâmetro de dificuldade: associado à dificuldade do item, sendo que quanto maior seu valor, mais difícil é o item. | — | 2009 a 2025 | `itens_prova` |
| `nu_param_c` | `NU_PARAM_C` | texto | Parâmetro de acerto ao acaso: é a probabilidade de um participante acertar o item não dominando a habilidade exigida. | — | 2009 a 2025 | `itens_prova` |
| `tx_cor` | `TX_COR` | texto | Cor da prova | — | 2009 a 2025 | `itens_prova` |
| `tp_presenca_cn` | `TP_PRESENCA_CN` | texto | Presença na prova objetiva de Ciências da Natureza | 0 = Faltou à prova; 1 = Presente na prova; 2 = Eliminado na prova | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tp_presenca_ch` | `TP_PRESENCA_CH` | texto | Presença na prova objetiva de Ciências Humanas | 0 = Faltou à prova; 1 = Presente na prova; 2 = Eliminado na prova | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tp_presenca_lc` | `TP_PRESENCA_LC` | texto | Presença na prova objetiva de Linguagens e Códigos | 0 = Faltou à prova; 1 = Presente na prova; 2 = Eliminado na prova | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tp_presenca_mt` | `TP_PRESENCA_MT` | texto | Presença na prova objetiva de Matemática | 0 = Faltou à prova; 1 = Presente na prova; 2 = Eliminado na prova | 2009 a 2025 | `microdados_enem`, `resultados` |
| `nu_nota_cn` | `NU_NOTA_CN` | texto | Nota da prova de Ciências da Natureza | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `nu_nota_ch` | `NU_NOTA_CH` | texto | Nota da prova de Ciências Humanas | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `nu_nota_lc` | `NU_NOTA_LC` | texto | Nota da prova de Linguagens e Códigos | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `nu_nota_mt` | `NU_NOTA_MT` | texto | Nota da prova de Matemática | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_respostas_cn` | `TX_RESPOSTAS_CN` | texto | Vetor com as respostas da parte objetiva da prova de Ciências da Natureza3 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_respostas_ch` | `TX_RESPOSTAS_CH` | texto | Vetor com as respostas da parte objetiva da prova de Ciências Humanas3 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_respostas_lc` | `TX_RESPOSTAS_LC` | texto | Vetor com as respostas da parte objetiva da prova de Linguagens e Códigos4 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_respostas_mt` | `TX_RESPOSTAS_MT` | texto | Vetor com as respostas da parte objetiva da prova de Matemática3 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `co_prova_cn` | `CO_PROVA_CN` | texto | Código do tipo de prova de Ciências da Natureza | 1483 = Azul; 1484 = Amarela; 1485 = Verde; 1486 = Cinza; 1487 = Laranja - Ampliada; 1488 = Laranja - Superampliada; 1490 = Laranja - Adaptada Ledor; 1491 = Roxo - Videoprova - Libras; 1498 = Laranja - Atendimento Especializado; 1569 = Azul (Reaplicação); … (lista completa no dicionário da fonte) | 2009 a 2025 | `microdados_enem`, `resultados` |
| `co_prova_ch` | `CO_PROVA_CH` | texto | Código do tipo de prova de Ciências Humanas | 1447 = Azul; 1448 = Amarela; 1449 = Branca; 1450 = Verde; 1451 = Laranja - Ampliada; 1452 = Laranja - Superampliada; 1454 = Laranja - Adaptada Ledor; 1455 = Roxo - Videoprova - Libras; 1495 = Laranja - Atendimento Especializado; 1539 = Azul (Reaplicação); … (lista completa no dicionário da fonte) | 2009 a 2025 | `microdados_enem`, `resultados` |
| `co_prova_lc` | `CO_PROVA_LC` | texto | Código do tipo de prova de Linguagens e Códigos | 1459 = Azul; 1460 = Amarela; 1461 = Verde; 1462 = Branca; 1463 = Laranja - Ampliada; 1464 = Laranja - Superampliada; 1466 = Laranja - Adaptada Ledor; 1467 = Roxo - Videoprova - Libras; 1496 = Laranja - Atendimento Especializado; 1549 = Azul (Reaplicação); … (lista completa no dicionário da fonte) | 2009 a 2025 | `microdados_enem`, `resultados` |
| `co_prova_mt` | `CO_PROVA_MT` | texto | Código do tipo de prova de Matemática | 1471 = Azul; 1472 = Amarela; 1473 = Verde; 1474 = Cinza; 1475 = Laranja - Ampliada; 1476 = Laranja - Superampliada; 1478 = Laranja - Adaptada Ledor; 1479 = Roxo - Videoprova - Libras; 1497 = Laranja - Atendimento Especializado; 1559 = Azul (Reaplicação); … (lista completa no dicionário da fonte) | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_gabarito_cn` | `TX_GABARITO_CN` | texto | Vetor com o gabarito da parte objetiva da prova de Ciências da Natureza5 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_gabarito_ch` | `TX_GABARITO_CH` | texto | Vetor com o gabarito da parte objetiva da prova de Ciências Humanas5 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_gabarito_lc` | `TX_GABARITO_LC` | texto | Vetor com o gabarito da parte objetiva da prova de Linguagens e Códigos6 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `tx_gabarito_mt` | `TX_GABARITO_MT` | texto | Vetor com o gabarito da parte objetiva da prova de Matemática5 | — | 2009 a 2025 | `microdados_enem`, `resultados` |
| `in_certificado` | `IN_CERTIFICADO` | texto | Indicador de solicitação de certificação no Ensino Médio4 | 1 = Sim; 0 = Não | 2009 a 2016 | `microdados_enem` |
| `q224` | `Q224` | texto | Informações gerais, revistas, jornais, TV ajudaram a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2009 | `microdados_enem` |
| `q225` | `Q225` | texto | Meu trabalho ajudou a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2009 | `microdados_enem` |
| `q226` | `Q226` | texto | Estímulo financeiro ajudou a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2009 | `microdados_enem` |
| `q227` | `Q227` | texto | Facilidade de obter emprego ajudou a tomar minha decisão sobre minha profissão | A = Ajudou muito; B = Ajudou pouco; C = Não ajudou | 2009 | `microdados_enem` |
| `q228` | `Q228` | texto | Continuou os estudos depois de ter concluído o ensino médio (2º grau) | A = Sim, estou estudando no momento atual; B = Sim, mas não estou estudando no momento atual; C = Não | 2009 | `microdados_enem` |
| `q229` | `Q229` | texto | Frequentou ou está frequentando um curso profissionalizante | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q230` | `Q230` | texto | Frequentou ou está frequentando um curso preparatório para vestibular | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q231` | `Q231` | texto | Frequentou ou está frequentando um curso superior | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q232` | `Q232` | texto | Frequentou ou está frequentando um curso de língua estrangeira | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q233` | `Q233` | texto | Frequentou ou está frequentando um curso de computação ou informática | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q234` | `Q234` | texto | Frequentou ou está frequentando um curso preparatório para outros concursos públicos | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q235` | `Q235` | texto | Frequentou ou está frequentando outro curso | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q236` | `Q236` | texto | O curso profissionalizante fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q237` | `Q237` | texto | O curso preparatório para vestibular fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q238` | `Q238` | texto | O curso superior fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q239` | `Q239` | texto | O curso de língua estrangeira fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q240` | `Q240` | texto | O curso de computação ou informática fez mais falta para minha vida, depois que terminei o ensino médio | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q241` | `Q241` | texto | Como realiza ou realizou o Curso de Educação de Jovens e Adultos - EJA | A = Frequenta curso presencial em escola pública; B = Frequenta curso presencial em escola particular; C = Frequenta curso presencial na empresa em que trabalha; D = Frequenta tele-sala; E = Frequenta curso promovido por instituição religiosa ou filantrópica; … (lista completa no dicionário da fonte) | 2009 | `microdados_enem` |
| `q242` | `Q242` | texto | Período em que cursa a EJA | A = Diurno; B = Noturno; C = A distância; D = Não curso | 2009 | `microdados_enem` |
| `q243` | `Q243` | texto | Já havia cursado antes a EJA e depois parou | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q244` | `Q244` | texto | Parou de frequentar a EJA porque o horário de trabalho era difícil/não tinha tempo de estudar | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q245` | `Q245` | texto | Parou de frequentar a EJA porque estudava no curso da empresa e fui demitido | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q246` | `Q246` | texto | Parou de frequentar a EJA porque teve problemas ligados à saúde ou acidentes ou pessoas da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q247` | `Q247` | texto | Parou de frequentar a EJA porque mudou de cidade | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q248` | `Q248` | texto | Parou de frequentar a EJA porque casou/teve filhos | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q249` | `Q249` | texto | Parou de frequentar a EJA porque não tinha interesse/desistiu | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q250` | `Q250` | texto | Parou de frequentar a EJA porque sentiu-se discriminado/sofreu agressão | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q251` | `Q251` | texto | Não frequentou | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q252` | `Q252` | texto | Frequentou alguma vez escola regular | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q253` | `Q253` | texto | Se já frequentou escola regular, em que série ou ano escolar deixou a escola | A = 1ª série do Ensino Fundamental; B = 2ª série do Ensino Fundamental; C = 3ª série do Ensino Fundamental; D = 4ª série do Ensino Fundamental; E = 5ª série do Ensino Fundamental; F = 6ª série do Ensino Fundamental; G = 7ª série do Ensino Fundamental; … (lista completa no dicionário da fonte) | 2009 | `microdados_enem` |
| `q254` | `Q254` | texto | Quanto tempo levou para cursar a 1ª Série do Ensino Médio | A = Não cursou/não frequentou; B = 1 ano; C = 2 ano; D = Mais de 2 anos | 2009 | `microdados_enem` |
| `q255` | `Q255` | texto | Quanto tempo levou para cursar a 2ª Série do Ensino Médio | A = Não cursou/não frequentou; B = 3 ano; C = 4 ano; D = Mais de 2 anos | 2009 | `microdados_enem` |
| `q256` | `Q256` | texto | Quanto tempo levou para cursar a 3ª Série do Ensino Médio | A = Não cursou/não frequentou; B = 5 ano; C = 6 ano; D = Mais de 2 anos | 2009 | `microdados_enem` |
| `q257` | `Q257` | texto | Em que tipo de escola cursou a 1ª Série do Ensino Médio | A = Escola da Prefeitura (Municipal); B = Escola estadual ou federal; C = Escola particular; D = Escola de igreja ou instituição filantrópica; E = Não cursou | 2009 | `microdados_enem` |
| `q258` | `Q258` | texto | Em que tipo de escola cursou a 2ª Série do Ensino Médio | A = Escola da Prefeitura (Municipal); B = Escola estadual ou federal; C = Escola particular; D = Escola de igreja ou instituição filantrópica; E = Não cursou | 2009 | `microdados_enem` |
| `q259` | `Q259` | texto | Em que tipo de escola cursou a 3ª Série do Ensino Médio | A = Escola da Prefeitura (Municipal); B = Escola estadual ou federal; C = Escola particular; D = Escola de igreja ou instituição filantrópica; E = Não cursou | 2009 | `microdados_enem` |
| `q260` | `Q260` | texto | Quantos anos tinha quando deixou de frequentar a escola regular | A = Menos de 10 anos; B = Entre 10 e 14 anos (inclusive); C = Entre 15 e 18 anos (inclusive); D = Entre 19 e 24 anos (inclusive); E = Entre 25 e 30 anos (inclusive); F = Mais de 30 anos; G = Nunca frequentei | 2009 | `microdados_enem` |
| `q261` | `Q261` | texto | Nunca frequentou uma escola regular porque não conseguiu vaga em escola pública / a família não tinha condições de pagar os estudos | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q262` | `Q262` | texto | Nunca frequentou uma escola regular porque não havia escola perto de casa | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q263` | `Q263` | texto | Nunca frequentou uma escola regular porque não gostava de estudar / não tinha interesse | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q264` | `Q264` | texto | Nunca frequentou uma escola regular por motivos ligados ao trabalho: horário de trabalho era difícil / não tinha tempo de estudar | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q265` | `Q265` | texto | Nunca frequentou uma escola regular porque parou de estudar porque casou / teve filhos / teve que cuidar da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q266` | `Q266` | texto | Nunca frequentou uma escola regular porque não tinha apoio da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q267` | `Q267` | texto | Nunca frequentou uma escola regular por problemas ligados à saúde: sofreu acidente/ficou doente/aconteceu algum acidente com pessoas da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q268` | `Q268` | texto | Nunca frequentou uma escola regular porque sofreu discriminação | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q269` | `Q269` | texto | Deixou de frequentar uma escola regular porque foi reprovado | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q270` | `Q270` | texto | Deixou de frequentar uma escola regular porque não conseguiu vaga em escola pública / a família não tinha condições de pagar os estudos | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q271` | `Q271` | texto | Deixou de frequentar uma escola regular porque não havia escola perto de casa | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q272` | `Q272` | texto | Deixou de frequentar uma escola regular porque a escola a escola que frequentava era muito ruim (tinha muita bagunça, não tinha professores, as aulas não eram boas, etc.) | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q273` | `Q273` | texto | Deixou de frequentar uma escola regular porque não gostava de estudar / não tinha interesse | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q274` | `Q274` | texto | Deixou de frequentar uma escola regular por motivos ligados ao trabalho: horário de trabalho era difícil / não tinha tempo de estudar | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q275` | `Q275` | texto | Deixou de frequentar uma escola regular porque parou de estudar porque casou / teve filhos / teve que cuidar da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q276` | `Q276` | texto | Deixou de frequentar uma escola regular porque não tinha apoio da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q277` | `Q277` | texto | Deixou de frequentar uma escola regular por problemas ligados à saúde: sofreu acidente/ficou doente/aconteceu algum acidente com pessoas da família | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q278` | `Q278` | texto | Deixou de frequentar uma escola regular porque sofreu discriminação na escola | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q279` | `Q279` | texto | Deixou de frequentar uma escola regular porque sofreu agressão (física ou verbal) na escola | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q280` | `Q280` | texto | Não voltou a estudar na EJA | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q281` | `Q281` | texto | Voltou a estudar ou a cursar a EJA para conseguir o primeiro emprego | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q282` | `Q282` | texto | Voltou a estudar ou a cursar a EJA para conseguir um emprego melhor | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q283` | `Q283` | texto | Voltou a estudar ou a cursar a EJA para melhorar de posição no emprego atual | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q284` | `Q284` | texto | Voltou a estudar ou a cursar a EJA para prestar vestibular e fazer uma faculdade | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q285` | `Q285` | texto | Voltou a estudar ou a cursar a EJA para fazer algum curso profissionalizante | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q286` | `Q286` | texto | Voltou a estudar ou a cursar a EJA para adquirir mais conhecimento, ficar atualizado | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q287` | `Q287` | texto | Voltou a estudar ou a cursar a EJA para ser alguém na vida, ter mais chances | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q288` | `Q288` | texto | Depois que voltou ou começou a estudar aumentou seus conhecimentos, adquiriu mais informações, tem mais preparo | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q289` | `Q289` | texto | Depois que voltou ou começou a estudar melhorou sua autoestima, sua satisfação pessoal | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q290` | `Q290` | texto | Depois que voltou ou começou a estudar teve reconhecimento no trabalho | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q291` | `Q291` | texto | Depois que voltou ou começou a estudar surgiram novas oportunidades de trabalho | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q292` | `Q292` | texto | Depois que voltou ou começou a estudar sua vida ficou pior, mais cansativa, mais corrida | A = Sim; B = Não | 2009 | `microdados_enem` |
| `q293` | `Q293` | texto | Não mudou nada depois que voltou ou começou a estudar | A = Sim; B = Não | 2009 | `microdados_enem` |
| `tp_lingua` | `TP_LINGUA` | texto | Língua Estrangeira | 0 = Inglês; 1 = Espanhol | 2010 a 2025 | `itens_prova`, `microdados_enem`, `resultados` |
| `tp_estado_civil` | `TP_ESTADO_CIVIL` | texto | Estado Civil | 0 = Não informado; 1 = Solteiro(a); 2 = Casado(a)/Em união estável/Mora com companheiro(a); 3 = Divorciado(a)/Desquitado(a)/Separado(a); 4 = Viúvo(a) | 2010 a 2025 | `microdados_enem`, `participantes` |
| `tp_cor_raca` | `TP_COR_RACA` | texto | Cor/raça | 0 = Não declarado; 1 = Branca; 2 = Preta; 3 = Parda; 4 = Amarela; 5 = Indígena | 2010 a 2025 | `microdados_enem`, `participantes` |
| `q01` | `Q01` | texto | Quantas pessoas moram com você? (incluindo filhos, irmãos, parentes e amigos) | A = Uma a três; B = Quatro a sete; C = Oito a dez; D = Mais de dez; E = Moro sozinho | 2010 | `microdados_enem` |
| `q02` | `Q02` | texto | Qual é o nível de escolaridade do seu pai? | A = Da 1ª à 4ª série do Ensino Fundamental (antigo primário); B = Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio); C = Ensino Médio (antigo 2º grau); D = Ensino Superior; E = Especialização; F = Mestrado; G = Doutorado; H = Não estudou.; I = Não sei | 2010 | `microdados_enem` |
| `q03` | `Q03` | texto | Qual é o nível de escolaridade da sua mãe? | A = Da 1ª à 4ª série do Ensino Fundamental (antigo primário); B = Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio); C = Ensino Médio (antigo 2º grau); D = Ensino Superior; E = Especialização; F = Mestrado; G = Doutorado; H = Não estudou.; I = Não sei | 2010 | `microdados_enem` |
| `q04` | `Q04` | texto | Somando a sua renda com a renda das pessoas que moram com você, quanto é, aproximadamente, a renda familiar mensal? | A = Até 1 salário mínimo (até R$ 510,00).; B = De 1 a 3 salários mínimos (de R$ 510,00 até R$ 1.530,00).; C = De 3 a 6 salários mínimos (de R$ 1.530,00 até R$ 3.060,00).; D = De 6 a 9 salários mínimos (de R$ 3.060,00 até R$ 4.590,00).; … (lista completa no dicionário da fonte) | 2010 | `microdados_enem` |
| `q05` | `Q05` | texto | Qual a sua renda mensal, aproximadamente? | A = Até 1 salário mínimo (até R$ 510,00).; B = De 1 a 3 salários mínimos (de R$ 510,00 até R$ 1.530,00).; C = De 3 a 6 salários mínimos (de R$ 1.530,00 até R$ 3.060,00).; D = De 6 a 9 salários mínimos (de R$ 3.060,00 até R$ 4.590,00).; … (lista completa no dicionário da fonte) | 2010 | `microdados_enem` |
| `q06` | `Q06` | texto | A casa onde você mora é? | A = Própria; B = Alugada; C = Cedida | 2010 | `microdados_enem` |
| `q07` | `Q07` | texto | Sua casa está localizada em? | A = Zona rural.; B = Zona urbana; C = Comunidade indígena.; D = Comunidade quilombola. | 2010 | `microdados_enem` |
| `q08` | `Q08` | texto | Você trabalha ou já trabalhou? | A = Sim; B = Não | 2010 | `microdados_enem` |
| `q09` | `Q09` | texto | Grau de importância quanto a sua decisão de trabalhar para ajudar meus pais nas despesas com a casa | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2010 | `microdados_enem` |
| `tp_ano_concluiu` | `TP_ANO_CONCLUIU` | texto | Ano de Conclusão do Ensino Médio | 0 = Não informado; 1 = 2024; 2 = 2023; 3 = 2022; 4 = 2021; 5 = 2020; 6 = 2019; 7 = 2018; 8 = 2017; 9 = 2016; 10 = 2015; 11 = 2014; 12 = 2013; 13 = 2012; 14 = 2011; 15 = 2010; 16 = 2009; 17 = 2008; 18 = 2007; 19 = Antes de 2007 | 2011 a 2025 | `microdados_enem`, `participantes` |
| `tp_escola` | `TP_ESCOLA` | texto | Tipo de escola do Ensino Médio | 1 = Não Respondeu; 2 = Pública; 3 = Privada | 2011 a 2023 | `microdados_enem` |
| `no_entidade_certificacao` | `NO_ENTIDADE_CERTIFICACAO` | texto | Nome da Entidade Certificadora | — | 2011 a 2016 | `microdados_enem` |
| `co_uf_entidade_certificacao` | `CO_UF_ENTIDADE_CERTIFICACAO` | texto | Código da Unidade da Federação da Entidade Certificadora | — | 2011 a 2016 | `microdados_enem` |
| `sg_uf_entidade_certificacao` | `SG_UF_ENTIDADE_CERTIFICACAO` | texto | Sigla da Unidade da Federação da Entidade Certificadora | — | 2011 a 2016 | `microdados_enem` |
| `q001` | `Q001` | texto | Até que série seu pai, ou o homem responsável por você, estudou? | A = Nunca estudou.; B = Não completou a 4ª série/5º ano do Ensino Fundamental.; C = Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q002` | `Q002` | texto | Até que série sua mãe, ou a mulher responsável por você, estudou? | A = Nunca estudou.; B = Não completou a 4ª série/5º ano do Ensino Fundamental.; C = Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q003` | `Q003` | texto | A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele). | A = Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q004` | `Q004` | texto | A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela). | A = Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q005` | `Q005` | texto | Incluindo você, quantas pessoas moram atualmente em sua residência? | 1 = 1, pois moro sozinho(a); 2 = 2 pessoas; 3 = 3 pessoas; 4 = 4 pessoas; 5 = 5 pessoas; 6 = 6 pessoas; 7 = 7 pessoas; 8 = 8 pessoas; 9 = 9 pessoas; 10 = 10 pessoas; 11 = 11 pessoas; 12 = 12 pessoas; 13 = 13 pessoas; 14 = 14 pessoas; 15 = 15 pessoas; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q006` | `Q006` | texto | Você possui renda? | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q007` | `Q007` | texto | Qual é a renda mensal de sua família? (Considere a sua renda com a das pessoas que moram com você) | A = Nenhuma renda; B = Até R$ 1.518,00; C = De R$ 1.518,01 até R$ 2.277,00; D = De R$ 2.277,01 até R$ 3.036,00; E = De R$ 3.036,01 até R$ 3.795,00; F = De R$ 3.795,01 até R$ 4.554,00; G = De R$ 4.554,01 até R$ 6.072,00; H = De R$ 6.072,01 até R$ 7.590,00; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q008` | `Q008` | texto | Em sua casa, você ou a pessoa responsável pela sua família costuma contratar os serviços de um(a) empregado(a) doméstico(a)? | A = Não; B = Sim, um ou dois dias por semana; C = Sim, três ou quatro dias por semana; D = Sim, pelo menos cinco dias por semana | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q009` | `Q009` | texto | Em sua casa, existe banheiro? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q010` | `Q010` | texto | Em sua casa, existe quarto para dormir? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q011` | `Q011` | texto | Incluindo você, as pessoas com quem você mora têm carro? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q012` | `Q012` | texto | Incluindo você, as pessoas com quem você mora têm motocicleta? | A = Não; B = Sim, uma; C = Sim, duas; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q013` | `Q013` | texto | Em sua casa, existe geladeira? | A = Não; B = Sim, uma; C = Sim, duas; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q014` | `Q014` | texto | Em sua casa, existe freezer independente (vertical ou horizontal)? (Não considere a segunda porta da geladeira.) | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q015` | `Q015` | texto | Em sua casa, existe máquina de lavar roupa? (Não considere o tanquinho) | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q016` | `Q016` | texto | Em sua casa, existe micro-ondas? | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q017` | `Q017` | texto | Em sua casa, existe aspirador de pó? | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q018` | `Q018` | texto | Em sua casa, existe aparelho de TV? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q019` | `Q019` | texto | Em sua casa, existe TV por assinatura? | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q020` | `Q020` | texto | Em sua casa, existe acesso à internet por rede wi-fi? | A = Não; B = Sim | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q021` | `Q021` | texto | Em sua casa, existe computador/notebook? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três; E = Sim, quatro ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q022` | `Q022` | texto | Incluindo você, as pessoas com quem você mora têm telefone celular? | A = Não; B = Sim, um; C = Sim, dois; D = Sim, três; E = Sim, quatro ou mais | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q023` | `Q023` | texto | Em que tipo de escola você frequentou ou frequenta o Ensino Médio? | A = Somente em escola pública.; B = Parte em escola pública e parte em escola privada sem bolsa de estudo integral; C = Parte em escola pública e parte em escola privada com bolsa de estudo integral; D = Somente em escola privada sem bolsa de estudo integral; … (lista completa no dicionário da fonte) | 2011 a 2025 | `microdados_enem`, `participantes`, `quest_hab_estudo` |
| `q024` | `Q024` | texto | Na sua residência tem computador? | A = Não.; B = Sim, um.; C = Sim, dois.; D = Sim, três.; E = Sim, quatro ou mais. | 2011 a 2023 | `microdados_enem`, `quest_hab_estudo` |
| `q025` | `Q025` | texto | Na sua residência tem acesso à Internet? | A = Não.; B = Sim. | 2011 a 2023 | `microdados_enem` |
| `q026` | `Q026` | texto | Você já concluiu ou está concluindo o Ensino Médio? | A = Já concluí o Ensino Médio.; B = Estou cursando e concluirei o Ensino Médio em 2018.; C = Estou cursando e concluirei o Ensino Médio após 2018.; D = Não concluí e não estou cursando o Ensino Médio. | 2011 a 2018 | `microdados_enem` |
| `q027` | `Q027` | texto | Você vivenciou problemas em sua rotina para estudar ou manter-se informado(a) durante a pandemia? | A = Sim.; B = Não. | 2011 a 2022 | `microdados_enem`, `quest_hab_estudo` |
| `q028` | `Q028` | texto | Quantas horas semanais você trabalha ou trabalhava aproximadamente? (Considere a atividade remunerada mais recente.) | A = Até 10 horas semanais.; B = De 11 a 20 horas semanais.; C = De 21 a 30 horas semanais.; D = De 31 a 40 horas semanais.; E = Mais de 40 horas semanais. | 2011 a 2016 | `microdados_enem` |
| `q029` | `Q029` | texto | Durante a pandemia, há relatos de pessoas que tiveram dificuldade para criar condições para estudar ou manterem-se informadas em casa, por exemplo, dificuldades com a falta de internet, equipamentos, espaço ou materiais. Você teve dificuldades de infraestrutura para estudar ou manter-se informado(a) durante 2021? | A = Sim.; B = Não. | 2011 a 2022 | `microdados_enem`, `quest_hab_estudo` |
| `q030` | `Q030` | texto | Indique a importância de cada um dos motivos abaixo na sua decisão de trabalhar: Sustentar minha família (esposo/a, filhos/as etc.). | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q031` | `Q031` | texto | Você precisou da ajuda de alguém para estudar ou manter-se informado(a) em 2021? | A = Sim.; B = Não.; C = Precisei de ajuda para estudar, mas não tive ninguém para me auxiliar. | 2011 a 2022 | `microdados_enem`, `quest_hab_estudo` |
| `q032` | `Q032` | texto | Indique a importância de cada um dos motivos abaixo na sua decisão de trabalhar: Adquirir experiência. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q033` | `Q033` | texto | Indique a importância de cada um dos motivos abaixo na sua decisão de trabalhar: Custear/pagar meus estudos. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q034` | `Q034` | texto | A partir da sua experiência de estudos em 2021, o quanto você se sente preparado(a) para conduzir o seu processo de aprendizagem? | A = Nada preparado(a).; B = Um pouco preparado(a).; C = Bem preparado(a).; D = Muito preparado(a).; E = Totalmente preparado(a). | 2011 a 2022 | `microdados_enem`, `quest_hab_estudo` |
| `q035` | `Q035` | texto | Indique os motivos que levaram você a participar do ENEM: Ingressar na Educação Superior pública. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q036` | `Q036` | texto | Indique os motivos que levaram você a participar do ENEM: Ingressar na Educação Superior privada. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q037` | `Q037` | texto | Indique os motivos que levaram você a participar do ENEM: Conseguir uma bolsa de estudos (ProUni, outras). | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q038` | `Q038` | texto | Indique os motivos que levaram você a participar do ENEM: Participar do Programa de Financiamento Estudantil - FIES. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q039` | `Q039` | texto | Indique os motivos que levaram você a participar do ENEM: Participar do Programa Ciências Sem Fronteiras. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q040` | `Q040` | texto | Indique os motivos que levaram você a participar do ENEM: Aumentar a possibilidade de conseguir um emprego. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q041` | `Q041` | texto | Indique os motivos que levaram você a participar do ENEM: Progredir no meu emprego atual. | 0 = 0 indica o fator menos relevante e 5 o fator mais relevante | 2011 a 2016 | `microdados_enem` |
| `q042` | `Q042` | texto | Em que tipo de escola você frequentou o Ensino Fundamental? | A = Somente em escola pública.; B = A maior parte em escola pública.; C = Somente em escola particular.; D = A maior parte em escola particular.; E = Somente em escola indígena.; F = A maior parte em escola indígena.; … (lista completa no dicionário da fonte) | 2011 a 2016 | `microdados_enem` |
| `q043` | `Q043` | texto | Marque entre as opções abaixo aquela que melhor descreve a modalidade de Ensino Fundamental que você frequentou | A = Cursei o Ensino Fundamental somente na modalidade regular.; B = Cursei o Ensino Fundamental parte na modalidade regular e parte na modalidade EJA (Educação de Jovens e Adultos).; … (lista completa no dicionário da fonte) | 2011 a 2016 | `microdados_enem` |
| `q044` | `Q044` | texto | Em que turno você frequentou o Ensino Fundamental? | A = Somente no diurno.; B = Parte no diurno e parte no noturno.; C = Somente no noturno. | 2011 a 2016 | `microdados_enem` |
| `q045` | `Q045` | texto | Durante o Ensino Fundamental, você abandonou os estudos por algum tempo e/ou foi reprovado? | A = Não abandonei, nem fui reprovado.; B = Não abandonei, mas fui reprovado.; C = Abandonei, mas não fui reprovado.; D = Abandonei e fui reprovado. | 2011 a 2016 | `microdados_enem` |
| `q046` | `Q046` | texto | Você já concluiu ou está concluindo o Ensino Médio? | A = Já concluí o Ensino Médio.; B = Estou cursando e concluirei o Ensino Médio em 2016.; C = Estou cursando e concluirei o Ensino Médio após 2016.; D = Não concluí e não estou cursando o Ensino Médio. | 2011 a 2016 | `microdados_enem` |
| `q047` | `Q047` | texto | Em que tipo de escola você frequentou o Ensino Médio? | A = Somente em escola pública.; B = Parte em escola pública e parte em escola privada sem bolsa de estudo integral.; C = Parte em escola pública e parte em escola privada com bolsa de estudo integral.; … (lista completa no dicionário da fonte) | 2011 a 2016 | `microdados_enem` |
| `q048` | `Q048` | texto | Marque entre as opções abaixo aquela que melhor descreve a modalidade de Ensino Médio que você frequentou | A = Cursei o Ensino Médio somente na modalidade regular.; B = Cursei o Ensino Médio parte na modalidade regular e parte na modalidade EJA (Educação de Jovens e Adultos).; C = Cursei o Ensino Médio somente na modalidade EJA (Educação de Jovens e Adultos).; … (lista completa no dicionário da fonte) | 2011 a 2016 | `microdados_enem` |
| `q049` | `Q049` | texto | Em que turno você frequentou o Ensino Médio? | A = Somente no diurno.; B = Parte no diurno e parte no noturno.; C = Somente no noturno. | 2011 a 2016 | `microdados_enem` |
| `q050` | `Q050` | texto | Durante o Ensino Médio, você abandonou os estudos por algum tempo e/ou foi reprovado? | A = Não abandonei, nem fui reprovado.; B = Não abandonei, mas fui reprovado.; C = Abandonei, mas não fui reprovado.; D = Abandonei e fui reprovado. | 2011 a 2016 | `microdados_enem` |
| `q051` | `Q051` | texto | Indique os cursos que você frequenta ou frequentou: Curso de computação ou informática | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q052` | `Q052` | texto | Indique os cursos que você frequenta ou frequentou: Curso preparatório para concursos públicos | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q053` | `Q053` | texto | Indique os cursos que você frequenta ou frequentou: Outro curso | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q054` | `Q054` | texto | Você cursa ou já cursou a Educação de Jovens e Adultos – EJA? | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q055` | `Q055` | texto | Como é ou era o principal curso de EJA que você frequenta ou frequentou? | A = Curso presencial em escola pública; B = Curso presencial em escola privada; C = Curso presencial na empresa em que trabalhei, instituição filantrópica ou religiosa; D = Curso a distância (via rádio, televisão, internet, correio, com apostilas); … (lista completa no dicionário da fonte) | 2011 a 2014 | `microdados_enem` |
| `q056` | `Q056` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Trabalhava, não tinha tempo de estudar | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q057` | `Q057` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Estudava no curso da empresa e foi interrompido | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q058` | `Q058` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Ocorreram problemas de saúde ou acidentes comigo ou familiares | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q059` | `Q059` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Mudei de bairro, cidade ou município | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q060` | `Q060` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Por motivos pessoais, casamento, filhos etc. | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q061` | `Q061` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Faltava-me interesse, desisti | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q062` | `Q062` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Senti-me discriminado(a) | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q063` | `Q063` | texto | Indique o que levou você a deixar de cursar a EJA (Se você não deixou de cursar a EJA, vá para a questão...): Temi/Sofri violência | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q064` | `Q064` | texto | Você já frequentou o ensino regular? | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q065` | `Q065` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de vaga em escola pública | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q066` | `Q066` | texto | Indique o que levou você a deixar de cursar o ensino regular: Ausência de escola perto de casa | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q067` | `Q067` | texto | Indique o que levou você a deixar de cursar o ensino regular: Dificuldades após reprovação | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q068` | `Q068` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de interesse em estudar | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q069` | `Q069` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de condições adequadas na escola | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q070` | `Q070` | texto | Indique o que levou você a deixar de cursar o ensino regular: Trabalho, falta de tempo para estudar | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q071` | `Q071` | texto | Indique o que levou você a deixar de cursar o ensino regular: Motivos pessoais, casamento/filhos etc. | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q072` | `Q072` | texto | Indique o que levou você a deixar de cursar o ensino regular: Falta de apoio familiar. | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q073` | `Q073` | texto | Indique o que levou você a deixar de cursar o ensino regular: Problemas de saúde ou acidente comigo ou familiares | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q074` | `Q074` | texto | Indique o que levou você a deixar de cursar o ensino regular: Discriminação/Preconceitos (sexo, raça, idade, classe etc.) | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `q075` | `Q075` | texto | Indique o que levou você a deixar de cursar o ensino regular: Medo de sofrer violência | A = Sim; B = Não | 2011 a 2014 | `microdados_enem` |
| `in_item_adaptado` | `IN_ITEM_ADAPTADO` | texto | Item pertencente à prova adaptada | 0 = Não; 1 = Sim | 2013 a 2025 | `itens_prova` |
| `tp_nacionalidade` | `TP_NACIONALIDADE` | texto | Nacionalidade | 0 = Não informado; 1 = Brasileiro(a); 2 = Brasileiro(a) Naturalizado(a); 3 = Estrangeiro(a); 4 = Brasileiro(a) Nato(a), nascido(a) no exterior | 2013 a 2025 | `microdados_enem`, `participantes` |
| `ano_concluiu` | `ANO_CONCLUIU` | texto | Ano de Conclusão do Ensino Médio | — | 2013 | `microdados_enem` |
| `q076` | `Q076` | texto | Quantos anos você tinha quando deixou de frequentar o ensino regular? | A = Menos de 10 anos; B = Entre 10 e 14 anos; C = Entre 15 e 18 anos; D = Entre 19 e 24 anos; E = Entre 25 e 30 anos; F = Mais de 30 anos; G = Não deixei de frequentar | 2013 a 2014 | `microdados_enem` |
| `in_treineiro` | `IN_TREINEIRO` | texto | Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos3 | 0 = Não; 1 = Sim | 2015 a 2025 | `microdados_enem`, `participantes` |
| `tp_versao_digital` | `TP_VERSAO_DIGITAL` | texto | Provas de LC do ENEM digital com mesmo código mas que apresentam itens ordenados de maneiras distintas conforme a opção de língua estrangeira do participante. | 0 = Inglês; 1 = Espanhol | 2020 | `itens_prova` |
| `tp_resposta` | `TP_RESPOSTA` | texto | Tipo de opção de resposta ao questionário | 0 = Não (Participante optou por não responder o questionário).; 1 = Sim (Participante optou por responder o questionário).; 2 = Responder Depois | 2022 | `quest_hab_estudo` |
| `q025a` | `Q025A` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Aparelho de rádio. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q025b` | `Q025B` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Computador/notebook. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q025c` | `Q025C` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Livros/apostilas/materiais impressos. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q025d` | `Q025D` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Tablet. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q025e` | `Q025E` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Telefone celular. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q025f` | `Q025F` | texto | Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Televisão. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026a` | `Q026A` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Audioaula/podcast avulsos. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026b` | `Q026B` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Audioaula/podcast em plataforma de educação a distância. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026c` | `Q026C` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Grupos de Whatsapp, Facebook, Telegram e similares. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026d` | `Q026D` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Livros/apostilas/materiais digitais. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026e` | `Q026E` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Programa de rádio. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026f` | `Q026F` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Programa de TV. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026g` | `Q026G` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Videoaula avulsa. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q026h` | `Q026H` | texto | Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Videoaula em plataforma de educação a distância. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028a` | `Q028A` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: eu me senti desestimulado(a) por não ter colegas com quem interagir sobre o que eu estava estudando. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028b` | `Q028B` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: tive dificuldade de compreender os conteúdos por falta de explicações de um professor em tempo real. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028c` | `Q028C` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: fiquei por muito tempo diante das telas, sem pequenos intervalos para descansar. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028d` | `Q028D` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: reduzi a prática de atividades físicas. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028e` | `Q028E` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: dormi por menos tempo. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028f` | `Q028F` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: tive episódios de insônia. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028g` | `Q028G` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: senti dificuldade em manter a motivação para estudar por minha conta. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028h` | `Q028H` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: senti dificuldade em me motivar a cumprir meu cronograma. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028i` | `Q028I` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: senti medo de não conseguir aprender os conteúdos. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028j` | `Q028J` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: senti ansiedade devido ao isolamento social e ao receio de contágio da doença. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028k` | `Q028K` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: dediquei tempo para ajudar algum familiar a estudar em casa. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028l` | `Q028L` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: precisei ficar em repouso porque tive Covid com sintomas. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028m` | `Q028M` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: precisei ficar em repouso porque tive outra doença. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028n` | `Q028N` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: precisei cuidar de algum familiar que teve Covid com sintomas. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028o` | `Q028O` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: precisei cuidar de algum familiar que teve outra doença. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028p` | `Q028P` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: tive que cuidar do(s) meu(s) irmão(s) menor(es) para meus pais trabalharem. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028q` | `Q028Q` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: tive que começar a trabalhar em casa para obter renda. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q028r` | `Q028R` | texto | Assinale a alternativa que complementa a oração: “Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque”: tive que trabalhar em serviço considerado essencial durante a pandemia. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030a` | `Q030A` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Equipamento (computador pessoal ou notebook) pouco disponível por ser compartilhado com outros familiares. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030b` | `Q030B` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Conexão ruim ou limitada com a internet. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030c` | `Q030C` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Equipamento (computador pessoal ou notebook) com configuração insuficiente para estudar ou acessar materiais. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030d` | `Q030D` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Material pedagógico insuficiente para estudar, faltando livros, apostilas, textos, vídeos. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030e` | `Q030E` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Local de estudos faltando boa iluminação, higiene, ventilação e silêncio. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030f` | `Q030F` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Local de estudos sem mobília para guardar e para dispor os materiais de estudo. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q030g` | `Q030G` | texto | Assinale a alternativa que corresponde com as PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Recursos insuficientes para alimentação. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032a` | `Q032A` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Amigo(s)/colega(s)/conhecido(s). | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032b` | `Q032B` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Filho(s)/sobrinho(s). | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032c` | `Q032C` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Irmão(s)/primo(s). | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032d` | `Q032D` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Namorado(a)/cônjuge/companheiro(a). | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032e` | `Q032E` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Pai/mãe. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032f` | `Q032F` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Professor(a) / orientador(a). | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q032g` | `Q032G` | texto | Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Tio(s)/Avô,avó. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033a` | `Q033A` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Com a alimentação. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033b` | `Q033B` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para acessar à internet. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033c` | `Q033C` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para comprar livros/apostilas ou fazer cópias. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033d` | `Q033D` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para comprar cursos online. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033e` | `Q033E` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para me inscrever em provas ou no Enem. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033f` | `Q033F` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para elaborar um cronograma de estudos. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033g` | `Q033G` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para pesquisar materiais na internet. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033h` | `Q033H` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para preencher formulários de inscrição. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033i` | `Q033I` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Por meio de empréstimo de algum equipamento (celular, computador, notebook, tablet) para eu estudar. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `q033j` | `Q033J` | texto | Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Por meio de explicação de conteúdos que eu não havia entendido. | A = Sim.; B = Não. | 2022 | `quest_hab_estudo` |
| `nu_sequencial` | `NU_SEQUENCIAL` | texto | Número sequencial da linha de resultados¹ | — | 2024 a 2025 | `resultados` |
| `co_escola` | `CO_ESCOLA` | texto | Código da Escola de conclusão do ensino médio² | — | 2024 a 2025 | `resultados` |
| `tp_status_redacao_av1` | `TP_STATUS_REDACAO_AV1` | texto | Situação da redação do participante atribuída pelo avaliador 1 | 1 = Sem problemas; 2 = Anulada; 3 = Cópia Texto Motivador; 4 = Em Branco; 6 = Fuga ao tema; 7 = Não atendimento ao tipo textual; 8 = Texto insuficiente; 9 = Parte desconectada | 2025 | `resultados` |
| `nu_nota_av1` | `NU_NOTA_AV1` | texto | Nota da prova de redação atribuída pelo avaliador 1 | — | 2025 | `resultados` |
| `nu_nota_comp1_av1` | `NU_NOTA_COMP1_AV1` | texto | Nota da competência 1 atribuída pelo avaliador 1 - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa | — | 2025 | `resultados` |
| `nu_nota_comp2_av1` | `NU_NOTA_COMP2_AV1` | texto | Nota da competência 2 atribuída pelo avaliador 1 - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa | — | 2025 | `resultados` |
| `nu_nota_comp3_av1` | `NU_NOTA_COMP3_AV1` | texto | Nota da competência 3 atribuída pelo avaliador 1 - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista | — | 2025 | `resultados` |
| `nu_nota_comp4_av1` | `NU_NOTA_COMP4_AV1` | texto | Nota da competência 4 atribuída pelo avaliador 1 - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação | — | 2025 | `resultados` |
| `nu_nota_comp5_av1` | `NU_NOTA_COMP5_AV1` | texto | Nota da competência 5 atribuída pelo avaliador 1 - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos | — | 2025 | `resultados` |
| `tp_status_redacao_av2` | `TP_STATUS_REDACAO_AV2` | texto | Situação da redação do participante atribuída pelo avaliador 2 | 1 = Sem problemas; 2 = Anulada; 3 = Cópia Texto Motivador; 4 = Em Branco; 6 = Fuga ao tema; 7 = Não atendimento ao tipo textual; 8 = Texto insuficiente; 9 = Parte desconectada | 2025 | `resultados` |
| `nu_nota_av2` | `NU_NOTA_AV2` | texto | Nota da prova de redação atribuída pelo avaliador 2 | — | 2025 | `resultados` |
| `nu_nota_comp1_av2` | `NU_NOTA_COMP1_AV2` | texto | Nota da competência 1 atribuída pelo avaliador 2 - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa | — | 2025 | `resultados` |
| `nu_nota_comp2_av2` | `NU_NOTA_COMP2_AV2` | texto | Nota da competência 2 atribuída pelo avaliador 2 - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa | — | 2025 | `resultados` |
| `nu_nota_comp3_av2` | `NU_NOTA_COMP3_AV2` | texto | Nota da competência 3 atribuída pelo avaliador 2 - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista | — | 2025 | `resultados` |
| `nu_nota_comp4_av2` | `NU_NOTA_COMP4_AV2` | texto | Nota da competência 4 atribuída pelo avaliador 2 - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação | — | 2025 | `resultados` |
| `nu_nota_comp5_av2` | `NU_NOTA_COMP5_AV2` | texto | Nota da competência 5 atribuída pelo avaliador 2 - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos | — | 2025 | `resultados` |
| `tp_status_redacao_av3` | `TP_STATUS_REDACAO_AV3` | texto | Situação da redação do participante atribuída pelo avaliador 3 (se convocado) | 1 = Sem problemas; 2 = Anulada; 3 = Cópia Texto Motivador; 4 = Em Branco; 6 = Fuga ao tema; 7 = Não atendimento ao tipo textual; 8 = Texto insuficiente; 9 = Parte desconectada | 2025 | `resultados` |
| `nu_nota_av3` | `NU_NOTA_AV3` | texto | Nota da prova de redação atribuída pelo avaliador 3 (se convocado) | — | 2025 | `resultados` |
| `nu_nota_comp1_av3` | `NU_NOTA_COMP1_AV3` | texto | Nota da competência 1 atribuída pelo avaliador 3 (se convocado) - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa | — | 2025 | `resultados` |
| `nu_nota_comp2_av3` | `NU_NOTA_COMP2_AV3` | texto | Nota da competência 2 atribuída pelo avaliador 3 (se convocado) - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa | — | 2025 | `resultados` |
| `nu_nota_comp3_av3` | `NU_NOTA_COMP3_AV3` | texto | Nota da competência 3 atribuída pelo avaliador 3 (se convocado) - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista | — | 2025 | `resultados` |
| `nu_nota_comp4_av3` | `NU_NOTA_COMP4_AV3` | texto | Nota da competência 4 atribuída pelo avaliador 3 (se convocado) - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação | — | 2025 | `resultados` |
| `nu_nota_comp5_av3` | `NU_NOTA_COMP5_AV3` | texto | Nota da competência 5 atribuída pelo avaliador 3 (se convocado) - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos | — | 2025 | `resultados` |
| `tp_status_redacao_av4` | `TP_STATUS_REDACAO_AV4` | texto | Situação da redação do participante atribuída por banca composta por 3 avaliadores (se convocada) | 1 = Sem problemas; 2 = Anulada; 3 = Cópia Texto Motivador; 4 = Em Branco; 6 = Fuga ao tema; 7 = Não atendimento ao tipo textual; 8 = Texto insuficiente; 9 = Parte desconectada | 2025 | `resultados` |
| `nu_nota_av4` | `NU_NOTA_AV4` | texto | Nota da prova de redação atribuída por banca composta por 3 avaliadores (se convocada) | — | 2025 | `resultados` |
| `nu_nota_comp1_av4` | `NU_NOTA_COMP1_AV4` | texto | Nota da competência 1 atribuída por banca composta por 3 avaliadores (se convocada) - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa. | — | 2025 | `resultados` |
| `nu_nota_comp2_av4` | `NU_NOTA_COMP2_AV4` | texto | Nota da competência 2 por banca composta por 3 avaliadores (se convocada) - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa. | — | 2025 | `resultados` |
| `nu_nota_comp3_av4` | `NU_NOTA_COMP3_AV4` | texto | Nota da competência 3 por banca composta por 3 avaliadores (se convocada) - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista. | — | 2025 | `resultados` |
| `nu_nota_comp4_av4` | `NU_NOTA_COMP4_AV4` | texto | Nota da competência 4 por banca composta por 3 avaliadores (se convocada) - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação. | — | 2025 | `resultados` |
| `nu_nota_comp5_av4` | `NU_NOTA_COMP5_AV4` | texto | Nota da competência 5 por banca composta por 3 avaliadores (se convocada) - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos. | — | 2025 | `resultados` |

## No lake

- Dataset `inep/enem`, particionado por `ano`; um Parquet por CSV de `DADOS`, no padrão `enem-microdados_<ano>__<arquivo>.parquet`.
- Todas as colunas são texto: o DuckDB lê o CSV sem inferir tipos, e os nomes saem normalizados (minúsculas, sem acento).
- A coluna `ano` é a edição, tirada do nome do arquivo; `nu_ano` (do dicionário) é o ano dentro do dado.
- Arquivos de checksum e documentos dentro de `DADOS` são ignorados.

## Cuidados de uso

- **O conjunto de colunas muda a cada era.** Em 2009 há 339 colunas, em 2017 e 2018 há 78, em 2019 a 2023 há 76 e em 2024 as colunas se dividem entre `participantes` (38) e `resultados` (42 em 2024, 70 em 2025). Junte edições pelo nome da coluna e confira a coluna *Período*.
- **Os códigos mudam.** Uma mesma variável pode ter listas de categorias diferentes entre edições (por exemplo, a classificação de renda e de escolaridade dos pais); consulte o dicionário da edição.
- **Participantes e resultados de 2024 e 2025 não se ligam por chave.** Não dá para cruzar o perfil do participante com a nota; a ligação com a escola está só em `resultados`.
- **Anonimização.** O número de inscrição é uma máscara sequencial e, em 2025, o código da escola é mascarado quando a escola tem menos de 10 participantes. O Inep não recomenda usar o código da escola para montar rankings.
- **Registros excluídos.** O Inep retira da base os participantes de provas com muito poucos casos (a edição 2025 lista as provas excluídas no Leia-me).
- **Sem conferência de duplicidade.** O lake guarda o que o CSV traz; nesta documentação a unicidade de `nu_inscricao` por edição foi conferida só em amostra.

## Exemplos

Média da nota de matemática por sexo na edição 2023 (colunas do arquivo `microdados_enem`, texto convertido para número):

```python
import duckdb

duckdb.sql("""
    SELECT tp_sexo, count(*) AS participantes,
           round(avg(try_cast(replace(nu_nota_mt, ',', '.') AS DOUBLE)), 1) AS media_mt
    FROM read_parquet('lake/inep/enem/ano=2023/*microdados_enem*.parquet', union_by_name = true)
    GROUP BY ALL
    ORDER BY tp_sexo
""").show()
```

## Referências

- Microdados do Enem: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
- Leia-me e dicionário de variáveis, dentro de cada ZIP em https://download.inep.gov.br/microdados/
