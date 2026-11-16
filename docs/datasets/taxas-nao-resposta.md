---
dataset:
  id: taxas-nao-resposta
  fonte: inep
  titulo: Indicadores — Taxas de não resposta
  resumo: Taxa de não resposta do Censo da Educação Básica por etapa, por recorte geográfico, localização e rede.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2011'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com a taxa de não resposta por etapa
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 49
  unidades_de_medida:
    Ano: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Total Ens. Fundamental: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Iniciais (1º ao 5º Ano): '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Finais (6º ao 9º Ano): '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 1º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 2º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 3º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 4º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 5º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 6º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 7º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 8º Ano: '%'
    Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 9º Ano: '%'
    Taxa de Não-Resposta - Ensino Médio - Total Médio: '%'
    Taxa de Não-Resposta - Ensino Médio - 1ª série: '%'
    Taxa de Não-Resposta - Ensino Médio - 2ª série: '%'
    Taxa de Não-Resposta - Ensino Médio - 3ª série: '%'
    Taxa de Não-Resposta - Ensino Médio - 4ª série: '%'
    Taxa de Não-Resposta - Ensino Médio - Total Médio Não-Seriado: '%'
    Ensino Fundamental de 8 e 9 anos - Total: '%'
    Ensino Fundamental de 8 e 9 anos - Anos Iniciais: '%'
    Ensino Fundamental de 8 e 9 anos - Anos Finais: '%'
    Ensino Fundamental de 8 e 9 anos - 1º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 2º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 3º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 4º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 5º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 6º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 7º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 8º Ano: '%'
    Ensino Fundamental de 8 e 9 anos - 9º Ano: '%'
    Ensino Médio - Total: '%'
    Ensino Médio - 1ª série: '%'
    Ensino Médio - 2ª série: '%'
    Ensino Médio - 3ª série: '%'
    Ensino Médio - 4ª série: '%'
    Ensino Médio - Não-Seriado: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Taxas de não resposta

## Resumo

