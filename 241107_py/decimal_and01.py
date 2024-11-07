# 두 개의 십진수를 입력받고 십진수를 and연산 진행 후 이진수로 변환
num1 = int(input('첫 번째 십진수를 입력하세요: '))
num2 = int(input('두 번째 십진수를 입력하세요: '))

and_dec = num1 & num2
binary = bin(and_dec)[2:]

# 출력
print(f"십진수 상태에서 AND 연산 결과 이진수: {binary}")
