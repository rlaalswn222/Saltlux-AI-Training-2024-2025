#네이버 웹툰 주간 창 들어가서 lxml로 텍스트 나눠주기

from bs4 import BeautifulSoup
import requests

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
print(res.raise_for_status())

soup= BeautifulSoup(res.text, 'lxml')
print(soup)