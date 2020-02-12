#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:17:12 2018

@author: abrantesasf
"""

import pandas as pd

'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the 
DataFrame. 

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# Change False to True to see Series indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print('Selecionando uma coluna:')
    print(football['year'])
    print('')
    print('Selecionando uma coluna com atalho:')
    print(football.year)  # shorthand for football['year']
    print('')
    print('Selecionando mais de uma coluna:')
    print(football[['year', 'wins', 'losses']])

'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
# Change False to True to see boolean indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print('Selecionando uma linha por sua posição com o ILOC:')
    print(football.iloc[[0]])
    print('')
    print('Selecionando uma linha por seu index label com o LOC:')
    print(football.loc[[0]])
    print('')
    print('Selecionando várias linhas com um range (index começa em 0):')
    print(football[3:5])
    print('')
    print('Selecionando linhas com uma condição booleana:')
    print(football[football.wins > 10])
    print('')
    print('Selecionando linhas com mais de uma condição booleana:')
    print(football[(football.wins > 10) & (football.team == "Packers")])