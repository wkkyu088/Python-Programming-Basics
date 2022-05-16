str = input("문자열을 입력하세요? ")
for i in range(len(str)):
    print(str[len(str)-i-1], end="")