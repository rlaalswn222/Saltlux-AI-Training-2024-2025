#URL에 들어가서 쿼리 변경 후에 해당 단어가 있는 것들 뽑아오기

from bs4 import BeautifulSoup
import requests as req

url = 'https://search.naver.com/search.naver'
res = req.get(url, params={'query': '정처기'}) 
#https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%EC%A0%95%EC%B2%98&qdt=0&ie=utf8&query=%EC%A0%95%EC%B2%98%EA%B8%B0 url주소에 쿼리 값이 정처기인 것

if res.status_code == 200: #정상 반응
    soup = BeautifulSoup(res.text, 'html.parser')
    #respons로 받아온 것을 html.parser라는 것으로 짜른다.

    #정보처리기사 포함된 텍스트를 모두 찾기
    target_lst = [] #빈공간부터 만들기
    for element in soup.find_all(text=True): #모든 텍스트를 가져옴, bs4로 다른 것을 모두 찾아주는 (find_all(txt면 다))

        #변수 element로 받아줌
        if '정보처리기사' in element: 
            # element안에 '정보처리기사'라는 단어가 있으면 target_lst에 쌓음 
            # .strip()으로 쌓아주는 것
            target_lst.append(element.strip())
            #striup(): 문자열의 시작과 끝에서 공백을 제거한 후 반환
    print(target_lst)
else:
    print(f'요청실패: {res.status_code}')
