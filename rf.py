# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:01:49 2023

@author: miles
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics
from sklearn.metrics import classification_report
import os

# 1-13a

os.chdir('1_13a')

X_rf = np.loadtxt("x_rf_1_13a.csv", delimiter=',')
y_rf = np.loadtxt("y_rf_1_13a.csv", delimiter=',')

X_train, X_test, y_train, y_test = train_test_split(X_rf, y_rf, random_state=1, test_size=0.5)
clf = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_split=10, class_weight='balanced')
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('1-13a')
print(classification_report(y_test, y_pred, digits=6))

os.chdir('..')

# 6-3a

os.chdir('6_3a')

X_rf1 = np.loadtxt("x_rf_6_3a.csv", delimiter=',')
y_rf1 = np.loadtxt("y_rf_6_3a.csv", delimiter=',')

X_train1, X_test1, y_train1, y_test1 = train_test_split(X_rf1, y_rf1, random_state=1, test_size=0.5)
clf1 = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_split=10, class_weight='balanced')
clf1 = clf1.fit(X_train1, y_train1)
y_pred1 = clf1.predict(X_test1)
print('6-3a')
print(classification_report(y_test1, y_pred1, digits=6))

os.chdir('..')

# 16-2a

os.chdir('16_2a')

X_rf2 = np.loadtxt("x_rf_16_2a.csv", delimiter=',')
y_rf2 = np.loadtxt("y_rf_16_2a.csv", delimiter=',')

X_train2, X_test2, y_train2, y_test2 = train_test_split(X_rf2, y_rf2, random_state=1, test_size=0.5)
clf2 = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_split=10, class_weight='balanced')
clf2 = clf2.fit(X_train2, y_train2)
y_pred2 = clf2.predict(X_test2)
print('16-2a')
print(classification_report(y_test2, y_pred2, digits=6))

os.chdir('..')





























