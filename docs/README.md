# Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira — microdados e indicadores (`inep`)

O `inep-fetcher` coleta do portal de downloads do Inep (`download.inep.gov.br`) os microdados de exames, censos e pesquisas e os indicadores educacionais, e os converte para o lake em Parquet. O conversor declara 34 datasets: 16 de microdados e 18 de indicadores educacionais.

## Microdados

| Dataset | O que é | Cobertura | Página |
|---|---|---|---|
| `ana` | Microdados da Avaliação Nacional da Alfabetização (ANA) de 2014 e 2016: proficiência e respostas dos alunos do 3º ano do ensino fundamental, resultados por escola e parâmetros dos itens | 2014 a 2016 | [ana](datasets/ana.md) |
| `censo-educacao-superior` | Microdados anuais do Censo da Educação Superior por curso e por instituição: cadastro, vagas, inscritos, ingressantes, matrículas, concluintes e docentes, de 1995 a 2024 | 1995 a 2024 | [censo-educacao-superior](datasets/censo-educacao-superior.md) |
| `censo-escolar` | Microdados anuais do Censo Escolar da Educação Básica por escola: cadastro, infraestrutura, matrículas, docentes e turmas, de 1995 a 2025 | 1995 a 2025 | [censo-escolar](datasets/censo-escolar.md) |
| `censo-magisterio` | Microdados do levantamento de 2003 com os profissionais do magistério da educação básica: perfil, vínculo, remuneração, formação e condições de trabalho; edição única | 2003 a 2003 | [censo-magisterio](datasets/censo-magisterio.md) |
| `enade-licenciaturas` | Microdados do Enade das Licenciaturas 2025: resultados da avaliação teórica e respostas ao Questionário do Estudante dos concluintes de licenciaturas, em 28 arquivos por tema | 2025 a 2025 | [enade-licenciaturas](datasets/enade-licenciaturas.md) |
| `enade` | Microdados do Exame Nacional de Desempenho dos Estudantes (Enade), edições 2010 a 2023: curso, presença, notas e questionário do estudante, em arquivos separados que só se ligam pelo código do curso | 2010 a 2023 | [enade](datasets/enade.md) |
| `enamed` | Microdados do Enamed 2025: resultados e questionários dos concluintes de Medicina (via Enade) e dos demais participantes, em 36 arquivos por tema, mais a tabela de parâmetros dos itens | 2025 a 2025 | [enamed](datasets/enamed.md) |
| `encceja` | Microdados do Exame Nacional para Certificação de Competências de Jovens e Adultos (Encceja) de 2013 a 2025: participantes regulares e privados de liberdade, questionários e itens das provas | 2013 a 2025 | [encceja](datasets/encceja.md) |
| `enem-por-escola` | Médias do Enem por escola, com participação, indicadores e taxas de rendimento, nas edições de 2005 a 2015, em um único arquivo | 2005 a 2015 | [enem-por-escola](datasets/enem-por-escola.md) |
| `enem` | Microdados do Exame Nacional do Ensino Médio: participantes, questionário socioeconômico, notas e itens das provas, de 1998 em diante | 1998 a 2025 | [enem](datasets/enem.md) |
| `idd` | Microdados por estudante concluinte usados no cálculo do IDD (valor agregado dos cursos de graduação), nas edições de 2021 a 2023 | 2021 a 2023 | [idd](datasets/idd.md) |
| `pesquisa-discriminacao` | Microdados da pesquisa de 2008 sobre preconceito e discriminação em escolas públicas, com diretores, professores, funcionários, alunos e pais | 2008 a 2008 | [pesquisa-discriminacao](datasets/pesquisa-discriminacao.md) |
| `pnd` | Microdados da Prova Nacional Docente 2025: resultados e questionário dos concluintes de licenciatura do Enade e dos demais participantes graduados em licenciatura, em 13 arquivos | 2025 a 2025 | [pnd](datasets/pnd.md) |
| `pnera` | Microdados da pesquisa de 2004 sobre a demanda e a oferta de educação em assentamentos do Incra: líderes comunitários, famílias assentadas e escolas | 2004 a 2004 | [pnera](datasets/pnera.md) |
| `saeb` | Microdados do Sistema de Avaliação da Educação Básica (Saeb), de 1995 a 2023: proficiência e respostas de alunos, questionários de escolas, diretores, professores e secretários, resultados agregados (2011) e itens das provas | 1995 a 2023 | [saeb](datasets/saeb.md) |
| `talis` | Microdados do Brasil na TALIS 2024: questionários de professores e diretores dos anos iniciais e finais do ensino fundamental, com pesos e questões nacionais | 2024 a 2024 | [talis](datasets/talis.md) |

