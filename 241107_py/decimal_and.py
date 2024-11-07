#숫자 두개를 이진수로 바꾼 다음에 연산을 해야할지, 두개를 십진수 상태에서?
# 십진수를 이진수로 변환 후에 and연산
num1 = int(input('첫 번째 십진수를 입력하세요: '))
num2 = int(input('두 번째 십진수를 입력하세요: '))

# 이진수로 변환
binary1 = bin(num1)[2:]
binary2 = bin(num2)[2:]

# print(f"첫 번째 숫자의 이진수: {binary1}")
# print(f"두 번째 숫자의 이진수: {binary2}")

and_result = int(binary1, 2) & int(binary2, 2)

# 결과를 이진수로 변환
binary = bin(and_result)[2:]

# 출력
print(f"이진수 상태에서 AND 연산 결과: {binary}")
