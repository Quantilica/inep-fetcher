# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

## [0.5.2] - 2026-11-05

### Corrigido
- Lake: ZIP cujos membros são planilhas (`.xls`/`.xlsx`) deixa de falhar com `Unsupported format: <membro>.xls`. Os membros Excel entram como arquivos de dados e são lidos com `pl.read_excel`, como o `.xlsx` solto, com o ZIP como origem no lake. Afeta os ZIPs só com planilhas (ex.: `docentes-curso-superior-dsu-*`, `media-alunos-por-turma-*`, `adequacao-formacao-docente-*`, 2011 a 2014). Reconverter esses datasets.
- Lake: lock file do Office (`~$<nome>.xlsx`, 165 bytes) esquecido dentro do ZIP deixa de ser lido como planilha e de derrubar o arquivo com `Could not find EOCD` (9 ZIPs de 2016 a 2022 em `adequacao-formacao-docente`, `media-alunos-por-turma`, `taxas-rendimento-escolar` e `taxas-transicao`).
- Lake: o checksum `md5_<nome>.txt` que o INEP põe nos ZIPs de indicadores deixa de virar Parquet como se fosse dado (459 de 1271 arquivos na primeira construção).

## [0.5.1] - 2026-11-04

### Corrigido
- Sem o extra `analysis`, o comando `convert` termina com código 1 e a instrução de instalação (`quantilica install inep --extra analysis`), sem traceback.

### Alterado
- O diretório de saída padrão (`/data/inep`) passa a ser declarado explicitamente no plugin; o valor não muda.

## [0.5.0] - 2026-11-04

### Corrigido
- Política de frescor volta a F2 (`HEAD_FALLBACK_GET`): `REMOTE_ONLY` (F3, para fontes sem validadores) causava re-download diário de fontes com Last-Modified/ETag, porque descartava o Last-Modified e o nome do arquivo caía em `@hoje`.

### Alterado
- Exige `quantilica-core>=0.16.0`.

## [0.4.2] - 2026-10-20

### Removido

- Remoção de certificado raiz RNP local acoplado (`_certs`), utilizando o pool seguro do sistema/certifi.

- Catálogo `enade`: entradas 2004-2009 descontinuadas — os microdados
  `microdados_enade_{2004..2009}.zip` foram removidos do portal do INEP
  (404 confirmado no dry-run agendado em 2026-10-12); o catálogo começa em
  2010 (total do catálogo: 796 → 790, ENADE: 19 → 13).

### Alterado

- `cli.py` protege o import do plugin; sem o host a CLI standalone sai com
  código 1 e orienta `quantilica install <fonte>`.
- `cli.py` ganha o bloco `if __name__ == "__main__": main()` (paridade com
  `bcb-sgs-fetcher`).

## [0.4.1] - 2026-08-31
### Corrigido
- Quitação de dívida de lint (E501) revelada ao preparar a primeira publicação; nenhum comportamento alterado.
### Alterado
- Primeira publicação efetiva do pacote (o repositório GitHub não existia antes de hoje; o tag v0.4.0 antecediu os workflows de CI).

## [0.4.0] - 2026-08-07
### Alterado
- Refatoração arquitetural: Remoção de dependências (`quantilica-cli` e `quantilica-catalog`) e limpeza de imports. Os fetchers agora são pacotes de extração puros, dependendo estritamente do `quantilica-core`.

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
