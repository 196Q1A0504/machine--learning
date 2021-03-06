# -*- coding: utf-8 -*-
"""gold prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sI6cDtl9ji-n7XQRsDv9h9nRDxbTzAob

DATA COLLECTION AND PROCESSING
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sms
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

gold_data = pd.read_csv('/content/gld_price_data (3).csv')

gold_data.head()

# number of rows and columns
gold_data.shape

# BASIC INFORMATION ABOUT THE DATA
gold_data.info()

# missing value
gold_data.isnull().sum()

#statistacal measure of data
gold_data.describe()

# positive and negative corellation
correlation = gold_data.corr()

#correlation values of gold
print(correlation['GLD'])

#splitting the features and target
X=gold_data.drop(['Date','GLD'],axis=1)
Y=gold_data['GLD']

print(X)

print(Y)

#SPLITTING INTO TRAINING DATA AND TEST DATA
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=2)

#model training =random forest regressor
regressor = RandomForestRegressor(n_estimators=100)

# training the model 
regressor.fit(X_train,Y_train)

# Model Evaluation
# prediction on Test Data
test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

#Compare the Actual Values and Predicted Values in a Plot
Y_test = list(Y_test)

plt.plot(Y_test, color='orange', label = 'Actual Value')
plt.plot(test_data_prediction, color='yellow', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()

