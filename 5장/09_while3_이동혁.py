'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 조건에 따라 반복하는 while문
            교재 129페이지
            
            1~10까지의 합계를 계산하여 출력하기
            시작 값 : 1
            종료 값 : 10
            증가 값 : 1
            for i in range(1,11) : => while문으로..
            
            필요한 변수 : sum, num
'''
num = 1
sum = 0
while num <= 10 :   # 종료값(조건식)
    sum = sum + num
    num += 1
print('합계 : {}' .format(sum))