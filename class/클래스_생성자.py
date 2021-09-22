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

# a = FourCal()
# # print(type(a))
# a.setdata(4,2)  # 생성자가 없을떄
# print(a.add())
# print(a.mul())
# print(a.div())
# # print(int(a.div()))

# b = FourCal()
# b.setdata(10,2)  # 생성자가 없을떄
# print(b.add())
# print(b.mul())
# print(b.div())

a = FourCal(4,2)
print(a.add())
print(a.mul())
print(a.div())

