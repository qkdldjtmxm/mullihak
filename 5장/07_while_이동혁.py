'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 조건에 따라 반복하는 while문
            교재 127페이지
'''
# while 조건식 : => :반드시 사용.
#       들여쓰기로 반복하면서 할일 작성.

# 반복문에서는 반드시 종료 조건이 있어야 한다.
# while true :      무한반복

under_construction = True   #공사중

# True일 동안 계속 반복 (무한반복)
while under_construction :
    response = input("공사가 완료 되었습니까? (예/아니오)")
    if response == "예" :
        under_construction = False  #공사 완료
        
print('루프 탈출!!!')