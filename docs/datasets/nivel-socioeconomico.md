---
dataset:
  id: nivel-socioeconomico
  fonte: inep
  titulo: Indicadores — Nível socioeconômico das escolas (INSE)
  resumo: Indicador de Nível Socioeconômico (INSE) por escola, a partir dos questionários do Saeb.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: a cada edição do Saeb (2015, 2019, 2021, 2023 no lake)
  cobertura:
    inicio: '2015'
    fim: '2023'
  unidade: uma escola numa edição do INSE
  granularidade:
    espacial: escola (com UF e município)
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 30
  unidades_de_medida:
    PC_NIVEL_1: '%'
    PC_NIVEL_2: '%'
    PC_NIVEL_3: '%'
    PC_NIVEL_4: '%'
    PC_NIVEL_5: '%'
    PC_NIVEL_6: '%'
    PC_NIVEL_7: '%'
    PC_NIVEL_8: '%'
    QTD_ALUNOS_INSE: alunos
    CO_ESCOLA: código
    CO_UF: código
    CO_MUNICIPIO: código
    ID_AREA: código
    TP_DEPENDENCIA: código
    TP_LOCALIZACAO: código
    TP_TIPO_REDE: código
    TP_CAPITAL: código
    NU_ANO_SAEB: código
    ID_ESCOLA: código
    NOME_MUNICIPIO: sem unidade (texto; numérico em uma edição)
    INSE_VALOR_ABSOLUTO: valor do indicador
    MEDIA_INSE: valor do indicador
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Nível socioeconômico das escolas (INSE)

## Resumo

