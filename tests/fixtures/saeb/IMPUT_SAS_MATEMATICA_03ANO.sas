
/**************************************************************************/
/*  MEC/INEP                                                              */
/*  Diretoria de Tratamento e Disseminação de Informações Educacionais    */
/*  Coordenação-Geral de Sistemas Integrados de Informações Educacionais  */
/*------------------------------------------------------------------------*/
/*  PROGRAMA:                                                             */
/*           INPUT_SAS_MATEMATICA_03ANO.sas                               */
/*------------------------------------------------------------------------*/
/*  DESCRICAO: PROGRAMA PARA LEITURA DOS MICRODADOS DO SAEB DE 2005       */                                           
/**************************************************************************/
/**************************************************************************/
/* 2)Este programa foi criado com o software SAS em 04/09/2007            */
/**************************************************************************/

DATA MATEMATICA_03ANO; 
INFILE "D:\DADOS\ALUNOS\MATEMATICA_03ANO.TXT"
LRECL=327 MISSOVER;
INPUT
@1	MASCARA		8.	/*Número gerado como código de acesso aos Estabelecimentos de Ensino Básico. */
@9	ANO_MASCARA	8.	/*Ano da Máscara*/
@17	ANO			8.	/*Ano de aplicação do Saeb*/
@25	SERIE  $Char2.	/*Série*/
@27	DISC   $Char1.	/*Disciplina*/
@28	TURMA		3.	/*Número da turma*/
@31	NOMETURMA	$Char30.	/*Nome da turma*/
@61	TURMA_APLI	3.	/*Turma com aplicação de provas*/
@64	EXTRA  $Char1.	/*Turma Extra*/
@65	ALUNO		3.	/*Código do aluno*/
@68	ALUNO_VALI	3.	/*Aluno_valido: Aluno que fez pelo menos um item na prova*/
@71	ESTRATO		6.	/*Estrato da Amostra*/
@77	DEP_ADM		3.	/*Dependência Administrativa (Estadual/Municipal/Particular)*/
@80	LOCAL		3.	/*Localização(Urbano/Rural)*/
@83	REDE		3.	/*Rede de Ensino(Publica/Particular)*/
@86	CODUF  $Char2.	/*Unidade da Federação*/
@88	REGIAO $Char1.	/*Região*/
@89	CAPITAL		3.	/*Variável que identifica se o participante da prova é da capital*/
@92	PESO_AT	    12.10	/*Peso do aluno na turma*/
@104	PESO_AC	12.10	/*Peso do aluno por disciplina*/
@116	PESO_EC	12.10	/*Peso da turma*/
@128	PESO_TC	12.10	/*Peso da escola*/
@140	CADERNO	3.	/*Caderno de provas*/
@143	BLOCO1	3.	/*Bloco 1 do caderno de provas*/
@146	BLOCO2	3.	/*Bloco 2 do caderno de provas*/
@149	BLOCO3	3.	/*Bloco 3 do caderno de provas*/
@152	RESP1	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@153	RESP2	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@154	RESP3	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@155	RESP4	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@156	RESP5	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@157	RESP6	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@158	RESP7	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@159	RESP8	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@160	RESP9	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@161	RESP10	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@162	RESP11	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@163	RESP12	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@164	RESP13	$Char1.	/*Respostas do aluno no Bloco 1 do caderno de provas*/
@165	RESP14	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@166	RESP15	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@167	RESP16	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@168	RESP17	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@169	RESP18	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@170	RESP19	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@171	RESP20	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@172	RESP21	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@173	RESP22	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@174	RESP23	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@175	RESP24	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@176	RESP25	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@177	RESP26	$Char1.	/*Respostas do aluno no Bloco 2 do caderno de provas*/
@178	RESP27	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@179	RESP28	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@180	RESP29	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@181	RESP30	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@182	RESP31	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@183	RESP32	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@184	RESP33	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@185	RESP34	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@186	RESP35	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@187	RESP36	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@188	RESP37	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@189	RESP38	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@190	RESP39	$Char1.	/*Respostas do aluno no Bloco 3 do caderno de provas*/
@191	GAB_BL1	$Char13.	/*Gabarito do Bloco 1 do caderno de provas*/
@204	GAB_BL2	$Char13.	/*Gabarito do Bloco 2 do caderno de provas*/
@217	GAB_BL3	$Char13.	/*Gabarito do Bloco 3 do caderno de provas*/
@230	PROFIC_250	12.10	/*Proficiência na escala 250 ; 50*/
@242	PROFIC_SAE	12.10	/*Proficiência na escala Saeb*/
@254	A111_001	$Char1.	/*Sexo*/
@255	A111_002	$Char1.	/*Como você se considera?*/
@256	A111_003	$Char1.	/*Qual e o mês do seu aniversário?*/
@257	A111_004	$Char1.	/*Qual é o ano do seu nascimento?*/
@258	A111_005	$Char1.	/*Na sua casa tem televisão em cores?*/
@259	A111_006	$Char1.	/*Na sua casa tem radio?*/
@260	A111_007	$Char1.	/*Na sua casa tem automóvel/ carro?*/
@261	A111_008	$Char1.	/*Na sua casa tem videocassete?*/
@262	A111_009	$Char1.	/*Na sua casa tem geladeira?*/
@263	A111_010	$Char1.	/*Na sua casa tem maquina de lavar roupa?*/
@264	A111_011	$Char1.	/*Na sua casa tem aspirador de pó?*/
@265	A111_012	$Char1.	/*Dentro de sua casa tem banheiro?*/
@266	A111_013	$Char1.	/*Na sua casa tem quartos para dormir?*/
@267	A111_014	$Char1.	/*Na sua casa tem freezer junto a geladeira(GELADEIRA DUPLEX)?*/
@268	A111_015	$Char1.	/*Na sua casa tem freezer separado da geladeira?*/
@269	A111_016	$Char1.	/*Na sua casa tem computador com internet?*/
@270	A111_017	$Char1.	/*Na sua casa tem computador sem internet?*/
@271	A111_018	$Char1.	/*Além dos livros escolares, quantos livros há em sua casa?*/
@272	A111_019	$Char1.	/*Onde você mora existe eletricidade?*/
@273	A111_020	$Char1.	/*Onde você mora chega água pela torneira?*/
@274	A111_021	$Char1.	/*Na sua casa trabalha alguma empregada domestica? Quantas?*/
@275	A111_022	$Char1.	/*Quantas pessoas moram com você?*/
@276	A112M001	$Char1.	/*Você mora com sua mãe?*/
@277	A112M002	$Char1.	/*Até que série sua mãe estudou?*/
@278	A112M003	$Char1.	/*Você vê sua mãe lendo?*/
@279	A112M004	$Char1.	/*Você mora com seu pai?*/
@280	A112M005	$Char1.	/*Até que série seu pai estudou?*/
@281	A112M006	$Char1.	/*Você vê seu pai lendo?*/
@282	A112M007	$Char1.	/*Quem é a pessoa que acompanha mais de perto sua vida escolar?*/
@283	A112M008	$Char1.	/*Até que série a pessoa INDICADA ACIMA estudou?*/
@284	A112M009	$Char1.	/*Você lê revistas em quadrinhos?*/
@285	A112M010	$Char1.	/*Você lê livros de literatura, como romance, poesia, etc?*/
@286	A112M011	$Char1.	/*Você lê jornais?*/
@287	A112M012	$Char1.	/*Você lê revistas de informação geral (Veja, IstoÉ, Época)?*/
@288	A112M013	$Char1.	/*Na sua casa tem enciclopédia?*/
@289	A112M014	$Char1.	/*Na sua casa tem atlas?*/
@290	A112M015	$Char1.	/*Na sua casa tem dicionário?*/
@291	A112M016	$Char1.	/*Na sua casa tem calculadora?*/
@292	A112M017	$Char1.	/*Com que freqüência seus pais ou responsáveis almoçam ou jantam com você?*/
@293	A112M018	$Char1.	/*Com que freqüência seus pais ou responsáveis ouvem musica com você?*/
@294	A112M019	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam sobre livros com você?*/
@295	A112M020	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam sobre filmes com você?*/
@296	A112M021	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam sobre programas de TV com você?*/
@297	A112M022	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam com seus amigos/ colegas de escola?*/
@298	A112M023	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam com outros amigos seus?*/
@299	A112M024	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam com o Diretor da sua escola?*/
@300	A112M025	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam com seus professores?*/
@301	A112M026	$Char1.	/*Com que freqüência seus pais ou responsáveis conversam sobre o que acontece na escola com você?*/
@302	A112M027	$Char1.	/*Com que freqüência seus pais ou responsáveis ajudam você a fazer a lição de casa?*/
@303	A112M028	$Char1.	/*Com que freqüência seus pais ou responsáveis cobram se você fez a lição de casa?*/
@304	A112M029	$Char1.	/*Com que freqüência seus pais ou responsáveis falam para você não faltar à escola?*/
@305	A112M030	$Char1.	/*Com que freqüência seus pais ou responsáveis falam para você tirar boas notas?*/
@306	A112M031	$Char1.	/*Com que freqüência seus pais ou responsáveis vão à reunião de pais na escola?*/
@307	A112M032	$Char1.	/*Quando você começou a estudar?*/
@308	A112M033	$Char1.	/*Você já foi reprovado(a)?*/
@309	A112M034	$Char1.	/*Você gosta de estudar matemática?*/
@310	A112M035	$Char1.	/*Você faz a lição de casa de matemática?*/
@311	A112M036	$Char1.	/*Seu professor de Matemática corrige a lição de casa?*/
@312	A112M037	$Char1.	/*Desde a 5ª série, quantas vezes você já mudou de escola?*/
@313	A112M038	$Char1.	/*Em que tipo de escola você já estudou?*/
@314	A112M039	$Char1.	/*Na sua turma os alunos fazem barulho e desordem?*/
@315	A112M040	$Char1.	/*Na sua turma os alunos prestam atenção no que os professores dizem?*/
@316	A112M041	$Char1.	/*Na sua turma os alunos fazem o que os professores pedem?*/
@317	A112M042	$Char1.	/*Na sua turma os professores têm que esperar muito para que os alunos fiquem quietos?*/
@318	A112M043	$Char1.	/*Você tem muitos amigos na sua sala de aula?*/
@319	A112M044	$Char1.	/*Seu professor de Matemática dá importância ao que você diz?*/
@320	A112M045	$Char1.	/*Seu professor de matemática elogia ou dá parabéns quando você tira boas notas*/
@321	A112M046	$Char1.	/*Seu professor de Matemática dá uma força para você estudar mais quando não tira notas boas?*/
@322	A112M047	$Char1.	/*Quando você precisa de ajuda, o professor de Matemática está sempre pronto para lhe atender?*/
@323	A112M048	$Char1.	/*Quando você falta às aulas, sua família é avisada?*/
@324	A112M049	$Char1.	/*Quando terminar a 8ª série, você pretende:*/
@325	A112M050	$Char1.	/*Você trabalha?*/
@326	A112M051	$Char1.	/*Você concluiu o ensino fundamental (antigo 1º grau) no supletivo?*/
;
RUN;
QUIT;