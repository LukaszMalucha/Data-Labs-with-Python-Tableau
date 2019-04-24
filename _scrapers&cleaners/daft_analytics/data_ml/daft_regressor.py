# -*- coding: UTF-8 -*-
# Importing the libraries

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
import xgboost




# Importing dataset
dataset = pd.read_csv('cork_sales_2018.csv')
X = dataset.iloc[:, 1:5].values   
y = dataset.iloc[:, 5:6].values   


# Encoding categorical data
labelencoder_X_0 = LabelEncoder()
X[:, 0] = labelencoder_X_0.fit_transform(X[:, 0])    ## transform county 
onehotencoder = OneHotEncoder(categorical_features = [0,1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]                         ## remove first column to avoid dummy variable trap

 
 
# Fitting Regressors
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)  
regressor.fit(X, y)        


xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                           colsample_bytree=1, max_depth=7)
xgb.fit(X,y)





## predict single property
home = np.array([['Douglas', 1, 2, 1]])
home[:,0] = labelencoder_X_0.transform(home[:,0])

home = onehotencoder.transform(home).toarray()
home = home[:, 1:]


rf_pred = regressor.predict(home)
xgb_pred = xgb.predict(home)
