marks = [90,25,67,45,80]
number = 0

for mark in marks :
    number += 1
    if mark < 60: 
        continue

    print("%d번 학생 축하축하. 합격목걸이 드립니다" %number)


print("-" * 90)
######################################################


# range(param)함수는 : -0~ param (불연속) 숫자 리스트 리턴
a = range(10) 
for num in a :
    print(num)


print("-" * 90)


# 1~10
b = range(1,11)
for num in b :
    print(num)
