# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:39:21 2024

@author: miles
"""
import numpy as np
import pandas as pd
import sklearn.metrics
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

feature_names = ["Ca", "Na", "Mg", "Fe", "K", "Ti"]

# 1-13a
result = permutation_importance(clf, X_test, y_test, n_repeats=10, random_state=1, n_jobs=2, scoring='f1_weighted')
forest_importances = pd.Series(result.importances_mean, index=feature_names)

# 6-3a
result1 = permutation_importance(clf1, X_test1, y_test1, n_repeats=10, random_state=1, n_jobs=2, scoring='f1_weighted')
forest_importances1 = pd.Series(result1.importances_mean, index=feature_names)

# 16-2a
result2 = permutation_importance(clf2, X_test2, y_test2, n_repeats=10, random_state=1, n_jobs=2, scoring='f1_weighted')
forest_importances2 = pd.Series(result2.importances_mean, index=feature_names)


df=pd.concat([forest_importances,forest_importances1, forest_importances2],axis=1)

# plot
fig, ax = plt.subplots()
df.plot.bar(yerr=[result.importances_std, result1.importances_std, result2.importances_std], ax=ax, edgecolor='k',
                            linewidth=1.5, fontsize=20)

ax.set_ylabel("Mean accuracy decrease", fontsize=20)
plt.legend(["1-13a", "6-3a","16-2a"], fontsize="16", loc ="upper left")
fig.tight_layout()
plt.setp(ax.spines.values(), linewidth=1)
plt.xticks(rotation=0)
plt.ylim=((0.0,0.40))
plt.margins(y=0)
plt.ylim=((0.0,0.40))
plt.show()



K_importance = np.mean([forest_importances["K"],forest_importances1["K"], forest_importances2["K"]])
Ti_importance = np.mean([forest_importances["Ti"],forest_importances1["Ti"], forest_importances2["Ti"]])
Mg_importance =np.mean([forest_importances["Mg"],forest_importances1["Mg"], forest_importances2["Mg"]])