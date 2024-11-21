# import numpy as np
# import pandas as pd    
# import statsmodels.api as sm
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_val_score

# df = pd.read_csv('C:/Users/r2com/Desktop/Python/code/sklearn_241120/bonton/boston.csv')

# #poly를 올려서 feature를 degree로 올려서 넣던지..
# # 경우의 수가 많아서 sklearn에서 제공하지 않음
# # Regression이 안돼서

# X = df.drop(columns='MEDV')
# y = df[['MEDV']]

# X = np.arange(4).reshape(2,2)
# print('일차 단항식 계수 feature: \n', poly)

# def polynomail_func(X):
#     y = 1+2*X +X**2 + X**3
#     return y
# y = polynomail_func(X)

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(poly, y)
# print('Polynomial 회귀 계수: \n', np.round(model.coef_, 2))
# print('Polynomial 회귀 shape: \n', modle.coef_.shape)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np

def polynomial_func(X):
    y = 1 + 2 * X + X ** 2 + X ** 3
    return y

# Pipeline 객체로 Streamline 하게 Polynomial Feature변환과 Linear Regression을 연결
model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                  ('linear', LinearRegression())])
X = np.arange(4).reshape(2,2)
y = polynomial_func(X)

model = model.fit(X, y)
print('Polynomial 회귀 계수\n', np.round(model.named_steps['linear'].coef_, 2))
