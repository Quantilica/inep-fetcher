---
dataset:
  id: taxas-transicao
  fonte: inep
  titulo: Indicadores — Taxas de transição
  resumo: Taxas de promoção, repetência, evasão e migração para a EJA entre dois anos letivos consecutivos, por série e recorte geográfico.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; cada arquivo cobre a transição entre dois anos letivos
  cobertura:
    inicio: '2007'
    fim: '2021'
  unidade: um recorte (Brasil, região ou UF; localização e dependência) numa transição entre dois anos, com a taxa por série e etapa
  granularidade:
    espacial: Brasil, grande região e UF
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 72
  unidades_de_medida:
    Ano: ano ou código
    Código do município: ano ou código
    Taxa de Promoção - Ensino Fundamental - Total: '%'
    Taxa de Promoção - Ensino Fundamental - Anos Iniciais: '%'
    Taxa de Promoção - Ensino Fundamental - Anos Finais: '%'
    Taxa de Promoção - Ensino Fundamental - 1º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 2º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 3º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 4º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 5º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 6º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 7º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 8º Ano: '%'
    Taxa de Promoção - Ensino Fundamental - 9º Ano: '%'
    Taxa de Promoção - Ensino Médio - Total: '%'
    Taxa de Promoção - Ensino Médio - 1ª série: '%'
    Taxa de Promoção - Ensino Médio - 2ª série: '%'
    Taxa de Promoção - Ensino Médio - 3ª série: '%'
    Taxa de Repetência - Ensino Fundamental - Total: '%'
    Taxa de Repetência - Ensino Fundamental - Anos Iniciais: '%'
    Taxa de Repetência - Ensino Fundamental - Anos Finais: '%'
    Taxa de Repetência - Ensino Fundamental - 1º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 2º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 3º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 4º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 5º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 6º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 7º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 8º Ano: '%'
    Taxa de Repetência - Ensino Fundamental - 9º Ano: '%'
    Taxa de Repetência - Ensino Médio - Total: '%'
    Taxa de Repetência - Ensino Médio - 1ª série: '%'
    Taxa de Repetência - Ensino Médio - 2ª série: '%'
    Taxa de Repetência - Ensino Médio - 3ª série: '%'
    Taxa de Evasão - Ensino Fundamental - Total: '%'
    Taxa de Evasão - Ensino Fundamental - Anos Iniciais: '%'
    Taxa de Evasão - Ensino Fundamental - Anos Finais: '%'
    Taxa de Evasão - Ensino Fundamental - 1º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 2º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 3º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 4º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 5º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 6º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 7º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 8º Ano: '%'
    Taxa de Evasão - Ensino Fundamental - 9º Ano: '%'
    Taxa de Evasão - Ensino Médio - Total: '%'
    Taxa de Evasão - Ensino Médio - 1ª série: '%'
    Taxa de Evasão - Ensino Médio - 2ª série: '%'
    Taxa de Evasão - Ensino Médio - 3ª série: '%'
    Migração para EJA - Ensino Fundamental - Total: '%'
    Migração para EJA - Ensino Fundamental - Anos Iniciais: '%'
    Migração para EJA - Ensino Fundamental - Anos Finais: '%'
    Migração para EJA - Ensino Fundamental - 1º Ano: '%'
    Migração para EJA - Ensino Fundamental - 2º Ano: '%'
    Migração para EJA - Ensino Fundamental - 3º Ano: '%'
    Migração para EJA - Ensino Fundamental - 4º Ano: '%'
    Migração para EJA - Ensino Fundamental - 5º Ano: '%'
    Migração para EJA - Ensino Fundamental - 6º Ano: '%'
    Migração para EJA - Ensino Fundamental - 7º Ano: '%'
    Migração para EJA - Ensino Fundamental - 8º Ano: '%'
    Migração para EJA - Ensino Fundamental - 9º Ano: '%'
    Migração para EJA - Ensino Médio - Total: '%'
    Migração para EJA - Ensino Médio - 1ª série: '%'
    Migração para EJA - Ensino Médio - 2ª série: '%'
    Migração para EJA - Ensino Médio - 3ª série: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Taxas de transição

