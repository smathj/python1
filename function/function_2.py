# 매개변수가 몇개인지 모를때 

''' 매개변수를 모두 더하는 함수 '''
def mySum(*args) :
    result = 0  # return용 value
    for i in args:
        result = result + i

    return result

# 1 ~ 10 까지 덧셈
print(mySum(1,2,3,4,5,6,7,8,9,10))



''' 매개변수를 모두 곱하는 함수 '''
def myMulti(*naTae) :
    result = 1  # return용 value
    for i in naTae:
        result = result * i

    return result

# 1 ~ 10 까지 곱셈
print(myMulti(1,2,3,4,5,6,7,8,9,10))


