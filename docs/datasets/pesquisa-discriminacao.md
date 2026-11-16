---
dataset:
  id: pesquisa-discriminacao
  fonte: inep
  titulo: Pesquisa de Ações Discriminatórias no Âmbito Escolar 2008 — microdados
  resumo: Microdados da pesquisa de 2008 sobre preconceito e discriminação em escolas públicas, com diretores, professores, funcionários, alunos e pais.
  orgao: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep)
  pagina_oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pesquisa-de-acoes-discriminatorias-no-ambito-escolar
  licenca: Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: levantamento único, referente a 2008; o Leia-me é datado de fevereiro de 2010
  cobertura:
    inicio: '2008'
    fim: '2008'
  unidade: um respondente do questionário (diretor, professor, funcionário, aluno ou pai/mãe), identificado pela coluna `publico`
  granularidade:
    espacial: escola amostrada, por estrato, região, UF e código de município do respondente; a fonte não traz o código da escola
    temporal: ano de referência da pesquisa (2008)
  formato_bruto: ZIP com arquivo TXT de largura fixa sem cabeçalho (2.601 caracteres por linha, na pasta DADOS), os mesmos dados em SAS (sas7bdat) e SPSS (sav), programas de leitura SAS e SPSS (INPUTS) e Leia-me em PDF (LEIA-ME)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 325
  unidades_de_medida:
    m_oh: matrículas
    n_h: escolas
    m_hi: matrículas
    n_hi: respondentes
    peso: peso de expansão do respondente (sem unidade)
    v0316: anos de idade
    v0256: anos
    v0258: anos
    v0259: anos
    v0265: anos
    v0266: anos
    v0268: anos
    v0269: meses
    v0283: irmãos
    v0284: filhos
    v0285: pessoas
    v0234: ano civil
    v0237: ano civil
    v0240: ano civil
    v0243: ano civil
    v0246: ano civil
    v0249: ano civil
    v0252: ano civil
    v0255: ano civil
    publico: código do público (1 a 5; sem unidade)
    v0001: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0002: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0003: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0004: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0005: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0006: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0007: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0008: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0009: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0010: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0011: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0012: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0013: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0014: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0015: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0016: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0017: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0018: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0019: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0020: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0021: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0022: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0023: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0024: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0025: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0026: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0027: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0028: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0029: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0030: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0031: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0032: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0033: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0034: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0035: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0036: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0037: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0038: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0039: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0040: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0041: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0042: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0043: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0044: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0045: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0046: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0047: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0048: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0049: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0050: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0051: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0052: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0053: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0054: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0055: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0056: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0057: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0058: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0059: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0060: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0061: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0062: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0063: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0064: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0065: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0066: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0067: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0068: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0069: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0070: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0071: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0072: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0073: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0074: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0075: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0076: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0077: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0078: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0079: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0080: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0081: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0082: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0083: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0084: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0085: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0086: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0087: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0088: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0089: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0090: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0091: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0092: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0093: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0094: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0095: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0096: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0097: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0098: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0099: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0100: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0101: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0102: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0103: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0104: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0105: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0106: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0107: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0108: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0109: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0110: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0111: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0112: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0113: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0114: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0115: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0116: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0117: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0118: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0119: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0120: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0121: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0122: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0123: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0124: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0125: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0126: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0127: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0128: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0129: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0130: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0131: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0132: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0133: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0134: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0135: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0136: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0137: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0138: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0139: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0140: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0141: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0142: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0143: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0144: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0145: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0146: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0147: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0148: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0149: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0150: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0151: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0152: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0153: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0154: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0155: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0156: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0157: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0158: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0159: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0160: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0161: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0162: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0163: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0164: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0165: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0166: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0167: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0168: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0169: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0170: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0171: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0172: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0173: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0174: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0175: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0176: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0177: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0178: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0179: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0180: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0181: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0182: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0183: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0184: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0185: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0186: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0187: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0188: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0189: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0190: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0191: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0192: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0193: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0194: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0195: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0196: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0197: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0198: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0199: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0200: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0201: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0202: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0203: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0204: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0205: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0206: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0207: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0208: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0209: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0210: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0211: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0212: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0213: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0214: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0215: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0216: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0217: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0218: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0219: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0220: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0221: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0222: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0223: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0224: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0225: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0226: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0227: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0228: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0229: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0230: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0231: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0232: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0233: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0235: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0236: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0238: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0239: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0241: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0242: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0244: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0245: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0247: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0248: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0250: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0251: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0253: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0254: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0257: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0260: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0261: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0262: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0263: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0264: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0267: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0270: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0271: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0272: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0273: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0274: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0275: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0276: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0277: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0278: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0279: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0280: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0281: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0282: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0286: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0287: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0288: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0289: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0290: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0291: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0292: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0293: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0294: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0295: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0296: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0297: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0298: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0299: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0300: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0301: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0302: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0303: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0304: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0305: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0306: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0307: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0308: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0309: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0310: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0311: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0312: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0313: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0314: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
    v0315: código de resposta, sem unidade (códigos na coluna Unidade / códigos)
  dados_pessoais:
  - coluna: v0002
    categoria: município do respondente (código)
  - coluna: v0008
    categoria: religião e participação religiosa do respondente
  - coluna: v0009
    categoria: religião e participação religiosa do respondente
  - coluna: v0010
    categoria: religião e participação religiosa do respondente
  - coluna: v0228
    categoria: sexo do respondente
  - coluna: v0229
    categoria: cor ou etnia do respondente
  - coluna: v0316
    categoria: idade do respondente
  - coluna: v0272
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0273
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0274
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0275
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0276
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0277
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0278
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0279
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0280
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0281
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0282
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0283
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0284
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0285
    categoria: com quem o aluno mora e número de filhos (aluno)
  - coluna: v0267
    categoria: escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente
  - coluna: v0288
    categoria: escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente
  - coluna: v0312
    categoria: escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente
  eras:
  - desde: '2008'
    mudanca: 'única edição: levantamento de 2008, publicado com Leia-me de fevereiro de 2010'
  revisado_em: '2026-11-15'
  versao_fetcher: 0.7.1
---

# Pesquisa de Ações Discriminatórias no Âmbito Escolar 2008 — microdados

## Resumo

