---
dataset:
  id: adequacao-formacao-docente
  fonte: inep
  titulo: Indicadores — Adequação da formação docente
  resumo: Percentual de docentes por grupo do indicador de adequação da formação do docente, por etapa e disciplina, em Brasil, regiões, UFs, municípios e escolas.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2013'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição do indicador, com o percentual de docentes por etapa e grupo
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 48
  unidades_de_medida:
    Ano: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Educação Infantil - Grupo 1: '%'
    Educação Infantil - Grupo 2: '%'
    Educação Infantil - Grupo 3: '%'
    Educação Infantil - Grupo 4: '%'
    Educação Infantil - Grupo 5: '%'
    Ensino Fundamental - Total - Grupo 1: '%'
    Ensino Fundamental - Total - Grupo 2: '%'
    Ensino Fundamental - Total - Grupo 3: '%'
    Ensino Fundamental - Total - Grupo 4: '%'
    Ensino Fundamental - Total - Grupo 5: '%'
    Ensino Fundamental - Anos Iniciais - Grupo 1: '%'
    Ensino Fundamental - Anos Iniciais - Grupo 2: '%'
    Ensino Fundamental - Anos Iniciais - Grupo 3: '%'
    Ensino Fundamental - Anos Iniciais - Grupo 4: '%'
    Ensino Fundamental - Anos Iniciais - Grupo 5: '%'
    Ensino Fundamental - Anos Finais - Grupo 1: '%'
    Ensino Fundamental - Anos Finais - Grupo 2: '%'
    Ensino Fundamental - Anos Finais - Grupo 3: '%'
    Ensino Fundamental - Anos Finais - Grupo 4: '%'
    Ensino Fundamental - Anos Finais - Grupo 5: '%'
    Ensino Médio - Grupo 1: '%'
    Ensino Médio - Grupo 2: '%'
    Ensino Médio - Grupo 3: '%'
    Ensino Médio - Grupo 4: '%'
    Ensino Médio - Grupo 5: '%'
    EJA - Fundamental - Grupo 1: '%'
    EJA - Fundamental - Grupo 2: '%'
    EJA - Fundamental - Grupo 3: '%'
    EJA - Fundamental - Grupo 4: '%'
    EJA - Fundamental - Grupo 5: '%'
    EJA - Médio - Grupo 1: '%'
    EJA - Médio - Grupo 2: '%'
    EJA - Médio - Grupo 3: '%'
    EJA - Médio - Grupo 4: '%'
    EJA - Médio - Grupo 5: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Adequação da formação docente

## Resumo

