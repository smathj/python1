coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피 준다")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다" % coffee)
    print( "-" * 40)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 장사 끝")
        break


