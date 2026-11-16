---
dataset:
  id: regularidade-corpo-docente
  fonte: inep
  titulo: Indicadores — Regularidade do corpo docente
  resumo: Distribuição das escolas por faixa do Indicador de Regularidade do Docente (IRD), por recorte geográfico, localização e dependência.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2013'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola) numa edição, com a distribuição de escolas por faixa do IRD
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 17
  unidades_de_medida:
    Ano: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Baixa regularidade (0-/2): '%'
    Média-baixa (2-/3): '%'
    Média-alta (3-/4): '%'
    Alta (4-/5): '%'
    Média do Indicador de Regularidade do Docente (IRD): '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Regularidade do corpo docente

## Resumo

O Indicador de Regularidade do Docente (IRD) do Inep avalia a regularidade do corpo docente das escolas pela permanência dos professores nas escolas nos últimos cinco anos. As planilhas trazem a distribuição das escolas por faixa do indicador.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/regularidade-corpo-docente` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2013 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola) numa edição, com a distribuição de escolas por faixa do IRD |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 17 |
| Unidades de medida | `Ano`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Baixa regularidade (0-/2)`: %; `Média-baixa (2-/3)`: %; `Média-alta (3-/4)`: %; `Alta (4-/5)`: %; `Média do Indicador de Regularidade do Docente (IRD)`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 39 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/IRD_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/regularidade-corpo-docente/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Distribuição das escolas segundo faixa do Indicador de Regularidade do Docente (IRD)".
- Nota da fonte: o indicador avalia a regularidade do corpo docente a partir da permanência dos professores nas escolas nos últimos cinco anos; a pontuação por docente está descrita na nota da planilha.
- As colunas são as faixas do indicador, por exemplo `Baixa regularidade (0-2)` (no lake, com `/` no lugar de `|`).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2013 | `ird_brasil` (8); `ird_regioes` (8); `ird_ufs` (9) |
| 2014 | `ird_brasil` (8); `ird_regioes` (8); `ird_ufs` (9) |
| 2015 | `ird_brasil` (8); `ird_regioes` (8); `ird_ufs` (9) |
| 2016 | `ird_brasil` (8); `ird_regioes` (8); `ird_ufs` (9) |
| 2017 | `ird_brasil_regioes_ufs` (8) |
| 2018 | `ird_brasil_regioes_ufs` (8) |
| 2019 | `ird_brasil_regioes_ufs` (8) |
| 2020 | `ird_brasil_regioes_ufs` (8) |
| 2021 | `ird_brasil_regioes_ufs` (8) |
| 2022 | `ird_brasil_regioes_ufs` (8) |
| 2023 | `ird_brasil_regioes_ufs` (8) |
| 2024 | `ird_brasil_regioes_ufs` (8) |
| 2025 | `ird_brasil_regioes_ufs` (8); `ird_escolas` (10); `ird_municipios` (11) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_escolas` e mais 3 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2013 a 2016 | `ird_brasil`, `ird_regioes` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_escolas` e mais 3 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_escolas` e mais 3 |
| `Baixa regularidade (0-/2)` | `Baixa regularidade (0-/2)` | decimal | Coluna «Baixa regularidade (0-/2)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_municipios` e mais 2 |
| `Média-baixa (2-/3)` | `Média-baixa (2-/3)` | decimal | Coluna «Média-baixa (2-/3)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_municipios` e mais 2 |
| `Média-alta (3-/4)` | `Média-alta (3-/4)` | decimal | Coluna «Média-alta (3-/4)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_municipios` e mais 2 |
| `Alta (4-/5)` | `Alta (4-/5)` | decimal | Coluna «Alta (4-/5)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `ird_brasil`, `ird_brasil_regioes_ufs`, `ird_municipios` e mais 2 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `ird_escolas`, `ird_municipios`, `ird_ufs` |
| `Unidades da Federação` | `Unidades da Federação` | texto | Coluna «Unidades da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2013 a 2016 | `ird_ufs` |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `ird_brasil_regioes_ufs` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas`, `ird_municipios` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas`, `ird_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas`, `ird_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas` |
| `Média do Indicador de Regularidade do Docente (IRD)` | `Média do Indicador de Regularidade do Docente (IRD)` | decimal | Coluna «Média do Indicador de Regularidade do Docente (IRD)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ird_escolas` |

## No lake

- Dataset `inep/regularidade-corpo-docente`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `ird_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Baixa regularidade (0-|2)"
    FROM read_parquet('lake/inep/regularidade-corpo-docente/ano=2025/regularidade-corpo-docente-ird-2025-brasil-regioes-ufs__ird_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
