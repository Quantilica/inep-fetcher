# inep-fetcher

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.12+-blue.svg?style=flat-square)

Utilitário de linha de comando para baixar dados públicos do [INEP](https://www.gov.br/inep/) (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira).
Descobre datasets a partir de um catálogo declarativo e faz o download organizado por grupo, com manifestos de proveniência via `quantilica-core`.

For full documentation, please visit [https://docs.quantilica.com](https://docs.quantilica.com).

## Instalação

```bash
pip install inep-fetcher
```

Com [uv](https://github.com/astral-sh/uv):

```bash
uv add inep-fetcher
```

**Requisitos:** Python 3.12+

## Uso

### Listar os datasets disponíveis

```bash
inep-fetcher discover
```

### Sincronizar (baixar) datasets

```bash
# Baixar todos os grupos — atenção: histórico completo passa de 20GB
inep-fetcher sync

# Baixar grupos específicos
inep-fetcher sync enem censo_escolar -o ./dados/inep

# Baixar todos os 18 grupos de indicadores educacionais de uma vez
inep-fetcher sync indicadores_educacionais

# Listar os arquivos que seriam baixados, sem baixar
inep-fetcher sync --dry-run
```

O `sync` aplica uma pausa de 0.3s entre downloads por padrão (cortesia ao
servidor); ajuste com `--sleeptime SEGUNDOS` se necessário.

**Microdados brutos** (16 grupos):

| Grupo | Descrição | Cobertura |
|---|---|---|
| `enem` | ENEM | 1998-presente, anual |
| `censo_escolar` | Censo Escolar (Educação Básica) | 1995-presente, anual |
| `censo_educacao_superior` | Censo da Educação Superior | 1995-2024, anual |
| `saeb` | SAEB | 1995-2023, bienal |
| `enade` | ENADE | 2004-2023, anual (sem 2020) |
| `ana` | Avaliação Nacional da Alfabetização | 2014, 2016 |
| `encceja` | Encceja | 2013-2025, com lacunas |
| `censo_magisterio` | Censo dos Profissionais do Magistério | 2003 |
| `enade_licenciaturas` | ENADE das Licenciaturas | 2025 |
| `enamed` | Enamed (Formação Médica) | 2025 |
| `pnd` | Prova Nacional Docente | 2025 |
| `pnera` | Pesquisa Nacional de Educação na Reforma Agrária | 2004 |
| `pesquisa_discriminacao` | Pesquisa de Ações Discriminatórias no Âmbito Escolar | 2008 |
| `idd` | Indicador de Diferença entre Desempenho Observado e Esperado | 2021-2023 |
| `enem_por_escola` | ENEM por Escola | 2005-2015 (agregado em 1 arquivo) |
| `talis` | TALIS (pesquisa internacional de docência) | 2018, 2024 |

**Indicadores Educacionais** (18 grupos, macro-alias `indicadores_educacionais`
expande para todos de uma vez — dados derivados/agregados, não microdados
brutos, publicados por ano/período em brasil-regiões-UF, município e escola):

| Grupo | Descrição |
|---|---|
| `adequacao_formacao_docente` | Adequação da Formação Docente |
| `complexidade_gestao_escola` | Complexidade de Gestão da Escola |
| `esforco_docente` | Esforço Docente |
| `indicadores_fluxo_educacao_superior` | Indicadores de Fluxo da Educação Superior |
| `indicadores_qualidade_educacao_superior` | Indicadores de Qualidade da Educação Superior |
| `indicadores_trajetoria_educacao_superior` | Indicadores de Trajetória da Educação Superior |
| `indicadores_financeiros_educacionais` | Indicadores Financeiros Educacionais |
| `media_alunos_por_turma` | Média de Alunos por Turma |
| `media_horas_aula_diaria` | Média de Horas Aula Diária |
| `nivel_socioeconomico` | Nível Socioeconômico (Inse) |
| `docentes_curso_superior` | Percentual de Docentes com Curso Superior |
| `docentes_pos_graduacao` | Percentual de Docentes com Pós-Graduação Stricto Sensu |
| `regularidade_corpo_docente` | Regularidade do Corpo Docente |
| `remuneracao_docentes` | Remuneração Média dos Docentes |
| `taxas_distorcao_idade_serie` | Taxas de Distorção Idade-Série |
| `taxas_nao_resposta` | Taxas de Não Resposta |
| `taxas_rendimento_escolar` | Taxas de Rendimento Escolar |
| `taxas_transicao` | Taxas de Transição |

### Nota sobre TLS

`download.inep.gov.br` não envia a cadeia de certificado completa no
handshake TLS (falta a CA intermediária `RNP ICPEdu GR46 OV TLS CA 2025`,
um problema conhecido do lado do servidor). Este pacote inclui essa CA
intermediária empacotada e configura a verificação TLS automaticamente —
nenhuma ação é necessária, e a verificação continua ativa (não usamos
`verify=False`).

### Integração com `quantilica-cli`

Se o `quantilica-cli` estiver instalado no mesmo ambiente, o `inep-fetcher` é
detectado automaticamente como plugin:

```bash
quantilica inep discover
```

## API Python

```python
from inep_fetcher.catalog import list_datasets

for entry in list_datasets(group="enem"):
    print(entry["id"], entry["url"])
```

## Desenvolvimento

```bash
git clone https://github.com/Quantilica/inep-fetcher.git
cd inep-fetcher
uv sync --group dev
uv run ruff check src/ tests/
uv run pytest
```

## Licença

MIT — veja [LICENSE](LICENSE).
