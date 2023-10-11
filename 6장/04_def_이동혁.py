'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려 받기.
    
    두 수를 전달받아 사칙 연산의 결과값을 돌려주는 함수.

    [알고리즘]
    (함수)
        두 수를 전달받아 매개변수에 저장한다.
        두 수를 계산한다.
        계산된 수를 함수를 호출한 곳으로 돌려준다.
    
    (메인)
        두 수를 입력받는다.
        두 수를 가지고 함수를 호출한다.
        돌려받은 값을 출력한다.
'''
#함수 선언
def cals(num1, num2) :
    sum = num1 + num2
    minus = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    return sum, minus, multi, div, rest

# 메인
num1 = int(input('첫번째 수를 입력하시오'))
num2 = int(input('두번째 수를 입력하시오'))

sum, minus, multi, div, rest = cals(num1, num2)
print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {minus}')
print(f'{num1} x {num2} = {multi}')
print(f'{num1} ÷ {num2} = {div}')
print(f'{num1} % {num2} = {rest}')