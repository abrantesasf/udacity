#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:36:28 2018

@author: abrantesasf
"""

import pandas as pd
import numpy as np

df = pd.read_csv('2_class_data.csv')
df.head()

# Criando ARRAYS do Numpy com os dados do dataframe:
X = np.array(df[['x1', 'x2']])
Y = np.array(df['y'])

type(X)
type(Y)
