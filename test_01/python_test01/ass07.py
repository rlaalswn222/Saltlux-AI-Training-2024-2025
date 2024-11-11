# 7. 십진수 a와 b가 주어집니다.
# 주어진 십진수 a와 b를 이진수로 변환하고, 그 후 다음 연산을 수행하세요:
# (1) a와 b를 더한 결과를 이진수로 출력하세요.
# (2) a에서 b를 뺀 결과를 이진수로 출력하세요.
# (3) a와 b의 AND 연산 결과를 이진수로 출력하세요.
# (4) a와 b의 OR 연산 결과를 이진수로 출력하세요.
# (5) a와 b의 XOR 연산 결과를 이진수로 출력하세요

#십진수를 이진수로 만드는 함수
def to_bin(num):
    binary =''
    if num == 0:
        num = '0'
    # 0이 될 때까지 while
    while num > 0:
        remain = num % 2  # 나머지를 구함
        binary = str(remain) + binary  # 나머지를 이진법 문자열에 앞으로 추가
        num = num // 2  # num에 몫을 저장하여 반복
    return binary

#십진수를 이진수로 바꿀 숫자 입력 받음
a = int(input('이진수로 바꾸고 싶은 첫번째 십진수 숫자를 입력하세요: '))
b = int(input('이진수로 바꾸고 싶은 두번째 십진수 숫자를 입력하세요: '))

# 십진수에서 덧셈, 뺄셈 후 to_bin함수 실행
sum = a+b
print(to_bin(sum))

sub = a-b
print(to_bin(sub))

#a, b를 이진수로 바꾼 후에 연산 진행
a=int(to_bin(a))
b=int(to_bin(b))

aaa = a & b
print(aaa)

ooo = a | b
print(ooo)

xxx = a ^ b
print(xxx)