#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:59:12 2018

@author: abrantesasf
"""

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array1

array2 = np.array([2, 3, 4, 5, 6])
array2

# Multiplicação vetorial dos arrays:
array1 * array2

# Dot product dos arrays
np.dot(array1, array2)



array3 = np.array([1, 2])
array3
matriz1 = np.array([[2, 4, 6], [3, 5, 7]])
matriz1

# Multiplicação do array pela matriz
np.dot(array3, matriz1)


array4 = np.array([8, 9, 10])
array4
matriz2 = np.array([[2, 4, 6], [3, 5, 7]])
matriz2
np.dot(matriz2, array4)
