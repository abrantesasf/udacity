#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:09:08 2018

@author: abrantesasf
"""

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################


#### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)


from sklearn.metrics import accuracy_score
y_pred = clf.predict(features_test)

acc = accuracy_score(y_pred, labels_test)
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}