  

DATA BIOLOGIA_03ANO; 

     INFILE 'D:\DADOS\ALUNOS\BIOLOGIA_03ANO.TXT' LRECL=238 MISSOVER;
     INPUT

@1	MASCARA		8.	/*	MASCARA	*/
@9	ANO_MASCARA	8.	/*	ANO_MASCARA	*/
@17	ANO		4.	/*	Ano de aplicação	*/
@21	SERIE		1.	/*	Série	*/
@22	DISC		$char1.	/*	Disciplina	*/
@23	TURMA		2.	/*	Número da turma	*/
@25	TURNO		$char9.	/*	Turno	*/
@34	ALUNO		3.	/*	Codigo do Aluno	*/
@37	ESTRATO		9.	/*	Estrato da Amostra	*/
@46	UPA		8.	/*	Unidade Primária de Amostragem	*/
@54	DEP_ADM		1.	/*	Dependência Administrativa (Estadual/Municipal/Particular)	*/
@55	LOCAL		1.	/*	Localização (Urbano/Rural)	*/
@56	REDE		1.	/*	Rede de Ensino(Publica/Particular)	*/
@57	UF		2.	/*	Unidade da Federação	*/
@59	REGIAO		1.	/*	Região	*/
@60	PROVA		$char1.	/*	Prova	*/
@61	PROFIC		8.4	/*	Proficiência	*/
@69	PESO_AC		8.4	/*	Peso calibrado (usado para expansão)	*/
@77	IDADE		2.	/*	Idade	*/
@79	A031_001	1.	/*	Sexo	*/
@80	A031_002	1.	/*	Voce se considera:	*/
@81	A031_003	2.	/*	Qual e o mes do seu aniversario?	*/
@83	A031_004	1.	/*	Qual e o ano do seu nascimento?	*/
@84	A031_005	1.	/*	Qual o seu estado civil?	*/
@85	A031_006	1.	/*	Quantos filhos voce tem?	*/
@86	A031_007	1.	/*	Voce trabalha?	*/
@87	A031_008	1.	/*	Quantas horas por semana voce trabalha?	*/
@88	A031_009	1.	/*	Onde voce mora existe agua encanada?	*/
@89	A031_010	1.	/*	Onde voce mora existe eletricidade?	*/
@90	A031_011	1.	/*	Onde voce mora existe calçamento?	*/
@91	A031_012	1.	/*	Quantas cozinhas ha onde voce mora?	*/
@92	A031_013	1.	/*	Quantos banheiros ha onde voce mora?	*/
@93	A031_014	1.	/*	Quantas salas ha onde voce mora?	*/
@94	A031_015	1.	/*	Quantos quartos ha onde voce mora?	*/
@95	A031_016	1.	/*	Quantos radios ha onde voce mora?	*/
@96	A031_017	1.	/*	Quantas TVs a cores ha onde voce mora?	*/
@97	A031_018	1.	/*	Quantos videocassetes ha onde voce mora?	*/
@98	A031_019	1.	/*	Quantas geladeiras ha onde voce mora?	*/
@99	A031_020	1.	/*	Quantos freezers ha onde voce mora?	*/
@100	A031_021	1.	/*	Quantas maquinas de lavar roupa ha onde voce mora?	*/
@101	A031_022	1.	/*	Quantos aspiradores de po ha onde voce mora?	*/
@102	A031_023	1.	/*	Quantos telefones residenciais ha onde voce mora?	*/
@103	A031_024	1.	/*	Quantos telefones celulares ha onde voce mora?	*/
@104	A031_025	1.	/*	Quantos computadores ha onde voce mora?	*/
@105	A031_026	1.	/*	Quantos automoveis ha onde voce mora?	*/
@106	A031_027	1.	/*	Em sua casa trabalha alguma empregada domestica, todos os dias uteis? Quantas?	*/
@107	A031_028	1.	/*	Quantas pessoas moram com voce?	*/
@108	A031_029	1.	/*	Voce mora com seu pai?	*/
@109	A031_030	1.	/*	Voce mora com sua mae?	*/
@110	A031_031	1.	/*	Voce mora com seus irmaos, irmas?	*/
@111	A031_032	1.	/*	Voce mora com sua esposa/seu marido?	*/
@112	A031_033	1.	/*	Voce mora com seus(suas) filhos(as)?	*/
@113	A031_034	1.	/*	Voce mora com outros parentes?	*/
@114	A031_035	1.	/*	Voce mora com amigos?	*/
@115	A031_036	1.	/*	Quantas pessoas ajudam a pagar as despesas da casa?	*/
@116	A031_037	1.	/*	Seu pai sabe ler e escrever?	*/
@117	A031_038	1.	/*	Ate que serie seu pai estudou?	*/
@118	A031_039	1.	/*	Sua mae sabe ler e escrever?	*/
@119	A031_040	1.	/*	Ate que serie sua mae estudou?	*/
@120	A031_041	1.	/*	Seu pai ou sua mae conhecem o diretor da sua escola?	*/
@121	A031_042	1.	/*	Seu pai ou sua mae conhecem algum(a) professor(a)?	*/
@122	A031_043	1.	/*	Seu pai ou sua mae conhecem algum amigo seu?	*/
@123	A031_044	1.	/*	Seu pai ou sua mae conhecem algum pai, mae de amigo seu?	*/
@124	A032_001	1.	/*	Quantos livros ha em sua casa?	*/
@125	A032_002	1.	/*	Voce leu revistas em quadrinhos neste ano?	*/
@126	A032_003	1.	/*	Voce leu livros neste ano?	*/
@127	A032_004	1.	/*	Voce leu jornal ou revista de informaçao geral neste ano?	*/
@128	A032_005	1.	/*	Voce leu revistas sobre esportes, musica, automoveis etc. neste ano?	*/
@129	A032_006	1.	/*	Voce leu outro material neste ano?	*/
@130	A032_007	1.	/*	Em que tipo de escola voce ja estudou?	*/
@131	A032_008	1.	/*	Voce ja repetiu de ano? Quantas vezes?	*/
@132	A032_009	1.	/*	Voce concluiu o Ensino Fundamental(1ºGrau) no Supletivo?	*/
@133	A032_010	1.	/*	Voce faz liçao de casa?	*/
@134	A032_011	1.	/*	Voce faz algum curso fora da escola, como esportes?	*/
@135	A032_012	1.	/*	Voce faz algum curso fora da escola, como linguas?	*/
@136	A032_013	1.	/*	Voce faz algum curso fora da escola, como computaçao?	*/
@137	A032_014	1.	/*	Voce faz algum curso fora da escola, como musica?	*/
@138	A032_015	1.	/*	Voce faz algum curso fora da escola, como reforço escolar?	*/
@139	A032_016	1.	/*	Voce faz algum outro curso fora da escola?	*/
@140	A032_017	1.	/*	Alem de cursos, voce participa de outras atividades, como gremio escolar?	*/
@141	A032_018	1.	/*	Alem de cursos, voce participa de outras atividades, como associaçao desportiva?	*/
@142	A032_019	1.	/*	Alem de cursos, voce participa de outras atividades, como associaçao de moradores?	*/
@143	A032_020	1.	/*	Alem de cursos, voce participa de outras atividades, como sindicato?	*/
@144	A032_021	1.	/*	Alem de cursos, voce participa de outras atividades, como movimento religioso?	*/
@145	A032_022	1.	/*	Alem de cursos, voce participa de outras atividades, como partido politico?	*/
@146	A032_023	1.	/*	Alem de cursos, voce participa de outras atividades, como organizaçoes nao-governamentais?	*/
@147	A032_024	1.	/*	Alem de cursos, voce participa de nenhuma outra atividade?	*/
@148	A032_025	1.	/*	Voce gosta desta disciplina?	*/
@149	A032_026	1.	/*	Neste ano, voce teve boas notas ou conceitos nesta disciplina?	*/
@150	A032_027	1.	/*	Voce sabe usar computador?	*/
@151	A032_028	1.	/*	Voce usa computador na escola?	*/
@152	CADERNO		2.	/*	Caderno de Provas	*/
@154	BLOCO1		2.	/*	Bloco 1 do caderno	*/
@156	BLOCO2		2.	/*	Bloco 2 do caderno	*/
@158	BLOCO3		2.	/*	Bloco 3 do caderno	*/
@160	Resp_Bl1	$char13.	/*	Respostas do aluno no Bloco 1 do Caderno	*/
@173	Resp_Bl2	$char13.	/*	Respostas do aluno no Bloco 2 do Caderno	*/
@186	Resp_Bl3	$char13.	/*	Respostas do aluno no Bloco 3 do Caderno	*/
@199	resp_total	$char39.	/*	Respostas do aluno nos 3 Blocos do Caderno	*/
@238	GAB_Bl1		$char13.	/*	Gabarito do Bloco 1 do Caderno	*/
@251	GAB_Bl2		$char13.	/*	Gabarito do Bloco 2 do Caderno	*/
@264	GAB_Bl3		$char13.	/*	Gabarito do Bloco 3 do Caderno	*/
;
run;
