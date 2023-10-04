'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : while문으로 별 만들기
'''
import turtle as t

t.shape('turtle')
t.speed(1000)

i = 1

while i <= 5 :
    t.forward(200)
    t.right(144)
    i += 1
    
t.mainloop() 