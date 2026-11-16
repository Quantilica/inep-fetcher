---
dataset:
  id: enem-por-escola
  fonte: inep
  titulo: Enem por Escola — microdados (2005 a 2015)
  resumo: Médias do Enem por escola, com participação, indicadores e taxas de rendimento, nas edições de 2005 a 2015, em um único arquivo.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual de 2005 a 2015 (11 edições); o Inep descontinuou o Enem por Escola depois de 2015
  cobertura:
    inicio: '2005'
    fim: '2015'
  unidade: uma escola numa edição do Enem por Escola (ano e código da escola no Educacenso)
  granularidade:
    espacial: escola, com UF e município
    temporal: ano da edição (coluna `nu_ano`)
  formato_bruto: ZIP com um único CSV com ponto e vírgula (latin-1), mais dicionário em xlsx, programas de leitura SAS e SPSS e documentos técnicos em PDF
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 27
  unidades_de_medida:
    nu_matriculas: alunos
    nu_participantes: participantes
    nu_participantes_nec_esp: participantes
    nu_taxa_participacao: percentual (de 0 a 100)
    nu_media_cn: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_ch: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_lp: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_mt: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_red: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_obj: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    nu_media_tot: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso)
    pc_formacao_docente: percentual (de 0 a 100)
    nu_taxa_permanencia: percentual (quase sempre de 0 a 100; veja Cuidados de uso)
    nu_taxa_aprovacao: percentual (de 0 a 100)
    nu_taxa_reprovacao: percentual (de 0 a 100)
    nu_taxa_abandono: percentual (de 0 a 100)
  dados_pessoais: nenhum
  eras:
  - desde: '2005'
    mudanca: 'primeira edição: média total (redação e prova objetiva) na escala de 0 a 100, pela Teoria Clássica dos Testes, para escolas com pelo menos 10 participantes concluintes'
  - desde: '2008'
    mudanca: a média total dá lugar à média da prova objetiva (só em 2008) e à média de redação, que segue até 2015
  - desde: '2009'
    mudanca: o Enem passa à Teoria de Resposta ao Item, com escala descrita como de 0 a 1.000, e as médias vêm por área de conhecimento (ciências da natureza, ciências humanas, linguagens e matemática); entra a taxa de participação, com mínimo de 2% para divulgar a escola
  - desde: '2011'
    mudanca: o mínimo de participação sobe para 50% e só conta como participante o concluinte que fez as quatro áreas e a redação; o número de escolas divulgadas cai de 19.691 (2010) para 10.077
  - desde: '2013'
    mudanca: só entram os participantes da 3ª série do ensino médio regular (com possibilidade de inclusão ou exclusão dos da 4ª série, a pedido da escola); entram os participantes com necessidade especial e o indicador de adequação da formação docente
  - desde: '2015'
    mudanca: 'última edição: aparece o Inse da escola (grupos de 1 a 6); a permanência na escola vale de 2014 a 2015'
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Enem por Escola — microdados (2005 a 2015)

## Resumo

