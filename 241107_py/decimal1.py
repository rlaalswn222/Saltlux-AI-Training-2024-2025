#이진수를 십진수로
num = int(input('십진수로 바꾸고 싶은 이진수를 입력하세요: '))

#십진수 문자열
decimal = 0

length = len(str(num))
num_list = str(num)
for round in range(length):
    bin = int(num_list[round]) * (2**(length-round-1))
    decimal += bin

print(decimal)