'''
[for문 ]

for 변수 in 리스트(또는 튜플,문자열):
    수행할 문장

'''

test_list = ['키북이','하북이','동경쿤']
for i in test_list: # List
    print(i)



print("-" * 90)
######################################################


a = [(1,2),(3,4),(5,6)] #  리스트안의 튜플
for(first,last) in a:   # 인덱싱이 튜플
    print(first + last)


print("-" * 90)
######################################################

marks = [90,25,67,45,80] # 리스트
number = 0
for mark in marks :
    number = number + 1 # 리시트 요소 새기
    if mark >= 60 :
        print("%d번 학생은 합격목걸이." %number)
    else :
        print("%d번 학생은 불합격목걸이." %number)

print("-" * 90)
######################################################




