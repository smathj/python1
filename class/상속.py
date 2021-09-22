class FourCal:

    # 생성자 추가하기
    def __init__(self, first, second) :
        self.first  = first
        self.second = second
        

    # 생성자가 없을때 
    def setdata(self, first, second) :
        self.first  = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result


class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result

    def div(self) :
        if self.second == 0:
            return 0
        else :
            return self.first / self.second

a = MoreFourCal(4,0)
print(a.pow())
print(a.div())

