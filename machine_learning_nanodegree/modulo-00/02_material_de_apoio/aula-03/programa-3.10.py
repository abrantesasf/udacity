#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:25:47 2018

@author: abrantesasf
"""

import pandas as pd
import numpy as np

col1 = [1, 2, 3]
col2 = [1, 2, 3, 4]

d = {'coluna1' : pd.Series(col1, index=['a', 'b', 'c']),
     'coluna2' : pd.Series(col2, index=['a', 'b', 'c', 'd'])
     }
type(d)

df = pd.DataFrame(d)
type(df)
df

df.apply(np.mean)

# Condição
df['coluna1'] > 1
# Aplicando a condição
df['coluna1'][df['coluna1'] > 1]
# Aplicando a condição e retornando 2 colunas:
df[['coluna1', 'coluna2']][df['coluna1'] > 1]

# A série Pandas tem o método MAP
df['coluna1'].map(lambda x: x > 1)
# O dataframe tem o método APPLY, que aplica a todas as colunas e linhas:
df.apply(lambda x: x > 1)
