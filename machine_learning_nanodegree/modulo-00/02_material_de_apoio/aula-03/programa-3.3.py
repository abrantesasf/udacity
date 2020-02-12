#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:21:29 2018

@author: abrantesasf
"""

import numpy as np

'''
The following code is to help you play with Numpy, which is a library 
that provides functions that are especially useful when you have to
work with large arrays and matrices of numeric data, like doing 
matrix matrix multiplications. Also, Numpy is battle tested and 
optimized so that it runs fast, much faster than if you were working
with Python lists directly.
'''

'''
The array object class is the foundation of Numpy, and Numpy arrays are like
lists in Python, except that every thing inside an array must be of the
same type, like int or float.
'''
# Change False to True to see Numpy arrays in action
if True:
    array = np.array([1, 4, 5, 8], float)
    print('Array unidimensional do Numpy:')
    print(array)
    print('')
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print('Array bidimensional do Numpy (matrix):')
    print(array)

'''
You can index, slice, and manipulate a Numpy array much like you would with a
a Python list.
'''
# Change False to True to see array indexing and slicing in action
if True:
    array = np.array([1, 4, 5, 8], float)
    print('Array unidimensional do Nympy, criado com np.array():')
    print(array)
    print('')
    print('Selecionando o elemento [1] (índice começa em 0):')
    print(array[1])
    print('')
    print('Selecionando o internalo [:2]')
    print(array[:2])
    print('')
    print('Alterando o segundo elemento para 5:')
    array[1] = 5.0
    print(array)

# Change False to True to see Matrix indexing and slicing in action
if True:
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print('Array bidimensional do Numpy (matrix):')
    print(two_D_array)
    print('')
    print('Selecionando o elemento [1][1]:')
    print(two_D_array[1][1])
    print('')
    print('Selecionando todos os elementos da segunda linha:')
    print(two_D_array[1, :])
    print('')
    print('Selecionando a terceira coluna de todas as linhas:')
    print(two_D_array[:, 2])

'''
Here are some arithmetic operations that you can do with Numpy arrays
'''
# Change False to True to see Array arithmetics in action
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print('Array 1:')
    print(array_1)
    print('Array 2:')
    print(array_2)
    print('')
    print('Array 1 + Array 2:')
    print(array_1 + array_2)
    print('')
    print('Array 1 - Array 2:')
    print(array_1 - array_2)
    print('')
    print('Array 1 * Array 2:')
    print(array_1 * array_2)

# Change False to True to see Matrix arithmetics in action
if True:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print('Array 1:')
    print(array_1)
    print('Array 2:')
    print(array_2)
    print('')
    print('Array 1 + Array 2:')
    print(array_1 + array_2)
    print('')
    print('Array 1 - Array 2:')
    print(array_1 - array_2)
    print('')
    print('Array 1 * Array 2:')
    print(array_1 * array_2)

'''
In addition to the standard arthimetic operations, Numpy also has a range of
other mathematical operations that you can apply to Numpy arrays, such as
mean and dot product.

Both of these functions will be useful in later programming quizzes.
'''
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print('Array 1:')
    print(array_1)
    print('Array 2:')
    print(array_2)
    print('')
    print('Média do Array 1:')
    print(np.mean(array_1))
    print('')
    print('Média do Array 2:')
    print(np.mean(array_2))
    print('')
    print('Dot product dos Arrays:')
    print(np.dot(array_1, array_2))