O Indicador de Nível Socioeconômico (INSE) do Inep resume o nível socioeconômico dos estudantes de cada escola, a partir das respostas aos questionários do Saeb. A planilha traz o número de alunos com INSE, o valor médio, a classificação e o percentual de alunos em cada nível.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/nivel-socioeconomico` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | a cada edição do Saeb (2015, 2019, 2021, 2023 no lake) |
| Cobertura | 2015 a 2023 |
| Unidade (uma linha) | uma escola numa edição do INSE |
| Granularidade | espacial: escola (com UF e município); temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 30 |
| Unidades de medida | `PC_NIVEL_1`: %; `PC_NIVEL_2`: %; `PC_NIVEL_3`: %; `PC_NIVEL_4`: %; `PC_NIVEL_5`: %; `PC_NIVEL_6`: %; `PC_NIVEL_7`: %; `PC_NIVEL_8`: %; `QTD_ALUNOS_INSE`: alunos; `CO_ESCOLA`: código; `CO_UF`: código; `CO_MUNICIPIO`: código; `ID_AREA`: código; `TP_DEPENDENCIA`: código; `TP_LOCALIZACAO`: código; `TP_TIPO_REDE`: código; `TP_CAPITAL`: código; `NU_ANO_SAEB`: código; `ID_ESCOLA`: código; `NOME_MUNICIPIO`: sem unidade (texto; numérico em uma edição); `INSE_VALOR_ABSOLUTO`: valor do indicador; `MEDIA_INSE`: valor do indicador |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 13 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2023/nivel_socioeconomico/INSE_2023_brasil.xlsx`.
- No bruto, cada arquivo se chama `indicadores/nivel-socioeconomico/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título da planilha: "Indicador de Nível Socioeconômico por escola". A fonte remete à nota técnica para mais informações.
- Colunas: identificação da escola, UF e município, dependência, localização, quantidade de alunos com INSE, valor do indicador, classificação e percentuais por nível (`PC_NIVEL_1` a `PC_NIVEL_8`).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2015 | `inse` (12) |
| 2019 | `nivel-socioeconomico-inse-estados` (16) |
| 2021 | `nivel-socioeconomico-inse-brasil` (14); `nivel-socioeconomico-inse-estados` (17) |
| 2023 | `nivel-socioeconomico-inse-brasil` (14); `nivel-socioeconomico-inse-escolas` (22); `nivel-socioeconomico-inse-estados` (17); `nivel-socioeconomico-inse-municipios` (19) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `CO_ESCOLA` | `CO_ESCOLA` | inteiro | Coluna «CO_ESCOLA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `NOME_ESCOLA` | `NOME_ESCOLA` | texto | Coluna «NOME_ESCOLA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `CO_UF` | `CO_UF` | inteiro | Coluna «CO_UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `inse`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `NOME_UF` | `NOME_UF` | texto | Coluna «NOME_UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 a 2019 | `inse`, `nivel-socioeconomico-inse-estados` |
| `CO_MUNICIPIO` | `CO_MUNICIPIO` | inteiro | Coluna «CO_MUNICIPIO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `inse`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-municipios` |
| `NOME_MUNICIPIO` | `NOME_MUNICIPIO` | inteiro | Coluna «NOME_MUNICIPIO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `ID_AREA` | `ID_AREA` | inteiro | Coluna «ID_AREA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `TP_DEPENDENCIA` | `TP_DEPENDENCIA` | inteiro | Coluna «TP_DEPENDENCIA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `TP_LOCALIZACAO` | `TP_LOCALIZACAO` | inteiro | Coluna «TP_LOCALIZACAO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `inse`, `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas` e mais 2 |
| `QTD_ALUNOS_INSE` | `QTD_ALUNOS_INSE` | inteiro | Coluna «QTD_ALUNOS_INSE» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `inse`, `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas` e mais 2 |
| `INSE_VALOR_ABSOLUTO` | `INSE_VALOR_ABSOLUTO` | decimal | Coluna «INSE_VALOR_ABSOLUTO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 | `inse` |
| `INSE_CLASSIFICACAO` | `INSE_CLASSIFICACAO` | texto | Coluna «INSE_CLASSIFICACAO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `inse`, `nivel-socioeconomico-inse-escolas` |
| `SIGLA_UF` | `SIGLA_UF` | texto | Coluna «SIGLA_UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 | `nivel-socioeconomico-inse-estados` |
| `TP_TIPO_REDE` | `TP_TIPO_REDE` | inteiro | Coluna «TP_TIPO_REDE» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `TP_CAPITAL` | `TP_CAPITAL` | inteiro | Coluna «TP_CAPITAL» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `MEDIA_INSE` | `MEDIA_INSE` | decimal | Coluna «MEDIA_INSE» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_1` | `PC_NIVEL_1` | decimal | Coluna «PC_NIVEL_1» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_2` | `PC_NIVEL_2` | decimal | Coluna «PC_NIVEL_2» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_3` | `PC_NIVEL_3` | decimal | Coluna «PC_NIVEL_3» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_4` | `PC_NIVEL_4` | decimal | Coluna «PC_NIVEL_4» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_5` | `PC_NIVEL_5` | decimal | Coluna «PC_NIVEL_5» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_6` | `PC_NIVEL_6` | decimal | Coluna «PC_NIVEL_6» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_7` | `PC_NIVEL_7` | decimal | Coluna «PC_NIVEL_7» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `PC_NIVEL_8` | `PC_NIVEL_8` | decimal | Coluna «PC_NIVEL_8» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2019 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `NU_ANO_SAEB` | `NU_ANO_SAEB` | inteiro | Coluna «NU_ANO_SAEB» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 a 2023 | `nivel-socioeconomico-inse-brasil`, `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados` e mais 1 |
| `SG_UF` | `SG_UF` | texto | Coluna «SG_UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 a 2023 | `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados`, `nivel-socioeconomico-inse-municipios` |
| `NO_UF` | `NO_UF` | texto | Coluna «NO_UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 a 2023 | `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-estados`, `nivel-socioeconomico-inse-municipios` |
| `NO_MUNICIPIO` | `NO_MUNICIPIO` | texto | Coluna «NO_MUNICIPIO» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2023 | `nivel-socioeconomico-inse-escolas`, `nivel-socioeconomico-inse-municipios` |
| `ID_ESCOLA` | `ID_ESCOLA` | inteiro | Coluna «ID_ESCOLA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2023 | `nivel-socioeconomico-inse-escolas` |
| `NO_ESCOLA` | `NO_ESCOLA` | texto | Coluna «NO_ESCOLA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2023 | `nivel-socioeconomico-inse-escolas` |

## No lake

- Dataset `inep/nivel-socioeconomico`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local, com o conversor atual, dos arquivos do catálogo.
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `nivel-socioeconomico-inse-2023-brasil.parquet` da edição mais recente do lake (ano 2023):

```python
import duckdb

duckdb.sql("""
    SELECT "NU_ANO_SAEB", "TP_TIPO_REDE", "TP_LOCALIZACAO"
    FROM read_parquet('lake/inep/nivel-socioeconomico/ano=2023/nivel-socioeconomico-inse-2023-brasil.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
