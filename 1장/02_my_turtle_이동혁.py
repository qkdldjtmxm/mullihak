'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 터틀 그리기.
'''
import turtle as t # 터틀 모듈을 사용하기 위한 준비
                   # turtle 클래스 객체를 t로 생성. (별명)
t.shape('turtle')
t.speed(1000)      #이동속도
# 선그리기

# t.forward(200)  #200 픽셀 이동.

# 삼각형 그리기
#t.forward(200)  #200 픽셀 이동
#t.left(120)      #왼쪽으로 120도 회전
#t.forward(200)  #200 픽셀 이동
#t.left(120)      #왼쪽으로 120도 회전
#t.forward(200)  #200 픽셀 이동
#t.left(120)      #왼쪽으로 120도 회전

for i in range(2880) :
    t.forward(0.125)  #200 픽셀 이동
    t.left(0.125)      #왼쪽으로 120도 회전






t.mainloop()    #그림판 유지