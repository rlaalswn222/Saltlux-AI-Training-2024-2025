# 2진수를 5진수와 10진수로 바꾸는 함수를 작성하시오. 
# + 10진수가 주어지면 2진수와 5진수로 바꿀수 있는 한꺼번에 작동할 수 있는 함수를 작성하시오.

# 2진수를 10진수와 5진수로 변환하는 함수

def to_(num): #num type=int
    decimal = 0
    length = len(str(num))
    num_list = str(num)
    for round in range(length):
        bin = int(num_list[round]) * (2**(length-round-1))
        decimal += bin

    num_dec = decimal
    five_num =''
    # 0이 될 때까지 while
    while num_dec > 0:
        remain = num_dec % 5  # 나머지를 구함
        five_num = str(remain) + five_num  # 나머지를 이진법 문자열에 앞으로 추가
        num_dec = num_dec//5 # num에 몫을 저장하여 반
    five_num = int(five_num) # type을 정수형으로 변환

    return decimal, five_num

num_2 = int(input('5진수와 10진수로 바꾸고 싶은 2진수를 입력하세요: '))
print(to_(num_2))
