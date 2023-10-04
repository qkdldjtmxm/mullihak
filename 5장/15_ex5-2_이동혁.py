'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 두 수를 입력 받아 두 수 사이읭 합계 출력하기
            1. 두 수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합계 출력하기
            
            심화문제 5-2, 141페이지
'''
# 두 수 입력받기
num1 = int(input('시작 숫자를 입력하시오 : '))
num2 = int(input('마지막 숫자를 입력하시오 : '))

# 만약 대 소가 바뀐다면
if num1 > num2 :
    num1, num2 = num2, num1
    

# 두 수 사이의 합 구하기
i = num1
sum = 0
while i <= num2 :
    sum = sum + i
    i += 1
print('두 수 사이의 합은 {}입니다.' .format(sum))

# 두 수 사이의 짝수의 합 구하기
i = num1 
sum = 0
while i <= num2 :
    if i % 2 == 0 :
            sum = sum + i
    i += 1
print('두 수 사이의 짝수의 합은 {}입니다.' .format(sum))