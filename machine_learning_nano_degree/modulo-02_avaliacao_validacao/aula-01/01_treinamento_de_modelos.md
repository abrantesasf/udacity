# Treinamento de Modelos

## Introdução

Nessa aula focaremos em 2 questões:

1 - **O quão bom é o meu modelo?** nesse caso, completamos
um certo modelo e precisamos saber se nosso modelo é bom ou não.
Para isso usaremos *métricas* que nos ajudarão a decidir se o
modelo é bom ou não.
2 - **Como melhorar o modelo?** uma vez que já sabemos se o
modelo é bom ou não, como melhorar o modelo baseado nessas
métricas?

## Esboço

Em ML temos um problema para resolver, que geralmente corresponde
a um conjunto de dados e mazer algumas predições, por exemplo.
Para resolver esse problema temos um conjunto de ferramentas, que
são os algoritmos. Temos que saber que ferramenta (algoritmo)
funcionará melhor para nosso problema e, para isso, temos
as métricas (que são usadas para avaliar todos os algoritmos
e seus parâmetros e decidir qual é o melhor algoritmo para
nosso problema).

```
PROBLEMA  -----  ALGORITMOS  -----  METRICAS
```

Nesta aula aprenderemos sobre as métricas (e técnicas) que nos
permitirão dizer quando um algoritmo está "trabalhando" bem
em nosso problema (e dados), e como ajustar esse algoritmo para
melhorar a solução.

## Relembrando estatística

Presumimos que você tem familiaridade com:

- Medidas de tendência central: média, mediana, moda
- Variabilidade de dados: intervalo interquartil, outliers,
desvio-padrão, correção de Bessel

Caso necessário, relembre esse material no **Módulo 00**.

## Numpy, Pandas e scikit-learn

No **Módulo 00**, aprenda o básico de:

- Numpy e Pandas
- Scikit-Learn

## Natureza dos dados

No **Módulo 00**, relembre sobre:

- Natureza dos dados

## Carregando dados no Pandas

Aprenderemos a carregar dados no Pandas. Se precisar, a documentação oficial
está em http://pandas.pydata.org/pandas-docs/stable/

