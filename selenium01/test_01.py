from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com')
driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys("아이유")
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('아이유')

# search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# search_button.click()

#driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys(Keys.ENTER) #이 방법 말고는 xml 접근 방식으로 접근
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

#뉴스 탭에서 tag갖고 올것

#//*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]/a/div
#//*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]/a
driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]/a').click()


# 뉴스 탭 클릭
# # //*[@id="hdtb-sc"]/div/div/div[1]/div/div[3]/a/div
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div/div/g-section-with-header/div[2]/div/div[2]/div[3]/div/a/div/div[2]'))
# ).click()
# driver.find_element(By.XPATH, '//*[@id="rso"]/div/div/g-section-with-header/div[2]/div/div[2]/div[3]/div/a/div/div[2]').click()

#//*[@id="rso"]/div/div/div[1]/div/div/a/div/div[2]/div[2]
# //*[@id="rso"]/div/div/div[2]/div/div/a/div/div[2]/div[2]
#//*[@id="rso"]/div/div/div[3]/div/div/a/div/div[2]/div[2]

# titles = []
# for num in range(1, 10):
#     links = driver.find_element(By.XPATH, '//*[@id="rso"]/div/div/div[{num}]/div/div/a/div/div[2]/div[2]')
#     for link in links:
#         titles.append(link.text)
#         print(titles)


# 뉴스 제목 가져오기
titles = []
links = driver.find_elements(By.CSS_SELECTOR,'.n0jPhd.ynAwRc.MBeuO.nDgy9d')
for link in links:
    titles.append(link.text)

print(titles)
# for num in range(1, 11):  # num 값을 1부터 10까지 반복
    
#     # 각 뉴스 제목의 XPath에 num 값을 삽입
#     title_xpath = f'//*[@id="rso"]/div/div/div[{num}]/div/div/a/div/div[2]/div[2]'
#     title_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, title_xpath))
#     )
#     titles.append(title_element.text)
#     # except Exception as e:
#     #     print(f"Element not found for div[{num}]: {e}")

# # 결과 출력
# for idx, title in enumerate(titles, 1):
#     print(f"Title {idx}: {title}")

# # WebDriver 종료
# driver.quit()