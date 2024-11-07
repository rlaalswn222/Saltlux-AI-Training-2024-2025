import requests
res = requests.get('http://naver.com')
print('resquest num:', res.status_code)

if res.status_code == requests.codes.ok:
    print('정상입니다.')
else: 
    print('문제가 생겼습니다.')