Microdados do Estudo sobre as Ações Discriminatórias no Âmbito Escolar, feito em 2008 pela Fundação Instituto de Pesquisas Econômicas (Fipe/USP) para o Inep, num survey em 500 escolas públicas estaduais e municipais de todo o país. Cinco questionários de autopreenchimento mediram percepções, atitudes e conhecimento de práticas discriminatórias (gênero, raça e etnia, condição socioeconômica, geração, deficiência, território e orientação sexual) entre diretores, professores, funcionários, alunos e pais ou mães de membros do Conselho Escolar ou da Associação de Pais e Mestres. Todos os respondentes ficam num único arquivo, com 18.599 linhas na fonte.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `inep/pesquisa-discriminacao` |
| Órgão | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) |
| Página oficial | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pesquisa-de-acoes-discriminatorias-no-ambito-escolar |
| Licença | Não informada especificamente para este conjunto; o portal do Inep declara que todo o conteúdo do site está sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | levantamento único, referente a 2008; o Leia-me é datado de fevereiro de 2010 |
| Cobertura | 2008 a 2008 |
| Unidade (uma linha) | um respondente do questionário (diretor, professor, funcionário, aluno ou pai/mãe), identificado pela coluna `publico` |
| Granularidade | espacial: escola amostrada, por estrato, região, UF e código de município do respondente; a fonte não traz o código da escola; temporal: ano de referência da pesquisa (2008) |
| Formato bruto | ZIP com arquivo TXT de largura fixa sem cabeçalho (2.601 caracteres por linha, na pasta DADOS), os mesmos dados em SAS (sas7bdat) e SPSS (sav), programas de leitura SAS e SPSS (INPUTS) e Leia-me em PDF (LEIA-ME) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 325 |
| Unidades de medida | `m_oh`: matrículas; `n_h`: escolas; `m_hi`: matrículas; `n_hi`: respondentes; `peso`: peso de expansão do respondente (sem unidade); `v0316`: anos de idade; `v0256`: anos; `v0258`: anos; `v0259`: anos; `v0265`: anos; `v0266`: anos; `v0268`: anos; `v0269`: meses; `v0283`: irmãos; `v0284`: filhos; `v0285`: pessoas; `v0234`: ano civil; `v0237`: ano civil; `v0240`: ano civil; `v0243`: ano civil; `v0246`: ano civil; `v0249`: ano civil; `v0252`: ano civil; `v0255`: ano civil; `publico`: código do público (1 a 5; sem unidade); `v0001`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0002`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0003`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0004`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0005`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0006`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0007`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0008`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0009`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0010`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0011`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0012`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0013`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0014`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0015`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0016`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0017`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0018`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0019`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0020`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0021`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0022`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0023`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0024`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0025`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0026`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0027`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0028`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0029`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0030`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0031`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0032`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0033`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0034`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0035`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0036`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0037`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0038`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0039`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0040`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0041`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0042`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0043`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0044`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0045`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0046`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0047`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0048`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0049`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0050`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0051`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0052`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0053`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0054`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0055`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0056`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0057`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0058`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0059`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0060`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0061`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0062`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0063`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0064`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0065`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0066`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0067`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0068`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0069`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0070`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0071`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0072`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0073`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0074`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0075`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0076`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0077`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0078`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0079`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0080`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0081`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0082`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0083`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0084`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0085`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0086`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0087`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0088`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0089`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0090`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0091`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0092`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0093`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0094`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0095`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0096`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0097`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0098`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0099`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0100`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0101`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0102`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0103`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0104`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0105`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0106`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0107`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0108`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0109`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0110`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0111`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0112`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0113`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0114`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0115`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0116`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0117`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0118`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0119`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0120`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0121`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0122`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0123`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0124`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0125`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0126`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0127`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0128`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0129`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0130`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0131`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0132`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0133`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0134`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0135`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0136`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0137`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0138`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0139`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0140`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0141`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0142`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0143`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0144`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0145`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0146`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0147`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0148`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0149`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0150`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0151`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0152`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0153`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0154`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0155`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0156`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0157`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0158`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0159`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0160`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0161`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0162`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0163`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0164`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0165`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0166`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0167`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0168`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0169`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0170`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0171`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0172`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0173`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0174`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0175`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0176`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0177`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0178`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0179`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0180`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0181`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0182`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0183`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0184`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0185`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0186`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0187`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0188`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0189`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0190`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0191`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0192`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0193`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0194`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0195`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0196`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0197`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0198`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0199`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0200`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0201`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0202`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0203`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0204`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0205`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0206`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0207`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0208`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0209`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0210`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0211`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0212`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0213`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0214`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0215`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0216`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0217`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0218`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0219`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0220`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0221`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0222`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0223`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0224`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0225`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0226`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0227`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0228`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0229`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0230`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0231`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0232`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0233`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0235`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0236`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0238`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0239`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0241`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0242`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0244`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0245`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0247`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0248`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0250`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0251`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0253`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0254`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0257`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0260`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0261`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0262`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0263`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0264`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0267`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0270`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0271`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0272`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0273`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0274`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0275`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0276`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0277`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0278`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0279`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0280`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0281`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0282`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0286`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0287`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0288`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0289`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0290`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0291`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0292`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0293`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0294`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0295`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0296`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0297`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0298`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0299`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0300`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0301`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0302`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0303`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0304`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0305`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0306`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0307`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0308`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0309`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0310`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0311`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0312`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0313`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0314`: código de resposta, sem unidade (códigos na coluna Unidade / códigos); `v0315`: código de resposta, sem unidade (códigos na coluna Unidade / códigos) |
| Dados pessoais | `v0002` (município do respondente (código)); `v0008` (religião e participação religiosa do respondente); `v0009` (religião e participação religiosa do respondente); `v0010` (religião e participação religiosa do respondente); `v0228` (sexo do respondente); `v0229` (cor ou etnia do respondente); `v0316` (idade do respondente); `v0272` (com quem o aluno mora e número de filhos (aluno)); `v0273` (com quem o aluno mora e número de filhos (aluno)); `v0274` (com quem o aluno mora e número de filhos (aluno)); `v0275` (com quem o aluno mora e número de filhos (aluno)); `v0276` (com quem o aluno mora e número de filhos (aluno)); `v0277` (com quem o aluno mora e número de filhos (aluno)); `v0278` (com quem o aluno mora e número de filhos (aluno)); `v0279` (com quem o aluno mora e número de filhos (aluno)); `v0280` (com quem o aluno mora e número de filhos (aluno)); `v0281` (com quem o aluno mora e número de filhos (aluno)); `v0282` (com quem o aluno mora e número de filhos (aluno)); `v0283` (com quem o aluno mora e número de filhos (aluno)); `v0284` (com quem o aluno mora e número de filhos (aluno)); `v0285` (com quem o aluno mora e número de filhos (aluno)); `v0267` (escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente); `v0288` (escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente); `v0312` (escolaridade do funcionário, da mãe do aluno ou do pai/mãe respondente) |
| Eras | 2008: única edição: levantamento de 2008, publicado com Leia-me de fevereiro de 2010 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.7.1 |

## Origem e coleta

- O fetcher baixa `https://download.inep.gov.br/microdados/microdados_pesquisa_acoes_discriminatorias_ambito_escolar_2008.zip` (10.040.792 bytes; última modificação na fonte em 2022-10-21, lido em 2026-11-15). A página oficial lista só esta edição.
- No bruto, o arquivo se chama `pesquisa-discriminacao/pesquisa-discriminacao-microdados_2008@AAAAMMDD.zip`, em que o sufixo é a data de modificação na fonte.
- O ZIP guarda tudo numa pasta cujo nome tem um erro de digitação (`mcrodados_pesquisa_acoes_discriminatorias_ambito_escolar_2008`). Em `DADOS` há `Microdados_200906.txt` (48.413.197 bytes), `Microdados_200906.sas7bdat` (50.856.960), `Microdados_200906.sav` (7.068.909) e um `hs_err_pid4036.log` (6.361 bytes, registro de falha de uma máquina virtual Java, sem relação com os dados). Em `INPUTS` há `input sas Microdados_200906.sas` e `input spss Microdados_200906.sps`; em `LEIA-ME` há `LEIA-ME.pdf` (7.459.640 bytes).
- O conversor lê só o TXT, usando as posições das colunas do programa SAS; os arquivos sas7bdat e sav e o log ficam de fora. O TXT tem 18.599 linhas na fonte (conferido em 2026-11-15), de 2.601 caracteres cada, sem cabeçalho.
- **Não há dicionário em planilha.** O dicionário de variáveis está no Leia-me em PDF (páginas 7 a 39, com tipo, tamanho, rótulo e códigos) e os mesmos rótulos e códigos estão nos comandos VARIABLE LABELS e VALUE LABELS do `input spss Microdados_200906.sps`; as descrições desta página vêm do programa SPSS e foram conferidas no PDF. O Leia-me traz ainda os questionários, o relatório final dos microdados e o relatório analítico, com o plano amostral e o cálculo dos pesos.