Microdados do Enem por Escola, o produto em que o Inep divulgou, de 2005 a 2015, as médias do Exame Nacional do Ensino Médio agregadas por escola, com o número de matrículas e de participantes, a taxa de participação e, conforme a edição, indicadores de nível socioeconômico, adequação da formação docente, permanência, taxas de rendimento e porte da escola. A fonte traz as onze edições empilhadas num arquivo único, uma linha por escola e ano. O Inep encerrou o produto depois da edição de 2015.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/enem-por-escola` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual de 2005 a 2015 (11 edições); o Inep descontinuou o Enem por Escola depois de 2015 |
| Cobertura | 2005 a 2015 |
| Unidade (uma linha) | uma escola numa edição do Enem por Escola (ano e código da escola no Educacenso) |
| Granularidade | espacial: escola, com UF e município; temporal: ano da edição (coluna `nu_ano`) |
| Formato bruto | ZIP com um único CSV com ponto e vírgula (latin-1), mais dicionário em xlsx, programas de leitura SAS e SPSS e documentos técnicos em PDF |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 27 |
| Unidades de medida | `nu_matriculas`: alunos; `nu_participantes`: participantes; `nu_participantes_nec_esp`: participantes; `nu_taxa_participacao`: percentual (de 0 a 100); `nu_media_cn`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_ch`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_lp`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_mt`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_red`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_obj`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `nu_media_tot`: pontos (escala de 0 a 100 até 2008 e escala TRI de 2009 em diante; veja Cuidados de uso); `pc_formacao_docente`: percentual (de 0 a 100); `nu_taxa_permanencia`: percentual (quase sempre de 0 a 100; veja Cuidados de uso); `nu_taxa_aprovacao`: percentual (de 0 a 100); `nu_taxa_reprovacao`: percentual (de 0 a 100); `nu_taxa_abandono`: percentual (de 0 a 100) |
| Dados pessoais | nenhum |
| Eras | 2005: primeira edição: média total (redação e prova objetiva) na escala de 0 a 100, pela Teoria Clássica dos Testes, para escolas com pelo menos 10 participantes concluintes; 2008: a média total dá lugar à média da prova objetiva (só em 2008) e à média de redação, que segue até 2015; 2009: o Enem passa à Teoria de Resposta ao Item, com escala descrita como de 0 a 1.000, e as médias vêm por área de conhecimento (ciências da natureza, ciências humanas, linguagens e matemática); entra a taxa de participação, com mínimo de 2% para divulgar a escola; 2011: o mínimo de participação sobe para 50% e só conta como participante o concluinte que fez as quatro áreas e a redação; o número de escolas divulgadas cai de 19.691 (2010) para 10.077; 2013: só entram os participantes da 3ª série do ensino médio regular (com possibilidade de inclusão ou exclusão dos da 4ª série, a pedido da escola); entram os participantes com necessidade especial e o indicador de adequação da formação docente; 2015: última edição: aparece o Inse da escola (grupos de 1 a 6); a permanência na escola vale de 2014 a 2015 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/enem_por_escola/2005_a_2015/microdados_enem_por_escola.zip` (8.813.782 bytes; última modificação na fonte em 2022-05-17, lido em 2026-11-15), um único arquivo para todo o período. O catálogo do fetcher registra que não existem arquivos por ano.
- No bruto, o arquivo se chama `enem-por-escola/enem-por-escola@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- O ZIP tem a pasta `DADOS` com `MICRODADOS_ENEM_ESCOLA.csv` (26.182.307 bytes descompactado), `DICIONÁRIO` com `Dicionário_Microdados_Enem_Escola.xlsx`, `INPUTS` com os programas de leitura SAS e SPSS e `LEIA-ME  e DOCUMENTOS TÉCNICOS` com o Leia-me (dezembro de 2018) e as notas técnicas das edições de 2005 a 2010, 2012, 2014 e 2015, mais notas informativas de 2011 e 2013. O Leia-me menciona um dicionário em formato ods, que o ZIP não traz.
- O CSV da fonte tem 172.305 linhas de dados, sem linhas em branco, nas 11 edições (conferido em 2026-11-15).

## Conteúdo

- **Uma tabela empilhada por ano.** Cada linha é uma escola numa edição, com dados cadastrais (UF, município, código e nome da escola no Educacenso, dependência administrativa e localização), dados de participação (matrículas, participantes e taxa de participação), médias das provas, indicadores (Inse, formação docente, permanência), taxas de rendimento (aprovação, reprovação e abandono) e o porte da escola.
- **Quais escolas aparecem.** Só entram escolas com resultado divulgado, nas etapas e modalidades de cada edição (ensino médio regular, magistério, não seriado, profissionalizante, EJA). As médias nas colunas valem para o ensino médio regular. O Leia-me diz que o aluno do ensino médio especial participa do exame, mas nunca teve a média divulgada, e que só participantes que se declararam concluintes e escolas com pelo menos 10 participantes entram nas médias.
- **Linhas por edição na fonte** (conferido no CSV): 2005, 16.052; 2006, 15.652; 2007, 16.770; 2008, 19.144; 2009, 18.042; 2010, 19.691; 2011, 10.077; 2012, 11.522; 2013, 14.117; 2014, 15.640; 2015, 15.598.
- **Médias por edição.** 2005 a 2007: só `nu_media_tot`. 2008: `nu_media_obj` e `nu_media_red`. 2009 a 2015: quatro áreas (`nu_media_cn`, `nu_media_ch`, `nu_media_lp`, `nu_media_mt`) e `nu_media_red`. As demais ficam vazias.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `microdados_enem_escola` (27) |

## Variáveis

