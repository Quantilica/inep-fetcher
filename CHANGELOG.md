# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2026-07-24

### Adicionado

- Catálogo inicial com 16 grupos de microdados do INEP: `enem` (1998-presente),
  `censo_escolar` (1995-presente), `censo_educacao_superior` (1995-2024),
  `saeb` (bienal, 1995-2023), `enade` (2004-2023, sem 2020), `ana` (2014,
  2016), `encceja` (2013-2025, com lacunas), `censo_magisterio` (2003),
  `enade_licenciaturas` (2025), `enamed` (2025), `pnd` (2025), `pnera`
  (2004), `pesquisa_discriminacao` (2008), `idd` (2021-2023),
  `enem_por_escola` (agregado 2005-2015) e `talis` (2018, 2024).
- Catálogo de 18 grupos de **Indicadores Educacionais** (dados derivados/
  agregados, não microdados brutos): `adequacao_formacao_docente`,
  `complexidade_gestao_escola`, `esforco_docente`,
  `indicadores_fluxo_educacao_superior`,
  `indicadores_qualidade_educacao_superior`,
  `indicadores_trajetoria_educacao_superior`,
  `indicadores_financeiros_educacionais`, `media_alunos_por_turma`,
  `media_horas_aula_diaria`, `nivel_socioeconomico`,
  `docentes_curso_superior`, `docentes_pos_graduacao`,
  `regularidade_corpo_docente`, `remuneracao_docentes`,
  `taxas_distorcao_idade_serie`, `taxas_nao_resposta`,
  `taxas_rendimento_escolar` e `taxas_transicao` — 647 datasets, com
  macro-alias `indicadores_educacionais` para baixar todos de uma vez.
  As URLs reais só ficam disponíveis via um fragmento carregado por AJAX
  por ano/período (não aparecem na página estática), então foram obtidas
  buscando cada fragmento individualmente; a nomenclatura muda de era
  dentro de quase todo indicador (prefixos compactos maiúsculos nos anos
  recentes vs. nomes descritivos com subdiretório extra nos anos antigos).
- CLI standalone (`inep-fetcher`, `argparse`) e plugin Typer/Rich para
  `quantilica-cli` (`quantilica inep`), com os comandos `sync` e `discover`.
- Manifestos de proveniência (`DownloadManifest`) via `quantilica-core` em
  todo download.
- Bundle da cadeia de CA intermediária da RNP/ICPEdu
  (`RNP ICPEdu GR46 OV TLS CA 2025`, emitida sob a raiz pública GlobalSign
  Root R46) para contornar a cadeia TLS incompleta servida por
  `download.inep.gov.br` (o servidor não envia o certificado intermediário
  no handshake).
- Flag `--sleeptime` (padrão 0.3s) em `sync`, aplicando uma pequena pausa
  entre downloads dentro de um grupo.

### Corrigido

- `cli.py` não suprimia os loggers verbosos de terceiros (`quantilica.core`,
  `httpx` via `log_step`) fora do modo `--verbose`, conforme
  `docs/docs/normas/cli-fetchers.md` §2.6 — padronizado com os demais
  fetchers do ecossistema.
