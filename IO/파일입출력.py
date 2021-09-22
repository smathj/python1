''' 파일 생성하기 

(1)
파일 객체 = open(파일 이름, 파일 열기모드)
                            r(읽기),w(쓰기),a(추가,append)
point 1. 파일이 없다면 생성한다

(2)
파일 객체.write(contents) 파일에 쓰기


(3)
파일 객체.close() 스트림 닫기

'''



# f = open("./IO/나태쿤의살생부.txt", 'w', encoding='utf8')

# for i in range(1,11) :
#     data = "%d번째 줄입니다\n" %i
#     f.write(data)

# f.close()


# # 한줄 읽기
# f = open("./IO/나태쿤의살생부.txt", 'r', encoding='utf8')
# line = f.readline()
# print(line)
# f.close()


# # 모든줄 읽기 - 반복문
# f = open("./IO/나태쿤의살생부.txt", 'r', encoding='utf8')
# while True :
#     line = f.readline()
#     if not line :
#         break
#     print(line)

# f.close()


# # 모든줄 읽기 - readlines() , return type = List
# f = open("./IO/나태쿤의살생부.txt", 'r', encoding='utf8')

# lines = f.readlines()
# for line in lines :
#     print(line)    

# f.close()


# # 모든줄 읽기 - read() 함수 사용 , return type = String
# f = open("./IO/나태쿤의살생부.txt", 'r', encoding='utf8')
# data = f.read()
# print(data)
# f.close()


# 파일에 추가하기 Like LogFile
# f = open("./IO/나태쿤의살생부.txt", 'a', encoding='utf8')
# for i in range(11,20) : # 11~19
#     data = "%d번째 줄입니다\n" %i
#     f.write(data)
# f.close


# open,close를 한번에 해주는 with문
with open("./IO/나태쿤의살생부.txt", 'a', encoding='utf8') as f :
    f.write("하북 보다 깊은 상처만 준난")
