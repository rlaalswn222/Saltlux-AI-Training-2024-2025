#html 파일로 만들어주기

import requests

res = requests.get('http://google.com')
res.raise_for_status()

with open('mygoogle.html', 'w', encoding='utf-8') as f:
    f.write(res.text)