from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb')

SCROLL_PAUSE_SEC = 1
last_height = driver.execute_script('return document.body.scrolHeight')

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrolHeight)")
    time.sleep(SCROLL_PAUSE_SEC)
    new_height = driver.execute_script('return document.body.scrolHeight')
    if new_height == last_height:
        break
    last_height = new_height
# lists = driver.find_element(By.CLASS_NAME, 'viewtype')
# print(len(lists))

lists = driver.find_element(By.ID, 'bestPrdList').find_elements(By.CLASS_NAME, 'viewtype')

for list_section in lists:
    bestlist = list_section.find_elements(By.TAG_NAME, 'li')
    for item in bestlist:
        print(item.text)