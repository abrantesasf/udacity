#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:21:38 2018

@author: abrantesasf
"""

def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    # importando o módulo do GaussianNB
    from sklearn.naive_bayes import GaussianNB
    
    # criando o classificador
    clf = GaussianNB()
    
    # ajustando o classificador e retornando
    return clf.fit(features_train, labels_train)
    