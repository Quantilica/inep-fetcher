# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.9.0] - 2026-11-28

### Adicionado

- Aviso de edição nova possivelmente não catalogada. O catálogo dos microdados é estático (ex.: `range(1998, 2026)` no ENEM) e nada avisava quando a fonte publicava uma edição nova. Para os grupos anuais (`enem`, `censo_escolar`, `censo_educacao_superior`), `list_datasets` passa a emitir um WARNING por execução quando o ano esperado (ano corrente menos 1 depois do mês de corte do grupo, menos 2 antes dele) não está no catálogo, dizendo qual grupo, até onde vai e qual edição é esperada. Meses de corte documentados em `EDICAO_ANUAL_MES_DE_CORTE` (ENEM e Censo Escolar: junho; Censo da Educação Superior: dezembro), estimativas do calendário usual, sem consulta à fonte. `edicoes_possivelmente_novas(hoje)` devolve a mesma lista. Não muda código de saída nem descobre edições: só avisa. Os grupos bienais, de edição única ou com lacunas não entram.

## [0.8.3] - 2026-11-25

### Corrigido

- O extra `analysis` passa a instalar `libarchive-c`, a reserva do leitor de RAR quando o 7-Zip não traz o codec RAR (caso do 7-Zip empacotado em algumas distribuições Linux). Sem ele, o RAR5 dos microdados do ENADE 2022 falhava com `RarUnavailableError` e o ano ficava fora do lake. Requer a biblioteca `libarchive` do sistema.

## [0.8.2] - 2026-11-25

### Corrigido

- O download recusa corpo que não é o arquivo esperado. O servidor do INEP responde HTTP 200 com uma página HTML ("Request Rejected", 243 bytes) quando bloqueia o cliente, e o `.rar` do ENADE 2022 chegou a ser gravado com ela, com carimbo mais novo que o arquivo real. O `quantilica-core` valida o arquivo pela extensão do destino e não conhece `.rar`, então só o `.rar` passava sem conferência. Agora o download vai para um arquivo de preparo ao lado do destino (`.<nome>.<host>-<pid>-<id>.parte.tmp`: extensão neutra, e o `.tmp` o faz ser ignorado por `select_current`, ingestão e auditoria) e só o substitui depois de conferido por `inep_fetcher.integridade.validar_corpo` (HTML, assinatura de `zip`, `xlsx`, `xls`, `rar` e `7z`, tamanho mínimo de 1 KiB) e pelas conferências do core (bloqueio de WAF, integridade do ZIP). O destino que já existia, e o sidecar dele, nunca são tocados por um corpo recusado (antes o core trocava o arquivo antes da conferência do INEP); o frescor segue sendo decidido pelo core sobre o destino (o preparo o espelha por link). Em recusa o preparo não fica no disco, o erro ("download recusado, versão anterior mantida") entra na lista de falhas da execução e a versão anterior segue como a atual. Arquivo que já estava no destino nunca é apagado: só gera aviso no log.
- O IDD 2022 (`microdados_IDD_2022.zip`) é um RAR5 publicado com extensão `.zip`: o core o recusaria como ZIP inválido e a primeira coleta nova dele falharia. O `.zip` agora aceita também a assinatura RAR (sem o teste de ZIP, que não se aplica).
- O preparo (e o sidecar e o `.tmp` parcial do core que ficam ao lado dele) deixado por uma execução morta é apagado no próximo download do mesmo destino. O nome do preparo leva um hash curto do nome do host e o pid dono (`.<nome>.<host>-<pid>-<id>.parte.tmp`). Preparo do próprio host: só o pid decide (morto, apaga; vivo, fica, qualquer que seja a idade do arquivo: o preparo nasce como link físico do destino e herda o `mtime` dele, que pode ter meses). Preparo de outro host (pasta compartilhada) ou dos formatos antigos (`.<nome>.<pid>-<id>.parte.tmp` e `.<nome>.<id>.parte`): só passadas 48 horas, contadas pelo `st_ctime` (a criação do link, não o `mtime` herdado). Nunca toca o destino, o sidecar dele nem o preparo de outro processo vivo.
- A conferência do preparo exige quebra de linha final num `.csv`/`.tsv`/`.txt` quando o servidor não anunciou o tamanho do corpo (sem `Content-Length` nem total em `Content-Range`), como o core faz em seus downloads; com o tamanho anunciado, o arquivo sem quebra final é aceito. O `ETag` com tamanho embutido não conta como tamanho anunciado (o rigor é maior que o do core nesse caso).
- O sidecar do arquivo promovido é regravado com `write_manifest_sidecar` do `quantilica-core` (com o `path` do destino); sem essa função o sidecar do preparo é movido.