## Resumo

Indicador do Inep de fluxo escolar: as taxas de transição entre dois anos consecutivos, calculadas a partir do Censo da Educação Básica, por série e etapa. Cada arquivo cobre um par de anos (por exemplo 2021/2022), e o lake guarda o primeiro ano na partição `ano`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/taxas-transicao` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; cada arquivo cobre a transição entre dois anos letivos |
| Cobertura | 2007 a 2021 |
| Unidade (uma linha) | um recorte (Brasil, região ou UF; localização e dependência) numa transição entre dois anos, com a taxa por série e etapa |
| Granularidade | espacial: Brasil, grande região e UF; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 72 |
| Unidades de medida | `Ano`: ano ou código; `Código do município`: ano ou código; `Taxa de Promoção - Ensino Fundamental - Total`: %; `Taxa de Promoção - Ensino Fundamental - Anos Iniciais`: %; `Taxa de Promoção - Ensino Fundamental - Anos Finais`: %; `Taxa de Promoção - Ensino Fundamental - 1º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 2º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 3º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 4º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 5º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 6º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 7º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 8º Ano`: %; `Taxa de Promoção - Ensino Fundamental - 9º Ano`: %; `Taxa de Promoção - Ensino Médio - Total`: %; `Taxa de Promoção - Ensino Médio - 1ª série`: %; `Taxa de Promoção - Ensino Médio - 2ª série`: %; `Taxa de Promoção - Ensino Médio - 3ª série`: %; `Taxa de Repetência - Ensino Fundamental - Total`: %; `Taxa de Repetência - Ensino Fundamental - Anos Iniciais`: %; `Taxa de Repetência - Ensino Fundamental - Anos Finais`: %; `Taxa de Repetência - Ensino Fundamental - 1º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 2º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 3º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 4º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 5º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 6º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 7º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 8º Ano`: %; `Taxa de Repetência - Ensino Fundamental - 9º Ano`: %; `Taxa de Repetência - Ensino Médio - Total`: %; `Taxa de Repetência - Ensino Médio - 1ª série`: %; `Taxa de Repetência - Ensino Médio - 2ª série`: %; `Taxa de Repetência - Ensino Médio - 3ª série`: %; `Taxa de Evasão - Ensino Fundamental - Total`: %; `Taxa de Evasão - Ensino Fundamental - Anos Iniciais`: %; `Taxa de Evasão - Ensino Fundamental - Anos Finais`: %; `Taxa de Evasão - Ensino Fundamental - 1º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 2º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 3º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 4º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 5º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 6º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 7º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 8º Ano`: %; `Taxa de Evasão - Ensino Fundamental - 9º Ano`: %; `Taxa de Evasão - Ensino Médio - Total`: %; `Taxa de Evasão - Ensino Médio - 1ª série`: %; `Taxa de Evasão - Ensino Médio - 2ª série`: %; `Taxa de Evasão - Ensino Médio - 3ª série`: %; `Migração para EJA - Ensino Fundamental - Total`: %; `Migração para EJA - Ensino Fundamental - Anos Iniciais`: %; `Migração para EJA - Ensino Fundamental - Anos Finais`: %; `Migração para EJA - Ensino Fundamental - 1º Ano`: %; `Migração para EJA - Ensino Fundamental - 2º Ano`: %; `Migração para EJA - Ensino Fundamental - 3º Ano`: %; `Migração para EJA - Ensino Fundamental - 4º Ano`: %; `Migração para EJA - Ensino Fundamental - 5º Ano`: %; `Migração para EJA - Ensino Fundamental - 6º Ano`: %; `Migração para EJA - Ensino Fundamental - 7º Ano`: %; `Migração para EJA - Ensino Fundamental - 8º Ano`: %; `Migração para EJA - Ensino Fundamental - 9º Ano`: %; `Migração para EJA - Ensino Médio - Total`: %; `Migração para EJA - Ensino Médio - 1ª série`: %; `Migração para EJA - Ensino Médio - 2ª série`: %; `Migração para EJA - Ensino Médio - 3ª série`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 30 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_brasil_regioes_ufs_2021_2022.zip`.
- No bruto, cada arquivo se chama `indicadores/taxas-transicao/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Fluxo Escolar - Taxas de Transição, Brasil, Regiões Geográficas e Unidades da Federação", com o par de anos.
- Nota da fonte: a taxa de promoção é a proporção de alunos matriculados na série k no primeiro ano que se matriculam em série superior a k no ano seguinte (a nota completa, com as demais taxas, está na planilha).
- Cada arquivo cobre um par de anos; a coluna `Ano` traz o ano inicial.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2007 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2008 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2009 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2010 | `taxa_de_transicao_brasil_regioes_ufs_e` (68) |
| 2011 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2012 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2013 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2014 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2015 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2016 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2017 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2018 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2019 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2020 | `tx_transicao_brasil_regioes_ufs` (68) |
| 2021 | `tx_transicao_brasil_regioes_ufs` (68); `tx_transicao_municipios` (71) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | texto | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - Total` | `Taxa de Promoção - Ensino Fundamental - Total` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - Anos Iniciais` | `Taxa de Promoção - Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - Anos Finais` | `Taxa de Promoção - Ensino Fundamental - Anos Finais` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 1º Ano` | `Taxa de Promoção - Ensino Fundamental - 1º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 2º Ano` | `Taxa de Promoção - Ensino Fundamental - 2º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 3º Ano` | `Taxa de Promoção - Ensino Fundamental - 3º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 4º Ano` | `Taxa de Promoção - Ensino Fundamental - 4º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 5º Ano` | `Taxa de Promoção - Ensino Fundamental - 5º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 6º Ano` | `Taxa de Promoção - Ensino Fundamental - 6º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 7º Ano` | `Taxa de Promoção - Ensino Fundamental - 7º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 8º Ano` | `Taxa de Promoção - Ensino Fundamental - 8º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Fundamental - 9º Ano` | `Taxa de Promoção - Ensino Fundamental - 9º Ano` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Fundamental › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Médio - Total` | `Taxa de Promoção - Ensino Médio - Total` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Médio › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Médio - 1ª série` | `Taxa de Promoção - Ensino Médio - 1ª série` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Médio › 1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Médio - 2ª série` | `Taxa de Promoção - Ensino Médio - 2ª série` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Médio › 2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Promoção - Ensino Médio - 3ª série` | `Taxa de Promoção - Ensino Médio - 3ª série` | decimal | Valor de «Taxa de Promoção» no recorte «Ensino Médio › 3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - Total` | `Taxa de Repetência - Ensino Fundamental - Total` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - Anos Iniciais` | `Taxa de Repetência - Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - Anos Finais` | `Taxa de Repetência - Ensino Fundamental - Anos Finais` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 1º Ano` | `Taxa de Repetência - Ensino Fundamental - 1º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 2º Ano` | `Taxa de Repetência - Ensino Fundamental - 2º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 3º Ano` | `Taxa de Repetência - Ensino Fundamental - 3º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 4º Ano` | `Taxa de Repetência - Ensino Fundamental - 4º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 5º Ano` | `Taxa de Repetência - Ensino Fundamental - 5º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 6º Ano` | `Taxa de Repetência - Ensino Fundamental - 6º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 7º Ano` | `Taxa de Repetência - Ensino Fundamental - 7º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 8º Ano` | `Taxa de Repetência - Ensino Fundamental - 8º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Fundamental - 9º Ano` | `Taxa de Repetência - Ensino Fundamental - 9º Ano` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Fundamental › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Médio - Total` | `Taxa de Repetência - Ensino Médio - Total` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Médio › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Médio - 1ª série` | `Taxa de Repetência - Ensino Médio - 1ª série` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Médio › 1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Médio - 2ª série` | `Taxa de Repetência - Ensino Médio - 2ª série` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Médio › 2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Repetência - Ensino Médio - 3ª série` | `Taxa de Repetência - Ensino Médio - 3ª série` | decimal | Valor de «Taxa de Repetência» no recorte «Ensino Médio › 3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - Total` | `Taxa de Evasão - Ensino Fundamental - Total` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - Anos Iniciais` | `Taxa de Evasão - Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - Anos Finais` | `Taxa de Evasão - Ensino Fundamental - Anos Finais` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 1º Ano` | `Taxa de Evasão - Ensino Fundamental - 1º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 2º Ano` | `Taxa de Evasão - Ensino Fundamental - 2º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 3º Ano` | `Taxa de Evasão - Ensino Fundamental - 3º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 4º Ano` | `Taxa de Evasão - Ensino Fundamental - 4º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 5º Ano` | `Taxa de Evasão - Ensino Fundamental - 5º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 6º Ano` | `Taxa de Evasão - Ensino Fundamental - 6º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 7º Ano` | `Taxa de Evasão - Ensino Fundamental - 7º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 8º Ano` | `Taxa de Evasão - Ensino Fundamental - 8º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Fundamental - 9º Ano` | `Taxa de Evasão - Ensino Fundamental - 9º Ano` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Fundamental › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Médio - Total` | `Taxa de Evasão - Ensino Médio - Total` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Médio › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Médio - 1ª série` | `Taxa de Evasão - Ensino Médio - 1ª série` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Médio › 1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Médio - 2ª série` | `Taxa de Evasão - Ensino Médio - 2ª série` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Médio › 2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Taxa de Evasão - Ensino Médio - 3ª série` | `Taxa de Evasão - Ensino Médio - 3ª série` | decimal | Valor de «Taxa de Evasão» no recorte «Ensino Médio › 3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - Total` | `Migração para EJA - Ensino Fundamental - Total` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - Anos Iniciais` | `Migração para EJA - Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - Anos Finais` | `Migração para EJA - Ensino Fundamental - Anos Finais` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 1º Ano` | `Migração para EJA - Ensino Fundamental - 1º Ano` | decimal/inteiro | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 2º Ano` | `Migração para EJA - Ensino Fundamental - 2º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 3º Ano` | `Migração para EJA - Ensino Fundamental - 3º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 4º Ano` | `Migração para EJA - Ensino Fundamental - 4º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 5º Ano` | `Migração para EJA - Ensino Fundamental - 5º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 6º Ano` | `Migração para EJA - Ensino Fundamental - 6º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 7º Ano` | `Migração para EJA - Ensino Fundamental - 7º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 8º Ano` | `Migração para EJA - Ensino Fundamental - 8º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Fundamental - 9º Ano` | `Migração para EJA - Ensino Fundamental - 9º Ano` | decimal | Valor de «Migração para EJA» no recorte «Ensino Fundamental › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Médio - Total` | `Migração para EJA - Ensino Médio - Total` | decimal | Valor de «Migração para EJA» no recorte «Ensino Médio › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Médio - 1ª série` | `Migração para EJA - Ensino Médio - 1ª série` | decimal | Valor de «Migração para EJA» no recorte «Ensino Médio › 1ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Médio - 2ª série` | `Migração para EJA - Ensino Médio - 2ª série` | decimal | Valor de «Migração para EJA» no recorte «Ensino Médio › 2ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Migração para EJA - Ensino Médio - 3ª série` | `Migração para EJA - Ensino Médio - 3ª série` | decimal | Valor de «Migração para EJA» no recorte «Ensino Médio › 3ª série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `taxa_de_transicao_brasil_regioes_ufs_e`, `tx_transicao_brasil_regioes_ufs`, `tx_transicao_municipios` |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | 2021 | `tx_transicao_municipios` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 | `tx_transicao_municipios` |
| `Código do município` | `Código do município` | inteiro | Coluna «Código do município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 | `tx_transicao_municipios` |
| `Nome do município` | `Nome do município` | texto | Coluna «Nome do município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 | `tx_transicao_municipios` |

## No lake

- Dataset `inep/taxas-transicao`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `tx_transicao_brasil_regioes_ufs_2021_2022.parquet` da edição mais recente do lake (ano 2021):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Taxa de Promoção - Ensino Fundamental - Total"
    FROM read_parquet('lake/inep/taxas-transicao/ano=2021/taxas-transicao-tx-transicao-brasil-regioes-ufs-2021-2022__tx_transicao_brasil_regioes_ufs_2021_2022.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
