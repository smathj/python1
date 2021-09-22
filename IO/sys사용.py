import sys
# import os
# os.system("pause")


''' 시스템 매개변수 이용 '''
# args = sys.argv[1:]

# for i in args :
#     print(i)


''' 대문자로 바꿔서 출력하기 '''
args = sys.argv[1:]

for i in args :
    print(i.upper(), end=' ')

