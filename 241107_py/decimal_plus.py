a = int(input('첫 번째 십진수를 입력하세요: '))
b = int(input('두 번째 십진수를 입력하세요: '))

#십진수 문자열
binary = ''
#나머지
remain = 0
bin =''
sum = a+b

length = len(str(sum))
sum_list = str(sum)

# 0인 경우 특별히 처리
if sum == 0:
    binary = '0'

# num이 0이 될 때까지 루프
while sum > 0:
    remain = sum % 2  # 나머지를 구함
    binary = str(remain) + binary  # 나머지를 이진법 문자열에 추가
    sum = sum // 2  # num에 몫을 저장하여 반복

print(binary)
