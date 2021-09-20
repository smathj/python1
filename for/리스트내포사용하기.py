a = [1,2,3,4]
result = []

for i in a :
    result.append(i*3)

print(result)

##################################

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


##################################

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 ==0]
print(result)


'''
[리스트 내포 문법]
표현식 for 항목 in 반복_가능_객체 if 조건

'''