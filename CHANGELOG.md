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
