'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 더하기 암산 문제 만들기
            2개의 수로 더하기 결과를 맞추는 게임.
            2개의 수는 1~100사이 랜덤으로 출제 됨.
            사용자가 0을 입력하면 프로그램은 종료.
            즉, 사용자가 0을 입력하기 전까지는 무한 반복하여 문제 풀기
            정답을 맞추면 " 참 잘했어요!"
            틀리면 정답을 알려주고, "정답은 00입니다. 틀렸습니다." 출력
            게임이 종료되면 "프로그램 종료!" 출력
    문제분석 :
    
    알고리즘 :
                
'''
import random

while True :
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    cal = random.randrange(2)
    if cal == 0 :
        answer = int(input('{} + {} = ' .format(num1, num2)))
        if answer == num1 + num2 :
            print('참 잘했어요!')
        elif answer == 0 :
            print('프로그램 종료!')
            break
        else :
            print('정답은 {}입니다. 틀렸습니다.' .format(num1+num2))
    else :
        answer = int(input('{} - {} = ' .format(num1, num2)))
        if answer == num1 - num2 :
            print('참 잘했어요!')
        elif answer == 0 :
            print('프로그램 종료!')
            break
        else :
            print('정답은 {}입니다. 틀렸습니다.' .format(num1-num2))