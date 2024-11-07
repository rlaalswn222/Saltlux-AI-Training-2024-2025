import re
text = '전화번호는 010-1234-5678 연락해'

#pattern = re.compile("\d{3}-\d{4}-\d{4}")
pat = re.compile("[0-9]{3} - [0-9]{4} - [0-9]{4}")
phone_list = pat.findall(text)
print(phone_list)
