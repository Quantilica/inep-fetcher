---
dataset:
  id: remuneracao-docentes
  fonte: inep
  titulo: Indicadores — Remuneração dos docentes da educação básica
  resumo: Remuneração média de docentes em exercício na educação básica, por escolaridade, com dados do Censo da Educação Básica e da RAIS.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2014'
    fim: '2021'
  unidade: um recorte (Brasil, região, UF ou município; dependência e escolaridade) numa edição, com número de docentes e estatísticas de remuneração
  granularidade:
    espacial: Brasil, grande região, UF e município, conforme o arquivo
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
    Código do município: ano ou código
    Dados gerais - Número de docentes Censo Escolar: docentes
    Dados gerais - % de docentes localizados na RAIS: '%'
    Dados de remuneração dos docentes localizados na RAIS - Carga horária média semanal: horas por semana
    Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 1º quartil: R$ ou %, conforme a coluna
    Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Mediana: R$ ou %, conforme a coluna
    Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Média: R$ ou %, conforme a coluna
    Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 3º quartil: R$ ou %, conforme a coluna
    Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Desvio padrão: R$ ou %, conforme a coluna
    Dados de remuneração dos docentes localizados na RAIS - Remuneração média padronizada para 40h semanais em R$: R$ ou %, conforme a coluna
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Remuneração dos docentes da educação básica

## Resumo

Indicador do Inep com a remuneração dos docentes em exercício na educação básica por escolaridade, obtida pelo cruzamento do Censo da Educação Básica com a Relação Anual de Informações Sociais (RAIS). As planilhas trazem o número de docentes, o percentual localizado na RAIS e estatísticas da remuneração bruta.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/remuneracao-docentes` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2014 a 2021 |
| Unidade (uma linha) | um recorte (Brasil, região, UF ou município; dependência e escolaridade) numa edição, com número de docentes e estatísticas de remuneração |
| Granularidade | espacial: Brasil, grande região, UF e município, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 17 |
| Unidades de medida | `Ano`: ano ou código; `Código do município`: ano ou código; `Dados gerais - Número de docentes Censo Escolar`: docentes; `Dados gerais - % de docentes localizados na RAIS`: %; `Dados de remuneração dos docentes localizados na RAIS - Carga horária média semanal`: horas por semana; `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 1º quartil`: R$ ou %, conforme a coluna; `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Mediana`: R$ ou %, conforme a coluna; `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Média`: R$ ou %, conforme a coluna; `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 3º quartil`: R$ ou %, conforme a coluna; `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Desvio padrão`: R$ ou %, conforme a coluna; `Dados de remuneração dos docentes localizados na RAIS - Remuneração média padronizada para 40h semanais em R$`: R$ ou %, conforme a coluna |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 19 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2021/remuneracao_docentes_brasil_regioes_ufs_2021.zip`.
- No bruto, cada arquivo se chama `indicadores/remuneracao-docentes/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Fonte declarada nas planilhas: Censo da Educação Básica e Relação Anual de Informações Sociais (RAIS), ano base de cada edição.
- Nota da fonte: o número de docentes é o de docentes em exercício na educação básica registrados no Censo Escolar; o percentual localizado na RAIS conta os docentes encontrados em algum vínculo.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2014 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2015 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2016 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2017 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2018 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2019 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2020 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14) |
| 2021 | `remuneracao_docentes_brasil` (13); `remuneracao_docentes_uf` (14); `remuneracao_docentes_municipios` (16) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | todo | `remuneracao_docentes_brasil` |
| `Dependência administrativa` | `Dependência administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Escolaridade do docente` | `Escolaridade do docente` | texto | Coluna «Escolaridade do docente» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados gerais - Número de docentes Censo Escolar` | `Dados gerais - Número de docentes Censo Escolar` | inteiro | Valor de «Dados gerais» no recorte «Número de docentes Censo Escolar»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados gerais - % de docentes localizados na RAIS` | `Dados gerais - % de docentes localizados na RAIS` | decimal/texto | Valor de «Dados gerais» no recorte «% de docentes localizados na RAIS»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 1º quartil` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 1º quartil` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração Bruta em R$ › 1º quartil»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Mediana` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Mediana` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração Bruta em R$ › Mediana»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Média` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Média` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração Bruta em R$ › Média»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 3º quartil` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - 3º quartil` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração Bruta em R$ › 3º quartil»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Desvio padrão` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração Bruta em R$ - Desvio padrão` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração Bruta em R$ › Desvio padrão»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Carga horária média semanal` | `Dados de remuneração dos docentes localizados na RAIS - Carga horária média semanal` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Carga horária média semanal»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Dados de remuneração dos docentes localizados na RAIS - Remuneração média padronizada para 40h semanais em R$` | `Dados de remuneração dos docentes localizados na RAIS - Remuneração média padronizada para 40h semanais em R$` | decimal/texto | Valor de «Dados de remuneração dos docentes localizados na RAIS» no recorte «Remuneração média padronizada para 40h semanais em R$»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `remuneracao_docentes_brasil`, `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `remuneracao_docentes_municipios`, `remuneracao_docentes_uf` |
| `Código do município` | `Código do município` | inteiro | Coluna «Código do município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 | `remuneracao_docentes_municipios` |
| `Nome do município` | `Nome do município` | texto | Coluna «Nome do município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2021 | `remuneracao_docentes_municipios` |

## No lake

- Dataset `inep/remuneracao-docentes`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local, com o conversor atual, dos arquivos do catálogo.
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `remuneracao_docentes_brasil_2021.parquet` da edição mais recente do lake (ano 2021):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Abrangência", "Dependência administrativa", "Dados gerais - Número de docentes Censo Escolar"
    FROM read_parquet('lake/inep/remuneracao-docentes/ano=2021/remuneracao-docentes-remuneracao-docentes-brasil-regioes-ufs-2021__remuneracao_docentes_brasil_2021.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
