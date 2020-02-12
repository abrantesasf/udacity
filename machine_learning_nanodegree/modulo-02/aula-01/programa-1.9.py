#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:26:59 2018

@author: abrantesasf
"""

#%% Imports Globais
import pandas as pd
import numpy as np

#%% Leitura dos dados
df = pd.read_csv('data-1.9.csv')
df.head()
len(df)

#%% Criação dos arrays Numpy
X = np.array(df[['x1', 'x2']])
Y = np.array(df['y'])

X[0:5]
Y[0:5]

#%% SVM
from sklearn.svm import SVC as svm

classifier = svm()
classifier.fit(X, Y)

classifier2 = svm(kernel = 'poly', degree = 2)
classifier2.fit(X, Y)

classifier3 = svm(kernel = 'rbf', gamma = 200)
classifier3.fit(X, Y)