As descrições vêm do dicionário de variáveis (xlsx) do ZIP, que também informa em quais edições cada variável existe; essa informação está no fim de cada descrição. Os códigos de `tp_dependencia_adm_escola`, `tp_localizacao_escola`, `inse` e `porte_escola` estão na própria descrição.
Valores ausentes ficam vazios. A coluna *Período* não se aplica, porque o lake não é particionado por ano: os anos estão na coluna `nu_ano`.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `nu_ano` | `NU_ANO` | texto | Ano da edição do Enem por Escola (2005 a 2015); em todas as edições | — | — |
| `co_uf_escola` | `CO_UF_ESCOLA` | texto | Código da Unidade da Federação da escola (código do IBGE); em todas as edições | — | — |
| `sg_uf_escola` | `SG_UF_ESCOLA` | texto | Sigla da Unidade da Federação da escola; em todas as edições | — | — |
| `co_municipio_escola` | `CO_MUNICIPIO_ESCOLA` | texto | Código do município da escola; o dicionário descreve o código de 7 dígitos: 1º dígito a região, 1º e 2º a UF, 3º ao 6º o município e 7º o dígito verificador; em todas as edições | — | — |
| `no_municipio_escola` | `NO_MUNICIPIO_ESCOLA` | texto | Nome do município da escola; em todas as edições | — | — |
| `co_escola_educacenso` | `CO_ESCOLA_EDUCACENSO` | texto | Código da escola, número gerado como identificador da escola no Educacenso; em todas as edições | — | — |
| `no_escola_educacenso` | `NO_ESCOLA_EDUCACENSO` | texto | Nome da escola no Educacenso do ano anterior; em todas as edições | — | — |
| `tp_dependencia_adm_escola` | `TP_DEPENDENCIA_ADM_ESCOLA` | texto | Tipo da dependência administrativa da escola no Educacenso: 1 = federal; 2 = estadual; 3 = municipal; 4 = privada; em todas as edições | — | — |
| `tp_localizacao_escola` | `TP_LOCALIZACAO_ESCOLA` | texto | Tipo de localização da escola: 1 = urbana; 2 = rural; em todas as edições | — | — |
| `nu_matriculas` | `NU_MATRICULAS` | texto | Número de alunos matriculados no Censo Escolar na 3ª e 4ª séries do Ensino Médio; em todas as edições (2005 a 2015) | — | — |
| `nu_participantes_nec_esp` | `NU_PARTICIPANTES_NEC_ESP` | texto | Número de participantes do Enem que cumprem os requisitos de participação no cálculo da média e têm necessidade especial; só nas edições de 2013 a 2015 | — | — |
| `nu_participantes` | `NU_PARTICIPANTES` | texto | Número de participantes do Enem que cumprem os requisitos de participação no cálculo da média; em todas as edições (2005 a 2015) | — | — |
| `nu_taxa_participacao` | `NU_TAXA_PARTICIPACAO` | texto | Taxa de participação: participantes no Enem da escola divididos pelos matriculados nos anos finais do Ensino Médio da escola, segundo o Censo Escolar, em percentual; só nas edições de 2009 a 2015 | — | — |
| `nu_media_cn` | `NU_MEDIA_CN` | texto | Média das notas de Ciências da Natureza do Ensino Médio Regular; só nas edições de 2009 a 2015 | — | — |
| `nu_media_ch` | `NU_MEDIA_CH` | texto | Média das notas de Ciências Humanas do Ensino Médio Regular; só nas edições de 2009 a 2015 | — | — |
| `nu_media_lp` | `NU_MEDIA_LP` | texto | Média das notas de Linguagens e Códigos do Ensino Médio Regular; só nas edições de 2009 a 2015 | — | — |
| `nu_media_mt` | `NU_MEDIA_MT` | texto | Média das notas de Matemática do Ensino Médio Regular; só nas edições de 2009 a 2015 | — | — |
| `nu_media_red` | `NU_MEDIA_RED` | texto | Média das notas de Redação do Ensino Médio Regular; só nas edições de 2008 a 2015 | — | — |
| `nu_media_obj` | `NU_MEDIA_OBJ` | texto | Média da prova objetiva do Ensino Médio Regular; só na edição de 2008 | — | — |
| `nu_media_tot` | `NU_MEDIA_TOT` | texto | Média total (redação e prova objetiva) do Ensino Médio Regular, corrigida pelo número de participantes; só nas edições de 2005 a 2007 | — | — |
| `inse` | `INSE` | texto | Indicador de Nível Socioeconômico da escola, em seis grupos: Grupo 1 reúne as escolas com Inse médio mais baixo e Grupo 6 as com Inse mais alto; só na edição de 2015 | — | — |
| `pc_formacao_docente` | `PC_FORMACAO_DOCENTE` | texto | Indicador de Adequação da Formação Docente da escola para lecionar no Ensino Médio, em percentual; só nas edições de 2013 a 2015 | — | — |
| `nu_taxa_permanencia` | `NU_TAXA_PERMANENCIA` | texto | Indicador de Permanência na Escola para o Ensino Médio; só nas edições de 2014 e 2015 | — | — |
| `nu_taxa_aprovacao` | `NU_TAXA_APROVACAO` | texto | Taxa de aprovação dos alunos no Ensino Médio; nas edições de 2005 e de 2007 a 2015 | — | — |
| `nu_taxa_reprovacao` | `NU_TAXA_REPROVACAO` | texto | Taxa de reprovação dos alunos no Ensino Médio; nas edições de 2005 e de 2007 a 2015 | — | — |
| `nu_taxa_abandono` | `NU_TAXA_ABANDONO` | texto | Taxa de abandono dos alunos no Ensino Médio; nas edições de 2005 e de 2007 a 2015 | — | — |
| `porte_escola` | `PORTE_ESCOLA` | texto | Porte da escola, pelo número de alunos matriculados no último ano do Ensino Médio: De 1 a 30 alunos; De 31 a 60 alunos; De 61 a 90 alunos; Maior que 90 alunos; em todas as edições (2005 a 2015) | — | — |

