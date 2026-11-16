---
dataset:
  id: esforco-docente
  fonte: inep
  titulo: Indicadores — Esforço docente
  resumo: Percentual de docentes por nível do Indicador de Esforço Docente (níveis 1 a 6), por etapa e recorte geográfico.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2013'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola) numa edição, com o percentual de docentes por etapa e nível
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 37
  unidades_de_medida:
    Ano: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Ensino Fundamental - Total - Nível 1: '%'
    Ensino Fundamental - Total - Nível 2: '%'
    Ensino Fundamental - Total - Nível 3: '%'
    Ensino Fundamental - Total - Nível 4: '%'
    Ensino Fundamental - Total - Nível 5: '%'
    Ensino Fundamental - Total - Nível 6: '%'
    Ensino Fundamental - Anos Iniciais - Nível 1: '%'
    Ensino Fundamental - Anos Iniciais - Nível 2: '%'
    Ensino Fundamental - Anos Iniciais - Nível 3: '%'
    Ensino Fundamental - Anos Iniciais - Nível 4: '%'
    Ensino Fundamental - Anos Iniciais - Nível 5: '%'
    Ensino Fundamental - Anos Iniciais - Nível 6: '%'
    Ensino Fundamental - Anos Finais - Nível 1: '%'
    Ensino Fundamental - Anos Finais - Nível 2: '%'
    Ensino Fundamental - Anos Finais - Nível 3: '%'
    Ensino Fundamental - Anos Finais - Nível 4: '%'
    Ensino Fundamental - Anos Finais - Nível 5: '%'
    Ensino Fundamental - Anos Finais - Nível 6: '%'
    Ensino Médio - Nível 1: '%'
    Ensino Médio - Nível 2: '%'
    Ensino Médio - Nível 3: '%'
    Ensino Médio - Nível 4: '%'
    Ensino Médio - Nível 5: '%'
    Ensino Médio - Nível 6: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Esforço docente

## Resumo

