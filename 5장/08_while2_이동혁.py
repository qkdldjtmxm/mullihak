'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 사용자로부터 암호를 입력 받아 로그인하기
            교재 128페이지
            
            사용자로부터 계속해서 암호를 입력 받는다.
            암호가 맞으면 로그인 성공 메세지를 출력한다.
            암호가 맞을 때 까지 반복
            암호는 1234
'''
pwd = ''

while pwd != '1234' :
    pwd = input('암호를 입력하시오 : ')

print('로그인 성공!')

under_construction = True 

while under_construction :
    response = input('암호를 입력하시오 : ')
    if response == '1234' :
        under_construction = False
print('로그인 성공!')