# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 23:57:36 2022

@author: SHERIF ATITEBI O
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib.colors import ListedColormap
#%%


dataset = pd.read_csv("Social_Network_Ads.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
#%%


#Splitting into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
#%%

#feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#%%

#Logistic Regression Model
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)
#%%

y_pred = classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
#%%

cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_test)
#%%













