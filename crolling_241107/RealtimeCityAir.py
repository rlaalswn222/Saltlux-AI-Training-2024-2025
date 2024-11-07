#api불러와서 데이터 출력하기

import requests
from bs4 import BeautifulSoup

res = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
resj =res.json()
citys = resj['RealtimeCityAir']['row']

#print(resj['RealtimeCityAir']['row'][0]['NO2'])

#서울구 이름과 해당 구의 미세먼지 데이터만 가져와 출력

for city in citys():
    city_name = city["MSRSTE_NM"]
    city_mvl = city["IDEX_MVL"]
    print(city_name, city_mvl)