## [0.8.1] - 2026-11-19

### Alterado

- Piso de `quantilica-analytics` do extra `analysis` sobe para 0.15.0 (`origin_outputs`, `LakeWriter.origin_complete`).
- CI e infraestrutura alinhados ao template (fetcher-template v0.2.1).

### Corrigido

- `lake`: o build sem mudança não lê mais o bruto. CSV e planilha soltos conferem `is_current` (sha256 do sidecar e rodapé do Parquet) antes de detectar separador, limpar o CSV ou ler a planilha. ZIP/7z/RAR declaram, em cada Parquet, a lista de todas as saídas do arquivo (`origin_outputs`, conhecidas antes da primeira gravação, inclusive no formato SAEB de largura fixa) e só são pulados, sem abrir nem extrair, quando todas existem com o sha256 atual (`origin_complete`). Uma conversão interrompida, um membro que falha (sem separador, TXT sem layout SAS, script inválido ou sem arquivo de dados) deixam a declaração incompleta e o arquivo é reaberto e o erro contado a cada build, como antes. Lake gravado sem a declaração reconverte uma vez e depois pula. As contagens de `converted`/`skipped`, `force` e o bruto novo ou alterado seguem como antes.

## [0.8.0] - 2026-11-16
### Adicionado
- Documentação dos dados em `docs/`, conforme a norma de documentação dos dados: página da fonte e, para cada um dos 34 datasets (16 de microdados e 18 de indicadores educacionais), página e esquema de referência com o dicionário de todas as variáveis. Os esquemas vêm de conversão local de amostras. O teste `tests/test_docs.py` a verifica; `quantilica-core[docs]` entra no grupo `dev`.
- Testes: identidade do registro conferida.

### Corrigido
- CI: o pyproject declara o PyPI antes do índice Quantilica (`[[tool.uv.index]]`), e o workflow perde `--index` e `--index-strategy`. Com a estratégia padrão `first-index`, o `uv sync` só consulta o índice para o que não está no PyPI (`quantilica-analytics`) e deixa de receber o 503 intermitente que o GitHub Pages devolve a caminhos inexistentes.
- `lake`: a detecção de separador de CSV registra em log (`debug`) quando o sniffing falha e cai no padrão `;`, em vez de engolir o erro em silêncio. Sem mudança de comportamento.

## [0.7.1] - 2026-11-14

### Corrigido
- `lake`: arquivos de checksum que acompanham o dado (TXT em que toda linha é `<hash hex de 32, 40, 64 ou 128 dígitos> *nome.ext` e há ao menos uma letra a-f nos hashes (um TXT de largura fixa só de dígitos não é checksum), como o `tx_rend_escolas_2023.txt` de `taxas-rendimento-escolar`; também `.md5`, `.sha1`, `.sha256`, `.sha512`) são ignorados, sem Parquet e sem o erro "separador de colunas não detectado". `.ods` já era ignorado (só `.xlsx`/`.xls`/`.csv`/`.txt` viram dado) e, quando há `.xlsx` e `.xls` com o mesmo nome na mesma pasta, só um é convertido, na ordem de preferência xlsx > xls > csv > txt (antes os dois disputavam o mesmo `file_key`).
- `lake`: o formato do arquivo compactado vem dos bytes mágicos, não da extensão. O IDD 2022 é um RAR v5 com extensão `.zip` e passa a ser lido pelo 7-Zip (`7z`, `7z.exe` ou `%ProgramFiles%\7-Zip`; `QUANTILICA_7Z` aponta outro executável). O código de saída 1 do 7-Zip (aviso, comum em RAR) não é erro; nomes demais para a linha de comando, ou membros que o 7-Zip não acha pelo nome, fazem a extração do arquivo inteiro por ele, numa pasta de preparo dentro do destino (o que já estava no destino não é apagado). O 7-Zip do Fedora não tem codec RAR: nesse caso o `libarchive-c` serve de reserva, se instalado. Sem leitor, o erro diz para instalar o 7-Zip.
- `lake`: ZIP com membro em Deflate64 (microdados do ENEM 2025, `RESULTADOS_2025.csv`) deixa de falhar com "That compression method is not supported". Os membros que o `zipfile` lê seguem por ele; só os de método não suportado são extraídos pelo 7-Zip, direto para o disco (nada de 2 GB em memória). `QUANTILICA_LAKE_SCRATCH` escolhe o disco do diretório temporário de extração.
- `lake` (indicadores): os CSVs de `qualidade-educacao-superior` (e de qualquer indicador exportado de planilha) deixam de ter o título como nome da 1ª coluna e `column01...` nas demais. As linhas do topo vazias ou só com a 1ª célula preenchida ("Ministério da Educação;;;", "Resultados ENADE 2004;;;", "CONCEITO ENADE - 2012;;;") são puladas (o DuckDB lê o original com `skip=N`, sem reescrever) e o cabeçalho é a primeira linha com duas células ou mais que não seja só de números. Colunas sem nome **e** sem nenhum valor (o `;;;;` no fim das linhas, até 16382 colunas no conceito ENADE 2017) saem (só aí o CSV é reescrito, preservando o texto bruto dos campos, aspas incluídas); coluna sem nome com valor fica como `columnNN` e coluna nomeada e vazia também fica. O separador detectado na 1ª linha só é trocado quando não separa o cabeçalho (menos de duas células) e outro separador o divide em duas ou mais; nesse caso vale o que der mais células. Aspa que abre e não fecha vale como texto passado de 1000 linhas ou 1 MB acumulados, sem perder nenhuma linha. A limpeza é em fluxo (stdlib, memória constante) e só roda nos grupos de indicadores; os microdados não mudam.

