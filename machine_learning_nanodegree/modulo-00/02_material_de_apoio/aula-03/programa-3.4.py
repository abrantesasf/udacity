#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:40:39 2018

@author: abrantesasf
"""

# Armazenar dados e fazer referência a eles

# Os dados no Pandas geralmente são contidos em um Dataframe
# O dataframe e uma estrutura bidimensional com colunas rotuladas
# que podem ter tipos diferentes. Para comparação, por exemplo,
# os arrays de Numpy devem ser com elementos do mesmo type.

# Para criar um dataframe do Pandas, temos que começar criando um dicionário
# Python, onde a Key será o nome da coluna que queremos para o
# dataframe, e o Value será uma Série Pandas com os valores de cada linha.
# Note que podemos especificar um index, que indica em que linha o valor
# da coluna deverá ficar.
import pandas as pd
d = {
     'name': pd.Series(['Braund', 'Cummings', 'Heikkinem', 'Allen'],
                    index=['a', 'b', 'c', 'd']),
     'age': pd.Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
     'fare': pd.Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
     'survive': pd.Series([False, True, True, False], index=['a', 'b', 'c', 'd'])
    }

type(d)
d
df = pd.DataFrame(d)
type(df)
df
