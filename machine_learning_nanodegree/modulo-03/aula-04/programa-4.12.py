#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:17:11 2018

@author: abrantesasf
"""

#
#	Polynomial Regression
#
#	In this exercise we will examine more complex models of test grades as a function of 
#	sleep using numpy.polyfit to determine a good relationship and incorporating more data.
#
#
#   at the end, store the coefficients of the polynomial you found in coeffs
#

import numpy as np

sleep = [5,6,7,8,10,12,16]
scores = [65,51,75,75,86,80,0]

# Para o modelo "y = ax^2 + bx + c" usamos grau 2:
coeffs = np.polyfit(sleep, scores, 2)
coeffs
