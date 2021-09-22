# 리턴 복수개

def add_and_mul(a,b) :
    return a+b, a*b

result = add_and_mul(3,4)

print(result)
print(result[0])
print(result[1])


''' 매개변수에 초기값 미리 설정 '''
def say_myself(name, old, man=True) :
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다" %old)
    if man :
        print("남자입니다")
    else   :
        print("여자입니다")
        
say_myself("나태쿤", 1)
say_myself("나태쿤", 1, True)
say_myself("나태쿤", 1, False)