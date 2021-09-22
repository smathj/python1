# 변수 유효범위


a = "치킨"          # 전역 변수
def myFood(a) :
    a = a + "&피자" # 지역 변수
    return a

print(a)
print(myFood(a))


a = myFood(a)       # a를 return 값으로 초기화

print(a)


''' global 사용하기 '''
# 비추하는 방법

b = "피자"
def myPizza() :
    global b
    b = b +"&콜라"
    return b

print(myPizza())
print(b)