## Indicadores educacionais

| Dataset | O que é | Cobertura | Página |
|---|---|---|---|
| `adequacao-formacao-docente` | Percentual de docentes por grupo do indicador de adequação da formação do docente, por etapa e disciplina, em Brasil, regiões, UFs, municípios e escolas | 2013 a 2025 | [adequacao-formacao-docente](datasets/adequacao-formacao-docente.md) |
| `complexidade-gestao-escola` | Percentual de escolas por nível do Indicador de Complexidade de Gestão da Escola (níveis 1 a 6), por recorte geográfico, localização e dependência | 2016 a 2025 | [complexidade-gestao-escola](datasets/complexidade-gestao-escola.md) |
| `docentes-curso-superior` | Percentual de docentes com curso superior na educação básica, por etapa, recorte geográfico, localização e rede | 2011 a 2025 | [docentes-curso-superior](datasets/docentes-curso-superior.md) |
| `docentes-pos-graduacao` | Percentual de docentes em exercício na educação superior com pós-graduação stricto sensu, por recorte, categoria, organização, grau, modalidade e área do curso | 2010 a 2024 | [docentes-pos-graduacao](datasets/docentes-pos-graduacao.md) |
| `esforco-docente` | Percentual de docentes por nível do Indicador de Esforço Docente (níveis 1 a 6), por etapa e recorte geográfico | 2013 a 2025 | [esforco-docente](datasets/esforco-docente.md) |
| `financeiros` | Estimativas do investimento público direto em educação por estudante, em valores nominais e reais, por nível de ensino | 2000 a 2021 | [financeiros](datasets/financeiros.md) |
| `fluxo-educacao-superior` | Taxas de evasão, conclusão, retenção e permanência na graduação, por atributos do aluno, para Brasil, regiões e UFs | 2010 a 2024 | [fluxo-educacao-superior](datasets/fluxo-educacao-superior.md) |
| `media-alunos-por-turma` | Média de alunos por turma por etapa e modalidade de ensino, por recorte geográfico, localização e rede | 2007 a 2025 | [media-alunos-por-turma](datasets/media-alunos-por-turma.md) |
| `media-horas-aula-diaria` | Média de horas-aula diária por etapa, por recorte geográfico, localização e rede | 2010 a 2025 | [media-horas-aula-diaria](datasets/media-horas-aula-diaria.md) |
| `nivel-socioeconomico` | Indicador de Nível Socioeconômico (INSE) por escola, a partir dos questionários do Saeb | 2015 a 2023 | [nivel-socioeconomico](datasets/nivel-socioeconomico.md) |
| `qualidade-educacao-superior` | Resultados dos indicadores de qualidade da educação superior do Inep: Conceito Enade, Conceito Preliminar de Curso (CPC), IDD e IGC, por curso e instituição | 2004 a 2025 | [qualidade-educacao-superior](datasets/qualidade-educacao-superior.md) |
| `regularidade-corpo-docente` | Distribuição das escolas por faixa do Indicador de Regularidade do Docente (IRD), por recorte geográfico, localização e dependência | 2013 a 2025 | [regularidade-corpo-docente](datasets/regularidade-corpo-docente.md) |
| `remuneracao-docentes` | Remuneração média de docentes em exercício na educação básica, por escolaridade, com dados do Censo da Educação Básica e da RAIS | 2014 a 2021 | [remuneracao-docentes](datasets/remuneracao-docentes.md) |
| `taxas-distorcao-idade-serie` | Taxa de distorção idade-série por série e etapa, por recorte geográfico, localização e dependência administrativa | 2006 a 2025 | [taxas-distorcao-idade-serie](datasets/taxas-distorcao-idade-serie.md) |
| `taxas-nao-resposta` | Taxa de não resposta do Censo da Educação Básica por etapa, por recorte geográfico, localização e rede | 2011 a 2025 | [taxas-nao-resposta](datasets/taxas-nao-resposta.md) |
| `taxas-rendimento-escolar` | Taxas de aprovação, reprovação e abandono por série e etapa, por recorte geográfico, localização e rede | 2007 a 2025 | [taxas-rendimento-escolar](datasets/taxas-rendimento-escolar.md) |
| `taxas-transicao` | Taxas de promoção, repetência, evasão e migração para a EJA entre dois anos letivos consecutivos, por série e recorte geográfico | 2007 a 2021 | [taxas-transicao](datasets/taxas-transicao.md) |
| `trajetoria-educacao-superior` | Indicadores de trajetória de curso de graduação (permanência, conclusão, desistência) por coorte de ingresso, curso e instituição | 2010 a 2020 | [trajetoria-educacao-superior](datasets/trajetoria-educacao-superior.md) |

