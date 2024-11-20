from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

housing = fetch_california_housing(as_frame=True)

housing = housing.frame

#변수
#MedInc(중위소득), Housing Age(주택 연식), AveRooms(평균 방 개수), AveBedrms(평균 침실 수)
#Population(인구수), AveOccup(평균 거주자 수), Latitude(위도), Longitude(경도)

print(housing.head())
print(housing.info())

num_columns = len(housing.columns) #열의 길이
fig, axs = plt.subplots(nrows = (num_columns +2)//3, ncols=3, figsize=(15,10)) #3개씩 나눠서
#num_columns + 2 : 0, 1, 1, 1, 2, 2, 2, ,,
#figsize = (가로, 세로)
axs = axs.flatten() #flatten: 벡터로 만들어 줌. 일렬로

for i, column in enumerate(housing.columns):
    housing.boxplot(column = column, ax = axs[i])
    axs[i].set_title(column)

plt.tight_layout()
plt.show()