## Conteúdo

- **Um arquivo, cinco públicos.** O arquivo `microdados_200906` junta todos os respondentes. A coluna `publico` diz quem respondeu: 1 = diretores, 2 = professores, 3 = funcionários, 4 = alunos e 5 = pais e mães. Contagens na fonte: 501 diretores, 1.005 professores, 1.004 funcionários, 15.087 alunos e 1.002 pais ou mães.
- **Quem respondeu a cada pergunta.** O rótulo de cada variável começa pelo público que a respondeu: `Todos`, `Dir`, `Prof`, `Func`, `Alun`, `Pais` ou combinações como `Dir/Prof` e `Alun/Pais`. Para os demais públicos a coluna fica vazia (por exemplo, `v0261`, a forma como o diretor assumiu a direção, só tem valor nas 498 linhas de diretores que a responderam).
- **Desenho amostral.** A amostra reúne 500 escolas públicas, sorteadas por probabilidade proporcional ao número de matrículas das séries-alvo em 35 estratos (região, capital ou não capital de UF, rural, e nível ou modalidade de ensino: fundamental, médio e EJA). As colunas `estrato`, `m_oh`, `n_h`, `m_hi`, `n_hi` e `peso` descrevem o desenho e o peso do respondente.
- **Blocos de assunto.** Mídia, lazer, escala de distância social, crenças e atitudes, conhecimento de práticas discriminatórias (humilhação, agressão, acusação injusta, desprezo, negação de vaga, exclusão de atividades), questões sociodemográficas e questões escolares.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2008 | `microdados06` (325) |

## Variáveis

