---
dataset:
  id: idd
  fonte: inep
  titulo: IDD — microdados do Indicador da Diferença entre os Desempenhos Observado e Esperado
  resumo: Microdados por estudante concluinte usados no cálculo do IDD (valor agregado dos cursos de graduação), nas edições de 2021 a 2023.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/idd
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual, acompanhando o ciclo do Enade; o lake tem as edições de 2021, 2022 e 2023
  cobertura:
    inicio: '2021'
    fim: '2023'
  unidade: um estudante concluinte participante do Enade, com o curso e a instituição em que se graduaria
  granularidade:
    espacial: curso de graduação, com código do curso e da IES (e-Mec) e município de funcionamento do curso
    temporal: ano do Enade da edição
  formato_bruto: ZIP anual (o de 2022 é, na verdade, um arquivo RAR com extensão .zip) com as pastas 1.LEIA-ME (manual do usuário em PDF e dicionário em xlsx e ods) e 2.DADOS (um TXT com ponto e vírgula)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 20
  unidades_de_medida:
    nt_ger: pontos (0 a 100)
    enem_nt_cn: pontos na escala do Enem
    enem_nt_ch: pontos na escala do Enem
    enem_nt_lc: pontos na escala do Enem
    enem_nt_mt: pontos na escala do Enem
  dados_pessoais:
  - coluna: nt_ger
    categoria: nota individual do estudante no Enade
  - coluna: enem_nt_cn
    categoria: nota individual do estudante no Enem
  - coluna: enem_nt_ch
    categoria: nota individual do estudante no Enem
  - coluna: enem_nt_lc
    categoria: nota individual do estudante no Enem
  - coluna: enem_nt_mt
    categoria: nota individual do estudante no Enem
  - coluna: ano_in_grad
    categoria: trajetória individual do estudante (ano de início da graduação e ano do Enem)
  - coluna: ano_enem
    categoria: trajetória individual do estudante (ano de início da graduação e ano do Enem)
  - coluna: ano_inicio_grad
    categoria: trajetória individual do estudante (ano de início da graduação e ano do Enem)
  - coluna: co_munic_curso
    categoria: município de funcionamento do curso do estudante
  eras:
  - desde: '2021'
    mudanca: 'primeira edição no lake: concluintes das licenciaturas e de bacharelados e tecnológicos avaliados no Enade de 2021 (30 áreas); inclui um arquivo TXT com cabeçalho entre aspas'
  - desde: '2022'
    mudanca: áreas de gestão e negócios do ciclo do Enade (26 áreas); o pacote foi reeditado em 2024 (arquivo `_v2`, versão corrigida em 20/08/2024 por adequação a nova metodologia)
  - desde: '2023'
    mudanca: áreas de saúde, engenharias e agrárias do ciclo do Enade (28 áreas); a coluna `ano_in_grad` passa a `ano_inicio_grad`; surge o código 8 (comunitária/confessional) em `co_categad`
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# IDD — microdados do Indicador da Diferença entre os Desempenhos Observado e Esperado

## Resumo

