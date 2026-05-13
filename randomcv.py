# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:26:42 2024

@author: miles
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
import sklearn.metrics
from sklearn.metrics import classification_report
import os

# randomized grid search cross-fold validation -- set and forget -- can speed up with n_jobs (based on number of threads/cores on your cpu)

# 1-13a

os.chdir('1_13a')

X_rf = np.loadtxt("x_rf_1_13a.csv", delimiter=',')
y_rf = np.loadtxt("y_rf_1_13a.csv", delimiter=',')

X_train, X_test, y_train, y_test = train_test_split(X_rf, y_rf, random_state=1, test_size=0.5)

n_estimators = [int(x) for x in np.linspace(start=10,stop=2000,num=20)]
max_depth = [int(x) for x in np.linspace(start=1, stop=100, num=20)]
min_samples_split = [5, 10, 15, 20, 25]


random_grid = {'n_estimators': n_estimators,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split}

rf = RandomForestClassifier(class_weight='balanced')
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100,
                               cv=5, verbose = 2, n_jobs=2, random_state=1, scoring='f1_weighted')
rf_random.fit(X_train, y_train)

y_pred = rf_random.predict(X_test)
print('1-13a')
print(classification_report(y_test, y_pred, digits=6))


# best_params are the best HYPERparameters

best_params_1_13a = rf_random.best_params_
print(best_params_1_13a)

os.chdir('..')

# 6-3a

os.chdir('6_3a')

X_rf1 = np.loadtxt("x_rf_6_3a.csv", delimiter=',')
y_rf1 = np.loadtxt("y_rf_6_3a.csv", delimiter=',')

X_train1, X_test1, y_train1, y_test1 = train_test_split(X_rf1, y_rf1, random_state=1, test_size=0.5)

n_estimators = [int(x) for x in np.linspace(start=10,stop=2000,num=20)]
max_depth = [int(x) for x in np.linspace(start=1, stop=100, num=20)]
min_samples_split = [5, 10, 15, 20, 25]


random_grid = {'n_estimators': n_estimators,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split}

rf1= RandomForestClassifier(class_weight='balanced')
rf_random1 = RandomizedSearchCV(estimator = rf1, param_distributions = random_grid, n_iter = 100,
                               cv=5, verbose = 2, n_jobs=2, random_state=1, scoring='f1_weighted')
rf_random1.fit(X_train1, y_train1)

y_pred1 = rf_random1.predict(X_test1)
print('6-3a')
print(classification_report(y_test1, y_pred1, digits=6))

best_params_6_3a = rf_random.best_params_
print(best_params_6_3a)

os.chdir('..')

# 16-2a

os.chdir('16_2a')

X_rf2 = np.loadtxt("x_rf_16_2a.csv", delimiter=',')
y_rf2 = np.loadtxt("y_rf_16_2a.csv", delimiter=',')

X_train2, X_test2, y_train2, y_test2 = train_test_split(X_rf2, y_rf2, random_state=1, test_size=0.5)

n_estimators = [int(x) for x in np.linspace(start=10,stop=2000,num=20)]
max_depth = [int(x) for x in np.linspace(start=1, stop=100, num=20)]
min_samples_split = [5, 10, 15, 20, 25]


random_grid = {'n_estimators': n_estimators,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split}

rf2 = RandomForestClassifier(class_weight='balanced')
rf_random2 = RandomizedSearchCV(estimator = rf2, param_distributions = random_grid, n_iter = 100,
                               cv=5, verbose = 2, n_jobs=2, random_state=1, scoring='f1_weighted')
rf_random2.fit(X_train2, y_train2)

y_pred2 = rf_random2.predict(X_test2)
print('16-2a')
print(classification_report(y_test2, y_pred2, digits=6))

best_params_16_2a = rf_random.best_params_
print(best_params_16_2a)

os.chdir('..')