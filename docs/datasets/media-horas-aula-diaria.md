---
dataset:
  id: media-horas-aula-diaria
  fonte: inep
  titulo: Indicadores — Média de horas-aula diária
  resumo: Média de horas-aula diária por etapa, por recorte geográfico, localização e rede.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; uma edição por ano de referência do Censo da Educação Básica
  cobertura:
    inicio: '2010'
    fim: '2025'
  unidade: um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com a média de horas-aula diária por etapa
  granularidade:
    espacial: Brasil, grande região, UF, município e escola, conforme o arquivo
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 81
  unidades_de_medida:
    Ano: ano ou código
    Código da UF: ano ou código
    Código do Município: ano ou código
    Código da Escola: ano ou código
    Hora-aula diária média - Educação Infantil - Creche: horas-aula por dia
    Hora-aula diária média - Educação Infantil - Pré-Escola: horas-aula por dia
    Hora-aula diária média - Educação Infantil - Total Ed. Infantil: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª Série/ - 2º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2ª Série/ - 3º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3ª Série/ - 4º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4ª Série/ - 5º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª Série/ - 6º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6ª Série/ - 7º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7ª Série/ - 8º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8ª Série/ - 9º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - TOTAL FUNDAMENTAL 8 E 9 ANOS: horas-aula por dia
    Hora-aula diária média - Ensino Médio - 1ª Série Médio: horas-aula por dia
    Hora-aula diária média - Ensino Médio - 2ª Série Médio: horas-aula por dia
    Hora-aula diária média - Ensino Médio - 3ª Série Médio: horas-aula por dia
    Hora-aula diária média - Ensino Médio - 4ª Série Médio: horas-aula por dia
    Hora-aula diária média - Ensino Médio - Médio Não-Seriado: horas-aula por dia
    Hora-aula diária média - Ensino Médio - Total Médio: horas-aula por dia
    Hora-aula diária média - Educação Infantil - Total: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - Total: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º ao 5º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º ao 9º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 9º Ano: horas-aula por dia
    Hora-aula diária média - Ensino Médio - Total: horas-aula por dia
    Educação Infantil - Total: horas-aula por dia
    Educação Infantil - Creche: horas-aula por dia
    Educação Infantil - Pré-Escola: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - Total: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - Anos Iniciais: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - Anos Finais: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 1º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 2º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 3º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 4º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 5º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 6º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 7º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 8º Ano: horas-aula por dia
    Ensino Fundamental 8 e 9 anos - 9º Ano: horas-aula por dia
    Ensino Médio - Total: horas-aula por dia
    Ensino Médio - 1ª Série: horas-aula por dia
    Ensino Médio - 2ª Série: horas-aula por dia
    Ensino Médio - 3ª Série: horas-aula por dia
    Ensino Médio - 4ª Série: horas-aula por dia
    Ensino Médio - Não-Seriado: horas-aula por dia
    Ensino Fundamental - Total: horas-aula por dia
    Ensino Fundamental - Anos Iniciais: horas-aula por dia
    Ensino Fundamental - Anos Finais: horas-aula por dia
    Ensino Fundamental - 1º Ano: horas-aula por dia
    Ensino Fundamental - 2º Ano: horas-aula por dia
    Ensino Fundamental - 3º Ano: horas-aula por dia
    Ensino Fundamental - 4º Ano: horas-aula por dia
    Ensino Fundamental - 5º Ano: horas-aula por dia
    Ensino Fundamental - 6º Ano: horas-aula por dia
    Ensino Fundamental - 7º Ano: horas-aula por dia
    Ensino Fundamental - 8º Ano: horas-aula por dia
    Ensino Fundamental - 9º Ano: horas-aula por dia
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Média de horas-aula diária

## Resumo