Microdados do Indicador da Diferença entre os Desempenhos Observado e Esperado (IDD), o indicador com que o Inep mede o valor agregado pelo curso de graduação ao desenvolvimento dos concluintes, comparando o desempenho no Enade com o desempenho esperado a partir do desempenho do mesmo estudante no Enem. Cada edição acompanha o ciclo do Enade e cobre só as áreas avaliadas naquele ano. O arquivo traz, por estudante concluinte, o curso e a instituição, a nota bruta no Enade e as notas das quatro provas objetivas do Enem do ano selecionado; o indicador do curso não vem no arquivo, e sim a base para calculá-lo.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/idd` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/idd |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual, acompanhando o ciclo do Enade; o lake tem as edições de 2021, 2022 e 2023 |
| Cobertura | 2021 a 2023 |
| Unidade (uma linha) | um estudante concluinte participante do Enade, com o curso e a instituição em que se graduaria |
| Granularidade | espacial: curso de graduação, com código do curso e da IES (e-Mec) e município de funcionamento do curso; temporal: ano do Enade da edição |
| Formato bruto | ZIP anual (o de 2022 é, na verdade, um arquivo RAR com extensão .zip) com as pastas 1.LEIA-ME (manual do usuário em PDF e dicionário em xlsx e ods) e 2.DADOS (um TXT com ponto e vírgula) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 20 |
| Unidades de medida | `nt_ger`: pontos (0 a 100); `enem_nt_cn`: pontos na escala do Enem; `enem_nt_ch`: pontos na escala do Enem; `enem_nt_lc`: pontos na escala do Enem; `enem_nt_mt`: pontos na escala do Enem |
| Dados pessoais | `nt_ger` (nota individual do estudante no Enade); `enem_nt_cn` (nota individual do estudante no Enem); `enem_nt_ch` (nota individual do estudante no Enem); `enem_nt_lc` (nota individual do estudante no Enem); `enem_nt_mt` (nota individual do estudante no Enem); `ano_in_grad` (trajetória individual do estudante (ano de início da graduação e ano do Enem)); `ano_enem` (trajetória individual do estudante (ano de início da graduação e ano do Enem)); `ano_inicio_grad` (trajetória individual do estudante (ano de início da graduação e ano do Enem)); `co_munic_curso` (município de funcionamento do curso do estudante) |
| Eras | 2021: primeira edição no lake: concluintes das licenciaturas e de bacharelados e tecnológicos avaliados no Enade de 2021 (30 áreas); inclui um arquivo TXT com cabeçalho entre aspas; 2022: áreas de gestão e negócios do ciclo do Enade (26 áreas); o pacote foi reeditado em 2024 (arquivo `_v2`, versão corrigida em 20/08/2024 por adequação a nova metodologia); 2023: áreas de saúde, engenharias e agrárias do ciclo do Enade (28 áreas); a coluna `ano_in_grad` passa a `ano_inicio_grad`; surge o código 8 (comunitária/confessional) em `co_categad` |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_IDD_<ano>.zip` para 2021, 2022 e 2023. A página oficial lista também as edições de 2014 a 2019 (arquivos `.7z`, como `microdados_IDD_2019.7z`), que o catálogo do fetcher não tem; elas não estão no lake. O Inep não lista edição de 2020.
- **2021:** ZIP de 4.085.569 bytes (modificado na fonte em 2022-09-12). Tem `1.LEIA-ME` (manual do usuário, dicionário em xlsx e ods) e `2.DADOS/MICRODADOS_IDD_2021_LGPD.txt` (16.612.726 bytes; 189.522 linhas de dados). O manual cita também uma nota técnica do cálculo do IDD, que não vem no ZIP.
- **2022:** a URL termina em `.zip`, mas o arquivo é um RAR (versão 5), com 3.942.384 bytes (modificado em 2024-08-20); `file` o identifica como "RAR archive data, v5" e um leitor de ZIP o recusa. Tem a mesma estrutura de pastas, com `MICRODADOS_IDD_2022_LGPD_v2.txt` (20.129.893 bytes; 235.891 linhas). O manual registra versão original de 02/04/2024 e versão corrigida de 20/08/2024, por adequação à nova metodologia.
- **2023:** ZIP de 4.296.066 bytes (modificado em 2025-04-11) com `MICRODADOS_IDD_2023_LGPD.txt` (21.551.851 bytes; 248.889 linhas).
- No bruto, os arquivos se chamam `idd/idd-microdados_<ano>@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte. Contagens de linhas conferidas nos TXT da fonte em 2026-11-15; os TXT usam CRLF e, em 2021, o cabeçalho vem entre aspas.

## Conteúdo

- **Um arquivo de dados por edição**, com 19 colunas: dados da IES e do curso (`co_ies`, `co_categad`, `co_orgacad`, `co_grupo`, `co_curso`, `co_modalidade`, `co_munic_curso`) e dados do estudante (inscrição e presença, ano de início da graduação, nota no Enade e notas do Enem).
- **O IDD em si não vem no arquivo.** A coluna `nt_ger` é a nota bruta do estudante no Enade, e as quatro `enem_nt_*` são as notas do Enem do ano indicado em `ano_enem`; o desempenho esperado e o indicador do curso saem da metodologia descrita na nota técnica de cada edição (Nota Técnica nº 8/2022 para 2021, nº 29/2023 para 2022 e nº 7/2024 para 2023, citadas pelos manuais).
- **Quem entra.** Só estudantes concluintes (`tp_inscricao` 1), com inscrição regular (`in_regular` 1) e presença com resultado válido (`tp_pres` 555), (nenhuma linha tem a nota do Enem em branco). Cada edição cobre as áreas do ciclo do Enade daquele ano, conforme os manuais: 2021, licenciaturas e bacharelados como Ciências Biológicas, Ciência da Computação, Ciências Sociais, Design, Educação Física, Filosofia, Geografia, História, Química e Sistemas de Informação, mais três tecnológicos de informática; 2022, bacharelados de negócios, direito, psicologia, jornalismo e áreas afins (Administração, Direito, Psicologia, Ciências Contábeis e Econômicas, entre outros) e tecnológicos de gestão e design; 2023, bacharelados da saúde, das engenharias e das ciências agrárias, arquitetura e tecnológicos da área.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2021 | `microdados_idd_lgpd` (19) |
| 2022 | `microdados_idd_lgpd_v2` (19) |
| 2023 | `microdados_idd_lgpd` (19) |

## Variáveis

As descrições e os códigos vêm do dicionário de variáveis (xlsx) de cada edição, que lista as mesmas 19 variáveis; a lista de áreas de `co_grupo`, que muda por edição, está só no dicionário. O dicionário também traz uma planilha de municípios (código, nome e UF) que o lake não carrega.
As colunas `ano_in_grad` (2021 e 2022) e `ano_inicio_grad` (2023) são a mesma variável com nomes diferentes; veja a coluna *Período*.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `nu_ano` | `NU_ANO` | texto | Ano de realização do Enade (2021, 2022 ou 2023, conforme a edição) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_ies` | `CO_IES` | texto | Código da IES (e-Mec) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_categad` | `CO_CATEGAD` | texto | Código da categoria administrativa da IES: 1 = pública federal; 2 = pública estadual; 3 = pública municipal; 4 = privada com fins lucrativos; 5 = privada sem fins lucrativos; 7 = especial; 8 = comunitária/confessional (só em 2023) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_orgacad` | `CO_ORGACAD` | texto | Código da organização acadêmica da IES: 10019 = Centro Federal de Educação Tecnológica; 10020 = centro universitário; 10022 = faculdade; 10026 = instituto federal de educação, ciência e tecnologia; 10028 = universidade | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_grupo` | `CO_GRUPO` | texto | Código da área de enquadramento do curso no Enade; a lista de áreas muda a cada edição, com 30 códigos em 2021, 26 em 2022 e 28 em 2023 (veja o dicionário de cada edição) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_curso` | `CO_CURSO` | texto | Código do curso (e-Mec) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_modalidade` | `CO_MODALIDADE` | texto | Modalidade de ensino: 0 = EaD; 1 = presencial | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `co_munic_curso` | `CO_MUNIC_CURSO` | texto | Código do município de funcionamento do curso (código do IBGE de 7 dígitos; o dicionário traz a planilha de municípios) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `tp_inscricao` | `TP_INSCRICAO` | texto | Tipo de inscrição: 1 = concluinte (único valor nos arquivos) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `in_regular` | `IN_REGULAR` | texto | Indicativo da condição da inscrição: 1 = regular (único valor nos arquivos) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `tp_inscricao_adm` | `TP_INSCRICAO_ADM` | texto | Tipo da origem da inscrição: 0 = tradicional; 2 = administrativo | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `ano_in_grad` | `ANO_IN_GRAD` | texto | Ano de início da graduação (edições 2021 e 2022; na edição de 2023 a coluna se chama `ano_inicio_grad`) | — | 2021 a 2022 | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `tp_pres` | `TP_PRES` | texto | Tipo de presença: 555 = presente com resultado válido (único valor nos arquivos) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `nt_ger` | `NT_GER` | texto | Nota bruta da prova no Enade: média ponderada da formação geral (25%) e do componente específico (75%), de 0 a 100 | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `ano_enem` | `ANO_ENEM` | texto | Identificação do ano do Enem selecionado para o estudante (de 2009 até 2021, 2022 e 2022 nas edições de 2021, 2022 e 2023, conforme os dados) | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `enem_nt_cn` | `ENEM_NT_CN` | texto | Nota da prova de Ciências da Natureza do Enem do ano selecionado | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `enem_nt_ch` | `ENEM_NT_CH` | texto | Nota da prova de Ciências Humanas do Enem do ano selecionado | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `enem_nt_lc` | `ENEM_NT_LC` | texto | Nota da prova de Linguagens e Códigos do Enem do ano selecionado | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `enem_nt_mt` | `ENEM_NT_MT` | texto | Nota da prova de Matemática do Enem do ano selecionado | — | todo | `microdados_idd_lgpd`, `microdados_idd_lgpd_v2` |
| `ano_inicio_grad` | `ANO_INICIO_GRAD` | texto | Ano de início da graduação (edição 2023; nas edições 2021 e 2022 a coluna se chama `ano_in_grad`; o dicionário de 2023 ainda a chama `ANO_IN_GRAD`) | — | 2023 | `microdados_idd_lgpd` |

## No lake

- Dataset `inep/idd`, particionado por `ano`; um Parquet por edição, no padrão `idd-microdados_<ano>__microdados_idd_<ano>_lgpd[_v2].parquet`.
- Todas as colunas são texto (o DuckDB lê o TXT sem inferir tipos); os nomes saem normalizados (minúsculas). O cabeçalho de 2021 chega sem aspas no lake.
- A coluna `ano` é a edição, tirada do nome do arquivo; `nu_ano` é o ano de realização do Enade dentro do dado.

## Cuidados de uso

- **Uma coluna muda de nome em 2023.** `ano_in_grad` (2021 e 2022) vira `ano_inicio_grad` (2023) no arquivo, enquanto o dicionário de 2023 ainda a chama `ANO_IN_GRAD`. Ao empilhar as edições, una por nome com `union_by_name` e junte as duas colunas (`coalesce`); sem isso, cada edição fica com a coluna da outra vazia.
- **O conjunto de cursos muda por edição.** Só entram as áreas avaliadas no Enade daquele ano, de modo que as edições não são comparáveis entre si por área; o `co_grupo` também troca de lista (30, 26 e 28 códigos). Não compare 2021, 2022 e 2023 como uma série.
- **Colunas sem variação.** `tp_inscricao` vale 1, `in_regular` vale 1 e `tp_pres` vale 555 em todas as linhas de todas as edições (conferido nos TXT da fonte); `tp_inscricao_adm` vale 0 em quase todas as linhas e 2 em 27 linhas de 2021 e em 2 de 2022 (em 2023 só há 0).
- **Notas zero existem.** Há linhas com `nt_ger` igual a 0 (107 em 2021, 89 em 2022 e 37 em 2023) e com notas do Enem iguais a 0; os arquivos não têm valores ausentes, de modo que o zero é um valor lido da fonte.
- **A escala do Enem não é a da prova do Enade.** `nt_ger` vai de 0 a 100 (o máximo observado é 89,7 em 2021, 96,6 em 2022 e 99,0 em 2023); as notas do Enem estão na escala do Enem (máximo observado de 996,1 em 2021, 996,5 em 2022 e 1008,3 em 2023, em matemática).
- **A edição de 2022 foi substituída.** A versão corrigida de 20/08/2024 (arquivo `_v2`) mudou a metodologia; qualquer cópia anterior a essa data não é equivalente.
- **Download de 2022.** A URL termina em `.zip`, mas o conteúdo é RAR; um leitor de ZIP recusa o arquivo.
- **Não há identificador de estudante, mas cada linha é uma pessoa.** Nenhum identificador direto é publicado e o nome dos arquivos traz o sufixo `LGPD`, mas o conjunto de curso, município, ano de início da graduação, ano do Enem e notas caracteriza o estudante; evite recortes com poucos casos. Não há linhas duplicadas em nenhuma edição (conferido nos TXT da fonte).
- **Sem chave.** Nenhuma coluna ou combinação identifica o estudante, por isso a chave do dataset fica vazia.

## Exemplos

Nota média no Enade por categoria administrativa e modalidade, juntando as três edições (os arquivos de 2023 têm `ano_inicio_grad` onde os demais têm `ano_in_grad`; o `union_by_name` e o `coalesce` tratam a troca de nome):

```python
import duckdb

duckdb.sql("""
    SELECT ano, co_categad, co_modalidade, count(*) AS estudantes,
           round(avg(try_cast(nt_ger AS DOUBLE)), 1) AS media_enade,
           round(avg(try_cast(coalesce(ano_inicio_grad, ano_in_grad) AS INTEGER)), 1) AS ano_medio_de_inicio
    FROM read_parquet('lake/inep/idd/ano=*/*.parquet', union_by_name = true, hive_partitioning = true)
    GROUP BY ALL
    ORDER BY ano, co_categad, co_modalidade
""").show()
```

## Referências

- Microdados do IDD: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/idd
- Manual do usuário e dicionário de variáveis de cada edição, dentro de cada pacote em https://download.inep.gov.br/microdados/