Indicador do Inep com a taxa de não resposta (TNR) do Censo da Educação Básica por etapa de ensino. As planilhas trazem a taxa por recorte geográfico, localização e rede.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/taxas-nao-resposta` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2011 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com a taxa de não resposta por etapa |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 49 |
| Unidades de medida | `Ano`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Total Ens. Fundamental`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Iniciais (1º ao 5º Ano)`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Finais (6º ao 9º Ano)`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 1º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 2º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 3º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 4º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 5º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 6º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 7º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 8º Ano`: %; `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 9º Ano`: %; `Taxa de Não-Resposta - Ensino Médio - Total Médio`: %; `Taxa de Não-Resposta - Ensino Médio - 1ª série`: %; `Taxa de Não-Resposta - Ensino Médio - 2ª série`: %; `Taxa de Não-Resposta - Ensino Médio - 3ª série`: %; `Taxa de Não-Resposta - Ensino Médio - 4ª série`: %; `Taxa de Não-Resposta - Ensino Médio - Total Médio Não-Seriado`: %; `Ensino Fundamental de 8 e 9 anos - Total`: %; `Ensino Fundamental de 8 e 9 anos - Anos Iniciais`: %; `Ensino Fundamental de 8 e 9 anos - Anos Finais`: %; `Ensino Fundamental de 8 e 9 anos - 1º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 2º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 3º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 4º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 5º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 6º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 7º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 8º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 9º Ano`: %; `Ensino Médio - Total`: %; `Ensino Médio - 1ª série`: %; `Ensino Médio - 2ª série`: %; `Ensino Médio - 3ª série`: %; `Ensino Médio - 4ª série`: %; `Ensino Médio - Não-Seriado`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 45 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/tnr_brasil_regioes_ufs_2025.zip`.
- No bruto, cada arquivo se chama `indicadores/taxas-nao-resposta/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Taxa de Não-Resposta (TNR)".
- Fonte declarada nas planilhas: Censo da Educação Básica/Inep (DEED).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2011 | `tx_nao_resposta_brasil` (22); `tx_nao_resposta_regioes` (22); `tx_nao_resposta_uf` (22) |
| 2012 | `taxa_no_resposta_brasil` (22); `taxa_no_resposta_regies` (22); `taxa_no_resposta_uf` (22) |
| 2013 | `taxa_no_resposta_brasil` (22); `taxa_no_resposta_regies` (22); `taxa_no_resposta_uf` (22) |
| 2014 | `taxa_no_resposta_brasil` (22); `taxa_no_resposta_regies` (22); `taxa_no_resposta_uf` (22) |
| 2015 | `tnr_brasil` (22); `tnr_regioes` (22); `tnr_ufs` (22) |
| 2016 | `tnr_brasil` (22); `tnr_regioes` (22); `tnr_ufs` (23) |
| 2017 | `tnr_brasil_regioes_ufs` (22) |
| 2018 | `tnr_brasil_regioes_ufs` (22) |
| 2019 | `tnr_brasil_regioes_ufs` (22) |
| 2020 | `tnr_brasil_regioes_ufs` (22) |
| 2021 | `tnr_brasil_regioes_ufs` (22) |
| 2022 | `tnr_brasil_regioes_ufs` (22) |
| 2023 | `tnr_brasil_regioes_ufs` (22) |
| 2024 | `tnr_brasil_regioes_ufs` (22) |
| 2025 | `tnr_brasil_regioes_ufs` (22); `tnr_escolas` (26); `tnr_municipios` (24) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 9 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2011 a 2016 | `taxa_no_resposta_brasil`, `tnr_brasil`, `tx_nao_resposta_brasil` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 9 |
| `Rede` | `Rede` | texto | Rede de ensino da escola (pública, privada ou total), conforme a planilha. | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Total Ens. Fundamental` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Total Ens. Fundamental` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › Total Ens. Fundamental»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Iniciais (1º ao 5º Ano)` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Iniciais (1º ao 5º Ano)` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › Anos Iniciais (1º ao 5º Ano)»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Finais (6º ao 9º Ano)` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - Anos Finais (6º ao 9º Ano)` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › Anos Finais (6º ao 9º Ano)»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 1º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 1º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 2º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 2º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 3º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 3º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 4º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 4º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 5º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 5º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 6º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 6º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 7º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 7º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 8º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 8º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 9º Ano` | `Taxa de Não-Resposta - Ensino Fundamental de 8 e 9 anos - 9º Ano` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Fundamental de 8 e 9 anos › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - Total Médio` | `Taxa de Não-Resposta - Ensino Médio - Total Médio` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › Total Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - 1ª série` | `Taxa de Não-Resposta - Ensino Médio - 1ª série` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › 1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - 2ª série` | `Taxa de Não-Resposta - Ensino Médio - 2ª série` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › 2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - 3ª série` | `Taxa de Não-Resposta - Ensino Médio - 3ª série` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › 3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - 4ª série` | `Taxa de Não-Resposta - Ensino Médio - 4ª série` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › 4ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Taxa de Não-Resposta - Ensino Médio - Total Médio Não-Seriado` | `Taxa de Não-Resposta - Ensino Médio - Total Médio Não-Seriado` | decimal | Valor de «Taxa de Não-Resposta» no recorte «Ensino Médio › Total Médio Não-Seriado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2015 | `taxa_no_resposta_brasil`, `taxa_no_resposta_regies`, `taxa_no_resposta_uf` e mais 6 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `taxa_no_resposta_regies`, `tnr_escolas`, `tnr_municipios` e mais 3 |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `taxa_no_resposta_uf`, `tnr_escolas`, `tnr_municipios` e mais 2 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - Total` | `Ensino Fundamental de 8 e 9 anos - Total` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - Anos Iniciais` | `Ensino Fundamental de 8 e 9 anos - Anos Iniciais` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - Anos Finais` | `Ensino Fundamental de 8 e 9 anos - Anos Finais` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 1º Ano` | `Ensino Fundamental de 8 e 9 anos - 1º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 2º Ano` | `Ensino Fundamental de 8 e 9 anos - 2º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 3º Ano` | `Ensino Fundamental de 8 e 9 anos - 3º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 4º Ano` | `Ensino Fundamental de 8 e 9 anos - 4º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 5º Ano` | `Ensino Fundamental de 8 e 9 anos - 5º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 6º Ano` | `Ensino Fundamental de 8 e 9 anos - 6º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 7º Ano` | `Ensino Fundamental de 8 e 9 anos - 7º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 8º Ano` | `Ensino Fundamental de 8 e 9 anos - 8º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Fundamental de 8 e 9 anos - 9º Ano` | `Ensino Fundamental de 8 e 9 anos - 9º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - Total` | `Ensino Médio - Total` | decimal | Valor de «Ensino Médio» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - 1ª série` | `Ensino Médio - 1ª série` | decimal | Valor de «Ensino Médio» no recorte «1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - 2ª série` | `Ensino Médio - 2ª série` | decimal | Valor de «Ensino Médio» no recorte «2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - 3ª série` | `Ensino Médio - 3ª série` | decimal | Valor de «Ensino Médio» no recorte «3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - 4ª série` | `Ensino Médio - 4ª série` | decimal/inteiro | Valor de «Ensino Médio» no recorte «4ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_escolas` e mais 3 |
| `Ensino Médio - Não-Seriado` | `Ensino Médio - Não-Seriado` | decimal | Valor de «Ensino Médio» no recorte «Não-Seriado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2025 | `tnr_brasil`, `tnr_brasil_regioes_ufs`, `tnr_regioes` e mais 1 |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `tnr_brasil_regioes_ufs` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tnr_escolas`, `tnr_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tnr_escolas` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tnr_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tnr_escolas` |
| `Município` | `Município` | texto | Coluna «Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tnr_municipios` |

## No lake

- Dataset `inep/taxas-nao-resposta`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `tnr_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Ensino Fundamental de 8 e 9 anos - Total"
    FROM read_parquet('lake/inep/taxas-nao-resposta/ano=2025/taxas-nao-resposta-tnr-brasil-regioes-ufs-2025__tnr_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
