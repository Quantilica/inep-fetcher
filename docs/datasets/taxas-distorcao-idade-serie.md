---
dataset:
  id: taxas-distorcao-idade-serie
  fonte: inep
  titulo: Indicadores — Taxas de distorção idade-série
  resumo: Taxa de distorção idade-série por série e etapa, por recorte geográfico, localização e dependência administrativa.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2006'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição, com a taxa de distorção por série e etapa
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 91
  unidades_de_medida:
    Ano: ano ou código
    Código da UF: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Taxa de Distorção Idade-Série - Ensino Fundamental - Total Fundamental: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª a 4ª Série - 1º ao 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª a 8ª Série - 6º ao 9º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 1º ANO: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª Série/ - 2º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 2ª Série/ - 3º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 3ª Série/ - 4º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 4ª Série/ - 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª Série/ - 6º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 6ª Série/ - 7º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 7ª Série/ - 8º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental - 8ª Série/ - 9º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - Total Médio: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ANO: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª Série/ - 2º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2ª Série/ - 3º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3ª Série/ - 4º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4ª Série/ - 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª Série/ - 6º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6ª Série/ - 7º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7ª Série/ - 8º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8ª Série/ - 9º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Total Fundamental: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Fundamental: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano Ensino Fundamental: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série Médio: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série Médio: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série Médio: '%'
    Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série Médio: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ao 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º ao 9º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8º Ano: '%'
    Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 9º Ano: '%'
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
    Ensino Médio - 1ª Série: '%'
    Ensino Médio - 2ª Série: '%'
    Ensino Médio - 3ª Série: '%'
    Ensino Médio - 4ª Série: '%'
    Ensino Fundamental - Total: '%'
    Ensino Fundamental - Anos Iniciais: '%'
    Ensino Fundamental - Anos Finais: '%'
    Ensino Fundamental - 1º Ano: '%'
    Ensino Fundamental - 2º Ano: '%'
    Ensino Fundamental - 3º Ano: '%'
    Ensino Fundamental - 4º Ano: '%'
    Ensino Fundamental - 5º Ano: '%'
    Ensino Fundamental - 6º Ano: '%'
    Ensino Fundamental - 7º Ano: '%'
    Ensino Fundamental - 8º Ano: '%'
    Ensino Fundamental - 9º Ano: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Taxas de distorção idade-série

## Resumo

