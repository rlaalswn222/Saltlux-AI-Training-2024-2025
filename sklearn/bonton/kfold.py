import numpy as np
import pandas as pd    
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv('C:/Users/r2com/Desktop/Python/code/sklearn_241120/bonton/boston.csv')

X = df.drop(columns='MEDV')
y = df[['MEDV']]

#양수여도 음수여도 0으로 가야한다. 따라서 negative -> neg 없으면 오류남
#따라서 rmse_score는 음수라서 -1 곱해줘야한다.
lr = LinearRegression()
neg_mse_scores = cross_val_score(lr, X, y, scoring='neg_mean_squared_error', cv = 5)
rmse_scores = np.sqrt(-1*neg_mse_scores) 
avg_rmse = np.mean(rmse_scores)

print('5 fold의 개별 Negative MSE score: ', np.round(neg_mse_scores, 2))
print('5 fold의 개별 RMSE scores: ', np.round(rmse_scores,2))
print('5 fold의 평균 RMSE: {0:3f}'.format(avg_rmse))
