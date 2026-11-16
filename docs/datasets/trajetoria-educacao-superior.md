---
dataset:
  id: trajetoria-educacao-superior
  fonte: inep
  titulo: Indicadores — Trajetória dos cursos de graduação
  resumo: Indicadores de trajetória de curso de graduação (permanência, conclusão, desistência) por coorte de ingresso, curso e instituição.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; arquivos por período de acompanhamento (por exemplo 2010-2019, 2020-2024)
  cobertura:
    inicio: '2010'
    fim: '2020'
  unidade: um curso de graduação de uma instituição, numa coorte de ingresso e ano de referência
  granularidade:
    espacial: curso de graduação (com região, UF e município do curso)
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 33
  unidades_de_medida:
    Categoria Administrativa: código da categoria (sem unidade)
    Organização Acadêmica: código da categoria (sem unidade)
    Grau Acadêmico: código da categoria (sem unidade)
    Modalidade de Ensino: código da categoria (sem unidade)
    Código da Instituição: ano, código ou quantidade de alunos
    Código do Curso de Graduação: ano, código ou quantidade de alunos
    Código da Região Geográfica do Curso: ano, código ou quantidade de alunos
    Código da Unidade Federativa do Curso: ano, código ou quantidade de alunos
    Código do Município do Curso: ano, código ou quantidade de alunos
    Código da área do Curso segundo a classificação CINE BRASIL: ano, código ou quantidade de alunos
    Código da Grande Área do Curso segundo a classificação CINE BRASIL: ano, código ou quantidade de alunos
    Ano de Ingresso: ano, código ou quantidade de alunos
    Ano de Referência: ano, código ou quantidade de alunos
    Prazo de Integralização em Anos: ano, código ou quantidade de alunos
    Ano de Integralização do Curso: ano, código ou quantidade de alunos
    Prazo de Acompanhamento do Curso em anos: ano, código ou quantidade de alunos
    Ano Máximo de Acompanhamento do Curso: ano, código ou quantidade de alunos
    Quantidade de Ingressantes no Curso: ano, código ou quantidade de alunos
    Quantidade de Permanência no Curso no ano de referência: ano, código ou quantidade de alunos
    Quantidade de Concluintes no Curso no ano de referência: ano, código ou quantidade de alunos
    Quantidade de Desistência no Curso no ano de referência: ano, código ou quantidade de alunos
    Quantidade de Falecimentos no Curso no ano de referência: ano, código ou quantidade de alunos
    Indicadores de Trajetória - Taxa de Permanência - TAP: '%'
    Indicadores de Trajetória - Taxa de Conclusão Acumulada - TCA: '%'
    Indicadores de Trajetória - Taxa de Desistência Acumulada - TODA: '%'
    Indicadores de Trajetória - Taxa de Conclusão Anual - TCAN: '%'
    Indicadores de Trajetória - Taxa de Desistência Anual - TDAN: '%'
    Indicadores de Trajetória - Taxa de Desistência Acumulada - TDA: '%'
    Indicadores de Trajetória - Taxa de Desistência Anual - TADA: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Trajetória dos cursos de graduação

## Resumo

