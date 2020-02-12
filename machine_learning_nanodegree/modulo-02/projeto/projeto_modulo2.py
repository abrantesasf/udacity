#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:49:53 2018

@author: abrantesasf
"""

#%% Ambiente da análise
def ambienteDaAnalise():
    """
    Abrantes Araújo Silva Filho
    abrantesasf@gmail.com
    
    Imprime informações a respeito do ambiente de análise utilizado,
    incluindo detalhes do hardware, software, versões do Python e
    packages utilizados.
    
    Pré-requisitos: utiliza os packages subprocess, sys, pip, platform,
                    psutil e math
    
    Limitações: essa função foi pensada para sistemas operacionais
                Linux, não testada em Windows ou Mac. Na verdae nem me
                preocupei em preparar a função para funcionar corretamente
                em Windows ou Mac, portanto provavelmente ela NÃO FUNCIONARÁ
                nesses sistemas operacionais!
    
    Inputs: nenhum
    
    Outputs: print de informações
    
    Retorno: nenhum
    """
    import os
    import subprocess
    import sys
    import pip
    import platform
    import psutil
    import math
    
    data = subprocess.check_output(['date', '+%Y-%m-%d, %H:%M (UTC %:z), %A']).replace('\n', '')
    
    nomeComputador = platform.node()
    arquiteturaComputador = platform.machine()
    processador = platform.processor()
    MHz = psutil.cpu_freq()[2] / 1000.0
    coresFisicos = psutil.cpu_count(logical = False)
    coresLogicos = psutil.cpu_count()
    memoriaFisica = math.ceil(psutil.virtual_memory()[0] / 1024 / 1024 / 1024.0)
    
    plataforma = platform.system()
    plataforma2 = sys.platform
    osName = os.name
    versaoSO = platform.version()
    release = platform.release()
    
    versaoPython = platform.python_version()
    implementacaoPython = platform.python_implementation()
    buildPython = platform.python_build()[0] + ', ' + platform.python_build()[1]
    interpreterPython = sys.version.replace('\n', '')
    
    pacotes = sorted(["%s==%s" % (i.key, i.version) \
                      for i in pip.get_installed_distributions()])
    
    print('|-----------------------------------------------------------|')
    print('|                         HARDWARE                          |')
    print('|-----------------------------------------------------------|')
    print('Host:           ' + nomeComputador)
    print('Arquitetura:    ' + arquiteturaComputador)
    print('Processador:    ' + processador + ' de ' + str(MHz) + ' MHz (' \
          + str(coresFisicos) + ' cores físicos e ' + str(coresLogicos) + \
          ' cores lógicos)')
    print('Memória física: ' + str(memoriaFisica) + ' GB')
    print('|-----------------------------------------------------------|')
    print('|                         SOFTWARE                          |')
    print('|-----------------------------------------------------------|')
    print('Plataforma:     ' + plataforma + ' (' + plataforma2 + ', ' + osName \
                                               + ')')
    print('Versão:         ' + versaoSO)
    print('Release:        ' + release)
    print('|-----------------------------------------------------------|')
    print('|                         PYTHON                            |')
    print('|-----------------------------------------------------------|')
    print('Python:         ' + versaoPython)
    print('Implementação:  ' + implementacaoPython)
    print('Build:          ' + buildPython)
    print('Interpreter:    ' + interpreterPython)
    print('|-----------------------------------------------------------|')
    print('|                         PACKAGES                          |')
    print('|-----------------------------------------------------------|')
    for pacote in pacotes:
        print(pacote)
    print('|-----------------------------------------------------------|')
    print('|                         DATA                              |')
    print('|-----------------------------------------------------------|')
    print('A data atual do sistema é: ' + data)

ambienteDaAnalise()

#%% Diretórios de trabalho
import os
diretorioTrabalho = '/home/abrantesasf/repositoriosGit/udacity/machine_learning_nanodegree/modulo-02/projeto'
os.chdir(diretorioTrabalho)
print('Diretório de trabalho:')
print(os.getcwd())
print('Arquivos no diretório:' )
os.listdir(os.getcwd())

#%% Importar bibliotecas
import numpy as np
import pandas as pd
import visuals as vs # Supplementary code
from sklearn.cross_validation import ShuffleSplit

#%% Importar dados
data = pd.read_csv('housing.csv')
type(data)

prices = data['MEDV']
type(prices)

features = data.drop('MEDV', axis = 1)
type(features)

#%% Conhecendo os dados
# Primeiras e útlimas observações
data.head()
data.tail()

# Alguma variável tem NA?
data.isna().apply(np.sum)

# Descrição básica dos dados:
data.describe()

# Range dos dados:
data.max() - data.min()

# Histograma e Boxplots das variáveis:
data.hist('MEDV')
data.boxplot('MEDV')

data.hist('RM')
data.boxplot('RM')

data.hist('LSTAT')
data.boxplot('LSTAT')

data.hist('PTRATIO')
data.boxplot('PTRATIO')

#%% Implementação: calcular estatísticas

# TODO: Preço mínimo dos dados

# Usando Pandas
#minimum_price = prices.min()
#minimum_price

# Usando Numpy
minimum_price = np.min(prices)
minimum_price

# TODO: Preço máximo dos dados

# Usando Pandas
#maximum_price = prices.max()
#maximum_price

# Usando Numpy
maximum_price = np.max(prices)
maximum_price

# TODO: Preço médio dos dados

# Usando Pandas
#mean_price = prices.mean()
#mean_price

# Usando Numpy
mean_price = np.mean(prices)
mean_price

# TODO: Preço mediano dos dados

# Usando Pandas
#median_price = prices.median()
#median_price

# Usando Numpy
median_price = np.median(prices)
median_price

# TODO: Desvio padrão do preço dos dados

# Usando Pandas
#std_price = prices.std()
#std_price

# Usando Numpy
std_price = np.std(prices, ddof = 1)
std_price

#%% Plot de correlações básicas:
data.plot.scatter('RM', 'MEDV')
data.plot.scatter('LSTAT', 'MEDV')
data.plot.scatter('PTRATIO', 'MEDV')
pd.plotting.scatter_matrix(data, alpha = 0.2, diagonal = 'kde')

#%% Estudando mais a relação entre PTRATIO e MEDV:
data['temp'] = features['PTRATIO'].apply(round).apply(int).apply(str)
data.boxplot('MEDV', by = 'temp', figsize=(10,10))
data.drop('temp', axis = 1)

#%% Função para retornar o R2 do modelo:
def performance_metric(y_true, y_predict):
    """ Calcular e retornar a pontuação de desempenho entre 
        valores reais e estimados baseado na métrica escolhida. """
    
    # Importa a função r2_score:
    from sklearn.metrics import r2_score
    
    # TODO: Calcular a pontuação de desempenho entre 'y_true' e 'y_predict'
    score = r2_score(y_true, y_predict)
    
    # Devolver a pontuação
    return score

# Teste da função:
# Modelo mais ou menos:
score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print "O coeficiente de determinação, R^2, do modelo é {:.3f}.".format(score)

# Modelo que só prevê a média:
x = np.mean([2.5, 0.0, 2.1, 7.8, 5.3])
score = performance_metric([3, -0.5, 2, 7, 4.2], [x, x, x, x, x])
print "O coeficiente de determinação, R^2, do modelo é {:.3f}.".format(score)

# Modelo que erra semprej (absolutamente exagerado):
score = performance_metric([3, -0.5, 2, 7, 4.2], [-9, 10, -4, 0, 99])
print "O coeficiente de determinação, R^2, do modelo é {:.3f}.".format(score)

#%% Randomizar e dividir os dados em treinamento e teste
# TODO: Importar 'train_test_split'
from sklearn.cross_validation import train_test_split

# TODO: Misturar e separar os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, prices,
                                                    test_size = 0.2,
                                                    random_state = 1974)

# Êxito
print "Separação entre treino e teste feita com êxito."
X_train.head()
y_train.head()

#%% Gera Learning Curves
# Utiliza as funções suplementares fornecidas pela Udacity, no
# arquivo visuals.py:
vs.ModelLearning(features, prices)

#%% Gera a Model Complexity Graph
vs.ModelComplexity(X_train, y_train)

#%% Treinar um modelo de árvore de decisão
# TODO: Importar 'make_scorer', 'DecisionTreeRegressor' e 'GridSearchCV'
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import make_scorer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV

def fit_model(X, y):
    """ Desempenhar busca em matriz sobre o parâmetro the 'max_depth' para uma 
        árvore de decisão de regressão treinada nos dados de entrada [X, y]. """
    
    # Gerar conjuntos de validação-cruzada para o treinamento de dados
    # sklearn versão 0.17: ShuffleSplit(n, n_iter=10, test_size=0.1, train_size=None, random_state=None)
    # sklearn versão 0.18: ShuffleSplit(n_splits=10, test_size=0.1, train_size=None, random_state=None)
    cv_sets = ShuffleSplit(n_splits = 10, test_size = 0.20, random_state = 0)

    # TODO: Gerar uma árvore de decisão de regressão de objeto
    regressor = DecisionTreeRegressor(random_state = 1974)

    # TODO: Gerar um dicionário para o parâmetro 'max_depth' com um alcance de 1 a 10
    params = {'max_depth': range(1,11)}

    # TODO: Transformar 'performance_metric' em uma função de pontuação utilizando 'make_scorer' 
    scoring_fnc = make_scorer(performance_metric)

    # TODO: Gerar o objeto de busca em matriz
    grid = GridSearchCV(estimator = regressor,
                        param_grid = params,
                        scoring = scoring_fnc,
                        cv = cv_sets)

    # Ajustar o objeto de busca em matriz com os dados para calcular o modelo ótimo
    grid = grid.fit(X, y)

    # Devolver o modelo ótimo depois de realizar o ajuste dos dados
    return grid.best_estimator_

# Ajustar os dados de treinamento para o modelo utilizando busca em matriz
reg = fit_model(X_train, y_train)

# Produzir valores para 'max_depth'
print "O parâmetro 'max_depth' é {} para o modelo ótimo.".format(reg.get_params()['max_depth'])