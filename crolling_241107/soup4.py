#.은 한개의 임의의 문자를 나타냄

import re
# r = re.compile('a.c')
# print(r.search('kkk'))
# print(r.search('abc'))
# print(r.search('aaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc'))

# #찾고자 하는 문자열은 span=(0, 3)

# #?: ?앞에 문자가 존재할수도 있고 존재하지 않을 수도 있는 경우를 나타내는 경우
# #ex) ab?c 라면 b는 있을ㅇ 수도 있고 없다고 취급할 수도 있다

# r1 = re.compile('ab?c')
# print(r1.search('abbc')) #아무것도 출력되지 않음
# print(r1.search('abc'))
# print(r1.search('ac'))

# *기호: 바로 앞의 문자가 0개 이상인 경우
# r2 = re.compile('ab*c')
# print(r2.search("a"))
# print(r2.search("ac"))
# print(r2.search("abbc"))

# #+기호: *와 유사 앞의 문자가 최소 1개 이상인 경우
# r3 = re.compile('ab+c')
# print(r3.search("a"))
# print(r3.search('abc'))

# ^: 시작되는 글자를 지정
r4 = re.compile('^a')
print(r4.search('bbc'))
print(r4.search('ab'))

#[] : 문자들을 넣으면 그 문자들 중 한개의 문자와 매치라는 의미를 가짐
# [a-c] #[abc]
#[0-5] #[012345]
#[a-zA-Z] 모든 알파벳
#[^0-9] 숫자
#[^0-999] - [0-9999] -[0-9999]
