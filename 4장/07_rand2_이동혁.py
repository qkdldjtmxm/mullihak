'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 선택문 if-else
           random을 이용한 가위바위보 게임. 

           random함수로 생성된 정수를 가지고 게임을 ㅇ진행
           0 => 가위
           1 => 바위
           2 => 보
           
           두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''
import random   #랜덤함수 가져오기

print('::가위 바위 보 게임 시작 ::')

player1 = input('Player1의 이름 : ')
player2 = input('Player2의 이름 : ')

num1 = random.randrange(3)     #랜덤으로 0,1,2 생성하여 변수에 저장
num2 = random.randrange(3)

# Player1의 가위바위보 출력
print(player1, ': ', end='')
if num1 == 0 :
    print('가위')
elif num1 == 1 :
    print('바위')
else :
    print('보')
    
# Player2의 가위바위보 출력
print(player2, ': ', end='')
if num2 == 0 :
    print('가위')
elif num2 == 1 :
    print('바위')
else :
    print('보')
    
#승자 판별
if num1 == num2 :
    print('비겼습니다.')
elif num1 == (num2 + 1) %3 :
    print(f'{player1}의 승리')
else :
    print(f'{player2}의 승리')