Indicador do Inep com a média de horas-aula diária, calculada a partir do Censo da Educação Básica por etapa de ensino. As planilhas trazem a média por recorte geográfico, localização e rede.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/media-horas-aula-diaria` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; uma edição por ano de referência do Censo da Educação Básica |
| Cobertura | 2010 a 2025 |
| Unidade (uma linha) | um recorte (Brasil, região, UF, município ou escola; localização e rede) numa edição, com a média de horas-aula diária por etapa |
| Granularidade | espacial: Brasil, grande região, UF, município e escola, conforme o arquivo; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 81 |
| Unidades de medida | `Ano`: ano ou código; `Código da UF`: ano ou código; `Código do Município`: ano ou código; `Código da Escola`: ano ou código; `Hora-aula diária média - Educação Infantil - Creche`: horas-aula por dia; `Hora-aula diária média - Educação Infantil - Pré-Escola`: horas-aula por dia; `Hora-aula diária média - Educação Infantil - Total Ed. Infantil`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª Série/ - 2º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2ª Série/ - 3º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3ª Série/ - 4º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4ª Série/ - 5º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª Série/ - 6º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6ª Série/ - 7º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7ª Série/ - 8º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8ª Série/ - 9º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - TOTAL FUNDAMENTAL 8 E 9 ANOS`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - 1ª Série Médio`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - 2ª Série Médio`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - 3ª Série Médio`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - 4ª Série Médio`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - Médio Não-Seriado`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - Total Médio`: horas-aula por dia; `Hora-aula diária média - Educação Infantil - Total`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - Total`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º ao 5º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º ao 9º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 9º Ano`: horas-aula por dia; `Hora-aula diária média - Ensino Médio - Total`: horas-aula por dia; `Educação Infantil - Total`: horas-aula por dia; `Educação Infantil - Creche`: horas-aula por dia; `Educação Infantil - Pré-Escola`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - Total`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - Anos Iniciais`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - Anos Finais`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 1º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 2º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 3º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 4º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 5º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 6º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 7º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 8º Ano`: horas-aula por dia; `Ensino Fundamental 8 e 9 anos - 9º Ano`: horas-aula por dia; `Ensino Médio - Total`: horas-aula por dia; `Ensino Médio - 1ª Série`: horas-aula por dia; `Ensino Médio - 2ª Série`: horas-aula por dia; `Ensino Médio - 3ª Série`: horas-aula por dia; `Ensino Médio - 4ª Série`: horas-aula por dia; `Ensino Médio - Não-Seriado`: horas-aula por dia; `Ensino Fundamental - Total`: horas-aula por dia; `Ensino Fundamental - Anos Iniciais`: horas-aula por dia; `Ensino Fundamental - Anos Finais`: horas-aula por dia; `Ensino Fundamental - 1º Ano`: horas-aula por dia; `Ensino Fundamental - 2º Ano`: horas-aula por dia; `Ensino Fundamental - 3º Ano`: horas-aula por dia; `Ensino Fundamental - 4º Ano`: horas-aula por dia; `Ensino Fundamental - 5º Ano`: horas-aula por dia; `Ensino Fundamental - 6º Ano`: horas-aula por dia; `Ensino Fundamental - 7º Ano`: horas-aula por dia; `Ensino Fundamental - 8º Ano`: horas-aula por dia; `Ensino Fundamental - 9º Ano`: horas-aula por dia |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 48 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/HAD_2025_BRASIL_REGIOES_UFS.zip`.
- No bruto, cada arquivo se chama `indicadores/media-horas-aula-diaria/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Média de Horas-Aula Diária".
- Nota da fonte: só entram as turmas de escolarização na modalidade regular.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2010 | `media_horas_aula_brasil` (25); `media_horas_aula_regies` (25); `media_horas_aula_ufs` (27) |
| 2011 | `horas_aula_brasil` (25); `horas_aula_regioes` (25); `horas_aula_ufs` (27) |
| 2012 | `horas_aula_brasil` (25); `horas_aula_regioes` (25); `horas_aula_ufs` (27) |
| 2013 | `media_horas_aula_brasil` (25); `media_horas_aula_regies` (25); `media_horas_aula_ufs` (27) |
| 2014 | `media_horas_aula_brasil` (25); `media_horas_aula_regies` (25); `media_horas_aula_ufs` (27) |
| 2015 | `had_brasil` (25); `had_regioes` (25); `had_uf` (27) |
| 2016 | `had_brasil` (25); `had_regioes` (25); `had_ufs` (26) |
| 2017 | `had_brasil_regioes_ufs` (25) |
| 2018 | `had_brasil_regioes_ufs` (25) |
| 2019 | `had_brasil_regioes_ufs` (25) |
| 2020 | `had_brasil_regioes_ufs` (25) |
| 2021 | `had_brasil_regioes_ufs` (25) |
| 2022 | `had_brasil_regioes_ufs` (25) |
| 2023 | `had_brasil_regioes_ufs` (25) |
| 2024 | `had_brasil_regioes_ufs` (25) |
| 2025 | `had_brasil_regioes_ufs` (25); `had_escolas` (29); `had_municipios` (27) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | inteiro | Ano de referência do arquivo: o ano do nome do arquivo de origem (nos arquivos que cobrem um período, o primeiro ano). | — | todo | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 10 |
| `Abrangência` | `Abrangência` | texto | Abrangência geográfica da linha: Brasil, grande região ou UF (nos arquivos de Brasil, regiões e UFs). | — | 2010 a 2016 | `had_brasil`, `horas_aula_brasil`, `media_horas_aula_brasil` |
| `Localização` | `Localização` | texto | Localização da escola (urbana, rural ou total), conforme a planilha. | — | todo | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 10 |
| `Rede` | `Rede` | texto | Rede de ensino da escola (pública, privada ou total), conforme a planilha. | — | 2010 a 2015 | `had_brasil`, `had_regioes`, `had_uf` e mais 6 |
| `Hora-aula diária média - Educação Infantil - Creche` | `Hora-aula diária média - Educação Infantil - Creche` | decimal | Valor de «Hora-aula diária média» no recorte «Educação Infantil › Creche»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Educação Infantil - Pré-Escola` | `Hora-aula diária média - Educação Infantil - Pré-Escola` | decimal | Valor de «Hora-aula diária média» no recorte «Educação Infantil › Pré-Escola»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Educação Infantil - Total Ed. Infantil` | `Hora-aula diária média - Educação Infantil - Total Ed. Infantil` | decimal | Valor de «Hora-aula diária média» no recorte «Educação Infantil › Total Ed. Infantil»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª Série/ - 2º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª Série/ - 2º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 1ª Série/ › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2ª Série/ - 3º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2ª Série/ - 3º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 2ª Série/ › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3ª Série/ - 4º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3ª Série/ - 4º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 3ª Série/ › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4ª Série/ - 5º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4ª Série/ - 5º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 4ª Série/ › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª Série/ - 6º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª Série/ - 6º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 5ª Série/ › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6ª Série/ - 7º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6ª Série/ - 7º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 6ª Série/ › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7ª Série/ - 8º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7ª Série/ - 8º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 7ª Série/ › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8ª Série/ - 9º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8ª Série/ - 9º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 8ª Série/ › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1ª a 4ª Série - 1º ao 5º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 1ª a 4ª Série › 1º ao 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5ª a 8ª Série - 6º ao 9º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 5ª a 8ª Série › 6º ao 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - TOTAL FUNDAMENTAL 8 E 9 ANOS` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - TOTAL FUNDAMENTAL 8 E 9 ANOS` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › TOTAL FUNDAMENTAL 8 E 9 ANOS»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Ensino Médio - 1ª Série Médio` | `Hora-aula diária média - Ensino Médio - 1ª Série Médio` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › 1ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - 2ª Série Médio` | `Hora-aula diária média - Ensino Médio - 2ª Série Médio` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › 2ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - 3ª Série Médio` | `Hora-aula diária média - Ensino Médio - 3ª Série Médio` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › 3ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - 4ª Série Médio` | `Hora-aula diária média - Ensino Médio - 4ª Série Médio` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › 4ª Série Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - Médio Não-Seriado` | `Hora-aula diária média - Ensino Médio - Médio Não-Seriado` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › Médio Não-Seriado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - Total Médio` | `Hora-aula diária média - Ensino Médio - Total Médio` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › Total Médio»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 | `media_horas_aula_brasil`, `media_horas_aula_regies`, `media_horas_aula_ufs` |
| `Região` | `Região` | texto | Brasil ou grande região da linha, conforme a planilha. | — | todo | `had_escolas`, `had_municipios`, `had_regioes` e mais 6 |
| `UF` | `UF` | texto | Coluna «UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `had_escolas`, `had_uf`, `had_ufs` e mais 2 |
| `Código da UF` | `Código da UF` | inteiro | Coluna «Código da UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2010 a 2015 | `had_uf`, `horas_aula_ufs`, `media_horas_aula_ufs` |
| `Hora-aula diária média - Educação Infantil - Total` | `Hora-aula diária média - Educação Infantil - Total` | decimal | Valor de «Hora-aula diária média» no recorte «Educação Infantil › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - Total` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - Total` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º ao 5º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 1º ao 5º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 1º ao 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º ao 9º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º ao 9º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 6º ao 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 2º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 3º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 4º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 5º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 6º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 7º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 8º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 9º Ano` | `Hora-aula diária média - Ensino Fundamental 8 e 9 anos - 9º Ano` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Fundamental 8 e 9 anos › 9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Hora-aula diária média - Ensino Médio - Total` | `Hora-aula diária média - Ensino Médio - Total` | decimal | Valor de «Hora-aula diária média» no recorte «Ensino Médio › Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2014 | `horas_aula_brasil`, `horas_aula_regioes`, `horas_aula_ufs` e mais 3 |
| `Educação Infantil - Total` | `Educação Infantil - Total` | decimal | Valor de «Educação Infantil» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Educação Infantil - Creche` | `Educação Infantil - Creche` | decimal | Valor de «Educação Infantil» no recorte «Creche»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Educação Infantil - Pré-Escola` | `Educação Infantil - Pré-Escola` | decimal | Valor de «Educação Infantil» no recorte «Pré-Escola»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Fundamental 8 e 9 anos - Total` | `Ensino Fundamental 8 e 9 anos - Total` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - Anos Iniciais` | `Ensino Fundamental 8 e 9 anos - Anos Iniciais` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - Anos Finais` | `Ensino Fundamental 8 e 9 anos - Anos Finais` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 1º Ano` | `Ensino Fundamental 8 e 9 anos - 1º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 2º Ano` | `Ensino Fundamental 8 e 9 anos - 2º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 3º Ano` | `Ensino Fundamental 8 e 9 anos - 3º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 4º Ano` | `Ensino Fundamental 8 e 9 anos - 4º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 5º Ano` | `Ensino Fundamental 8 e 9 anos - 5º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 6º Ano` | `Ensino Fundamental 8 e 9 anos - 6º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 7º Ano` | `Ensino Fundamental 8 e 9 anos - 7º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 8º Ano` | `Ensino Fundamental 8 e 9 anos - 8º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Fundamental 8 e 9 anos - 9º Ano` | `Ensino Fundamental 8 e 9 anos - 9º Ano` | decimal | Valor de «Ensino Fundamental 8 e 9 anos» no recorte «9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2020 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Ensino Médio - Total` | `Ensino Médio - Total` | decimal | Valor de «Ensino Médio» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Médio - 1ª Série` | `Ensino Médio - 1ª Série` | decimal | Valor de «Ensino Médio» no recorte «1ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Médio - 2ª Série` | `Ensino Médio - 2ª Série` | decimal | Valor de «Ensino Médio» no recorte «2ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Médio - 3ª Série` | `Ensino Médio - 3ª Série` | decimal | Valor de «Ensino Médio» no recorte «3ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Médio - 4ª Série` | `Ensino Médio - 4ª Série` | decimal | Valor de «Ensino Médio» no recorte «4ª Série»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 4 |
| `Ensino Médio - Não-Seriado` | `Ensino Médio - Não-Seriado` | decimal | Valor de «Ensino Médio» no recorte «Não-Seriado»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2015 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_regioes` e mais 2 |
| `Dependência Administrativa` | `Dependência Administrativa` | texto | Dependência administrativa da escola (federal, estadual, municipal, privada ou total), conforme a planilha. | — | 2016 a 2025 | `had_brasil`, `had_brasil_regioes_ufs`, `had_escolas` e mais 3 |
| `Unidade Geográfica` | `Unidade Geográfica` | texto | Unidade geográfica da linha: Brasil, grande região, UF ou município, conforme o arquivo. | — | 2017 a 2025 | `had_brasil_regioes_ufs` |
| `Ensino Fundamental - Total` | `Ensino Fundamental - Total` | decimal | Valor de «Ensino Fundamental» no recorte «Total»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - Anos Iniciais` | `Ensino Fundamental - Anos Iniciais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Iniciais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - Anos Finais` | `Ensino Fundamental - Anos Finais` | decimal | Valor de «Ensino Fundamental» no recorte «Anos Finais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 1º Ano` | `Ensino Fundamental - 1º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «1º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 2º Ano` | `Ensino Fundamental - 2º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «2º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 3º Ano` | `Ensino Fundamental - 3º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «3º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 4º Ano` | `Ensino Fundamental - 4º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «4º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 5º Ano` | `Ensino Fundamental - 5º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «5º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 6º Ano` | `Ensino Fundamental - 6º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «6º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 7º Ano` | `Ensino Fundamental - 7º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «7º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 8º Ano` | `Ensino Fundamental - 8º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «8º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Ensino Fundamental - 9º Ano` | `Ensino Fundamental - 9º Ano` | decimal | Valor de «Ensino Fundamental» no recorte «9º Ano»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2021 a 2025 | `had_brasil_regioes_ufs`, `had_escolas`, `had_municipios` |
| `Código do Município` | `Código do Município` | inteiro | Coluna «Código do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `had_escolas`, `had_municipios` |
| `Nome do Município` | `Nome do Município` | texto | Coluna «Nome do Município» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `had_escolas`, `had_municipios` |
| `Código da Escola` | `Código da Escola` | inteiro | Coluna «Código da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `had_escolas` |
| `Nome da Escola` | `Nome da Escola` | texto | Coluna «Nome da Escola» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `had_escolas` |
| `Sigla da UF` | `Sigla da UF` | texto | Coluna «Sigla da UF» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | 2025 | `had_municipios` |

## No lake

- Dataset `inep/media-horas-aula-diaria`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local de amostra: todas as edições do catálogo para Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, só a edição mais recente (as colunas de identificação desses arquivos podem variar nas edições não amostradas).
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `had_brasil_regioes_ufs_2025.parquet` da edição mais recente do lake (ano 2025):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano", "Unidade Geográfica", "Localização", "Educação Infantil - Total"
    FROM read_parquet('lake/inep/media-horas-aula-diaria/ano=2025/media-horas-aula-diaria-had-2025-brasil-regioes-ufs__had_brasil_regioes_ufs_2025.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