Indicador do Inep com a taxa de distorção idade-série, calculada a partir do Censo da Educação Básica, por série e etapa de ensino. As planilhas trazem a taxa por recorte geográfico, localização e dependência administrativa.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/taxas-distorcao-idade-serie` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2006 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição, com a taxa de distorção por série e etapa |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 91 |
| Unidades de medida | `Ano`: ano ou código; `Código da UF`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Taxa de Distorção Idade-Série - Ensino Fundamental - Total Fundamental`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª a 4ª Série - 1º ao 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª a 8ª Série - 6º ao 9º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 1º ANO`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª Série/ - 2º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 2ª Série/ - 3º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 3ª Série/ - 4º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 4ª Série/ - 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª Série/ - 6º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 6ª Série/ - 7º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 7ª Série/ - 8º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental - 8ª Série/ - 9º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Médio - Total Médio`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ANO`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª Série/ - 2º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2ª Série/ - 3º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3ª Série/ - 4º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4ª Série/ - 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª Série/ - 6º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6ª Série/ - 7º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7ª Série/ - 8º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8ª Série/ - 9º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Total Fundamental`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Fundamental`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano Ensino Fundamental`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série Médio`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série Médio`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série Médio`: %; `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série Médio`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ao 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º ao 9º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8º Ano`: %; `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 9º Ano`: %; `Ensino Fundamental de 8 e 9 anos - Total`: %; `Ensino Fundamental de 8 e 9 anos - Anos Iniciais`: %; `Ensino Fundamental de 8 e 9 anos - Anos Finais`: %; `Ensino Fundamental de 8 e 9 anos - 1º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 2º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 3º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 4º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 5º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 6º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 7º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 8º Ano`: %; `Ensino Fundamental de 8 e 9 anos - 9º Ano`: %; `Ensino Médio - Total`: %; `Ensino Médio - 1ª Série`: %; `Ensino Médio - 2ª Série`: %; `Ensino Médio - 3ª Série`: %; `Ensino Médio - 4ª Série`: %; `Ensino Fundamental - Total`: %; `Ensino Fundamental - Anos Iniciais`: %; `Ensino Fundamental - Anos Finais`: %; `Ensino Fundamental - 1º Ano`: %; `Ensino Fundamental - 2º Ano`: %; `Ensino Fundamental - 3º Ano`: %; `Ensino Fundamental - 4º Ano`: %; `Ensino Fundamental - 5º Ano`: %; `Ensino Fundamental - 6º Ano`: %; `Ensino Fundamental - 7º Ano`: %; `Ensino Fundamental - 8º Ano`: %; `Ensino Fundamental - 9º Ano`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 59 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/TDI_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/taxas-distorcao-idade-serie/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Taxa de Distorção Idade-Série".
- A fonte não traz a definição da taxa nas planilhas; ela está na nota técnica do Inep.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2006 | `tdi06_br_reg` (21); `tdi06_uf` (22) |
| 2007 | `tdi_brasil` (20); `tdi_regio` (21); `tdi_ufs` (22) |
| 2008 | `tdi_brasil` (20); `tdi_regies` (21); `tdi_ufs` (22) |
| 2009 | `dados_tdi_brasil` (20); `dados_tdi_regies` (21); `dados_tdi_uf` (22) |
| 2010 | `dados_tdi_brasil` (21); `dados_tdi_regies` (21); `dados_tdi_uf` (22) |
| 2011 | `tdi_brasil` (21); `tdi_regioes` (21); `tdi_ufs` (22) |
| 2012 | `tdi_brasil` (21); `tdi_regioes` (21); `tdi_ufs` (22) |
| 2013 | `tdi_brasil` (21); `tdi_regies` (21); `tdi_uf` (22) |
| 2014 | `tdi_brasil` (21); `tdi_regies` (21); `tdi_uf` (22) |
| 2015 | `tdi_brasil` (21); `tdi_regioes` (21); `tdi_ufs` (23) |
| 2016 | `tdi_brasil` (21); `tdi_regioes` (21); `tdi_ufs` (22) |
| 2017 | `tdi_brasil_regioes_ufs` (21) |
| 2018 | `tdi_brasil_regioes_ufs` (21) |
| 2019 | `tdi_brasil_regioes_ufs` (21) |
| 2020 | `tdi_brasil_regioes_ufs` (21) |
| 2021 | `tdi_brasil_regioes_ufs` (21) |
| 2022 | `tdi_brasil_regioes_ufs` (21) |
| 2023 | `tdi_brasil_regioes_ufs` (21) |
| 2024 | `tdi_brasil_regioes_ufs` (21) |
| 2025 | `tdi_brasil_regioes_ufs` (21); `tdi_escolas` (26); `tdi_municipios` (24) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 11 |
| `Brasil e Regiões` | `Brasil e Regiões` | texto | Brasil ou grande região da linha. | — | 2006 | `tdi06_br_reg` |
| `Dep. Adm.` | `Dep. Adm.` | texto | Dependência administrativa da escola, conforme a planilha. | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 11 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - Total Fundamental` | `Taxa de Distorção Idade-Série - Ensino Fundamental - Total Fundamental` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › Total Fundamental»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª a 4ª Série - 1º ao 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª a 4ª Série - 1º ao 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 1ª a 4ª Série › 1º ao 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª a 8ª Série - 6º ao 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª a 8ª Série - 6º ao 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 5ª a 8ª Série › 6º ao 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 1º ANO` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 1º ANO` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 1º ANO»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª Série/ - 2º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 1ª Série/ - 2º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 1ª Série/ › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 2ª Série/ - 3º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 2ª Série/ - 3º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 2ª Série/ › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 3ª Série/ - 4º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 3ª Série/ - 4º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 3ª Série/ › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 4ª Série/ - 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 4ª Série/ - 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 4ª Série/ › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª Série/ - 6º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 5ª Série/ - 6º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 5ª Série/ › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 6ª Série/ - 7º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 6ª Série/ - 7º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 6ª Série/ › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 7ª Série/ - 8º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 7ª Série/ - 8º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 7ª Série/ › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental - 8ª Série/ - 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental - 8ª Série/ - 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental › 8ª Série/ › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 | `tdi06_br_reg`, `tdi06_uf` |
| `Taxa de Distorção Idade-Série - Ensino Médio - Total Médio` | `Taxa de Distorção Idade-Série - Ensino Médio - Total Médio` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › Total Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 8 |
| `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série` | `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 1ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 8 |
| `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série` | `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 2ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 8 |
| `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série` | `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 3ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 8 |
| `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série` | `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 4ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2006 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 8 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `dados_tdi_regies`, `dados_tdi_uf`, `tdi06_uf` e mais 7 |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `dados_tdi_uf`, `tdi06_uf`, `tdi_escolas` e mais 2 |
| `Rede` | `Rede` | texto | Rede de ensino da escola (pública, privada ou total), conforme a planilha. | — | 2007 a 2015 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 6 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ANO` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ANO` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1º ANO»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª Série/ - 2º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª Série/ - 2º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1ª Série/ › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2ª Série/ - 3º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2ª Série/ - 3º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 2ª Série/ › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3ª Série/ - 4º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3ª Série/ - 4º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 3ª Série/ › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4ª Série/ - 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4ª Série/ - 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 4ª Série/ › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª Série/ - 6º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª Série/ - 6º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 5ª Série/ › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6ª Série/ - 7º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6ª Série/ - 7º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 6ª Série/ › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7ª Série/ - 8º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7ª Série/ - 8º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 7ª Série/ › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8ª Série/ - 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8ª Série/ - 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 8ª Série/ › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1ª a 4ª Série › 1º ao 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 5ª a 8ª Série › 6º ao 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_brasil`, `dados_tdi_regies`, `dados_tdi_uf` e mais 4 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Total Fundamental` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Total Fundamental` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › Total Fundamental»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2014 | `dados_tdi_brasil`, `dados_tdi_regies`, `tdi_brasil` e mais 5 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Fundamental` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - Fundamental` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › Fundamental»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2007 a 2010 | `dados_tdi_uf`, `tdi_ufs` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano Ensino Fundamental` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano Ensino Fundamental` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1º Ano Ensino Fundamental»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2008 | `tdi_ufs` |
| `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série Médio` | `Taxa de Distorção Idade-Série - Ensino Médio - 1ª Série Médio` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 1ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2008 | `tdi_ufs` |
| `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série Médio` | `Taxa de Distorção Idade-Série - Ensino Médio - 2ª Série Médio` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 2ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2008 | `tdi_ufs` |
| `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série Médio` | `Taxa de Distorção Idade-Série - Ensino Médio - 3ª Série Médio` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 3ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2008 | `tdi_ufs` |
| `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série Médio` | `Taxa de Distorção Idade-Série - Ensino Médio - 4ª Série Médio` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Médio › 4ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2008 | `tdi_ufs` |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2010 a 2016 | `dados_tdi_brasil`, `tdi_brasil` |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ao 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º ao 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1º ao 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º ao 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º ao 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 6º ao 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 1º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 2º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 3º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 4º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 5º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 6º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 7º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 8º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 9º Ano` | `Taxa de Distorção Idade-Série - Ensino Fundamental de 8 e 9 anos - 9º Ano` | decimal | Valor de «Taxa de Distorção Idade-Série» no recorte «Ensino Fundamental de 8 e 9 anos › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `tdi_brasil`, `tdi_regies`, `tdi_regioes` e mais 2 |
| `Ensino Fundamental de 8 e 9 anos - Total` | `Ensino Fundamental de 8 e 9 anos - Total` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - Anos Iniciais` | `Ensino Fundamental de 8 e 9 anos - Anos Iniciais` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - Anos Finais` | `Ensino Fundamental de 8 e 9 anos - Anos Finais` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 1º Ano` | `Ensino Fundamental de 8 e 9 anos - 1º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 2º Ano` | `Ensino Fundamental de 8 e 9 anos - 2º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 3º Ano` | `Ensino Fundamental de 8 e 9 anos - 3º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 4º Ano` | `Ensino Fundamental de 8 e 9 anos - 4º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 5º Ano` | `Ensino Fundamental de 8 e 9 anos - 5º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 6º Ano` | `Ensino Fundamental de 8 e 9 anos - 6º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 7º Ano` | `Ensino Fundamental de 8 e 9 anos - 7º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 8º Ano` | `Ensino Fundamental de 8 e 9 anos - 8º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Fundamental de 8 e 9 anos - 9º Ano` | `Ensino Fundamental de 8 e 9 anos - 9º Ano` | decimal | Valor de «Ensino Fundamental de 8 e 9 anos» no recorte «9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_regioes` e mais 1 |
| `Ensino Médio - Total` | `Ensino Médio - Total` | decimal | Valor de «Ensino Médio» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Ensino Médio - 1ª Série` | `Ensino Médio - 1ª Série` | decimal | Valor de «Ensino Médio» no recorte «1ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Ensino Médio - 2ª Série` | `Ensino Médio - 2ª Série` | decimal | Valor de «Ensino Médio» no recorte «2ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Ensino Médio - 3ª Série` | `Ensino Médio - 3ª Série` | decimal | Valor de «Ensino Médio» no recorte «3ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Ensino Médio - 4ª Série` | `Ensino Médio - 4ª Série` | decimal/inteiro | Valor de «Ensino Médio» no recorte «4ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Código da UF` | `Código da UF` | inteiro | Coluna «Código da UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `tdi_ufs` |
| `Sigla da UF` | `Sigla da UF` | texto | Coluna «Sigla da UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 a 2025 | `tdi_municipios`, `tdi_ufs` |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | 2016 a 2025 | `tdi_brasil`, `tdi_brasil_regioes_ufs`, `tdi_escolas` e mais 3 |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `tdi_brasil_regioes_ufs` |
| `Ensino Fundamental - Total` | `Ensino Fundamental - Total` | decimal | Valor de «Ensino Fundamental» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - Anos Iniciais` | `Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - Anos Finais` | `Ensino Fundamental - Anos Finais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 1º Ano` | `Ensino Fundamental - 1º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 2º Ano` | `Ensino Fundamental - 2º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 3º Ano` | `Ensino Fundamental - 3º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 4º Ano` | `Ensino Fundamental - 4º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 5º Ano` | `Ensino Fundamental - 5º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 6º Ano` | `Ensino Fundamental - 6º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 7º Ano` | `Ensino Fundamental - 7º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 8º Ano` | `Ensino Fundamental - 8º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Ensino Fundamental - 9º Ano` | `Ensino Fundamental - 9º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `tdi_brasil_regioes_ufs`, `tdi_escolas`, `tdi_municipios` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tdi_escolas`, `tdi_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tdi_escolas`, `tdi_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tdi_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `tdi_escolas` |

## No lake

- Dataset `inep/taxas-distorcao-idade-serie`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `tdi_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Ensino Fundamental - Total"
    FROM read_parquet('lake/inep/taxas-distorcao-idade-serie/ano=2025/taxas-distorcao-idade-serie-tdi-2025-brasil-regioes-ufs__tdi_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
