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

url = "https://kream.co.kr/exhibitions/2575"
driver.get(url)

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


# lists = driver.find_element(By.CLASS_NAME, 'exhibition_item_products exhibition_item_section product_list')

# for list_section in lists:
#     bestlist = list_section.find_elements(By.TAG_NAME, 'li')
#     for item in bestlist:
#         #//*[@id="ex0"]/div[2]/div[1]/a/div[1]/div[1]/span
#         print('순위: ', driver.find_elements_by_xpath('//*[@id="ex0"]/div[2]/div[1]/a/div[1]/div[1]/span')) #순번
#         # print('상품명: ', driver.find_elements(By.CLASS_NAME, 'item_inner').product.find_element(By.CLASS_NAME, 'translated_name').text) #제품명
#         # print('가격: ', area.find_element(By.CLASS_NAME, 'amount').text.strip()) #가격
#         # print('URL: ', driver.find_elements(By.CLASS_NAME, 'item_inner').product.get_attribute('href') ) #링크

#         print('-'*100)
# 전체 리스트 항목을 선택하도록 XPath 수정
lists = driver.find_elements(By.XPATH, '//*[@id="ex0"]/div[contains(@class, "exhibition_item_products")]//li')

for item in lists:
        # 순위 추출
    rank = item.find_element(By.CLASS_NAME, "tag_text").text

        #브랜드 추출
    brand = item.find_element(By.CLASS_NAME, 'product_info_brand.brand').text
        # 상품명 추출
    name = item.find_element(By.CLASS_NAME, "translated_name").text

        # 가격 추출5
    price = item.find_element(By.CLASS_NAME, "amount").text

        # 링크 추출
    link = item.find_element(By.CSS_SELECTOR, "a.item_inner").get_attribute("href")

    print(f"순위: {rank}")
    print(f"브랜드: {brand}")
    print(f"상품명: {name}")
    print(f"가격: {price}")
    print(f"URL: {link}")
    print("-" * 100)


driver.quit()