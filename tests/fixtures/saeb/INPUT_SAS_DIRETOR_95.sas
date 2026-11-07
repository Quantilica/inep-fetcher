   /**************************************************/
  /*          QUESTIONÁRIO - DIRETOR                */
 /*                ANO - 1995                      */
/**************************************************/

DATA DIRETOR_95; 
     INFILE    'D:\DADOS\DIRETOR\DIRETOR_95.TXT'
     LRECL=472 MISSOVER;
     INPUT

@1			ANO			8.		/*Ano*/
@9			SERIE		8.		/*Serie*/
@17			ESTRATO		8.		/*Estrato*/
@25			UPA			8.		/*Unidade Primaria de Amostragem*/
@33			PESO_EC		8.		/*Peso calibrado(usado para expansao)*/
@41			DEP_ADM		8.		/*Dependencia Administrativa(Estadual/Municipal/Particular)*/
@49			LOCAL		8.		/*Localizacao(Urbano/Rural)*/
@57			REDE		8.		/*Rede de Ensino(Publica/Particular)*/
@65			UF			8.		/*Unidade da Federação*/
@73			REGIAO		8.		/*Região*/
@81			D_001		8.		/*Sexo*/
@89			D_002		8.		/*Idade*/
@97			D_003		8.		/*Qual e o seu ultimo nivel de escolaridade completo?*/
@105		D_004		8.		/*Qual e o seu nivel de escolaridade especifico na area de Administraçao Escolar?*/
@113		D_005		8.		/*Voce participou de cursos de capacitaçao, treinamento ou atualizaçao na area de Administraçao Escolar neste ano letivo?*/
@121		D_006		8.		/*Caso tenha participado de cursos de capacitaçao, treinamento ou atualizaçao na area de Administraçao Escolar neste ano, indique quantas horas voce frequentou:*/
@129		D_007		8.		/*Ha quantos anos voce trabalha no magisterio?*/
@137		D_008		8.		/*Quantos anos de trabalho voce tem em funçoes administrativas?*/
@145		D_009		8.		/*Ha quantos anos voce e diretor desta escola?*/
@153		D_010		8.		/*Voce ingressou na carreira do magisterio por meio de concurso publico?*/
@161		D_011		8.		/*Voce assumiu a direçao desta escola por meio de:*/
@169		D_012		8.		/*Qual e a sua situaçao trabalhista nesta escola?*/
@177		D_013_01	8.		/*Indique o mes do seu ultimo salario bruto mensal nesta escola:*/
@185		D_013_02	8.		/*Indique o valor do seu ultimo salario bruto mensal nesta escola:*/
@193		D_014		8.		/*A escola desenvolveu um projeto pedagogico neste ano letivo?*/
@201		D_015		8.		/*Quem participou da elaboraçao ou atualizaçao do plano de trabalho da escola para este ano letivo?*/
@209		D_016_1		8.		/*Meta que constou do plano de trabalho:cumprimento dos conteudos previstos para cada serie e disciplina*/
@217		D_016_2		8.		/*Meta que constou do plano de trabalho:melhoria dos resultados do processo ensino-aprendizagem*/
@225		D_016_3		8.		/*Meta que constou do plano de trabalho:diminuiçao da evasao dos alunos*/
@233		D_016_4		8.		/*Meta que constou do plano de trabalho:diminuiçao da reprovaçao dos alunos*/
@241		D_016_5		8.		/*Meta que constou do plano de trabalho:cumprimento das atividades escolares*/
@249		D_017		8.		/*A escola funcionou com Conselho de Escola neste ano letivo?*/
@257		D_018		8.		/*Se escola funcionou com Conselho de Escola, indique quantas vezes ela se reuniu durante este ano letivo:*/
@265		D_019		8.		/*A escola funcionou com Conselho de Classe neste ano letivo?*/
@273		D_020		8.		/*Durante este ano letivo, o relacionamento desta escola com outros orgaos do sistema foi marcado por:*/
@281		D_021_1		8.		/*Caracterizou a captaçao de recursos financeiros para a escola:repasse feito diretamente pelo MEC/FNDE*/
@289		D_021_2		8.		/*Caracterizou a captaçao de recursos financeiros para a escola:repasse feito pela Secretaria Estadual/Municipal de Educaçao*/
@297		D_021_3		8.		/*Caracterizou a captaçao de recursos financeiros para a escola:recursos captados junto a comunidade por meio de campanhas e eventos*/
@305		D_021_4		8.		/*Caracterizou a captaçao de recursos financeiros para a escola:recursos provenientes das contribuiçoes dos alunos por meio da APM*/
@313		D_021_5		8.		/*Caracterizou a captaçao de recursos financeiros para a escola:recursos provenientes da cobrança das mensalidades escolares*/
@321		D_021_6		8.		/*Nao houve captaçao de recursos financeiros pela escola*/
@329		D_022		8.		/*Caso a sua escola tenha recebido recursos financeiros, voce considera que este processo:*/
@337		D_023_1		8.		/*Problema que dificultou a gestao da escola, neste ano letivo:numero insuficiente de professores*/
@345		D_023_2		8.		/*Problema que dificultou a gestao da escola, neste ano letivo:numero insuficiente de pessoal tecnico-administrativo*/
@353		D_023_3		8.		/*Problema que dificultou a gestao da escola, neste ano letivo:interrupçao das atividades escolares*/
@361		D_023_4		8.		/*Problema que dificultou a gestao da escola, neste ano letivo:rotatividade dos professores*/
@369		D_023_5		8.		/*Problema que dificultou a gestao da escola, neste ano letivo:insuficiencia de recursos financeiros*/
@377		D_024_1		8.		/*Procedimento que caracteriza sua gestao na escola:organizaçao da estrutura administrativa da escola*/
@385		D_024_2		8.		/*Procedimento que caracteriza sua gestao na escola:acompanhamento do trabalho pedagogico dos professores*/
@393		D_024_3		8.		/*Procedimento que caracteriza sua gestao na escola:analise e discussao, com os professores, sobre mecanismos para avaliaçao dos alunos*/
@401		D_024_4		8.		/*Procedimento que caracteriza sua gestao na escola:Estimulo a participaçao dos professores e equipe tecnica administrativa das decisoes relativas a administraçao da escola*/
@409		D_024_5		8.		/*Procedimento que caracteriza sua gestao na escola:participaçao da comunidade na administraçao da escola*/
@417		D_024_6		8.		/*Procedimento que caracteriza sua gestao na escola:controle e acompanhamento do trabalho da escola*/
@425		D_024_7		8.		/*Procedimento que caracteriza sua gestao na escola:iniciativa de promover palestras, cursos, seminarios, etc. para os professores*/
@433		D_025		8.		/*Qual a sua opiniao sobre a aprendizagem dos alunos desta escola?*/
@441		D_026		8.		/*Neste ano letivo, quantas vezes voce realizou reunioes com professores para tratar de assuntos pedagogicos?*/
@449		D_027		8.		/*Neste ano letivo, quantas vezes voce realizou reunioes com professores e equipe tecnica para tratar de assuntos administrativos?*/
@457		D_028		8.		/*Voce realizou reunioes com pais ou responsaveis pelos alunos durante este ano letivo?*/
@465		D_029		8.		/*No caso de terem ocorrido reunioes com pais ou responsavei, quantos deles participaram?*/
;
RUN;
QUIT;