## Como o Inep publica

- Os microdados saem em um ZIP por edição (ou RAR, em alguns casos), com pastas de dados (CSV ou TXT), dicionário de variáveis em planilha, scripts de leitura (SAS, SPSS, R) e documentos técnicos. O ZIP do Enem 2025 usa compressão Deflate64, que o conversor lê por meio do 7-Zip.
- Desde a Lei Geral de Proteção de Dados, o Inep publica modelos simplificados de microdados (Enem desde a edição de 2020, com mudanças adicionais em 2024), com mascaramento de identificadores e exclusão de variáveis; as páginas de cada dataset descrevem o que a fonte informa.
- Os indicadores educacionais saem em planilhas (XLSX ou XLS) dentro de ZIP, com título, notas e fonte acima e abaixo da tabela e cabeçalho de dois a quatro níveis; não há dicionário de variáveis, e as definições estão nos títulos, notas e notas técnicas do Inep.
- O portal do Inep declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15); os conjuntos não declaram licença própria.
- A cadeia de certificados do servidor `download.inep.gov.br` vem incompleta (falta o certificado intermediário); clientes que não completam a cadeia pelo campo de acesso à autoridade do certificado falham na verificação.

## Esquemas de referência

Os esquemas (`*.schema.json`) foram gerados por conversão local, com o conversor atual, de amostras dos arquivos (os CSV e TXT truncados às primeiras linhas; para os indicadores, todas as edições de Brasil, regiões e UFs e, nos arquivos de municípios e de escolas, a edição mais recente). As colunas e os períodos de arquivos fora das amostras podem faltar. Nomes de coluna com espaço nas pontas constam sem os espaços, e `|` consta como `/`, porque a verificação da documentação compara os nomes depois de aparar a tabela.

## Fora do lake

- `pnd` (Prova Nacional Docente 2025): a fonte publica `microdados_pnd_2025.rar`; o catálogo do fetcher aponta para `.zip`, que responde 404. A página foi escrita a partir do RAR da fonte.
- `talis` 2018: a URL do catálogo responde 404; só a edição 2024 está no lake.
- `enade` 2004 a 2009 e `idd` 2014 a 2019 existem na fonte e não constam do catálogo nem do lake (ver as páginas).
