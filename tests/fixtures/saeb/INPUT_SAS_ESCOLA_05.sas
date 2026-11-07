
/**************************************************************************/
/*  MEC/INEP                                                              */
/*  Diretoria de Tratamento e Disseminação de Informações Educacionais    */
/*  Coordenação-Geral de Sistemas Integrados de Informações Educacionais  */
/*------------------------------------------------------------------------*/
/*  PROGRAMA:                                                             */
/*           INPUT_SAS_ESCOLA_05.sas                                      */
/*------------------------------------------------------------------------*/
/*  DESCRICAO: PROGRAMA PARA LEITURA DOS MICRODADOS DO SAEB DE 2005       */                                           
/**************************************************************************/
/**************************************************************************/
/* 2)Este programa foi criado com o software SAS em 04/09/2007            */
/**************************************************************************/
 	
DATA ESCOLA;
INFILE 'D:\DADOS\ESCOLA\ESCOLA_05.TXT'
LRECL=129 MISSOVER;
INPUT 	
@1	MASCARA	8.		/*Número gerado como código de acesso aos Estabelecimentos de Ensino Básico*/
@9	ANO_MASCARA	8.	/*Ano da Máscara*/
@17	ANO		8.		/*Ano de aplicação*/
@25	DEP_ADM	3.		/*Dependência Administrativa(Estadual/Municipal/Particular)*/
@28	LOCAL	3.		/*Localização(Urbano/Rural)*/
@31	REDE	3.		/*Rede de Ensino(Publica/Particular)*/
@34	CODUF	$Char2.	/*Unidade da Federação*/
@36	REGIAO	8.		/*Região*/
@44	CAPITAL	3.		/*Variável que identifica se a escola é da capital */
@47	PESO_TC	12.10	/*Peso da escola*/
@59	Q1_1	$Char1.	/*Estado de conservação do TELHADO*/
@60	Q1_2	$Char1.	/*Estado de conservação das PAREDES*/
@61	Q1_3	$Char1.	/*Estado de conservação do PISO*/
@62	Q1_4	$Char1.	/*Estado de conservação das PORTAS*/
@63	Q1_5	$Char1.	/*Estado de conservação das JANELAS*/
@64	Q1_6	$Char1.	/*Estado de conservação dos BANHEIROS*/
@65	Q1_7	$Char1.	/*Estado de conservação da COZINHA*/
@66	Q1_8	$Char1.	/*Estado de conservação das INSTALAÇÕES HIDRÁULICAS*/
@67	Q1_9	$Char1.	/*Estado de conservação das INSTALAÇÕES ELÉTRICAS*/
@68	Q2_1	$Char1.	/*As salas de aula são iluminadas?*/
@69	Q2_2	$Char1.	/*As salas de aula são arejadas?*/
@70	Q3_1	$Char1.	/*Limpeza da ENTRADA DO PRÉDIO*/
@71	Q3_2	$Char1.	/*Limpeza das PAREDES EXTERNAS*/
@72	Q3_3	$Char1.	/*Limpeza das PORTAS*/
@73	Q3_4	$Char1.	/*Limpeza das JANELAS*/
@74	Q3_5	$Char1.	/*Limpeza do PÁTIO*/
@75	Q3_6	$Char1.	/*Limpeza dos CORREDORES*/
@76	Q3_7	$Char1.	/*Limpeza das SALAS DE AULA*/
@77	Q3_8	$Char1.	/*Limpeza dos BANHEIROS*/
@78	Q3_9	$Char1.	/*Limpeza da COZINHA*/
@79	Q4_1	$Char1.	/*Existem muros, grades ou cercas em condições de garantir segurança do alunos?*/
@80	Q4_2	$Char1.	/*Existe controle de entrada e saída de alunos?*/
@81	Q4_3	$Char1.	/*Existe controle de entrada de pessoas estranhas na escola?*/
@82	Q4_4	$Char1.	/*Os portões permanecem trancados durante o funcionamento da escola?*/
@83	Q4_5	$Char1.	/*Existe algum tipo de vigilância para o período diurno?*/
@84	Q4_6	$Char1.	/*Existe algum tipo de vigilância para o período noturno?*/
@85	Q4_7	$Char1.	/*Existe algum tipo de vigilância para os finais de semana e feriados?*/
@86	Q4_8	$Char1.	/*Há algum tipo de policiamento para inibir furtos, etc?*/
@87	Q4_9	$Char1.	/*Há algum tipo de policiamento para inibir tráfico, etc dentro da escola?*/
@88	Q4_10	$Char1.	/*Há algum tipo de policiamento para inibir tráfico, etc nas imediações da escola?*/
@89	Q4_11	$Char1.	/*A escola tem algum sistema de proteção contra incêndio?*/
@90	Q4_12	$Char1.	/*As sala onde são guardados os equipamentos mais caros têm dispositivos de segurança?*/
@91	Q4_13	$Char1.	/*A escola apresenta sinais de depredação?*/
@92	Q4_14	$Char1.	/*Existe uma boa iluminação do lado de fora da escola?*/
@93	Q4_15	$Char1.	/*A escola adota medidas de segurança para os alunos nas imediações da escola?*/
@94	Q4_16	$Char1.	/*A escola é servida por transporte público fácil em todos os turnos?*/
@95	Q5_1	$Char1.	/*Total de computadores na escola*/
@96	Q5_2	$Char1.	/*Computadores para uso dos alunos*/
@97	Q5_3	$Char1.	/*Computadores com acesso à Internet para uso dos alunos*/
@98	Q5_4	$Char1.	/*Computadores para uso dos professores*/
@99	Q5_5	$Char1.	/*Computadores com acesso à Internet para uso dos professores*/
@100 Q5_6	$Char1.	/*Computadores exclusivamente para uso administrativo*/
@101 Q6_1	$Char1.	/*Conservação da TELEVISÃO*/
@102 Q6_2	$Char1.	/*Conservação da ANTENA PARABÓLICA*/
@103 Q6_3	$Char1.	/*Conservação do VIDEOCASSETE*/
@104 Q6_4	$Char1.	/*Conservação da MÁQUINA FOTOCOPIADORA (XEROX)*/
@105 Q6_5	$Char1.	/*Conservação do MIMEÓGRAFO*/
@106 Q6_6	$Char1.	/*Conservação do PROJETOR DE SLIDES*/
@107 Q6_7	$Char1.	/*Conservação do RETROPROJETOR*/
@108 Q6_8	$Char1.	/*Conservação da MÁQUINA DE DATILOGRAFIA*/
@109 Q6_9	$Char1.	/*Conservação da IMPRESSORA*/
@110 Q6_10	$Char1.	/*Conservação do APARELHO DE SOM*/
@111 Q7_1	$Char1.	/*Pichação de muros ou paredes das dependências  internas da escola*/
@112 Q7_2	$Char1.	/*Pichação de muros ou paredes das dependências  externas da escola*/
@113 Q7_3	$Char1.	/*Depredação de banheiros*/
@114 Q7_4	$Char1.	/*Depredação de dependências internas da escola*/
@115 Q7_5	$Char1.	/*Depredação de dependências externas da escola*/
@116 Q8		$Char1.	/*Qual o percentual de alunos que utiliza a biblioteca durante o mês?*/
@117 Q9		$Char1.	/*Existe uma pessoa responsável pela biblioteca?*/
@118 Q10	$Char1.	/*Os professores realizam trabalhos na biblioteca, fazendo uso de materiais disponíveis?*/
@119 Q11	$Char1.	/*Os alunos levam livros para casa?*/
@120 Q12	$Char1.	/*Os professores levam livros para casa?*/
@121 Q13	$Char1.	/*Membros da comunidade levam livros para casa?*/
@122 Q14_1	$Char1.	/*Conservação dos LIVROS DE ESTUDO*/
@123 Q14_2	$Char1.	/*Conservação dos LIVROS DE LITERATURA*/
@124 Q14_3	$Char1.	/*Conservação das REVISTAS DE INFORMAÇÃO GERAL (VEJA, ÉPOCA etc)*/
@125 Q14_4	$Char1.	/*Conservação dos JORNAIS*/
@126 Q14_5	$Char1.	/*Conservação de REVISTAS EM QUADRINHOS*/
@127 Q15	$Char1.	/*Como você avalia esta escola, considerando as infra-estrutura e condições gerais?*/
@128 Q16	$Char1.	/*Como você avalia esta escola, considerando as dependências externas?*/
;
run;quit;