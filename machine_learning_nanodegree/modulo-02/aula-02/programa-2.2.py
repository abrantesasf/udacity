#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:25:12 2018

@author: abrantesasf
"""

#%% Imports globais
import pandas as pd
import numpy as np

#%% Lê arquivo de dados
df = pd.read_csv('data-2.2.csv')
df.head()

#%% Gera arrays do Numpy
X = np.array(df[['x1', 'x2']])
Y = np.array(df['y'])

#%% Separa os dados de treinamento e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)
len(X_train)
len(X_test)
len(Y_train)
len(Y_test)

