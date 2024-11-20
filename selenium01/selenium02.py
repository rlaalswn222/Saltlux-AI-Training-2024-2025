from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pandas


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81%20%EA%B1%B0%EC%B9%98%EB%8C%80&channel=auto')

#전체를 접근해놓고 해도 상관없긵함!
#^는 논리 연산자
#비교를 할 때 사용한다 
#ex) CSS에서 a[href^="https"]는 href 속성이 "https"로 시작하는 모든 a 태그를 선택합니다.
