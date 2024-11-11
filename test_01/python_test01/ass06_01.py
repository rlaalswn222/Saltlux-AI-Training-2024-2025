# 문제 6 : 숫자 추측 게임
# 문제 6에서 점수가 마이너스가 되면 게임 종료 되는 코드

from random import randint 
import numpy as np

scope = int(input('랜덤으로 선택될 숫자의 마지막 범위를 입력하세요: ')) #범위 지정
num_random =  np.random.randint(1, scope+1) #random 하게 생성된 정수
score = 100 #초기 점수 100점


while True:
    answer = int(input('랜덤한 숫자를 맞춰보세요: '))

    if answer > num_random:
        print('더 작은 숫자입니다.')
        score -= 10 #점수 차감

        if score < 0:
            print('맞출 기회를 다 썼습니다.')
            break

    elif answer < num_random:
        print('더 큰 숫자입니다.')
        score -= 10 #점수 차감
    
        if score < 0:
            print('맞출 기회를 다 썼습니다.')
            break

    else:
        print('정답입니다!')
        print(f'최종 점수: {score}')
        break

