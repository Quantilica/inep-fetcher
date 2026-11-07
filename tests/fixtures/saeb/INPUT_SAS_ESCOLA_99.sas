DATA ESCOLAS_99; 

     INFILE 'D:\DADOS\ESCOLAS\ESCOLAS_99.TXT' LRECL=260 MISSOVER;
     INPUT

@1	MASCARA		8.	/*	MASCARA	*/
@9	ANO_MASCARA	8.	/*	ANO_MASCARA	*/	
@17	ANO		4.	/*	Ano de aplicação	*/
@21	SERIE		2.	/*	Série	*/
@23	ESTRATO		9.	/*	Estrato da Amostra	*/
@31	UPA		12.	/*	Unidade Primária de Amostragem	*/
@43	PESO_EC		8.4	/*	Peso calibrado(usado para expansão)	*/
@51	DEP_ADM		8.	/*	Dependência Administrativa(Estadual/Municipal/Particular)	*/
@59	LOCAL		8.	/*	Localização(Urbano/Rural)	*/
@67	REDE		8.	/*	Rede de Ensino(Publica/Particular)	*/
@75	UF		8.	/*	Unidade da Federação	*/
@83	REGIAO		8.	/*	Região	*/
@91	E_1_1	8.	/*	As salas de aula sao iluminadas?	*/	
@99	E_1_2	8.	/*	As salas de aula sao arejadas?	*/	
@107	E_1_3	8.	/*	Nas salas de aula, o volume dos ruidos externos prejudica a concentraçao do alunos?	*/	
@115	E_1_4	8.	/*	As salas de aulas estao limpas?	*/	
@123	E_2_1	8.	/*	Os banheiros, em sua maioria, estao funcionando?	*/
@131	E_2_2	8.	/*	Os banheiros, em sua maioria, estao limpos?	*/
@139	E_2_3	8.	/*	Existe algum banheiro interditado?	*/
@147	E_3_1	8.	/*	Existem muros, grades ou cercas em condiçoes de garantir a segurança dos alunos?	*/
@155	E_3_2	8.	/*	Ha policial ou vigia de forma permanente na escola?	*/
@163	E_3_3	8.	/*	Existe controle de entrada e saida de alunos?	*/
@171	E_3_4	8.	/*	Existe controle de entrada de pessoas estranhas na escola?	*/
@179	E_3_5	8.	/*	A escola tem algum sistema de proteçao contra incendio?	*/
@187	E_3_6	8.	/*	As salas onde sao guardados os equipamentos mais caros tem dispositivos para tranca-las?	*/
@195	E_3_7	8.	/*	A escola apresenta sinais de depredaçao?	*/
@203	E_4_0	8.	/*	Numero de computadores para uso dos alunos	*/
@211	E_5_1	8.	/*	Atendimento medico e um serviço oferecido pela escola?	*/
@219	E_5_2	8.	/*	Atendimento odontologico e um serviço oferecido pela escola?	*/
@227	E_5_3	8.	/*	Atividades culturais e recreativas em espaços fora da escola sao um serviço oferecido pela escola?	*/
@235	E_5_4	8.	/*	Merenda e um serviço oferecido pela escola?	*/
@243	E_5_5	8.	/*	Transporte e um serviço oferecido pela escola?	*/
@251	E_6_0	8.	/*	Em relaçao a infra-estrutura e funcionamento, como voce avalia esta escola, de maneira geral?	*/
;
run;
