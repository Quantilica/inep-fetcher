---
dataset:
  id: fluxo-educacao-superior
  fonte: inep
  titulo: Indicadores — Fluxo da educação superior (graduação)
  resumo: Taxas de evasão, conclusão, retenção e permanência na graduação, por atributos do aluno, para Brasil, regiões e UFs.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual; série 2010 a 2024 no arquivo
  cobertura:
    inicio: '2010'
    fim: '2024'
  unidade: um ano de fluxo (par de anos subsequentes) por recorte geográfico, com a taxa por atributo do aluno
  granularidade:
    espacial: Brasil, grande região e UF
    temporal: ano
  formato_bruto: ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 23
  unidades_de_medida:
    Ano Fluxo: ano ou código
    Total: '%'
    Sexo - Feminino: '%'
    Sexo - Masculino: '%'
    Cor-Raça - Amarela: '%'
    Cor-Raça - Branca: '%'
    Cor-Raça - Indígena: '%'
    Cor-Raça - Parda: '%'
    Cor-Raça - Preta: '%'
    Cor-Raça - Sem Declaração 1: '%'
    Faixa de Idade - Até 19 anos: '%'
    Faixa de Idade - 20 a 22 anos: '%'
    Faixa de Idade - 23 e 24 anos: '%'
    Faixa de Idade - 25 a 29 anos: '%'
    Faixa de Idade - 30 a 39 anos: '%'
    Faixa de Idade - 40 a 49 anos: '%'
    Faixa de Idade - 50 anos ou mais: '%'
    Deficiência - Sim: '%'
    Deficiência - Não: '%'
    Preto/Pardo/Indígena (PPI) - Sim: '%'
    Preto/Pardo/Indígena (PPI) - Não 1: '%'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Indicadores — Fluxo da educação superior (graduação)

## Resumo

Indicadores de fluxo da educação superior do Inep (taxas de evasão, conclusão, retenção e permanência em cursos de graduação), calculados do acompanhamento longitudinal de dois anos subsequentes e organizados por atributos do aluno (sexo, cor/raça, faixa de idade, deficiência).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/fluxo-educacao-superior` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual; série 2010 a 2024 no arquivo |
| Cobertura | 2010 a 2024 |
| Unidade (uma linha) | um ano de fluxo (par de anos subsequentes) por recorte geográfico, com a taxa por atributo do aluno |
| Granularidade | espacial: Brasil, grande região e UF; temporal: ano |
| Formato bruto | ZIP (ou XLSX/XLS/CSV avulso) com planilhas com título, notas e fonte acima e abaixo da tabela; cabeçalho de dois a quatro níveis |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 23 |
| Unidades de medida | `Ano Fluxo`: ano ou código; `Total`: %; `Sexo - Feminino`: %; `Sexo - Masculino`: %; `Cor-Raça - Amarela`: %; `Cor-Raça - Branca`: %; `Cor-Raça - Indígena`: %; `Cor-Raça - Parda`: %; `Cor-Raça - Preta`: %; `Cor-Raça - Sem Declaração 1`: %; `Faixa de Idade - Até 19 anos`: %; `Faixa de Idade - 20 a 22 anos`: %; `Faixa de Idade - 23 e 24 anos`: %; `Faixa de Idade - 25 a 29 anos`: %; `Faixa de Idade - 30 a 39 anos`: %; `Faixa de Idade - 40 a 49 anos`: %; `Faixa de Idade - 50 anos ou mais`: %; `Deficiência - Sim`: %; `Deficiência - Não`: %; `Preto/Pardo/Indígena (PPI) - Sim`: %; `Preto/Pardo/Indígena (PPI) - Não 1`: % |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O catálogo do fetcher tem 3 arquivo(s) para este conjunto; exemplo de URL: `https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/indicadores_fluxo_UF_2010_2024.zip`.
- No bruto, cada arquivo se chama `indicadores/fluxo-educacao-superior/<id do catálogo>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação na fonte.
- Os ZIP trazem uma planilha por recorte (por exemplo Brasil, regiões geográficas e UFs; municípios; escolas) e, às vezes, notas técnicas.

## Conteúdo

- Planilhas por indicador: `TX_EVASAO`, `TX_CONCLUSAO`, `TX_RETENCAO` e `TX_PERMANENCIA`.
- Título da planilha de evasão: "Taxa de Evasão de Alunos no Sistema de Educação Superior (Graduação)", calculada do acompanhamento longitudinal de dois anos subsequentes, por atributos do aluno.
- Há arquivos para Brasil, regiões e UFs, com período 2010 a 2024 no nome; o lake guarda o primeiro ano do período na partição `ano`.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2010 | `indic_brasil` (19); `indic_regiao` (20); `indic_uf` (16) |

## Variáveis

