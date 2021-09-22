#오류 회피하기

try:
    f = open("구라파일", 'r')
except FileNotFoundError:
    pass

