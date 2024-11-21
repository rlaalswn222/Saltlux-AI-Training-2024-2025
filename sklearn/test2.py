
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

housing = fetch_california_housing()
data = pd.DataFrame(housing.data, columns = housing.feature_names)
data['MedHouseVal'] = housing.target

corr_matrix = data.corr()
plt.figure(figsize = (12, 8))
sns.heatmap(corr_matrix, annot=True, cmap= 'coolwarm', fmt ='.2f', linewidths=0.5)
plt.title('Corrleation Matrix')
plt.show()