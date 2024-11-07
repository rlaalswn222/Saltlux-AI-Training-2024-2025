num = int(input('이진법으로 바꾸고 싶은 십진법 숫자를 입력하세요: '))

remain = 0
binary = ''

if num == 0:
    binary = '0'
while num >0:
    reamin = num % 2
    binary  = str(reamin) + binary
    num = num // 2

print(binary)