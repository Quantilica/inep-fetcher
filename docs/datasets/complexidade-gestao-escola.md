---
dataset:
  id: complexidade-gestao-escola
  fonte: inep
  titulo: Indicadores — Complexidade de gestão da escola
  resumo: Percentual de escolas por nível do Indicador de Complexidade de Gestão da Escola (níveis 1 a 6), por recorte geográfico, localização e dependência.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2016'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição, com o percentual de escolas por nível
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
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
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Nível 1: '%'
    Nível 2: '%'
    Nível 3: '%'
    Nível 4: '%'
    Nível 5: '%'
    Nível 6: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Complexidade de gestão da escola

## Resumo

O Indicador de Complexidade de Gestão da Escola (ICG) do Inep classifica as escolas de educação básica em níveis de 1 a 6; níveis elevados indicam maior complexidade de gestão. As planilhas trazem o percentual de escolas em cada nível, por recorte.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/complexidade-gestao-escola` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2016 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e dependência) numa edição, com o percentual de escolas por nível |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 19 |
| Unidades de medida | `Ano`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Nível 1`: %; `Nível 2`: %; `Nível 3`: %; `Nível 4`: %; `Nível 5`: %; `Nível 6`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 39 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/ICG_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/complexidade-gestao-escola/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Percentual de escolas por nível do Indicador de complexidade de gestão da escola".
- Nota da fonte: o indicador classifica as escolas em níveis de 1 a 6 conforme a complexidade de gestão, a partir de características das escolas no Censo da Educação Básica (a lista completa está na nota da planilha).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2016 | `icg_brasil` (10); `icg_regioes` (10); `icg_ufs` (11) |
| 2017 | `icg_brasil_regioes_ufs` (10) |
| 2018 | `icg_brasil_regioes_ufs` (10) |
| 2019 | `icg_brasil_regioes_ufs` (10) |
| 2020 | `icg_brasil_regioes_ufs` (10) |
| 2021 | `icg_brasil_regioes_ufs` (10) |
| 2022 | `icg_brasil_regioes_ufs` (10) |
| 2023 | `icg_brasil_regioes_ufs` (10) |
| 2024 | `icg_brasil_regioes_ufs` (10) |
| 2025 | `icg_brasil_regioes_ufs` (10); `icg_escolas` (10); `icg_municipios` (13) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_escolas` e mais 3 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2016 | `icg_brasil`, `icg_regioes` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_escolas` e mais 3 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_escolas` e mais 3 |
| `Nível 1` | `Nível 1` | decimal | Coluna «Nível 1» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Nível 2` | `Nível 2` | decimal | Coluna «Nível 2» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Nível 3` | `Nível 3` | decimal | Coluna «Nível 3» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Nível 4` | `Nível 4` | decimal | Coluna «Nível 4» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Nível 5` | `Nível 5` | decimal | Coluna «Nível 5» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Nível 6` | `Nível 6` | decimal | Coluna «Nível 6» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `icg_brasil`, `icg_brasil_regioes_ufs`, `icg_municipios` e mais 2 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `icg_escolas`, `icg_municipios`, `icg_ufs` |
| `Unidade da Federação` | `Unidade da Federação` | texto | Coluna «Unidade da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2016 | `icg_ufs` |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `icg_brasil_regioes_ufs` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas`, `icg_municipios` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas`, `icg_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas`, `icg_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas` |
| `Nível de complexidade de gestão da escola` | `Nível de complexidade de gestão da escola` | texto | Coluna «Nível de complexidade de gestão da escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `icg_escolas` |

## No lake

- Dataset `inep/complexidade-gestao-escola`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `icg_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Nível 1"
    FROM read_parquet('lake/inep/complexidade-gestao-escola/ano=2025/complexidade-gestao-escola-icg-2025-brasil-regioes-ufs__icg_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
