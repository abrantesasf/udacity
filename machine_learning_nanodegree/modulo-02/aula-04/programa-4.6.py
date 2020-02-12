#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 01:03:08 2018

@author: abrantesasf
"""

#%% Import, read, and split data
import pandas as pd
import numpy as np

#%% Lê os dados em um dataframe do Pandas e cria os arrays Numpy
data = pd.read_csv('data.csv')
data.head()
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

#%% Assusta o seed
# Fix random seed
np.random.seed(55)

#%% Importa os algoritmos de classificação
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from utils import *

### Logistic Regression
estimator = LogisticRegression()

### Decision Tree
#estimator = GradientBoostingClassifier()

### Support Vector Machine
#estimator = SVC(kernel='rbf', gamma=1000)

#%% Plota as learning curves
num_trainings = 10
draw_learning_curves(X, y, estimator, num_trainings)
