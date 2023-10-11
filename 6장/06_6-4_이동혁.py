'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 mon을 입력받아 최대, 최소값을 찾아 돌려주는 함수.
    
    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.
    
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려 받은 최대값 또는 최소값을 출력한다.
'''
import random
# 함수 선언
def max1() :
    result = max(list)
    return result

def min1() :
    result = min(list)
    return result

while True :
    list = random.choices(range(1,100), k=10)     #랜덤 리스트 1~99까지 10개의 수
    print(list)     # 리스트 출력
    cur = input('max or min? : ')   # 무엇을 알고 싶은가
    if cur == 'max' :       
        print(max1())
    elif cur == 'min' :
        print(min1())
    else :
        print('retry')