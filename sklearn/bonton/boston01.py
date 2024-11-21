import numpy as np
import pandas as pd    
import statsmodels.api as sm
df = pd.read_csv('C:/Users/r2com/Desktop/Python/code/sklearn_241120/bonton/boston.csv')

X = df.drop(columns='MEDV')
y = df[['MEDV']]
X_constant = sm.add_constant(X)
model_1 = sm.OLS(y, X_constant) #최소제곱법
lin_reg = model_1.fit()
print(lin_reg.summary())
