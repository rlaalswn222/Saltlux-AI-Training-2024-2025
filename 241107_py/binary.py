#십진수를 이진수로
num = int(input('이진법으로 바꾸고 싶은 십진법 숫자를 입력하세요: '))

#나머지
remain = 0
#이진법 문자열 생성
binary = ''

# 0인 경우 특별히 처리
if num == 0:
    binary = '0'

# num이 0이 될 때까지 루프
while num > 0:
    remain = num % 2  # 나머지를 구함
    binary = str(remain) + binary  # 나머지를 이진법 문자열에 추가
    num = num // 2  # num에 몫을 저장하여 반복

print(binary)
