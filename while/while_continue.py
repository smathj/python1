a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print("a가 홀수일때 , a의 값 %d" %a)


print("-" * 40)
print("b가 3의 배수가 아닐때 ")
b = 0
while b < 10:
    b += 1
    if b % 3 == 0: 
        continue
    print(b)