As descrições e os códigos vêm do programa SPSS (`VARIABLE LABELS` e `VALUE LABELS`) e do dicionário do Leia-me; as 325 colunas do arquivo têm rótulo. O prefixo do rótulo (`Todos`, `Dir`, `Prof`, `Func`, `Alun`, `Pais` e combinações) indica qual público respondeu a pergunta.
Valores ausentes ficam vazios. Em perguntas de marcação (como `Alun - Mora com a mãe`), a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `estrato` | `ESTRATO` | texto | estrato | — | todo |
| `m_oh` | `M_OH` | inteiro | matricula total no estrato | — | todo |
| `n_h` | `N_H` | inteiro | numero de escolas no estrato | — | todo |
| `m_hi` | `M_HI` | inteiro | matricula na escola i do estrato h | — | todo |
| `n_hi` | `N_HI` | inteiro | numero de pais / maes estudados na escola i do estrato h | — | todo |
| `peso` | `PESO` | decimal | peso | — | todo |
| `regiao` | `REGIAO` | texto | região da escola | C = Centro-Oeste; SE = Sudeste; N = Norte; NE = Nordeste; S = Sul | todo |
| `uf` | `UF` | texto | uf da escola | 11 = RO; 12 = AC; 13 = AM; 14 = RR; 15 = PA; 16 = AP; 17 = TO; 21 = MA; 22 = PI; 23 = CE; 24 = RN; 25 = PB; 26 = PE; 27 = AL; 28 = SE; 29 = BA; 31 = MG; 32 = ES; 33 = RJ; 35 = SP; 41 = PR; 42 = SC; 43 = RS; 50 = MS; 51 = MT; 52 = GO; 53 = DF | todo |
| `v0001` | `V0001` | inteiro | Prof/Alun - Modalidade | 1 = Ensino Fundamental; 2 = Ensino Médio; 3 = EJA Fundamental; 4 = EJA Médio | todo |
| `v0002` | `V0002` | inteiro | Todos - Código do Município (código de 7 dígitos, como 3550308; o dicionário não diz se é o do respondente ou o da escola) | — | todo |
| `v0003` | `V0003` | inteiro | Todos - Assiste televisão | 1 = Sim; 2 = Não | todo |
| `v0004` | `V0004` | inteiro | Todos - Ouve rádio | 1 = Sim; 2 = Não | todo |
| `v0005` | `V0005` | inteiro | Todos - Lê jornal | 1 = Sim; 2 = Não | todo |
| `v0006` | `V0006` | inteiro | Todos - Lê revistas de notícias/atualidades | 1 = Sim; 2 = Não | todo |
| `v0007` | `V0007` | inteiro | Todos - Utiliza/acessa internet | 1 = Sim; 2 = Não | todo |
| `v0008` | `V0008` | inteiro | Todos - Tem religião | 1 = Sim; 2 = Não | todo |
| `v0009` | `V0009` | inteiro | Todos - Religião | 1 = Budista; 2 = Candomblé/umbanda; 3 = Católica; 4 = Evangélica; 5 = Espírita; 6 = Judaica; 7 = Muçulmana; 8 = Outras | todo |
| `v0010` | `V0010` | inteiro | Todos - Como considera a participação religiosa | 1 = Muito Participante; 2 = Pouco Participante; 3 = Nada Participante | todo |
| `v0011` | `V0011` | inteiro | Todos - Frase com maior concordância com relação a uma pessoa POBRE | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0012` | `V0012` | inteiro | Todos - Frase com maior concordância com relação a uma pessoa NEGRA | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0013` | `V0013` | inteiro | Todos - Frase com maior concordância com relação a uma pessoa da RAÇA INDÍGENA | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0014` | `V0014` | inteiro | Todos - Frase com maior concordância com relação a um CIGANO(A) | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0015` | `V0015` | inteiro | Todos - Frase com maior concordância com relação a um(a) HOMOSSEXUAL | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0016` | `V0016` | inteiro | Todos - Frase com maior concordância com relação a um(a) MORADOR(A) DE PERIFERIA OU FAVELA | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0017` | `V0017` | inteiro | Todos - Frase com maior concordância com relação a um(a) AGRICULTOR(A), TRABALHADOR(A) OU MORADOR(A) DE ÁREA RURAL | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0018` | `V0018` | inteiro | Todos - Frase com maior concordância com relação a um(a) DEFICIENTE FÍSICO | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0019` | `V0019` | inteiro | Todos - Frase com maior concordância com relação a um(a) DEFICIENTE MENTAL | 1 = Aceitaria como aluno(a) da escola; 2 = Aceitaria que meu (minha) filho(a) se casasse com ele(a); 3 = Aceitaria que estudasse em minha casa com meu(minha) filho(a); 4 = Aceitaria que meu (minha) filho(a) namorasse com ele(a); … (lista completa no dicionário da fonte) | todo |
| `v0020` | `V0020` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0021` | `V0021` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0022` | `V0022` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0023` | `V0023` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0024` | `V0024` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0025` | `V0025` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0026` | `V0026` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0027` | `V0027` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0028` | `V0028` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0029` | `V0029` | inteiro | Todos - ALUNO(A) ter sido humilhado(a) por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0030` | `V0030` | inteiro | Todos - ALUNA ter sido humilhada por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0031` | `V0031` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0032` | `V0032` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0033` | `V0033` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0034` | `V0034` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0035` | `V0035` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0036` | `V0036` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0037` | `V0037` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0038` | `V0038` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0039` | `V0039` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0040` | `V0040` | inteiro | Todos - PROFESSOR(A) ter sido humilhado(a) por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0041` | `V0041` | inteiro | Todos - PROFESSORA ter sido humilhada por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0042` | `V0042` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0043` | `V0043` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0044` | `V0044` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0045` | `V0045` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0046` | `V0046` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0047` | `V0047` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0048` | `V0048` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0049` | `V0049` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0050` | `V0050` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0051` | `V0051` | inteiro | Todos - FUNCIONÁRIO(A) ter sido humilhado(a) por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0052` | `V0052` | inteiro | Todos - FUNCIONÁRIA ter sido humilhada por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0053` | `V0053` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0054` | `V0054` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0055` | `V0055` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0056` | `V0056` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0057` | `V0057` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0058` | `V0058` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0059` | `V0059` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0060` | `V0060` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0061` | `V0061` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0062` | `V0062` | inteiro | Todos - ALUNO(A) ter sido agredido(a) fisicamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0063` | `V0063` | inteiro | Todos - ALUNA ter sido agredida fisicamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0064` | `V0064` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0065` | `V0065` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0066` | `V0066` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0067` | `V0067` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0068` | `V0068` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0069` | `V0069` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0070` | `V0070` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0071` | `V0071` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0072` | `V0072` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0073` | `V0073` | inteiro | Todos - PROFESSOR(A) ter sido agredido(a) fisicamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0074` | `V0074` | inteiro | Todos - PROFESSORA ter sido agredida fisicamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0075` | `V0075` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0076` | `V0076` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0077` | `V0077` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0078` | `V0078` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0079` | `V0079` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0080` | `V0080` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0081` | `V0081` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0082` | `V0082` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0083` | `V0083` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0084` | `V0084` | inteiro | Todos - FUNCIONÁRIO(A) ter sido agredido(a) fisicamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0085` | `V0085` | inteiro | Todos - FUNCIONÁRIA ter sido agredida fisicamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0086` | `V0086` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0087` | `V0087` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0088` | `V0088` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0089` | `V0089` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0090` | `V0090` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0091` | `V0091` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0092` | `V0092` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0093` | `V0093` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0094` | `V0094` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0095` | `V0095` | inteiro | Todos - ALUNO(A) ter sido acusado(a) injustamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0096` | `V0096` | inteiro | Todos - ALUNA ter sido acusada injustamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0097` | `V0097` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0098` | `V0098` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0099` | `V0099` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0100` | `V0100` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0101` | `V0101` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0102` | `V0102` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0103` | `V0103` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0104` | `V0104` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0105` | `V0105` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0106` | `V0106` | inteiro | Todos - PROFESSOR(A) ter sido acusado(a) injustamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0107` | `V0107` | inteiro | Todos - PROFESSORA ter sido acusada injustamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0108` | `V0108` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0109` | `V0109` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0110` | `V0110` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0111` | `V0111` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0112` | `V0112` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0113` | `V0113` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0114` | `V0114` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0115` | `V0115` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0116` | `V0116` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0117` | `V0117` | inteiro | Todos - FUNCIONÁRIO(A) ter sido acusado(a) injustamente por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0118` | `V0118` | inteiro | Todos - FUNCIONÁRIA ter sido acusada injustamente por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0119` | `V0119` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0120` | `V0120` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0121` | `V0121` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0122` | `V0122` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0123` | `V0123` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0124` | `V0124` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0125` | `V0125` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0126` | `V0126` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0127` | `V0127` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0128` | `V0128` | inteiro | Alun/Pais - ALUNO(A) ser tratado(a) com desprezo ou falta de consideração por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0129` | `V0129` | inteiro | Alun/Pais - ALUNA ser tratada com desprezo ou falta de consideração por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0130` | `V0130` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser NEGRO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0131` | `V0131` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser ÍNDIO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0132` | `V0132` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser CIGANO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0133` | `V0133` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser HOMOSSEXUAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0134` | `V0134` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser DEFICIENTE FÍSICO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0135` | `V0135` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser DEFICIENTE MENTAL | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0136` | `V0136` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser POBRE | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0137` | `V0137` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser MORADOR(A) DA PERIFERIA OU FAVELA | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0138` | `V0138` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser MORADOR(A) DO CAMPO AO ASSENTAMENTO | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0139` | `V0139` | inteiro | Prof/Pais - Ter sido negada vaga na escola a um(a) aluno(a) por ser MAIS VELHO(A)/IDOSO(A) | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0140` | `V0140` | inteiro | Prof/Pais - Ter sido negada vaga na escola a uma alunoa por ser MULHER | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0141` | `V0141` | inteiro | Todos - Pessoas (alunos, professores, funcionários) perseguidos ou maltratados por outros alunos | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0142` | `V0142` | inteiro | Todos - Alunos deixarem ou abandonarem a escola por causa de outros alunos | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0143` | `V0143` | inteiro | Todos - Pessoas (alunos, professores, funcionários) com apelidos preconceituosos | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0144` | `V0144` | inteiro | Todos - Alunos serem excluídos de atividades na escola por preconceito ou discriminação | 1 = Vi nesta escola; 2 = Não vi, mas soube que aconteceu nesta escola; 3 = Nem vi, nem soube que aconteceu nesta escola | todo |
| `v0145` | `V0145` | inteiro | Todos - Os brancos em geral, são mais estudiosos que os negros | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0146` | `V0146` | inteiro | Todos - O número de deficientes físicos na escola é muito pequeno para se preocupar com eles | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0147` | `V0147` | inteiro | Todos - Pessoas homossexuais não são confiáveis | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0148` | `V0148` | inteiro | Todos - Depois de certa idade é mais difícil aprender | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0149` | `V0149` | inteiro | Todos - Ciganos não gostam de trabalhar | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0150` | `V0150` | inteiro | Todos - Para dar aulas nas escolas do campo os professores não precisam ser tão preparados quando os da cidade | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0151` | `V0151` | inteiro | Todos - A mulher é melhor do que o homem na cozinha | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0152` | `V0152` | inteiro | Todos - Crianças brancas aprendem mais rápido que crianças negras | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0153` | `V0153` | inteiro | Todos - Os estudantes pobres são mais revoltados | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0154` | `V0154` | inteiro | Todos - Os índios pertencem a uma raça inferior | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0155` | `V0155` | inteiro | Todos - Os estudantes cegos deveriam estudar numa escola especial para portadores de deficiência visual | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0156` | `V0156` | inteiro | Todos - Os negros são mais violentos que os brancos | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0157` | `V0157` | inteiro | Todos - Não evito, mas também não procuro chegar perto de homossexuais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0158` | `V0158` | inteiro | Todos - Os estudantes do campo são mais lentos para aprender | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0159` | `V0159` | inteiro | Todos - Os professores mais velhos têm menos capacidade para ensinar | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0160` | `V0160` | inteiro | Todos - Homens não devem trabalhar na cantina das escolas | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0161` | `V0161` | inteiro | Todos - Professor de escola de periferia não precisa se vestir bem | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0162` | `V0162` | inteiro | Todos - Índio não tem cabeça para estudar coisas de branco | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0163` | `V0163` | inteiro | Todos - Negro tem corpo bom para trabalho braçal | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0164` | `V0164` | inteiro | Todos - Um professor deficiente físico tem dificuldade de controlar a turma | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0165` | `V0165` | inteiro | Todos - Ciganos vivem roubando | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0166` | `V0166` | inteiro | Todos - Os estudantes da cidade são mais inteligentes, mais rápidos para aprender que os estudantes do campo | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0167` | `V0167` | inteiro | Todos - Os estudantes negros costumam fazer baderna na escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0168` | `V0168` | inteiro | Todos - Os estudantes de escola pobre se envolvem mais com atos de violência | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0169` | `V0169` | inteiro | Todos - Uma lésbica é mais aceita na escola do que um gay | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0170` | `V0170` | inteiro | Todos - Estudantes com deficiência vão à escola somente para socializar | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0171` | `V0171` | inteiro | Todos - Os brancos merecem trabalhos mais valorizados do que os negros | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0172` | `V0172` | inteiro | Todos - Os alunos homossexuais não são alunos normais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0173` | `V0173` | inteiro | Todos - Os estudantes da periferia são mais lentos para aprender | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0174` | `V0174` | inteiro | Todos - Tem que separar uma sala para alunos normais e outra sala para alunos com deficiência | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0175` | `V0175` | inteiro | Todos - Brancos gostam mais de estudar do que os negros | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0176` | `V0176` | inteiro | Todos - Mulher como porteira deixaria os alunos entrando e saindo a toda hora | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0177` | `V0177` | inteiro | Todos - Os professores mais velhos não compreendem a linguagem dos estudantes | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0178` | `V0178` | inteiro | Todos - Todo professor deficiente tem dificuldade de dar aulas | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0179` | `V0179` | inteiro | Todos - Os negros costumam se exibir mais do que os brancos em ocasiões sociais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0180` | `V0180` | inteiro | Todos - Os estudantes da periferia só se interessam pela merenda | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0181` | `V0181` | inteiro | Todos - Existem trabalhos que devem ser realizados apenas por homens | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0182` | `V0182` | inteiro | Todos - Acho muito difícil aceitar a homossexualidade masculina | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0183` | `V0183` | inteiro | Todos - Os estudantes de escola de reforma agrária se envolvem mais com atos de violência | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0184` | `V0184` | inteiro | Todos - O estudante que entra mais velho na escola tem mais dificuldade para aprender | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0185` | `V0185` | inteiro | Todos - As negras têm mais jeito para domésticas do que as brancas | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0186` | `V0186` | inteiro | Todos - O número de deficientes na escola é muito pequeno para se preocupar com eles | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0187` | `V0187` | inteiro | Todos - Apenas mulheres devem trabalhar nas cantinas da escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0188` | `V0188` | inteiro | Todos - Os brancos são mais evoluídos que os negros | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0189` | `V0189` | inteiro | Todos - Os índios têm conseguido mais direitos do que merecem | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0190` | `V0190` | inteiro | Todos - A mulher é mais habilidosa para cuidar da casa | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0191` | `V0191` | inteiro | Todos - Ciganos detestam responsabilidades | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0192` | `V0192` | inteiro | Todos - Para dar aulas para deficientes, só se o professor ganhar mais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0193` | `V0193` | inteiro | Todos - Os estudantes brancos são mais comportados em sala de aula | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0194` | `V0194` | inteiro | Todos - Os estudantes da periferia assaltam sua própria escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0195` | `V0195` | inteiro | Todos - Quanto mais jovem a diretora da escola, mais ela irá entender os estudantes | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0196` | `V0196` | inteiro | Todos - Os estudantes surdos deveriam estudar numa escola especial para portadores de deficiências auditivas | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0197` | `V0197` | inteiro | Todos - Os brancos são superiores aos negros | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0198` | `V0198` | inteiro | Todos - As escolas deveriam demitir os professores homossexuais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0199` | `V0199` | inteiro | Todos - Professor de escola de periferia não precisa ser bem preparado | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0200` | `V0200` | inteiro | Todos - Os estudantes que vêm do campo faltam às aulas por preguiça | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0201` | `V0201` | inteiro | Todos - Eu não aceito a homossexualidade | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0202` | `V0202` | inteiro | Todos - Um professor surdo só pode dar aula para estudante surdo | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0203` | `V0203` | inteiro | Todos - Os alunos homossexuais deveriam estudar em salas separadas dos demais alunos | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0204` | `V0204` | inteiro | Todos - Os negros têm conseguido mais do que merecem | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0205` | `V0205` | inteiro | Todos - Estudante mais velho tem problema com aprendizagem | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0206` | `V0206` | inteiro | Todos - As escolas do campo não precisam ser tão bem construídas quanto às da cidade | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0207` | `V0207` | inteiro | Todos - Para cuidar de alunos deficientes, só se o funcionário ganhar mais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0208` | `V0208` | inteiro | Todos - Os negros não devem se queixar, eles estão onde devem estar | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0209` | `V0209` | inteiro | Todos - Lugar de índio é no mato | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0210` | `V0210` | inteiro | Todos - Caso exista um homossexual na sala de aula, os pais devem transferir seu filho da escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0211` | `V0211` | inteiro | Todos - Os estudantes pobres são mais indisciplinados | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0212` | `V0212` | inteiro | Todos - O número de cegos na escola é muito pequeno para se preocupar com eles | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0213` | `V0213` | inteiro | Todos - O estudante com deficiência cria problemas na escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0214` | `V0214` | inteiro | Todos - Pais de estudantes normais preferem que seus filhos convivam com estudantes normais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0215` | `V0215` | inteiro | Todos - Índio não precisa das coisas dos brancos | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0216` | `V0216` | inteiro | Todos - Alunos homossexuais deveriam ser afastados da escola | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0217` | `V0217` | inteiro | Todos - Os negros deveriam tentar ser como os brancos | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0218` | `V0218` | inteiro | Todos - Ciganos não cumprem as obrigações | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0219` | `V0219` | inteiro | Todos - Os professores mais novos entendem melhor os alunos | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0220` | `V0220` | inteiro | Todos - Atualmente os negros têm mais influência política do que merecem | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0221` | `V0221` | inteiro | Todos - Para a escola do campo, qualquer professor serve | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0222` | `V0222` | inteiro | Todos - A homossexualidade é uma doença | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0223` | `V0223` | inteiro | Todos - Os negros sabem cozinhar melhor | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0224` | `V0224` | inteiro | Todos - Existem trabalhos que devem ser realizados apenas por mulheres | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0225` | `V0225` | inteiro | Todos - Os brancos, em geral, são mais estudiosos que os índios | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0226` | `V0226` | inteiro | Todos - Os professores que não são gays são mais respeitados pelos estudantes | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0227` | `V0227` | inteiro | Todos - Os negros têm mais habilidade em trabalhos manuais | 1 = Discorda muito; 2 = Discorda pouco; 3 = Concorda pouco; 4 = Concorda muito | todo |
| `v0228` | `V0228` | inteiro | Todos - Sexo | 1 = Masculino; 2 = Feminino | todo |
| `v0229` | `V0229` | inteiro | Todos - Como se classifica (cor/etnia) | 1 = Amarelo ou oriental; 2 = Branco; 3 = Caboclo; 4 = Cafuso; 5 = Índio; 6 = Moreno; 7 = Mulato; 8 = Preto; 9 = Pardo | todo |
| `v0230` | `V0230` | inteiro | Dir/Prof/Func - Exerce outra atividade remunerada além de lecionar na escola | 1 = Sim; 2 = Não | todo |
| `v0231` | `V0231` | inteiro | Dir - Está estudando atualmente | 1 = Não está estudando; 2 = Está estudando: Ensino Superior; 3 = Está estudando: Pós-graduação (lato sensu) - especialização com no mínimo 360 horas; 4 = Está estudando: Pós-graduação (stricto sensu) - mestrado e/ou doutorado | todo |
| `v0232` | `V0232` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - EDUCAÇÃO PARA RELAÇÕES ÉTNICO-RACIAIS | 1 = Sim; 2 = Não | todo |
| `v0233` | `V0233` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - EDUCAÇÃO PARA RELAÇÕES ÉTNICO-RACIAIS | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0234` | `V0234` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - EDUCAÇÃO PARA RELAÇÕES ÉTNICO-RACIAIS | — | todo |
| `v0235` | `V0235` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - DIREITOS HUMANOS | 1 = Sim; 2 = Não | todo |
| `v0236` | `V0236` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - DIREITOS HUMANOS | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0237` | `V0237` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - DIREITOS HUMANOS | — | todo |
| `v0238` | `V0238` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - EDUCAÇÃO AMBIENTAL | 1 = Sim; 2 = Não | todo |
| `v0239` | `V0239` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - EDUCAÇÃO AMBIENTAL | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0240` | `V0240` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - EDUCAÇÃO AMBIENTAL | — | todo |
| `v0241` | `V0241` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - GÊNERO E IDENTIDADE DO GÊNERO | 1 = Sim; 2 = Não | todo |
| `v0242` | `V0242` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - GÊNERO E IDENTIDADE DO GÊNERO | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0243` | `V0243` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - GÊNERO E IDENTIDADE DO GÊNERO | — | todo |
| `v0244` | `V0244` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - EDUCAÇÃO NO CAMPO | 1 = Sim; 2 = Não | todo |
| `v0245` | `V0245` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - EDUCAÇÃO NO CAMPO | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0246` | `V0246` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - EDUCAÇÃO NO CAMPO | — | todo |
| `v0247` | `V0247` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - HISTÓRIA E CULTURA DA ÁFRICA E SEUS AFRO-DESCENDENTES | 1 = Sim; 2 = Não | todo |
| `v0248` | `V0248` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - HISTÓRIA E CULTURA DA ÁFRICA E SEUS AFRO-DESCENDENTES | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0249` | `V0249` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - HISTÓRIA E CULTURA DA ÁFRICA E SEUS AFRO-DESCENDENTES | — | todo |
| `v0250` | `V0250` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - HISTÓRIA E CULTURA INDÍGENA | 1 = Sim; 2 = Não | todo |
| `v0251` | `V0251` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - HISTÓRIA E CULTURA INDÍGENA | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0252` | `V0252` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - HISTÓRIA E CULTURA INDÍGENA | — | todo |
| `v0253` | `V0253` | inteiro | Dir/Prof - Curso de formação continuada que fez/está fazendo - IDENTIFICAÇÃO DE EXPLORAÇÃO DO TRABALHO INFANTIL | 1 = Sim; 2 = Não | todo |
| `v0254` | `V0254` | inteiro | Dir/Prof - Carga horária do curso de formação continuada que fez/está fazendo - IDENTIFICAÇÃO DE EXPLORAÇÃO DO TRABALHO INFANTIL | 1 = Menos de 40 horas; 2 = 40 horas ou mais | todo |
| `v0255` | `V0255` | inteiro | Dir/Prof - Ano em que fez o curso de formação continuada - IDENTIFICAÇÃO DE EXPLORAÇÃO DO TRABALHO INFANTIL | — | todo |
| `v0256` | `V0256` | inteiro | Dir - Tempo que lecionou (em anos) | — | todo |
| `v0257` | `V0257` | inteiro | Dir - Nunca lecionou (1 = nunca lecionou; vazio caso contrário) | — | todo |
| `v0258` | `V0258` | inteiro | Dir - Tempo que trabalha nesta escola (em anos) | — | todo |
| `v0259` | `V0259` | inteiro | Dir - Tempo como diretor nesta escola (em anos) | — | todo |
| `v0260` | `V0260` | inteiro | Dir - Carga horária de trabalho nesta escola | 1 = Até 20 horas semanais; 2 = De 21 a 40 horas semanais; 3 = Mais de 40 horas semanais | todo |
| `v0261` | `V0261` | inteiro | Dir - Forma como assumiu a direção da escola | 1 = Concurso público; 2 = Exame de seleção; 3 = Eleição; 4 = Exame de seleção e eleição; 5 = Indicação política; 6 = Rotativo; 7 = Substituição do titular; 8 = Outra forma | todo |
| `v0262` | `V0262` | inteiro | Dir - A escola consegue oferecer vagas para todos os alunos que a procuram | 1 = Sim; 2 = Não | todo |
| `v0263` | `V0263` | inteiro | Dir - Principal critério para a admissão de alunos na escola | 1 = Prova de seleção; 2 = Sorteio; 3 = Proximidade do local de moradia; 4 = Ordem de chegada à escola no dia da matrícula; 5 = Prioridade para alunos de baixa renda; 6 = Encaminhamento de outra escola; 7 = Indicação política ou de amigos; … (lista completa no dicionário da fonte) | todo |
| `v0264` | `V0264` | inteiro | Dir - Escola oferece atividades extra-curriculares nos finais de semana | 1 = Sim, sempre; 2 = Sim, às vezes; 3 = Não, nunca; 4 = Não tem atividades na escola no final de semana | todo |
| `v0265` | `V0265` | inteiro | Prof - Tempo que leciona | — | todo |
| `v0266` | `V0266` | inteiro | Prof - Tempo que leciona nesta escola (em anos) | — | todo |
| `v0267` | `V0267` | inteiro | Func - Nível de escolaridade mais elevado | 1 = Nunca frequentou escola; 2 = Começou a estudar, mas não completou a 4ª série do Ensino Fundamental; 3 = Começou a estudar, e completou a 4ª série do Ensino Fundamental; 4 = Começou a estudar, mas não completou a 8ª série do Ensino Fundamental; … (lista completa no dicionário da fonte) | todo |
| `v0268` | `V0268` | inteiro | Func - Tempo em anos que trabalha na escola | — | todo |
| `v0269` | `V0269` | inteiro | Func - Tempo em meses que trabalha na escola | — | todo |
| `v0270` | `V0270` | inteiro | Func - Carga horária de trabalho na escola | 1 = Até 20 horas semanais; 2 = De 21 a 40 horas semanais; 3 = Mais de 40 horas semanais | todo |
| `v0271` | `V0271` | inteiro | Func - Participa ou trabalha em atividades extra-curriculares nos finais de semana | 1 = Sim, sempre; 2 = Sim, de vez em quando; 3 = Não, nunca; 4 = Não tem atividades na escola no final de semana | todo |
| `v0272` | `V0272` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0273` | `V0273` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0274` | `V0274` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0275` | `V0275` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0276` | `V0276` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0277` | `V0277` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0278` | `V0278` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0279` | `V0279` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0280` | `V0280` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0281` | `V0281` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0282` | `V0282` | inteiro | Alun - Mora com ... (a coluna traz um código numérico quando a opção foi marcada e fica vazia caso contrário; o dicionário não lista o código) | — | todo |
| `v0283` | `V0283` | inteiro | Alun - Número de irmãos com quem mora | — | todo |
| `v0284` | `V0284` | inteiro | Alun - Número de filhos com quem mora | — | todo |
| `v0285` | `V0285` | inteiro | Alun - Número de outros parentes/pessoas com quem mora | — | todo |
| `v0286` | `V0286` | inteiro | Alun - Pai ou padrasto sabe ou sabia ler e escrever | 1 = Sim; 2 = Não; 3 = Não tem pai ou padrasto | todo |
| `v0287` | `V0287` | inteiro | Alun - Mãe ou madrasta sabe ou sabia ler e escrever | 1 = Sim; 2 = Não; 3 = Não tem mãe ou madrasta | todo |
| `v0288` | `V0288` | inteiro | Alun - Nível de escolaridade da mãe ou madrasta | 1 = Nunca frequentou escola; 2 = Começou a estudar, mas não completou a 4ª série do Ensino Fundamental; 3 = Começou a estudar, e completou a 4ª série do Ensino Fundamental; 4 = Começou a estudar, mas não completou a 8ª série do Ensino Fundamental; … (lista completa no dicionário da fonte) | todo |
| `v0289` | `V0289` | inteiro | Alun - Quando entrou na escola | 1 = No maternal (jardim da infância); 2 = Na pré-escola; 3 = Na primeira série; 4 = No curso de alfabetização/educação de jovens e adultos | todo |
| `v0290` | `V0290` | inteiro | Alun - Da quinta série do Ensino Fundamental até hoje, sempre estudou nesta escola | 1 = Sim; 2 = Não, mas só estudou em escola(s) pública(s); 3 = Não, mas já estudou em escola(s) privada(s) | todo |
| `v0291` | `V0291` | inteiro | Alun - Há quanto tempo estuda nesta escola | 1 = Menos de 1 ano; 2 = De 1 ano a menos de 2 anos; 3 = De 2 anos a menos de 3 anos; 4 = De 3 anos a menos de 4 anos; 5 = De 4 anos a menos de 5 anos; 6 = Mais de 5 anos | todo |
| `v0292` | `V0292` | inteiro | Alun - Está cursando a série pela primeira vez | 1 = Sim; 2 = Não | todo |
| `v0293` | `V0293` | inteiro | Alun - Desde que começou a estudar, já repetiu de ano | 1 = Sim, uma vez; 2 = Sim, duas vezes; 3 = Sim, três vezes ou mais; 4 = Nunca repetiu de ano | todo |
| `v0294` | `V0294` | inteiro | Alun - Desde que começou a estudar, abandonou a escola durante algum tempo | 1 = Sim, por menos de um ano; 2 = Sim, por um ano; 3 = Sim, entre um e dois anos; 4 = Sim, por mais de dois anos; 5 = Não, nunca abandonou a escola | todo |
| `v0295` | `V0295` | inteiro | Alun - Quando terminar o nível que está cursando, pretende: | 1 = Somente continuar estudando; 2 = Somente trabalhar; 3 = Continuar estudando e trabalhar; 4 = Ainda não sabe | todo |
| `v0296` | `V0296` | inteiro | Alun - Se encontra com colegas/amigos de sala, fora da escola | 1 = Sim, muitas vezes; 2 = Sim, de vez em quando; 3 = Não, nunca | todo |
| `v0297` | `V0297` | inteiro | Alun - Se sente deixado de lado na sala de aula pelos professores | 1 = Sim, muitas vezes; 2 = Sim, de vez em quando; 3 = Nunca ou quase nunca | todo |
| `v0298` | `V0298` | inteiro | Alun - Relação com colegas/amigos da turma | 1 = Tem amizade com todo mundo; 2 = Tem amizade com a maioria da turma; 3 = Tem amizade com poucos da turma; 4 = Não tem amizade com ninguém da turma | todo |
| `v0299` | `V0299` | inteiro | Alun - Pessoa que acompanha de perto a vida escolar | 1 = Mãe; 2 = Outra mulher da família; 3 = Pai; 4 = Outro homem da família; 5 = Empregado(a); 6 = Ninguém | todo |
| `v0300` | `V0300` | inteiro | Alun - Frequência com que os pais conversam com você sobre situações preconceituosas ou de discriminação | 1 = Sempre; 2 = De vez em quando; 3 = Nunca | todo |
| `v0301` | `V0301` | inteiro | Alun - Frequência com que os pais conversam com seus colegas sobre ocorrência de situações preconceituosas na classe | 1 = Sempre; 2 = De vez em quando; 3 = Nunca | todo |
| `v0302` | `V0302` | inteiro | Alun - Frequência com que os pais conversam com seus professores sobre ocorrência de situações preconceituosas na classe | 1 = Sempre; 2 = De vez em quando; 3 = Nunca | todo |
| `v0303` | `V0303` | inteiro | Alun - Frequência com que os pais conversam com seu diretor sobre ocorrência de situações preconceituosas na classe | 1 = Sempre; 2 = De vez em quando; 3 = Nunca | todo |
| `v0304` | `V0304` | inteiro | Alun - Participa DURANTE A SEMANA de atividades fora do horário de aula | 1 = Sim, sempre; 2 = Sim, às vezes; 3 = Não, nunca; 4 = Não tem atividades na escola fora do horário de aula | todo |
| `v0305` | `V0305` | inteiro | Alun - Participa NOS FINAIS DE SEMANA de atividades fora do horário de aula | 1 = Sim, sempre; 2 = Sim, às vezes; 3 = Não, nunca; 4 = Não tem atividades na escola fora do horário de aula | todo |
| `v0306` | `V0306` | inteiro | Pais - Tempo que o(a) filho(a) está estudando nesta escola | 1 = Menos de 1 ano; 2 = De 1 ano a menos de 2 anos; 3 = De 2 anos a menos de 3 anos; 4 = De 3 anos a menos de 4 anos; 5 = De 4 anos a menos de 5 anos; 6 = Mais de 5 anos | todo |
| `v0307` | `V0307` | inteiro | Pais - Tempo que participa do Conselho Escolar | 1 = Menos de 1 ano; 2 = De 1 a 3 anos; 3 = Mais de 3 anos | todo |
| `v0308` | `V0308` | inteiro | Pais - Participa de alguma atividade nesta escola no final de semana | 1 = Sim, sempre; 2 = Sim, de vez em quando; 3 = Não, nunca; 4 = Não tem atividades na escola no final de semana | todo |
| `v0309` | `V0309` | inteiro | Pais - Ajuda seu filho nas tarefas escolares | 1 = Sim, ajuda a estudar na época das provas; 2 = Sim, ajuda somente quando ele tem que fazer trabalho de pesquisa; 3 = Sim, ajuda a fazer todo o dever de casa diariamente; 4 = Não, porque seu filho raramente tem tarefas escolares para fazer em casa; … (lista completa no dicionário da fonte) | todo |
| `v0310` | `V0310` | inteiro | Pais - Ajuda seu filho nas tarefas escolares | 1 = Sim, ajuda a estudar na época das provas; 2 = Sim, ajuda somente quando ele tem que fazer trabalho de pesquisa; 3 = Sim, ajuda a fazer todo o dever de casa diariamente; 4 = Não, porque seu filho raramente tem tarefas escolares para fazer em casa; … (lista completa no dicionário da fonte) | todo |
| `v0311` | `V0311` | inteiro | Pais - Ajuda seu filho nas tarefas escolares | 1 = Sim, ajuda a estudar na época das provas; 2 = Sim, ajuda somente quando ele tem que fazer trabalho de pesquisa; 3 = Sim, ajuda a fazer todo o dever de casa diariamente; 4 = Não, porque seu filho raramente tem tarefas escolares para fazer em casa; … (lista completa no dicionário da fonte) | todo |
| `v0312` | `V0312` | inteiro | Pais - Nível de escolaridade mais elevado | 1 = Nunca frequentou escola; 2 = Começou a estudar, mas não completou a 4ª série do Ensino Fundamental; 3 = Começou a estudar, e completou a 4ª série do Ensino Fundamental; 4 = Começou a estudar, mas não completou a 8ª série do Ensino Fundamental; … (lista completa no dicionário da fonte) | todo |
| `v0313` | `V0313` | inteiro | Prof - Está estudando atualmente | 1 = Não está estudando; 2 = Está estudando: Ensino Médio; 3 = Está estudando: Ensino Superior; 4 = Está estudando: Pós-graduação (lato sensu) - especialização com no mínimo 360 horas; 5 = Está estudando: Pós-graduação (stricto sensu) - mestrado e/ou doutorado | todo |
| `v0314` | `V0314` | inteiro | Func - Está estudando atualmente | 1 = Não está estudando; 2 = Sim, Ensino Fundamental; 3 = Sim, Educação de Jovens e Adultos Fundamental; 4 = Sim, Ensino Médio; 5 = Sim, Educação de Jovens e Adultos Médio; 6 = Educação de Jovens e Adultos Profissionalizante; 7 = Sim, Superior | todo |
| `v0315` | `V0315` | inteiro | Pais - Está estudando atualmente | 1 = Não está estudando; 2 = Sim, Ensino Fundamental; 3 = Sim, Educação de Jovens e Adultos Fundamental; 4 = Sim, Ensino Médio; 5 = Sim, Educação de Jovens e Adultos Médio; 6 = Educação de Jovens e Adultos Profissionalizante; 7 = Sim, Superior | todo |
| `v0316` | `V0316` | inteiro | Todos - Idade | — | todo |
| `publico` | `PUBLICO` | inteiro | Publico | 1 = Diretores; 2 = Professores; 3 = Funcionários; 4 = Alunos; 5 = Pais e Mães | todo |

## No lake

- Dataset `inep/pesquisa-discriminacao`, particionado por `ano` (única partição: 2008); um Parquet, `pesquisa-discriminacao-microdados_2008__microdados_200906.parquet`.
- Os nomes das colunas saem normalizados (minúsculas; `Região` do programa SPSS vira `regiao`).
- As colunas têm tipo, ao contrário do que ocorre em outros datasets do Inep: `estrato`, `regiao` e `uf` são texto, `peso` é decimal e as demais (`m_oh`, `n_h`, `m_hi`, `n_hi`, `publico` e todas as `v0001` a `v0316`) são inteiros, conforme o formato de cada coluna no programa SAS. Células em branco viram nulos.
- A coluna `ano` é a edição, tirada do nome do arquivo.

## Cuidados de uso

- **Sempre filtre ou agrupe por `publico`.** As perguntas não se aplicam a todos os públicos, e o conjunto de respondentes de cada pergunta muda (por exemplo, `v0001`, a modalidade, só tem valor para professores e alunos). Contar linhas sem filtro mistura cinco populações.
- **Pesos não são comparáveis entre públicos.** O Leia-me define uma fórmula de peso para cada público (diretores: `m_oh / (n_h x m_hi)`; alunos: `m_oh / (n_h x n_hi)`; professores, funcionários e pais: o peso do plano amostral multiplicado por `1 / n_hi`). Na fonte, a soma de `peso` é 8.365.097 para alunos (as matrículas do universo) e cerca de 114 mil para cada um dos outros quatro públicos. Use o peso só dentro de um público, ou padronize-o como indica o Leia-me.
- **`n_hi` e `m_hi` não valem para todos.** Na fonte, `m_hi` fica vazio para os alunos e `n_hi` fica vazio para os diretores. O rótulo de `n_hi` no programa SPSS fala em "pais e mães", mas o Leia-me o define, nos pesos, como o número de respondentes do público amostrados na escola.
- **Não há identificador de respondente nem de escola.** Nenhuma coluna identifica a escola, de modo que não é possível agrupar respondentes por escola; a chave do dataset fica vazia. `estrato` e `v0002` (município) são as menores agregações disponíveis.
- **Questões sensíveis.** O questionário pergunta sobre raça e etnia, deficiência, religião, orientação sexual, violência, condição socioeconômica e território, em escalas de concordância e de distância social. As respostas são autodeclaradas e opinativas, não medem fatos.
- **Dados pessoais.** O arquivo traz sexo, cor ou etnia, idade, religião, escolaridade, com quem o aluno mora e o código do município do respondente. O Leia-me informa que o questionário pedia que o respondente não colocasse o nome e que as informações seriam repassadas ao Inep de forma agregada e consolidada; o arquivo não traz nome nem identificador. Evite cruzar município, idade, sexo e cor ou etnia em recortes pequenos.
- **Quadro de amostra do Leia-me.** A tabela do início do Leia-me lista professores 1.004 e funcionários 1.005; o arquivo (`publico` 2 e 3) e a tabela do relatório final trazem 1.005 professores e 1.004 funcionários.
- **Rótulos do dicionário.** `Região` usa as siglas C, N, NE, S e SE (as cinco grandes regiões) e `uf` usa o código de UF do IBGE (11 a 53). As colunas `v0272` a `v0282` (com quem o aluno mora) não têm lista de códigos no dicionário; na fonte, `v0272` assume o valor 1 e `v0273` o valor 2.
- **Escalas de resposta variam.** Há perguntas Sim/Não (1 e 2), de concordância (Discorda muito a Concorda muito) e de frequência ("Vi nesta escola", "Não vi, mas sou", "Nem vi, nem sou"); confira os códigos na coluna *Unidade / códigos* antes de agregar.

## Exemplos

Percentual de respondentes com religião, por público e ponderado pelo peso do respondente (`v0008`: 1 = sim, 2 = não). A amostra do lake só traz diretores e professores; no lake completo aparecem os cinco públicos:

```python
import duckdb

duckdb.sql("""
    SELECT publico, count(*) AS respondentes,
           round(100 * sum(peso) FILTER (WHERE v0008 = 1) / sum(peso) FILTER (WHERE v0008 IS NOT NULL), 1) AS pct_com_religiao
    FROM read_parquet('lake/inep/pesquisa-discriminacao/ano=2008/*.parquet')
    GROUP BY publico
    ORDER BY publico
""").show()
```

## Referências

- Microdados da Pesquisa de Ações Discriminatórias no Âmbito Escolar 2008: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/pesquisa-de-acoes-discriminatorias-no-ambito-escolar
- Leia-me (dicionário de variáveis, questionários, relatórios final e analítico) e programas de leitura SAS e SPSS, dentro do ZIP em https://download.inep.gov.br/microdados/microdados_pesquisa_acoes_discriminatorias_ambito_escolar_2008.zip
