# O que é machine learning?

## Introdução

Já vimos que ML é usado para muitas coisas legais, como:

- Reconhecimento de imagens e sons
- Detecção de spam
- Detecção de fraude
- Mercado de ações
- Ensinar um computador a jogar xadrez
- Carros autônomos
- etc.

Então, o que é ML? Para responder essa pergunta, considere a seguinte
diferença entre humanos e computadores: humanos aprendem com experiências
passadas, e os computadores só fazem o que eles são mandados ou seja, devem
ser programados para fazer as coisas. A questão que se colaca então é:
*podemos fazer os computadores aprenderem com a experiência também?*

Sim. E isso é exatamente o que ML é: ensinar computadores a aprender
como realizar tarefas a partir de experiências passadas. E o que são essas
experiências passadas para os computadores? **dados**. Então ML, no fim,
é sobre ensinar os computadores a realizarem tarefas baseados em dados
(a experiência passada).

Vamos ver alguns exemplos.

## Árvores de decisão
Queremos recomendar alguns apps para usuários, baseados no sexo e idade dos
usuários. Podemos então criar uma **árvore de decisão**, a partir dos dados
passados, para decidir qual aplicativo sugerir para um novo usuário.

## Naive Bayes
Construiremos um detector de spam, olhando em dados passados de e-mails.
Podemos pesquisar uma determinada palavra e, dados que o e-mail tem
essa palavra, aprender a probabilidade desse email ser spam. Podemos agregar
outras coisas para aumentar a probabilidade, por exemplo, além de certas
palavras podemos verificar se o e-mail tem erros de gramática, ou
se não tem um título. Assim, quando um novo e-mail for recebido,
de acordo com as probabilidades passadas aprendidas pelo computador,
ele classificará o e-mail como spam ou ham.

## Graident Descent
É um algoritmo muito utilizado em ML e sua essência é a seguinte:
dado um problema a ser solucionado, o processo de solução deve
ser "andar" pequenos passos na direção correta, avaliando e
corrigindo essa direção a cada passo, até chegarmos na solução.

## Regressão Linear
Quando queremos determinar um desfecho futuro numérico (contínuo)
a partir de dados passados, podemos usar regressão linear.
O "gradient descent" aqui é minimizar a soma dos erros.

## Regressão Logística
Quando queremos determinar um desfecho binário, podemos
usar regressão logística. O "gradient descent" aqui é
minimizar a *log loss function*.

## Suport Vector Machine (SVM)
Aqui tentamos maximizar a distância mínima da linha até os
pontos.

## Redes Neurais
Modelos mais complexos para tomar decisões podem ser modelados através
de redes neurais, onde os dados são "fitrados" por "neurônios" e
a união de vários desses neurônios e suas decisões foram a rede
neural. Os neurônios "filtram" os dados de acordo com alguma
regra previamente estabelecida.

## Kernel Method
É um outro método de separação e decisão, principalmente quando
separadores lineares não são suficientes. Sua essência é trabalhar
separando os pontos através de linhas curvas ou planos tri ou multi
dimensionais. Esse método é utilizado em outros algoritmos,
principalmente no Support Vector Machine (SVM).

## K-Means
Separa um conjunto de pontos em grupos (clusters), a partir
de um algoritmo que acha os melhores centroides para cada grupo,
baseando-se na distância que os pontos estão desses centroids. Note
que o K-Means exige a especificação de um número K de clusters
previamente.

## Hierarchical Clusters
É uma maneira de clusterizar pontos, sem especificar o número K
de clusters previamente. Olhamos os pontos próximos e agrupamo-os.
Depois olhamos os próximos pontos mais próximos e também agrupamos.
Isso ocorre até que a distância entre os grupos mais próximos seja
acima de um determinado valor que especificamos previamente.