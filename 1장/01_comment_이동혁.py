'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 주석과 출력 함수 사용하기.
'''
# 학과 학번 이름을 저장하시오.
major = "컴퓨터공"
id = 202395023
name = "이동혁"

# 출력한다
print('학과 : {}학부' .format(major))
print('학번 : {}' .format(id))
print('이름 : {}' .format(name))

# 안녕하세요. 저는 00학과 00학번 000입니다.
print("안녕하세요. 저는 {}학과 {}학번 {}입니다." .format(major, id, name))

# 파이썬을 10개 출력하시오. (반복문 사용안함)
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')
print('파이썬')

print('파이썬' *256)

num1 = '10'
num2 = '20'

print(num1 + num2)