O Indicador de Adequação da Formação Docente (AFD) do Inep classifica os docentes de cada turma e disciplina em grupos segundo a adequação de sua formação à disciplina que lecionam. As planilhas trazem o percentual de docentes por grupo do indicador, por etapa de ensino, localização e dependência administrativa.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/adequacao-formacao-docente` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2013 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição do indicador, com o percentual de docentes por etapa e grupo |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 48 |
| Unidades de medida | `Ano`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Educação Infantil - Grupo 1`: %; `Educação Infantil - Grupo 2`: %; `Educação Infantil - Grupo 3`: %; `Educação Infantil - Grupo 4`: %; `Educação Infantil - Grupo 5`: %; `Ensino Fundamental - Total - Grupo 1`: %; `Ensino Fundamental - Total - Grupo 2`: %; `Ensino Fundamental - Total - Grupo 3`: %; `Ensino Fundamental - Total - Grupo 4`: %; `Ensino Fundamental - Total - Grupo 5`: %; `Ensino Fundamental - Anos Iniciais - Grupo 1`: %; `Ensino Fundamental - Anos Iniciais - Grupo 2`: %; `Ensino Fundamental - Anos Iniciais - Grupo 3`: %; `Ensino Fundamental - Anos Iniciais - Grupo 4`: %; `Ensino Fundamental - Anos Iniciais - Grupo 5`: %; `Ensino Fundamental - Anos Finais - Grupo 1`: %; `Ensino Fundamental - Anos Finais - Grupo 2`: %; `Ensino Fundamental - Anos Finais - Grupo 3`: %; `Ensino Fundamental - Anos Finais - Grupo 4`: %; `Ensino Fundamental - Anos Finais - Grupo 5`: %; `Ensino Médio - Grupo 1`: %; `Ensino Médio - Grupo 2`: %; `Ensino Médio - Grupo 3`: %; `Ensino Médio - Grupo 4`: %; `Ensino Médio - Grupo 5`: %; `EJA - Fundamental - Grupo 1`: %; `EJA - Fundamental - Grupo 2`: %; `EJA - Fundamental - Grupo 3`: %; `EJA - Fundamental - Grupo 4`: %; `EJA - Fundamental - Grupo 5`: %; `EJA - Médio - Grupo 1`: %; `EJA - Médio - Grupo 2`: %; `EJA - Médio - Grupo 3`: %; `EJA - Médio - Grupo 4`: %; `EJA - Médio - Grupo 5`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 39 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/AFD_2025_BRASIL_REGIOES_UF.zip`.
- No bruto, cada arquivo se chama `indicadores/adequacao-formacao-docente/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- O título das planilhas é "Percentual de docentes por grupo do indicador de adequação da formação do docente", por recorte e ano.
- Nota da fonte: o docente é contabilizado em cada turma e disciplina que leciona; entram os professores responsáveis pela regência de classe e os de regência de módulo ou disciplina de turma de educação a distância. A definição dos grupos está na nota técnica do Inep (não reproduzida na planilha).
- Colunas: etapas de ensino (por exemplo Educação Infantil, Ensino Fundamental) por grupo do indicador (Grupo 1, Grupo 2...).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2013 | `afd_brasil` (39); `afd_regioes` (39); `afd_ufs` (40) |
| 2014 | `afd_brasil` (39); `afd_regioes` (39); `afd_ufs` (40) |
| 2015 | `afd_brasil` (39); `afd_regioes` (39); `afd_ufs` (40) |
| 2016 | `afd_brasil` (39); `afd_regioes` (39); `afd_ufs` (40) |
| 2017 | `afd_brasil_regioes_ufs` (39) |
| 2018 | `afd_brasil_regioes_ufs` (39) |
| 2019 | `afd_brasil_regioes_ufs` (39) |
| 2020 | `afd_brasil_regioes_ufs` (39) |
| 2021 | `afd_brasil_regioes_ufs` (39) |
| 2022 | `afd_brasil_regioes_ufs` (39) |
| 2023 | `afd_brasil_regioes_ufs` (39) |
| 2024 | `afd_brasil_regioes_ufs` (39) |
| 2025 | `afd_brasil_regioes_ufs` (39); `afd_escolas` (44); `afd_municipios` (42) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2013 a 2016 | `afd_brasil`, `afd_regioes` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Educação Infantil - Grupo 1` | `Educação Infantil - Grupo 1` | decimal | Valor de «Educação Infantil» no recorte «Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Educação Infantil - Grupo 2` | `Educação Infantil - Grupo 2` | decimal | Valor de «Educação Infantil» no recorte «Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Educação Infantil - Grupo 3` | `Educação Infantil - Grupo 3` | decimal | Valor de «Educação Infantil» no recorte «Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Educação Infantil - Grupo 4` | `Educação Infantil - Grupo 4` | decimal | Valor de «Educação Infantil» no recorte «Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Educação Infantil - Grupo 5` | `Educação Infantil - Grupo 5` | decimal | Valor de «Educação Infantil» no recorte «Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Total - Grupo 1` | `Ensino Fundamental - Total - Grupo 1` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Total - Grupo 2` | `Ensino Fundamental - Total - Grupo 2` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Total - Grupo 3` | `Ensino Fundamental - Total - Grupo 3` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Total - Grupo 4` | `Ensino Fundamental - Total - Grupo 4` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Total - Grupo 5` | `Ensino Fundamental - Total - Grupo 5` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Grupo 1` | `Ensino Fundamental - Anos Iniciais - Grupo 1` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Grupo 2` | `Ensino Fundamental - Anos Iniciais - Grupo 2` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Grupo 3` | `Ensino Fundamental - Anos Iniciais - Grupo 3` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Grupo 4` | `Ensino Fundamental - Anos Iniciais - Grupo 4` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Grupo 5` | `Ensino Fundamental - Anos Iniciais - Grupo 5` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Grupo 1` | `Ensino Fundamental - Anos Finais - Grupo 1` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Grupo 2` | `Ensino Fundamental - Anos Finais - Grupo 2` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Grupo 3` | `Ensino Fundamental - Anos Finais - Grupo 3` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Grupo 4` | `Ensino Fundamental - Anos Finais - Grupo 4` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Grupo 5` | `Ensino Fundamental - Anos Finais - Grupo 5` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Médio - Grupo 1` | `Ensino Médio - Grupo 1` | decimal | Valor de «Ensino Médio» no recorte «Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Médio - Grupo 2` | `Ensino Médio - Grupo 2` | decimal | Valor de «Ensino Médio» no recorte «Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Médio - Grupo 3` | `Ensino Médio - Grupo 3` | decimal | Valor de «Ensino Médio» no recorte «Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Médio - Grupo 4` | `Ensino Médio - Grupo 4` | decimal | Valor de «Ensino Médio» no recorte «Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Ensino Médio - Grupo 5` | `Ensino Médio - Grupo 5` | decimal | Valor de «Ensino Médio» no recorte «Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Fundamental - Grupo 1` | `EJA - Fundamental - Grupo 1` | decimal | Valor de «EJA» no recorte «Fundamental › Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Fundamental - Grupo 2` | `EJA - Fundamental - Grupo 2` | decimal/inteiro | Valor de «EJA» no recorte «Fundamental › Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Fundamental - Grupo 3` | `EJA - Fundamental - Grupo 3` | decimal | Valor de «EJA» no recorte «Fundamental › Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Fundamental - Grupo 4` | `EJA - Fundamental - Grupo 4` | decimal | Valor de «EJA» no recorte «Fundamental › Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Fundamental - Grupo 5` | `EJA - Fundamental - Grupo 5` | decimal/inteiro | Valor de «EJA» no recorte «Fundamental › Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Médio - Grupo 1` | `EJA - Médio - Grupo 1` | decimal | Valor de «EJA» no recorte «Médio › Grupo 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Médio - Grupo 2` | `EJA - Médio - Grupo 2` | decimal | Valor de «EJA» no recorte «Médio › Grupo 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Médio - Grupo 3` | `EJA - Médio - Grupo 3` | decimal | Valor de «EJA» no recorte «Médio › Grupo 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Médio - Grupo 4` | `EJA - Médio - Grupo 4` | decimal | Valor de «EJA» no recorte «Médio › Grupo 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `EJA - Médio - Grupo 5` | `EJA - Médio - Grupo 5` | decimal | Valor de «EJA» no recorte «Médio › Grupo 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `afd_brasil`, `afd_brasil_regioes_ufs`, `afd_escolas` e mais 3 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `afd_escolas`, `afd_municipios`, `afd_ufs` |
| `Unidade da Federação` | `Unidade da Federação` | texto | Coluna «Unidade da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2013 a 2016 | `afd_ufs` |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `afd_brasil_regioes_ufs` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_escolas` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_escolas`, `afd_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_escolas`, `afd_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_escolas` |
| `Sigla` | `Sigla` | texto | Coluna «Sigla» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `afd_municipios` |

## No lake

- Dataset `inep/adequacao-formacao-docente`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `afd_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Educação Infantil - Grupo 1"
    FROM read_parquet('lake/inep/adequacao-formacao-docente/ano=2025/adequacao-formacao-docente-afd-2025-brasil-regioes-uf__afd_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
- Notas técnicas dos indicadores educacionais, na página dos indicadores.
