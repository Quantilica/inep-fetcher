---
dataset:
  id: docentes-pos-graduacao
  fonte: inep
  titulo: Indicadores — Docentes com pós-graduação stricto sensu (educação superior)
  resumo: Percentual de docentes em exercício na educação superior com pós-graduação stricto sensu, por recorte, categoria, organização, grau, modalidade e área do curso.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano do Censo da Educação Superior
  cobertura:
    inicio: '2010'
    fim: '2024'
  unidade: um recorte (unidade geográfica ou instituição; categoria, organização, grau, modalidade, área) numa edição, com o percentual de docentes com pós-graduação stricto sensu
  granularidade:
    espacial: Brasil, UF, município e instituição, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 19
  unidades_de_medida:
    Ano: ano ou código
    Cógido da Instituição: ano ou código
    Código do Município: ano ou código
    Percentual de Docentes com Pós-Graduação Stricto Sensu - Total: '%'
    Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Mestrado: '%'
    Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Doutorado: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Docentes com pós-graduação stricto sensu (educação superior)

## Resumo

Indicador do Inep com o percentual de docentes em exercício com pós-graduação stricto sensu (mestrado e doutorado), calculado a partir do Censo da Educação Superior, para Brasil, UFs, instituições e outros recortes.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/docentes-pos-graduacao` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano do Censo da Educação Superior |
| Cobertura | 2010 a 2024 |
| Unidade (uma linha) | um recorte (unidade geográfica ou instituição; categoria, organização, grau, modalidade, área) numa edição, com o percentual de docentes com pós-graduação stricto sensu |
| Granularidade | espacial: Brasil, UF, município e instituição, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 19 |
| Unidades de medida | `Ano`: ano ou código; `Cógido da Instituição`: ano ou código; `Código do Município`: ano ou código; `Percentual de Docentes com Pós-Graduação Stricto Sensu - Total`: %; `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Mestrado`: %; `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Doutorado`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 15 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/dados_abertos/indicadores_educacionais/percentual_de_docentes_com_pos_graduacao_stricto_sensu/percentual_docente_2024.zip`.
- No bruto, cada arquivo se chama `indicadores/docentes-pos-graduacao/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Percentual de Docentes em Exercício com Pós-Graduação Stricto Sensu".
- Colunas: total e por grau de formação (mestrado e doutorado), por categoria administrativa, organização acadêmica, grau acadêmico, modalidade e área geral do curso (Cine Brasil).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2010 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2011 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2012 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2013 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2014 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2015 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2016 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2017 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2018 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2019 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2020 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2021 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2022 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2023 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |
| 2024 | `perc_docentes_brasil` (10); `perc_docentes_ies` (11); `perc_docentes_municipio` (12); `perc_docentes_regiao_uf` (9) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | todo | `perc_docentes_brasil` |
| `Categoria Administrativa` | `Categoria Administrativa` | texto | Coluna «Categoria Administrativa» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Organização Acadêmica` | `Organização Acadêmica` | texto | Coluna «Organização Acadêmica» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Grau Acadêmico` | `Grau Acadêmico` | texto | Coluna «Grau Acadêmico» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_municipio`, `perc_docentes_regiao_uf` |
| `Modalidade de Ensino` | `Modalidade de Ensino` | texto | Coluna «Modalidade de Ensino» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_brasil` |
| `Área Geral do Curso (Cine Brasil)` | `Área Geral do Curso (Cine Brasil)` | texto | Coluna «Área Geral do Curso (Cine Brasil)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_municipio`, `perc_docentes_regiao_uf` |
| `Percentual de Docentes com Pós-Graduação Stricto Sensu - Total` | `Percentual de Docentes com Pós-Graduação Stricto Sensu - Total` | decimal | Valor de «Percentual de Docentes com Pós-Graduação Stricto Sensu» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Mestrado` | `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Mestrado` | decimal | Valor de «Percentual de Docentes com Pós-Graduação Stricto Sensu» no recorte «Grau de Formação › Mestrado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Doutorado` | `Percentual de Docentes com Pós-Graduação Stricto Sensu - Grau de Formação - Doutorado` | decimal | Valor de «Percentual de Docentes com Pós-Graduação Stricto Sensu» no recorte «Grau de Formação › Doutorado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `perc_docentes_brasil`, `perc_docentes_ies`, `perc_docentes_municipio` e mais 1 |
| `Cógido da Instituição` | `Cógido da Instituição` | inteiro | Coluna «Cógido da Instituição» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_ies` |
| `Nome da Instituição` | `Nome da Instituição` | texto | Coluna «Nome da Instituição» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_ies` |
| `Sigla da Instituição` | `Sigla da Instituição` | texto | Coluna «Sigla da Instituição» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_ies` |
| `Região Geográfica` | `Região Geográfica` | texto | Coluna «Região Geográfica» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_ies`, `perc_docentes_regiao_uf` |
| `Unidade da Federação` | `Unidade da Federação` | texto | Coluna «Unidade da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_ies` |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `perc_docentes_municipio` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_municipio` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_municipio` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `perc_docentes_municipio` |

## No lake

- Dataset `inep/docentes-pos-graduacao`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local, com o conversor atual, dos arquivos do catálogo.
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `perc_docentes_brasil_2024.parquet` da edição mais recente do lake (ano 2024):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Categoria Administrativa", "Percentual de Docentes com Pós-Graduação Stricto Sensu - Total"
    FROM read_parquet('lake/inep/docentes-pos-graduacao/ano=2024/docentes-pos-graduacao-percentual-docente-2024__perc_docentes_brasil_2024.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