O Indicador de Esforço Docente (IED) do Inep classifica os docentes em níveis de 1 a 6 conforme o esforço empreendido no exercício da profissão; níveis elevados indicam maior esforço. As planilhas trazem o percentual de docentes por nível e etapa.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/esforco-docente` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2013 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola) numa edição, com o percentual de docentes por etapa e nível |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 37 |
| Unidades de medida | `Ano`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Ensino Fundamental - Total - Nível 1`: %; `Ensino Fundamental - Total - Nível 2`: %; `Ensino Fundamental - Total - Nível 3`: %; `Ensino Fundamental - Total - Nível 4`: %; `Ensino Fundamental - Total - Nível 5`: %; `Ensino Fundamental - Total - Nível 6`: %; `Ensino Fundamental - Anos Iniciais - Nível 1`: %; `Ensino Fundamental - Anos Iniciais - Nível 2`: %; `Ensino Fundamental - Anos Iniciais - Nível 3`: %; `Ensino Fundamental - Anos Iniciais - Nível 4`: %; `Ensino Fundamental - Anos Iniciais - Nível 5`: %; `Ensino Fundamental - Anos Iniciais - Nível 6`: %; `Ensino Fundamental - Anos Finais - Nível 1`: %; `Ensino Fundamental - Anos Finais - Nível 2`: %; `Ensino Fundamental - Anos Finais - Nível 3`: %; `Ensino Fundamental - Anos Finais - Nível 4`: %; `Ensino Fundamental - Anos Finais - Nível 5`: %; `Ensino Fundamental - Anos Finais - Nível 6`: %; `Ensino Médio - Nível 1`: %; `Ensino Médio - Nível 2`: %; `Ensino Médio - Nível 3`: %; `Ensino Médio - Nível 4`: %; `Ensino Médio - Nível 5`: %; `Ensino Médio - Nível 6`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 39 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/IED_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/esforco-docente/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Percentual de docentes por níveis do indicador de esforço docente".
- Nota da fonte: o indicador classifica o docente em níveis de 1 a 6 de acordo com o esforço no exercício da profissão, a partir de características dos dados do Censo da Educação Básica (detalhadas na nota da planilha).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2013 | `ied_brasil` (28); `ied_regioes` (28); `ied_ufs` (29) |
| 2014 | `ied_brasil` (28); `ied_regioes` (28); `ied_ufs` (29) |
| 2015 | `ied_brasil` (28); `ied_regioes` (28); `ied_ufs` (29) |
| 2016 | `ied_brasil` (28); `ied_regioes` (28); `ied_ufs` (29) |
| 2017 | `ied_brasil_regioes_ufs` (28) |
| 2018 | `ied_brasil_regioes_ufs` (28) |
| 2019 | `ied_brasil_regioes_ufs` (28) |
| 2020 | `ied_brasil_regioes_ufs` (28) |
| 2021 | `ied_brasil_regioes_ufs` (28) |
| 2022 | `ied_brasil_regioes_ufs` (28) |
| 2023 | `ied_brasil_regioes_ufs` (28) |
| 2024 | `ied_brasil_regioes_ufs` (28) |
| 2025 | `ied_brasil_regioes_ufs` (28); `ied_escolas` (33); `ied_municipios` (31) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2013 a 2016 | `ied_brasil`, `ied_regioes` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 1` | `Ensino Fundamental - Total - Nível 1` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 2` | `Ensino Fundamental - Total - Nível 2` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 3` | `Ensino Fundamental - Total - Nível 3` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 4` | `Ensino Fundamental - Total - Nível 4` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 5` | `Ensino Fundamental - Total - Nível 5` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Total - Nível 6` | `Ensino Fundamental - Total - Nível 6` | decimal | Valor de «Ensino Fundamental» no recorte «Total › Nível 6»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 1` | `Ensino Fundamental - Anos Iniciais - Nível 1` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 2` | `Ensino Fundamental - Anos Iniciais - Nível 2` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 3` | `Ensino Fundamental - Anos Iniciais - Nível 3` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 4` | `Ensino Fundamental - Anos Iniciais - Nível 4` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 5` | `Ensino Fundamental - Anos Iniciais - Nível 5` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Iniciais - Nível 6` | `Ensino Fundamental - Anos Iniciais - Nível 6` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais › Nível 6»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 1` | `Ensino Fundamental - Anos Finais - Nível 1` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 2` | `Ensino Fundamental - Anos Finais - Nível 2` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 3` | `Ensino Fundamental - Anos Finais - Nível 3` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 4` | `Ensino Fundamental - Anos Finais - Nível 4` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 5` | `Ensino Fundamental - Anos Finais - Nível 5` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Fundamental - Anos Finais - Nível 6` | `Ensino Fundamental - Anos Finais - Nível 6` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais › Nível 6»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 1` | `Ensino Médio - Nível 1` | decimal | Valor de «Ensino Médio» no recorte «Nível 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 2` | `Ensino Médio - Nível 2` | decimal | Valor de «Ensino Médio» no recorte «Nível 2»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 3` | `Ensino Médio - Nível 3` | decimal | Valor de «Ensino Médio» no recorte «Nível 3»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 4` | `Ensino Médio - Nível 4` | decimal | Valor de «Ensino Médio» no recorte «Nível 4»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 5` | `Ensino Médio - Nível 5` | decimal | Valor de «Ensino Médio» no recorte «Nível 5»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Ensino Médio - Nível 6` | `Ensino Médio - Nível 6` | decimal | Valor de «Ensino Médio» no recorte «Nível 6»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `ied_brasil`, `ied_brasil_regioes_ufs`, `ied_escolas` e mais 3 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `ied_escolas`, `ied_municipios`, `ied_ufs` |
| `Unidade da Federação` | `Unidade da Federação` | texto | Coluna «Unidade da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2013 a 2016 | `ied_ufs` |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `ied_brasil_regioes_ufs` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_escolas` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_escolas`, `ied_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_escolas`, `ied_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_escolas` |
| `Sigla` | `Sigla` | texto | Coluna «Sigla» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `ied_municipios` |

## No lake

- Dataset `inep/esforco-docente`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `ied_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Ensino Fundamental - Total - Nível 1"
    FROM read_parquet('lake/inep/esforco-docente/ano=2025/esforco-docente-ied-2025-brasil-regioes-ufs__ied_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
