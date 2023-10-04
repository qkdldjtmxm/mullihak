'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 사용자가 입력하는 숫자의 합을 계산하기
'''
# 합계 변수 
sum = 0

# 숫자 입력받기 
num = int(input('숫자를 입력하시오 : '))
sum = sum + num

# no라고 할때 까지 반복
under_construction = True
while under_construction :
    response = input('계속? (yes/no) : ')
    if response == 'yes' :
        num = int(input('숫자를 입력하시오 : '))
        sum = sum + num
        
    else :
        under_construction = False
print('합계는 : {}' .format(sum))

# --------------------------------------------------------------------------

sum = 0

asw = 'yes'

while asw == "yes" :
    num = int(input('숫자를 입력하시오 : '))
    sum = sum + num
    asw = int('계속? (yes/no) : ')
print('합계는 : {}' .format(sum))