'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395023 이동혁
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
            
    Test word : programming
'''
# 단어 입력받아 변수에 저장
word = input('단어를 입력하세요 : ')


print(':: break1 ::')
for i in word :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        break
    else :
        print(i, end='')    

print()

print(':: break2 ::')
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        break
    else :
        print(i, end='')  
        
print()

print(':: continue ::')
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        continue
    print(i, end='')    #prgrmmng