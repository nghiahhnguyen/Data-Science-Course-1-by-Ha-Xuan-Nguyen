#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:22:40 2018

@author: nghia-nguyen
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# Load dataset
iris=datasets.load_iris()

X=iris.data
y=iris.target
knn = KNeighborsClassifier(n_neighbors = 15)
knn.fit(X, y)

print("15NN accuary score of Iris data:", knn.score(X,y))

X_new = np.array([[5.1, 3.5, 1.4, 0.2],[5.9, 3. , 5.1, 1.8]])
prediction = knn.predict(X_new)
print("Prediction for X_new is", prediction)

# 

