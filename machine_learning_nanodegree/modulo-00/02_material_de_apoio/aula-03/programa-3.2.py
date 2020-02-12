#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:16:58 2018

@author: abrantesasf
"""

# Numpy tem funções para várias tarefas estatísticas
# Ex.: média, mediana, variância, desvio padrão, etc.
import numpy as np

# Tecnicamente os arrays de Numpy são diferentes das listas Python,
# mas executar operações Numpy em uma lista Python transformará a 
# lista como um array Numpy nos bastidores
numbers = [1, 2, 3, 4, 5]
np.mean(numbers)
np.median(numbers)
np.std(numbers)
np.var(numbers)
