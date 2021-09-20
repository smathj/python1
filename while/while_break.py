coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee -= coffee
        print("-" * 40)


    elif money > 300:
        print("거스름돈 %d 를 주고 커피를 줍니다" %(money - 300))
        coffee -= coffee
        print("-" * 40)

    elif money < 300:
        print("커피는 300원 입니다. 다시 돈을 넣어주세요")
        print("-" * 40)

    elif money == 0:
        break