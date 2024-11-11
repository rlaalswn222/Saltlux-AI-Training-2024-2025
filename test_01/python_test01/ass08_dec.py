# + 10진수가 주어지면 2진수와 5진수로 바꿀수 있는 한꺼번에 작동할 수 있는 함수를 작성하시오.


def ten_to_bin_five(num): #num type=int
    num_5 =num
    if num == 0:
        num = '0'
    
    binary ='' #10진수를 2진수로
    # 0이 될 때까지 while
    while num > 0:
        remain = num % 2  # 나머지를 구함
        binary = str(remain) + binary  # 나머지를 이진법 문자열에 앞으로 추가
        num = num // 2  # num에 몫을 저장하여 반복

    five_num ='' #10진수를 5진수로
    # 0이 될 때까지 while
    while num_5 > 0:
        remain = num_5 % 5  # 나머지를 구함
        five_num = str(remain) + five_num  # 나머지를 이진법 문자열에 앞으로 추가
        num_5 = num_5//5 # num에 몫을 저장하여 반
    # five_num = int(five_num) # type을 정수형으로 변환
    return binary, five_num

num_2 = int(input('2진수와 5진수로 바꿀 수 있는 10진수를 입력하세요: '))
print(ten_to_bin_five(num_2))