Indicadores de trajetória de curso de graduação do Inep: para cada curso e coorte de ingresso, a quantidade de ingressantes, de permanência, de concluintes, de desistência e de falecimentos no ano de referência e os indicadores de trajetória calculados.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/trajetoria-educacao-superior` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; arquivos por período de acompanhamento (por exemplo 2010-2019, 2020-2024) |
| Cobertura | 2010 a 2020 |
| Unidade (uma linha) | um curso de graduação de uma instituição, numa coorte de ingresso e ano de referência |
| Granularidade | espacial: curso de graduação (com região, UF e município do curso); temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 33 |
| Unidades de medida | `Categoria Administrativa`: código da categoria (sem unidade); `Organização Acadêmica`: código da categoria (sem unidade); `Grau Acadêmico`: código da categoria (sem unidade); `Modalidade de Ensino`: código da categoria (sem unidade); `Código da Instituição`: ano, código ou quantidade de alunos; `Código do Curso de Graduação`: ano, código ou quantidade de alunos; `Código da Região Geográfica do Curso`: ano, código ou quantidade de alunos; `Código da Unidade Federativa do Curso`: ano, código ou quantidade de alunos; `Código do Município do Curso`: ano, código ou quantidade de alunos; `Código da área do Curso segundo a classificação CINE BRASIL`: ano, código ou quantidade de alunos; `Código da Grande Área do Curso segundo a classificação CINE BRASIL`: ano, código ou quantidade de alunos; `Ano de Ingresso`: ano, código ou quantidade de alunos; `Ano de Referência`: ano, código ou quantidade de alunos; `Prazo de Integralização em Anos`: ano, código ou quantidade de alunos; `Ano de Integralização do Curso`: ano, código ou quantidade de alunos; `Prazo de Acompanhamento do Curso em anos`: ano, código ou quantidade de alunos; `Ano Máximo de Acompanhamento do Curso`: ano, código ou quantidade de alunos; `Quantidade de Ingressantes no Curso`: ano, código ou quantidade de alunos; `Quantidade de Permanência no Curso no ano de referência`: ano, código ou quantidade de alunos; `Quantidade de Concluintes no Curso no ano de referência`: ano, código ou quantidade de alunos; `Quantidade de Desistência no Curso no ano de referência`: ano, código ou quantidade de alunos; `Quantidade de Falecimentos no Curso no ano de referência`: ano, código ou quantidade de alunos; `Indicadores de Trajetória - Taxa de Permanência - TAP`: %; `Indicadores de Trajetória - Taxa de Conclusão Acumulada - TCA`: %; `Indicadores de Trajetória - Taxa de Desistência Acumulada - TODA`: %; `Indicadores de Trajetória - Taxa de Conclusão Anual - TCAN`: %; `Indicadores de Trajetória - Taxa de Desistência Anual - TDAN`: %; `Indicadores de Trajetória - Taxa de Desistência Acumulada - TDA`: %; `Indicadores de Trajetória - Taxa de Desistência Anual - TADA`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 11 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/indicadores_trajetoria_es_2020_2024.zip`.
- No bruto, cada arquivo se chama `indicadores/trajetoria-educacao-superior/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Título das planilhas: "Indicadores de Trajetória de Curso de Graduação".
- Cada linha é um curso de graduação de uma instituição, para uma coorte de ingresso e um ano de referência, com prazo de integralização e de acompanhamento do curso.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2010 | `indicadores_trajetoria_educacao_superior` (31) |
| 2011 | `indicadores_trajetoria_educacao_superior` (31) |
| 2012 | `indicadores_trajetoria_educacao_superior` (31) |
| 2013 | `indicadores_trajetoria_educacao_superior` (31) |
| 2014 | `indicadores_trajetoria_educacao_superior` (31) |
| 2015 | `indicadores_trajetoria_educacao_superior` (31) |
| 2016 | `indicadores_trajetoria_educacao_superior` (31) |
| 2017 | `indicadores_trajetoria_educacao_superior` (31) |
| 2018 | `indicadores_trajetoria_educacao_superior` (31) |
| 2019 | `indicadores_trajetoria_educacao_superior` (31) |
| 2020 | `indicadores_trajetoria_educacao_superior` (31) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Código da Instituição` | `Código da Instituição` | inteiro | Coluna «Código da Instituição» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Nome da Instituição` | `Nome da Instituição` | texto | Coluna «Nome da Instituição» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Categoria Administrativa` | `Categoria Administrativa` | inteiro | Coluna «Categoria Administrativa» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Organização Acadêmica` | `Organização Acadêmica` | inteiro | Coluna «Organização Acadêmica» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código do Curso de Graduação` | `Código do Curso de Graduação` | inteiro | Coluna «Código do Curso de Graduação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Nome do Curso de Graduação` | `Nome do Curso de Graduação` | texto | Coluna «Nome do Curso de Graduação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código da Região Geográfica do Curso` | `Código da Região Geográfica do Curso` | inteiro | Coluna «Código da Região Geográfica do Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código da Unidade Federativa do Curso` | `Código da Unidade Federativa do Curso` | inteiro | Coluna «Código da Unidade Federativa do Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código do Município do Curso` | `Código do Município do Curso` | inteiro | Coluna «Código do Município do Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Grau Acadêmico` | `Grau Acadêmico` | inteiro | Coluna «Grau Acadêmico» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Modalidade de Ensino` | `Modalidade de Ensino` | inteiro | Coluna «Modalidade de Ensino» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código da área do Curso segundo a classificação CINE BRASIL` | `Código da área do Curso segundo a classificação CINE BRASIL` | texto | Coluna «Código da área do Curso segundo a classificação CINE BRASIL» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Nome da área do Curso segundo a classificação CINE BRASIL` | `Nome da área do Curso segundo a classificação CINE BRASIL` | texto | Coluna «Nome da área do Curso segundo a classificação CINE BRASIL» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Código da Grande Área do Curso segundo a classificação CINE BRASIL` | `Código da Grande Área do Curso segundo a classificação CINE BRASIL` | texto | Coluna «Código da Grande Área do Curso segundo a classificação CINE BRASIL» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Nome da Grande Área do Curso segundo a classificação CINE BRASIL` | `Nome da Grande Área do Curso segundo a classificação CINE BRASIL` | texto | Coluna «Nome da Grande Área do Curso segundo a classificação CINE BRASIL» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Ano de Ingresso` | `Ano de Ingresso` | inteiro | Coluna «Ano de Ingresso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Ano de Referência` | `Ano de Referência` | inteiro | Coluna «Ano de Referência» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Prazo de Integralização em Anos` | `Prazo de Integralização em Anos` | inteiro | Coluna «Prazo de Integralização em Anos» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Ano de Integralização do Curso` | `Ano de Integralização do Curso` | inteiro | Coluna «Ano de Integralização do Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Prazo de Acompanhamento do Curso em anos` | `Prazo de Acompanhamento do Curso em anos` | inteiro | Coluna «Prazo de Acompanhamento do Curso em anos» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Ano Máximo de Acompanhamento do Curso` | `Ano Máximo de Acompanhamento do Curso` | inteiro | Coluna «Ano Máximo de Acompanhamento do Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Quantidade de Ingressantes no Curso` | `Quantidade de Ingressantes no Curso` | inteiro | Coluna «Quantidade de Ingressantes no Curso» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Quantidade de Permanência no Curso no ano de referência` | `Quantidade de Permanência no Curso no ano de referência` | inteiro | Coluna «Quantidade de Permanência no Curso no ano de referência» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Quantidade de Concluintes no Curso no ano de referência` | `Quantidade de Concluintes no Curso no ano de referência` | inteiro | Coluna «Quantidade de Concluintes no Curso no ano de referência» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Quantidade de Desistência no Curso no ano de referência` | `Quantidade de Desistência no Curso no ano de referência` | inteiro | Coluna «Quantidade de Desistência no Curso no ano de referência» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Quantidade de Falecimentos no Curso no ano de referência` | `Quantidade de Falecimentos no Curso no ano de referência` | inteiro | Coluna «Quantidade de Falecimentos no Curso no ano de referência» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo |
| `Indicadores de Trajetória - Taxa de Permanência - TAP` | `Indicadores de Trajetória - Taxa de Permanência - TAP` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Permanência › TAP»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo |
| `Indicadores de Trajetória - Taxa de Conclusão Acumulada - TCA` | `Indicadores de Trajetória - Taxa de Conclusão Acumulada - TCA` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Conclusão Acumulada › TCA»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo |
| `Indicadores de Trajetória - Taxa de Desistência Acumulada - TODA` | `Indicadores de Trajetória - Taxa de Desistência Acumulada - TODA` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Desistência Acumulada › TODA»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 |
| `Indicadores de Trajetória - Taxa de Conclusão Anual - TCAN` | `Indicadores de Trajetória - Taxa de Conclusão Anual - TCAN` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Conclusão Anual › TCAN»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo |
| `Indicadores de Trajetória - Taxa de Desistência Anual - TDAN` | `Indicadores de Trajetória - Taxa de Desistência Anual - TDAN` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Desistência Anual › TDAN»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2010 a 2015 |
| `Indicadores de Trajetória - Taxa de Desistência Acumulada - TDA` | `Indicadores de Trajetória - Taxa de Desistência Acumulada - TDA` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Desistência Acumulada › TDA»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2011 a 2020 |
| `Indicadores de Trajetória - Taxa de Desistência Anual - TADA` | `Indicadores de Trajetória - Taxa de Desistência Anual - TADA` | decimal | Valor de «Indicadores de Trajetória» no recorte «Taxa de Desistência Anual › TADA»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | 2016 a 2020 |

## No lake

- Dataset `inep/trajetoria-educacao-superior`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local, com o conversor atual, dos arquivos do catálogo.
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `indicadores_trajetoria_educacao_superior_2020_2024.parquet` da edição mais recente do lake (ano 2020):

```python
import duckdb

duckdb.sql("""
    SELECT "Código da Instituição", "Nome da Instituição", "Categoria Administrativa"
    FROM read_parquet('lake/inep/trajetoria-educacao-superior/ano=2020/indicadores-trajetoria-educacao-superior-indicadores-trajetoria-es-2020-2024__indicadores_trajetoria_educacao_superior_2020_2024.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
