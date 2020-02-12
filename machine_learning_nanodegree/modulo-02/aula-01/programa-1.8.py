#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:51:44 2018

@author: abrantesasf
"""

#%% Imports
import pandas as pd
import numpy as np

#%% Leitura do dataframe do Pandas e criação de arrays do Numpy
df = pd.read_csv('data.csv')
df.head()

X = np.array(df[['x1', 'x2']])
Y = np.array(df['y'])

X[0:5]
Y[0:5]

#%% Regerssão logística
from sklearn.linear_model import LogisticRegression as lr
classifier = lr()

classifier.fit(X, Y)
print(classifier)

#%% Redes neurais
from sklearn.neural_network import MLPClassifier as rn
classifier = rn()

classifier.fit(X, Y)

#%% Árvores de decisão
from sklearn.ensemble import GradientBoostingClassifier as ad
classifier = ad()

classifier.fit(X, Y)

#%% SVM
from sklearn.svm import SVC as svm
classifier = svm()

classifier.fit(X, Y)
