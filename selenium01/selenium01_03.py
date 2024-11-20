from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb')

# 스크롤 다운
SCROLL_PAUSE_SEC = 1
last_height = driver.execute_script('return document.body.scrollHeight')

# 끝까지 스크롤 다운
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(SCROLL_PAUSE_SEC)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

# lists = driver.find_element(By.CLASS_NAME, 'viewtype')
# print(len(lists))

lists = driver.find_element(By.ID, 'bestPrdList').find_elements(By.CLASS_NAME, 'viewtype')

for list_section in lists:
    bestlist = list_section.find_elements(By.TAG_NAME, 'li')
    for item in bestlist:
        print('No: ', item.find_element(By.CLASS_NAME, 'best').text) #순번
        print('Product: ', item.find_element(By.CLASS_NAME, 'pname').find_element(By.TAG_NAME, 'p').text) #제품명
        print('Price: ', item.find_element(By.CLASS_NAME, 'sale_price').text) #가격
        print('URL: ', item.find_element(By.CLASS_NAME, 'box_pd.ranking_pd').find_element(By.TAG_NAME, 'a').get_attribute('href')) #링크

        print('-'*100)
