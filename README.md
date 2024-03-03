# Delivery_Zomato
This repository contains files and script to build a company strategy dashboard.


## Problema de negócio

A Zomato é um serviço de busca de restaurantes para quem quer sair para jantar, buscar comida ou pedir em casa na Índia, Brasil, Portugal, Turquia, Indonésia, Nova Zelândia, Itália, Filipinas, África do Sul, Sri Lanka, Catar, Emirados Árabes Unidos, Reino Unido, Estados Unidos, Austrália e Canadá. O site estava posicionado no ranking Alexa como 99 na Índia e 595 no mundo em Outubro de 2015. 
Então imagine que você acaba de ser contratado como Cientista de Dados da empresa na Zomato, a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra que é também recente contrato a identificar pontos chaves da empresa para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Zomato respondendo às perguntas que ele fizer. Portanto, deve construir um dashboards, a partir dessas análises, para responder ás seguintes perguntas.
### Geral
  1. Quantos restaurantes únicos estão registrados?
  2. Quantos países únicos estão registrados?
  3. Quantas cidades únicas estão registradas?
  4. Qual o total de avaliações feitas?
  5. Qual o total de tipos de culinária registrados?


### Pais
  1. Qual o nome do país que possui mais cidades registradas?
  2. Qual o nome do país que possui mais restaurantes registrados?
  3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
  registrados?
  4. Qual o nome do país que possui a maior quantidade de tipos de culinária
  distintos?
  5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
  6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
  entrega?
  7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
  reservas?
  8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
  registrada?
  9. Qual o nome do país que possui, na média, a maior nota média registrada?
  10. Qual o nome do país que possui, na média, a menor nota média registrada?
  11. Qual a média de preço de um prato para dois por país?
  

### Cidade

  1. Qual o nome da cidade que possui mais restaurantes registrados?
  2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
  4?
  3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
  2.5?
  4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
  5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
  distintas?
  6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
  reservas?
  7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
  entregas?
  8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
  aceitam pedidos online?

### Restaurantes

  1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
  2. Qual o nome do restaurante com a maior nota média?
  3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
  pessoas?
  4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
  média de avaliação?
  5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
  possui a maior média de avaliação?
  6. Os restaurantes que aceitam pedido online são também, na média, os
  restaurantes que mais possuem avaliações registradas?
  7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
  possuem o maior valor médio de um prato para duas pessoas?
  8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
  possuem um valor médio de prato para duas pessoas maior que as churrascarias
  americanas (BBQ)?
### Tipos de Culinária

  1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
  restaurante com a maior média de avaliação?
  2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
  restaurante com a menor média de avaliação?
  3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
  restaurante com a maior média de avaliação?
  4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
  restaurante com a menor média de avaliação?
  5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
  restaurante com a maior média de avaliação?
  6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
  restaurante com a menor média de avaliação?
  7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
  restaurante com a maior média de avaliação?
  8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
  restaurante com a menor média de avaliação?
  9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
  restaurante com a maior média de avaliação?
  10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
  restaurante com a menor média de avaliação?
  11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
  pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele
visualizasse as principais informações das perguntas que ele fez. O CEO precisa
dessas informações o mais rápido possível, uma vez que ele também é novo na
empresa e irá utilizá-las para entender melhor a empresa Zomato para conseguir
tomar decisões mais assertivas. Seu trabalho é utilizar os dados que a empresa Zomato possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.


2. Premissas assumidas para a análise 
1. A análise foi realizada com os dados coletados até 2019. 
2. Marketplace foi o modelo de negócio assumido. 
3. Os 3 principais visões do negócio foram: Visão Países, visão cidades e visão culinária.

## 3. Estratégia da solução
   
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
  0. Visão Macro dos negócio
  1. Visão da atuação por País.
  2. Visão da atuação por Cidade 
  3. Visão da atuação por tipo culinário
Cada visão é representada pelo seguinte conjunto de métricas.

### 0.	Visão Macro do negócio
  a.	Total 
  a.	País
  b.	Cidades
  c.	Restaurantes
  d.	Variedade culinária 
  1. Visão de atuação por País 
  a. Quantidade de Restaurantes
  b. Quantidade de Cidades 
  c. Média de Avaliações 
  d. Preço médio do prato para dois
  2. Visão de atuação por Cidade
  a. Cidades que mais tem restaurantes
  b. Cidades que possuir mais restaurantes com avaliação acima de 4 
  c. Cidades que mais possui restaurantes com avaliações abaixo de 2.5
  d. Cidades que mais apresenta culinária distintas

### 3. Visão por culinária
  a. 5 Variedade de Culinária mais consumida, com as melhores avaliações nos restaurantes mais bem avaliados.
  b. Restaurantes que mais possuir boa avaliação 
  c. Top 10 Culinária com a melhor média de avaliação no geral
  d. Top 10 Culinária com a pior média de avaliação no geral

## 4. Top 3 Insights de dados
  1. A base de dados é altamente dominada pela índia, mais cidades, mais restaurantes e tipo culinário registrados, inclusive os restaurantes indianos são especializados em outras culinárias com notas excelentes. 
  2. A Indonésia tem maior número de avaliações, mesmo tendo somente três cidades registradas, estando em 14º lugar na lista dos países que mais possuir restaurantes registrados, com apenas 82 restaurantes, o que é muito pequeno comparado ao primeiro lugar Índia com o número 3507 restaurantes registrados, outro dado importante, é que a média do preço do prato para dois é exorbitante na Indonésia, o que significa, esses restaurantes não são sensíveis a população, esses dados vem de uma grande tendência turistas nas três cidades registradas mais forte em Jakarta que possui melhor média e uns dos principais pontos turísticos comparado a Bogor e Tangerang, o que pode leva uma oportunidade de negócios com empresas de turismo e hotéis.
  3.  Os países e cidades que possuir mais tipos culinário parece estar relacionado ao turismo.
  5. O produto final do projeto Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://project-currycompany.streamlit.app/ 
## 6. Conclusão 

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. Da visão da Empresa, podemos concluir que a Índia é um país com maior variedade culinária possuindo excelentes avaliações e que restaurantes como Byg Brewski Brewing Company e Hitchki, são destaque em excelência em duas variedades culinárias ao mesmo tempo. Além disso, pode concluir que tipos culinários mais consumido em geral são North Indian, Chinese, Fast Food e Italian, sendo que os dois primeiros estão relacionando com fato que conjunto de dados possuir mais informações da índia e as duas são as maiores populações do mundo. 


## 7. Próximo passos 

  1. Analisar as cidades estão registradas que são de países emergentes são cidades turísticas.
  2. Analisar se variedade culinária está correlacionada a quantidade de turistas. 
  3. Adicionar novas visões de negócio, quantidade de turista, informar se o preço dos pratos estão na mesma moeda.