## [0.7.0] - 2026-11-14

### Corrigido
- `lake`: as planilhas de todos os indicadores (`taxas-transicao`, `taxas-rendimento-escolar`, `taxas-distorcao-idade-serie`, `taxas-nao-resposta`, `adequacao-formacao-docente`, `esforco-docente`, `media-alunos-por-turma`, `media-horas-aula-diaria`, `complexidade-gestao-escola`, `regularidade-corpo-docente`, `docentes-curso-superior`, `docentes-pos-graduacao`, `remuneracao-docentes`, `trajetoria-educacao-superior`, `nivel-socioeconomico`...) deixam de gerar colunas `__UNNAMED__N`, `coluna_N` e linhas de título, cabeçalho e nota como se fossem dados. O leitor acha o cabeçalho real: pula título e notas acima da tabela, junta 2 a 4 níveis mesclados num nome só (`Taxa de Promoção - Ensino Fundamental - Anos Iniciais`), tira asteriscos e remissões de nota (`Média6`, `docentes1,2`, `(1)`), ignora a linha de nomes técnicos (`NU_ANO_CENSO`) onde há rótulo legível e usa-a onde falta, tira o rodapé (`Fonte:`, `Notas:`), lê `--`, `-`, `...` e `*` como nulo e devolve as colunas numéricas tipadas. O ano no fim do rótulo (`Taxa de Aprovação - 2007`), o título de faixa mesclado sobre as colunas-chave (`Ano`, `Região`...) e o título descritivo longo repetido em todas as colunas não entram no nome, que fica estável entre as edições. Código com zero à esquerda (`04`, `0012`) continua texto, `*`, `**` e `***` valem "sem dado", os decimais voltam com a precisão da planilha (sem corte em 9 casas) e rodapé de duas células, cabeçalho só de anos e primeira linha de dados vazia ou com sigilo `x` não são confundidos com dado ou cabeçalho. O corpo é lido como texto e tipado depois: texto que aparece no meio da coluna (`A123`, `0012`, `.`, `#NAME?`) não é anulado nem convertido, e as linhas vazias do começo da folha (INSE 2015 e por escola) não deslocam mais o cabeçalho. O `x` de sigilo da fonte continua como texto, como as letras de legenda (`a`, `c`, `d`): o lake espelha a fonte. Planilhas que já começam no cabeçalho não mudam.
- `financeiros`: o rótulo da última coluna de um grupo não vale mais para a primeira coluna do grupo vizinho (em `variacao-investimento`, `Ensino Médio` e `Educação Superior` saíam com `De 5ª a 8ª séries`; em `investimento-estudante-duracao-teorica`, `Educação Superior` entrava no nome de uma coluna de outro grupo), e o asterisco de nota sai de `Duração Teórica do Ensino * (anos)`.
- `nivel-socioeconomico` (INSE 2015 e por escola): o título e a nota acima da linha de nomes deixam de entrar como dados e as colunas ganham o nome técnico (`CO_ESCOLA`, `NOME_ESCOLA`...) em vez de `coluna_N`.

## [0.6.1] - 2026-11-14

