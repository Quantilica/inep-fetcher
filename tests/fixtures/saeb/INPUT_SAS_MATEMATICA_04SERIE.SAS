DATA MATEMATICA_04ANO; 

     INFILE 'D:\DADOS\ALUNOS\MATEMATICA_04SERIE.TXT' LRECL=217 MISSOVER;
     INPUT

@1	MASCARA		8.	/*	MASCARA	*/
@9	ANO_MASCARA	8.	/*	ANO_MASCARA	*/
@17	ANO		4.	/*	Ano de aplicação	*/
@21	SERIE		1.	/*	Série	*/
@22	DISC		$char1.	/*	Disciplina	*/
@23	TURMA		2.	/*	Número da turma	*/
@25	TURNO		$char9.	/*	Turno	*/
@34	ALUNO		2.	/*	Codigo do Aluno	*/
@36	ESTRATO		9.	/*	Estrato da Amostra	*/
@45	UPA		8.	/*	Unidade Primária de Amostragem	*/
@53	DEP_ADM		1.	/*	Dependência Administrativa (Estadual/Municipal/Particular)	*/
@54	LOCAL		1.	/*	Localização (Urbano/Rural)	*/
@55	REDE		1.	/*	Rede de Ensino(Publica/Particular)	*/
@56	UF		2.	/*	Unidade da Federação	*/
@58	REGIAO		1.	/*	Região	*/
@59	PESO_AC		8.4	/*	Peso calibrado (usado para expansão)	*/
@67	PROVA		$char1.	/*	Prova	*/
@68	PROFIC		8.4	/*	Proficiência	*/
@76	IDADE		2.	/*	Idade	*/
@78	A041_001	1.	/*	Sexo	*/
@79	A041_002	1.	/*	Voce se considera:	*/
@80	A041_003	2.	/*	Qual e o mes do seu aniversario?	*/
@82	A041_004	1.	/*	Qual e o ano do seu nascimento?	*/
@83	A041_005	1.	/*	Voce trabalha?	*/
@84	A041_006	1.	/*	No lugar onde voce mora existe agua encanada?	*/
@85	A041_007	1.	/*	E eletricidade, existe?	*/
@86	A041_008	1.	/*	A rua em que voce mora tem calçamento?	*/
@87	A041_009	1.	/*	Quantas cozinhas ha onde voce mora?	*/
@88	A041_010	1.	/*	Quantos banheiros ha onde voce mora?	*/
@89	A041_011	1.	/*	Quantas salas ha onde voce mora?	*/
@90	A041_012	1.	/*	Quantos quartos ha onde voce mora?	*/
@91	A041_013	1.	/*	Quantos radios ha onde voce mora?	*/
@92	A041_014	1.	/*	Quantas TVs a cores ha onde voce mora?	*/
@93	A041_015	1.	/*	Quantos videocassetes ha onde voce mora?	*/
@94	A041_016	1.	/*	Quantas geladeiras ha onde voce mora?	*/
@95	A041_017	1.	/*	Quantos freezers ha onde voce mora?	*/
@96	A041_018	1.	/*	Quantas maquinas de lavar roupa ha onde voce mora?	*/
@97	A041_019	1.	/*	Quantos aspiradores de po ha onde voce mora?	*/
@98	A041_020	1.	/*	Quantos telefones residenciais ha onde voce mora?	*/
@99	A041_021	1.	/*	Quantos telefones celulares ha onde voce mora?	*/
@100	A041_022	1.	/*	Quantos computadores ha onde voce mora?	*/
@101	A041_023	1.	/*	Quantos automoveis ha onde voce mora?	*/
@102	A041_024	1.	/*	Em sua casa trabalha alguma empregada domestica, todos os dias uteis? Quantas?	*/
@103	A041_025	1.	/*	Quantas pessoas moram com voce?	*/
@104	A041_026	1.	/*	Voce mora com seu pai?	*/
@105	A041_027	1.	/*	Voce mora com sua mae?	*/
@106	A041_028	1.	/*	Voce mora com seus irmaos, irmas?	*/
@107	A041_029	1.	/*	Voce mora com outros parentes?	*/
@108	A041_030	1.	/*	Voce mora com amigos?	*/
@109	A041_031	1.	/*	Quantas pessoas ajudam a pagar as despesas da casa?	*/
@110	A041_032	1.	/*	Seu pai sabe ler e escrever?	*/
@111	A041_033	1.	/*	Ate que serie seu pai estudou?	*/
@112	A041_034	1.	/*	Sua mae sabe ler e escrever?	*/
@113	A041_035	1.	/*	Ate que serie sua mae estudou?	*/
@114	A041_036	1.	/*	Seu pai ou sua mae conhecem o diretor da sua escola?	*/
@115	A041_037	1.	/*	Seu pai ou sua mae conhecem seu(sua) professor(a)?	*/
@116	A041_038	1.	/*	Seu pai ou sua mae conhecem algum amigo seu?	*/
@117	A041_039	1.	/*	Seu pai ou sua mae conhecem algum pai, mae de amigo seu?	*/
@118	A042_001	1.	/*	Quantos livros ha em sua casa?	*/
@119	A042_002	1.	/*	Voce leu revistas em quadrinhos neste ano?	*/
@120	A042_003	1.	/*	Voce leu livros neste ano?	*/
@121	A042_004	1.	/*	Voce leu jornal ou revista de informaçao geral neste ano?	*/
@122	A042_005	1.	/*	Voce leu revistas sobre esportes, musica, automoveis etc. neste ano?	*/
@123	A042_006	1.	/*	Voce leu outro material neste ano?	*/
@124	A042_007	1.	/*	Em que tipo de escola voce ja estudou?	*/
@125	A042_008	1.	/*	Voce ja repetiu de ano? Quantas vezes?	*/
@126	A042_009	1.	/*	Voce faz liçao de casa?	*/
@127	A042_010	1.	/*	Voce gosta desta disciplina?	*/
@128	A042_011	1.	/*	Neste ano, voce teve boas notas ou conceitos nesta disciplina?	*/
@129	A042_012	1.	/*	Voce sabe usar computador?	*/
@130	A042_013	1.	/*	Voce usa computador na escola?	*/
@131	CADERNO		2.			/*	Caderno de Provas	*/
@133	BLOCO1		2.			/*	Bloco 1 do caderno	*/
@135	BLOCO2		2.			/*	Bloco 2 do caderno	*/
@137	BLOCO3		2.			/*	Bloco 3 do caderno	*/
@139	RESP_BL1	$char13.	/*	Respostas do aluno no Bloco 1 do Caderno	*/
@152	RESP_BL2	$char13.	/*	Respostas do aluno no Bloco 2 do Caderno	*/
@165	RESP_BL3	$char13.	/*	Respostas do aluno no Bloco 3 do Caderno	*/
@178	GAB_BL1		$char13.	/*	Gabarito do Bloco 1 do Caderno	*/
@191	GAB_BL2		$char13.	/*	Gabarito do Bloco 2 do Caderno	*/
@204	GAB_BL3		$char13.	/*	Gabarito do Bloco 3 do Caderno	*/
;
run;
