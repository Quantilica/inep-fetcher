---
dataset:
  id: docentes-curso-superior
  fonte: inep
  titulo: Indicadores — Percentual de docentes com curso superior
  resumo: Percentual de docentes com curso superior na educação básica, por etapa, recorte geográfico, localização e rede.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2011'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com o percentual de docentes com curso superior por etapa
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 26
  unidades_de_medida:
    Ano: ano ou código
    Código da UF: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Educação Infantil - Total: '%'
    Educação Infantil - Creche: '%'
    Educação Infantil - Pré-Escola: '%'
    Ensino Fundamental - Total: '%'
    Ensino Fundamental - Anos Iniciais: '%'
    Ensino Fundamental - Anos Finais: '%'
    Ensino Médio: '%'
    Educação Profissional: '%'
    EJA: '%'
    Educação Especial: '%'
    Educação de Jovens e Adultos (EJA): '%'
    Educação de Jovens e Adultos (EJA - Ensino Fundamental): '%'
    Educação de Jovens e Adultos (EJA - Ensino Médio): '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Percentual de docentes com curso superior

## Resumo

Indicador do Inep com o percentual de docentes com curso superior, calculado a partir do Censo da Educação Básica, por etapa de ensino, recorte geográfico, localização e rede.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/docentes-curso-superior` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2011 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com o percentual de docentes com curso superior por etapa |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 26 |
| Unidades de medida | `Ano`: ano ou código; `Código da UF`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Educação Infantil - Total`: %; `Educação Infantil - Creche`: %; `Educação Infantil - Pré-Escola`: %; `Ensino Fundamental - Total`: %; `Ensino Fundamental - Anos Iniciais`: %; `Ensino Fundamental - Anos Finais`: %; `Ensino Médio`: %; `Educação Profissional`: %; `EJA`: %; `Educação Especial`: %; `Educação de Jovens e Adultos (EJA)`: %; `Educação de Jovens e Adultos (EJA - Ensino Fundamental)`: %; `Educação de Jovens e Adultos (EJA - Ensino Médio)`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 45 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/DSU_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/docentes-curso-superior/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Percentual de Docentes com Curso Superior".
- Colunas por etapa: Educação Infantil (total, creche, pré-escola), Ensino Fundamental (total, anos iniciais e finais), Ensino Médio, Educação Profissional, conforme o cabeçalho.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2011 | `dsu_brasil` (14); `dsu_estados` (16); `dsu_regies` (14) |
| 2012 | `dsu_brasil` (14); `dsu_estados` (16); `dsu_regies` (14) |
| 2013 | `dsu_brasil` (14); `dsu_estados` (16); `dsu_regies` (14) |
| 2014 | `dsu_brasil` (14); `dsu_regies` (14); `dsu_ufs` (16) |
| 2015 | `dsu_brasil` (14); `dsu_regioes` (14); `dsu_uf` (16) |
| 2016 | `dsu_brasil` (14); `dsu_regioes` (14); `dsu_ufs` (15) |
| 2017 | `dsu_brasil_regioes_ufs` (14) |
| 2018 | `dsu_brasil_regioes_ufs_atualizado` (14) |
| 2019 | `dsu_brasil_regioes_ufs` (14) |
| 2020 | `dsu_brasil_regioes_ufs` (14) |
| 2021 | `dsu_brasil_regioes_ufs` (14) |
| 2022 | `dsu_brasil_regioes_ufs` (14) |
| 2023 | `dsu_brasil_regioes_ufs` (14) |
| 2024 | `dsu_brasil_regioes_ufs` (14) |
| 2025 | `dsu_brasil_regioes_ufs` (14); `dsu_escolas` (19); `dsu_municipios` (17) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2011 a 2016 | `dsu_brasil` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Rede` | `Rede` | texto | Rede de ensino da escola (pública, privada ou total), conforme a planilha. | — | 2011 a 2015 | `dsu_brasil`, `dsu_estados`, `dsu_regies` e mais 3 |
| `Educação Infantil - Total` | `Educação Infantil - Total` | decimal | Valor de «Educação Infantil» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Educação Infantil - Creche` | `Educação Infantil - Creche` | decimal | Valor de «Educação Infantil» no recorte «Creche»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Educação Infantil - Pré-Escola` | `Educação Infantil - Pré-Escola` | decimal | Valor de «Educação Infantil» no recorte «Pré-Escola»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Ensino Fundamental - Total` | `Ensino Fundamental - Total` | decimal | Valor de «Ensino Fundamental» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Ensino Fundamental - Anos Iniciais` | `Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Ensino Fundamental - Anos Finais` | `Ensino Fundamental - Anos Finais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Ensino Médio` | `Ensino Médio` | decimal | Coluna «Ensino Médio» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 7 |
| `Educação Profissional` | `Educação Profissional` | decimal | Coluna «Educação Profissional» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2011 a 2024 | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 5 |
| `EJA` | `EJA` | decimal | Coluna «EJA» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2011 a 2014 | `dsu_brasil`, `dsu_estados`, `dsu_regies` e mais 1 |
| `Educação Especial` | `Educação Especial` | decimal | Coluna «Educação Especial» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2011 a 2024 | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 5 |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `dsu_escolas`, `dsu_estados`, `dsu_municipios` e mais 4 |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `dsu_escolas`, `dsu_estados`, `dsu_municipios` e mais 2 |
| `Código da UF` | `Código da UF` | inteiro | Coluna «Código da UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2011 a 2015 | `dsu_estados`, `dsu_uf`, `dsu_ufs` |
| `Educação de Jovens e Adultos (EJA)` | `Educação de Jovens e Adultos (EJA)` | decimal | Coluna «Educação de Jovens e Adultos (EJA)» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2015 a 2025 | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 5 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | 2016 a 2025 | `dsu_brasil`, `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` e mais 4 |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `dsu_brasil_regioes_ufs`, `dsu_brasil_regioes_ufs_atualizado` |
| `Educação de Jovens e Adultos (EJA - Ensino Fundamental)` | `Educação de Jovens e Adultos (EJA - Ensino Fundamental)` | decimal | Valor de «Educação de Jovens e Adultos (EJA» no recorte «Ensino Fundamental)»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2025 | `dsu_brasil_regioes_ufs`, `dsu_escolas`, `dsu_municipios` |
| `Educação de Jovens e Adultos (EJA - Ensino Médio)` | `Educação de Jovens e Adultos (EJA - Ensino Médio)` | decimal | Valor de «Educação de Jovens e Adultos (EJA» no recorte «Ensino Médio)»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2025 | `dsu_brasil_regioes_ufs`, `dsu_escolas`, `dsu_municipios` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `dsu_escolas`, `dsu_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `dsu_escolas`, `dsu_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `dsu_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `dsu_escolas` |

## No lake

- Dataset `inep/docentes-curso-superior`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `dsu_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Educação Infantil - Total"
    FROM read_parquet('lake/inep/docentes-curso-superior/ano=2025/docentes-curso-superior-dsu-2025-brasil-regioes-ufs__dsu_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