### Corrigido
- `nivel-socioeconomico` (INSE 2019, estados e municípios): a nota de rodapé que vem *acima* do cabeçalho deixa de virar o nome de uma coluna (as demais ficavam `__UNNAMED__N`). O cabeçalho é a primeira linha com duas células ou mais; as notas saem e o asterisco de remissão dos nomes (`MEDIA_INSE*`) também. Os arquivos de 2021 e 2023 não mudam.

## [0.6.0] - 2026-11-14

### Corrigido
- `financeiros` e `fluxo-educacao-superior`: as planilhas com título e cabeçalho em vários níveis viram colunas com nomes estáveis (níveis unidos por " - ", título e nota de rodapé fora; `--`, `-`, `...` e `*` como nulo; valores numéricos tipados). Antes o título entrava no nome da coluna (acima de 128 caracteres, com quebras de linha). Os demais indicadores continuam lidos como antes.

### Adicionado
- O fetcher declara os fatos da fonte (`FetcherInfo`: id canônico, apelidos, órgão, licença, página e cadência) para o registro de fetchers da Quantilica.

### Alterado
- Requer `quantilica-core>=0.19.0` (e `quantilica-cli>=0.17.0` como host).
- `FetcherInfo.licenca` passa a declarar a licença da fonte: Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016.

## [0.5.6] - 2026-11-07

### Corrigido
- `lake`: CSV separado por `|` passa a ser reconhecido (o separador é o mais frequente na primeira linha, entre `;`, `,`, `|` e tabulação). No SAEB 2021 e 2023, os arquivos da educação infantil, do diretor (2021) e do secretário municipal usam `|` e eram recusados pela verificação de separador da 0.5.5; antes dela, viravam tabelas de uma coluna só.

## [0.5.5] - 2026-11-07

### Adicionado
- `lake`: microdados do SAEB de 1995, 1997, 1999, 2001, 2003 e 2005 (TXT de largura fixa) passam a ser convertidos. O layout vem dos scripts SAS que acompanham os dados (`INPUT_SAS_*.sas`, em 2005 `IMPUT_SAS_*.sas`): cada TXT vira um Parquet com uma coluna por campo, texto sem espaços nas pontas, números tipados (informato `w.d` sem ponto no campo divide por 10^d, como no SAS) e vazio como nulo. O TXT é pareado ao script pelo nome do `INFILE`. Os ZIPs dentro do ZIP de 1999 (`DADOS/ALUNOS.zip` etc.) são extraídos. Script com campos sobrepostos ou além do `LRECL`, TXT sem layout e layout sem TXT são listados em `result.errors` sem interromper os demais arquivos.

### Corrigido
- `lake`: no SAEB 1999, os sete arquivos da 3ª série (`*_03ANO`) declaram no script os campos `GAB_Bl1` a `GAB_Bl3` depois do fim das linhas. Como no SAS com `MISSOVER`, campo que começa depois do fim dos dados vira coluna nula, com aviso no log, em vez de impedir a conversão.
- `lake`: o script do SAEB 1999 de escolas (`escolas_99.txt`) tem campos sobrepostos (`ESTRATO` e `UPA`) e não bate com os dados. Uma correção específica desloca uma coluna os campos a partir de `UPA`, e só é aplicada depois de conferir nos dados (ponto decimal em `PESO_EC`, faixas de `DEP_ADM` e `LOCAL`); se os dados não confirmarem, o arquivo é listado como erro.
- `lake`: TXT de dados sem separador de colunas detectado (largura fixa lida como CSV) deixa de virar tabela de uma coluna só e passa a ser erro. Antes, SAEB 1995, 1997, 2001, 2003 e 2005 gravavam essas tabelas sem aviso e o de 1999 falhava com "nenhum arquivo de dados encontrado".

## [0.5.4] - 2026-11-07

### Corrigido
- `lake`: em ZIPs com pasta `DADOS/` (ENEM, SAEB, censos), só o que está nela é lido como dado. No ENEM 2023, os cadernos de prova em texto para leitor de tela (`PROVAS E GABARITOS/*_DOSVOX_*.txt`) eram lidos como CSV: um virava tabela sem sentido e outro interrompia a conversão com `CSV Error on Line: 626`.
- `lake`: o filtro de documentação compara nomes sem acento, então `DICIONÁRIO/` deixa de entrar no lake como dado.

## [0.5.3] - 2026-11-06

### Corrigido
- O extra `analysis` passa a declarar `fastexcel`, necessário para ler planilhas `.xlsx`/`.xls` na conversão para o lake; sem ele a conversão de indicadores em Excel falhava em instalações limpas.

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