A fonte não publica dicionário de variáveis para estes indicadores: o significado de cada coluna está no título da planilha, nos cabeçalhos e nas notas de rodapé. A descrição de cada coluna abaixo é derivada do nome da coluna no lake, que reúne os níveis do cabeçalho da planilha separados por ` - `.
A coluna *Arquivos* diz de que arquivo do lake vem a coluna (o nome do arquivo sem o ano); a coluna *Período* diz em que edições ela existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano Fluxo` | `Ano Fluxo` | texto | Coluna «Ano Fluxo» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Total` | `Total` | decimal | Coluna «Total» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Sexo - Feminino` | `Sexo - Feminino` | decimal | Valor de «Sexo» no recorte «Feminino»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Sexo - Masculino` | `Sexo - Masculino` | decimal | Valor de «Sexo» no recorte «Masculino»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Cor-Raça - Amarela` | `Cor-Raça - Amarela` | decimal | Valor de «Cor-Raça» no recorte «Amarela»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Cor-Raça - Branca` | `Cor-Raça - Branca` | decimal | Valor de «Cor-Raça» no recorte «Branca»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Cor-Raça - Indígena` | `Cor-Raça - Indígena` | decimal | Valor de «Cor-Raça» no recorte «Indígena»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Cor-Raça - Parda` | `Cor-Raça - Parda` | decimal | Valor de «Cor-Raça» no recorte «Parda»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Cor-Raça - Preta` | `Cor-Raça - Preta` | decimal | Valor de «Cor-Raça» no recorte «Preta»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Cor-Raça - Sem Declaração 1` | `Cor-Raça - Sem Declaração 1` | decimal | Valor de «Cor-Raça» no recorte «Sem Declaração 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao` |
| `Faixa de Idade - Até 19 anos` | `Faixa de Idade - Até 19 anos` | decimal | Valor de «Faixa de Idade» no recorte «Até 19 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 20 a 22 anos` | `Faixa de Idade - 20 a 22 anos` | decimal | Valor de «Faixa de Idade» no recorte «20 a 22 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 23 e 24 anos` | `Faixa de Idade - 23 e 24 anos` | decimal | Valor de «Faixa de Idade» no recorte «23 e 24 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 25 a 29 anos` | `Faixa de Idade - 25 a 29 anos` | decimal | Valor de «Faixa de Idade» no recorte «25 a 29 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 30 a 39 anos` | `Faixa de Idade - 30 a 39 anos` | decimal | Valor de «Faixa de Idade» no recorte «30 a 39 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 40 a 49 anos` | `Faixa de Idade - 40 a 49 anos` | decimal | Valor de «Faixa de Idade» no recorte «40 a 49 anos»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Faixa de Idade - 50 anos ou mais` | `Faixa de Idade - 50 anos ou mais` | decimal | Valor de «Faixa de Idade» no recorte «50 anos ou mais»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Deficiência - Sim` | `Deficiência - Sim` | decimal | Valor de «Deficiência» no recorte «Sim»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Deficiência - Não` | `Deficiência - Não` | decimal | Valor de «Deficiência» no recorte «Não»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_brasil`, `indic_regiao`, `indic_uf` |
| `Região Geográfica` | `Região Geográfica` | texto | Coluna «Região Geográfica» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `indic_regiao` |
| `Unidade da Federação` | `Unidade da Federação` | texto | Coluna «Unidade da Federação» da planilha; descrição derivada do cabeçalho, que a fonte não explica à parte | — | todo | `indic_uf` |
| `Preto/Pardo/Indígena (PPI) - Sim` | `Preto/Pardo/Indígena (PPI) - Sim` | decimal | Valor de «Preto/Pardo/Indígena (PPI)» no recorte «Sim»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_uf` |
| `Preto/Pardo/Indígena (PPI) - Não 1` | `Preto/Pardo/Indígena (PPI) - Não 1` | decimal | Valor de «Preto/Pardo/Indígena (PPI)» no recorte «Não 1»; descrição derivada do cabeçalho da planilha, que a fonte não explica à parte | — | todo | `indic_uf` |

## No lake

- Dataset `inep/fluxo-educacao-superior`, particionado por `ano` (tirado do nome do arquivo de origem)
- Um Parquet por planilha. O conversor acha o cabeçalho real, junta os níveis num nome só (` - `), tira título, notas e rodapé e tipa as colunas (número ou texto).
- Nesta documentação, o esquema de referência vem de conversão local, com o conversor atual, dos arquivos do catálogo.
- Nomes de coluna saem como estão na planilha (com maiúsculas, acentos e espaços). Nesta página, espaços nas pontas foram removidos e `|` virou `/`, porque a verificação da documentação não os aceita.

## Cuidados de uso

- **Os nomes de coluna mudam entre edições.** Os títulos das planilhas e os níveis do cabeçalho variam; junte edições pelo nome e confira a coluna *Período*.
- **Tipos mistos.** Uma coluna que aparece com mais de um tipo no esquema (número e texto) é número em umas edições e texto em outras, por exemplo por causa de marcadores de ausência ou sigilo da planilha; faça o cast ao empilhar.
- **Colunas de identificação variam por recorte.** Os arquivos de Brasil, regiões e UFs, de municípios e de escolas têm colunas diferentes; as linhas de totais (Brasil, região) convivem com as de UF no mesmo arquivo.
- **Descrições derivadas do cabeçalho.** A fonte não traz dicionário; consulte o título e as notas da planilha de origem e a nota técnica do Inep para a definição do indicador.

## Exemplos

Primeiras linhas do arquivo `indic_brasil_2010_2024.parquet` da edição mais recente do lake (ano 2010):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano Fluxo", "Total", "Sexo - Feminino"
    FROM read_parquet('lake/inep/fluxo-educacao-superior/ano=2010/indicadores-fluxo-educacao-superior-indicadores-fluxo-brasil-2010-2024__indic_brasil_2010_2024.parquet')
    LIMIT 10
""").show()
```

## Referências

- Indicadores Educacionais do Inep: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
