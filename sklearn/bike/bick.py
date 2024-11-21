import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import missingno as msno #결측치 보는 plot

df_train = pd.read_csv('C:/Users/r2com/Desktop/Python/code/sklearn_241120/bike/train.csv')
#df_train.info()
df_train['datetime']
df_train["date"] = df_train.datetime.apply(lambda x : x.split()[0])
df_train["hour"] = df_train.datetime.apply(lambda x : x.split()[1].split(":")[0])
df_train["weekday"] = df_train.date.apply(lambda dateString : calendar.day_name[datetime.strptime(dateString,"%Y-%m-%d").weekday()])
df_train["month"] = df_train.date.apply(lambda dateString : calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])
df_train["season"] = df_train.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })
df_train["weather"] = df_train.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })
                                    
categoryVariableList = ["hour","weekday","month","season","weather","holiday","workingday"]
for var in categoryVariableList:
    df_train[var] = df_train[var].astype("category")

msno.matrix(df_train,figsize=(12,5))
#plt.show()


df_train_1 = df_train.copy() 


df_train_1['datetime'] = pd.to_datetime(df_train_1['datetime']) #drop안했음.
#슬라이싱이 가능하게 datetime구조로 바꿈.
df_train_1.dtypes
df_train_1.isna().sum()
df_train_1['year'] = df_train_1['datetime'].dt.year
df_train_1['month'] = df_train_1['datetime'].dt.month
df_train_1['day'] = df_train_1['datetime'].dt.day
df_train_1['hour'] = df_train_1['datetime'].dt.hour
df_train_1['minute'] = df_train_1['datetime'].dt.minute
df_train_1['second'] = df_train_1['datetime'].dt.second
#요일 데이터 -일요일은 0
df_train_1['dayofweek'] = df_train_1['datetime'].dt.dayofweek

figure, ((ax1, ax2, ax3),(ax4, ax5,ax6))=plt.subplots(nrows=2,ncols=3)
figure.set_size_inches(18,8)

sns.barplot(data=df_train_1, x="year", y="count", ax=ax1)
sns.barplot(data=df_train_1, x="month", y="count", ax=ax2)
sns.barplot(data=df_train_1, x="day", y="count", ax=ax3)
sns.barplot(data=df_train_1, x="hour", y="count", ax=ax4)
sns.barplot(data=df_train_1, x="minute", y="count", ax=ax5)
sns.barplot(data=df_train_1, x="second", y="count", ax=ax6)

ax1.set(ylabel='Count', title ="Year rental amount")
ax2.set(ylabel='month', title ="Month rental amount")
ax3.set(ylabel='day', title ="Day rental amount")
ax4.set(ylabel='hour', title ="Hour rental amount")

plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12,10)
sns.boxplot(data=df_train_1, y="count", orient= "v", ax=axes[0][0])
sns.boxplot(data=df_train_1, y="count", x = "season",orient= "v", ax=axes[0][1])
sns.boxplot(data=df_train_1, y="count", x="hour",orient= "v", ax=axes[1][0])
sns.boxplot(data=df_train_1, y="count", x="workingday",orient= "v", ax=axes[1][1])

axes[0][0].set(ylabel='Count',title="Rental amount")
axes[0][1].set(xlabel='Season',ylabel='Count',title="Seasonal Rental amount")
axes[1][0].set(xlabel='Hour of The Day',ylabel='Count',title="Hour Rental amount")
axes[1][1].set(xlabel='Working Day',ylabel='Count',title="Working or not Rental amount")
plt.show()

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplot(nrows = 5)
fig.set_size_inches(18, 25)

#꺽은선 그래프
sns.pointplot(data = df_train_1, x = "hour", y="count", ax =ax1)

sns.pointplot(data=df_train_1, x="hour",y="count", hue="workingday",ax=ax2)

sns.pointplot(data=df_train_1, x="hour",y="count", hue="dayofweek",ax=ax3)

sns.pointplot(data=df_train_1, x="hour",y="count", hue="weather",ax=ax4)

sns.pointplot(data=df_train_1, x="hour",y="count", hue="season",ax=ax5)

plt.show()