'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 피자의 면적을 구하시오.
           피자의 반지름이 필요하다.
           피자의 반지름은 입력 받아 계산한다.
'''
# 1. 반지름을 입력 받아 변수에 저장.
r = int(input('피자의 반지름을 입력하시오(cm) : '))
PI = 3.14

# 2. 피자의 면적 계산
area = PI * r**2

# 3. 피자의 면적 출력
print("반지름이 {}cm인 피자의 면적은 {:.2f}cm²입니다.".format(r, area))