## No lake

- Dataset `inep/enem-por-escola`, sem partições; um Parquet, `enem-por-escola__microdados_enem_escola.parquet`.
- Todas as colunas são texto, inclusive as médias e as taxas (que usam ponto como separador decimal); os nomes saem normalizados (minúsculas).
- O ano é a coluna `nu_ano`; não há coluna `ano` de partição.

## Cuidados de uso

- **As escalas das médias mudam em 2009.** Até 2008 as notas vão de 0 a 100 (Teoria Clássica dos Testes); de 2009 em diante usam a escala da Teoria de Resposta ao Item, que o Leia-me descreve como de 0 a 1.000 (no CSV da fonte, as médias de 2005 a 2008 ficam abaixo de 83 e as de 2009 a 2015 chegam a 930). Nunca compare médias de antes e depois de 2009, nem `nu_media_tot` ou `nu_media_obj` com as médias por área.
- **As colunas de média dependem do ano.** `nu_media_tot` existe só em 2005 a 2007, `nu_media_obj` só em 2008, `nu_media_red` de 2008 em diante e as quatro áreas de 2009 em diante; a taxa de aprovação, reprovação e abandono não existe em 2006 e a de permanência só em 2014 e 2015. Os vazios não são erro, são variáveis que a edição não trazia.
- **O universo de escolas muda por regra de divulgação.** O mínimo de 10 participantes vale em todas as edições; a taxa mínima de participação foi de 2% em 2009 e 2010 e de 50% a partir de 2011, e a definição de participante mudou em 2011 e em 2013. Por isso o número de escolas cai de 19.691 em 2010 para 10.077 em 2011. Não leia a variação do número de linhas ou das médias como variação da qualidade das escolas.
- **Participação voluntária e uso para ranking.** O Leia-me lembra que o Enem é voluntário e que a representatividade da média varia com a taxa de participação. Em nota de 15 de setembro de 2017, o Inep encerrou o produto, apontando a inadequação do uso como indicador de qualidade e o uso inapropriado para ranquear escolas.
- **Não dá para reconstruir médias de município, UF ou Brasil.** O Leia-me avisa que a média das médias das escolas não reproduz as médias individuais dessas agregações.
- **A chave natural quase se repete.** A fonte traz uma só escola duplicada num mesmo ano: o par `nu_ano` 2012 e `co_escola_educacenso` 35290804 aparece em duas linhas, com 50 matrículas e 51 participantes numa e 51 e 50 na outra; nas demais 172.303 linhas o par é único. Por isso a chave do dataset fica vazia. O código da escola pode mudar entre anos e o nome é o do Educacenso do ano anterior.
- **Inse só em 2015.** O dicionário e os dados concordam que o indicador de nível socioeconômico existe apenas na edição de 2015, em grupos de 1 a 6 (texto "Grupo N"); o Leia-me o cita também entre as novidades de 2013.
- **Valor fora da faixa.** Em `nu_taxa_permanencia`, uma linha de 2015 tem o valor 5822 (a escola tem 304 matrículas), fora da faixa de 0 a 100 das demais; as taxas de aprovação, reprovação e abandono e as demais taxas ficam entre 0 e 100.
- **Taxas em escala de 0 a 100.** As taxas e `pc_formacao_docente` vêm como percentual (por exemplo, 94.89), não como fração.
- **Sem dados pessoais.** Cada linha é uma escola; o arquivo não tem informação de pessoa. O nome e o código da escola são públicos no Educacenso.

## Exemplos

Média de redação por ano e dependência administrativa da escola (1 federal, 2 estadual, 3 municipal, 4 privada), sem misturar anos, porque a escala muda em 2009. A amostra do lake tem só as primeiras linhas do arquivo (2005 a 2008, uma UF); no lake completo aparecem todos os anos de 2008 a 2015:

```python
import duckdb

duckdb.sql("""
    SELECT nu_ano, tp_dependencia_adm_escola AS dependencia, count(*) AS escolas,
           round(avg(try_cast(nu_media_red AS DOUBLE)), 1) AS media_redacao
    FROM read_parquet('lake/inep/enem-por-escola/*.parquet')
    WHERE try_cast(nu_media_red AS DOUBLE) IS NOT NULL
    GROUP BY ALL
    ORDER BY nu_ano, dependencia
""").show()
```

## Referências

- Microdados do Enem por Escola: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola
- Leia-me, dicionário e notas técnicas de cada edição, dentro do ZIP em https://download.inep.gov.br/microdados/enem_por_escola/2005_a_2015/microdados_enem_por_escola.zip
