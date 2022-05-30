print("** 문자열 합산 프로그램 **")

result = ""
while True:
    str = input("문자열을 입력하세요? ")
    if str == "": break
    result = result + str
    print(result)
    
countA = 0
for c in result:
    if c=='a':
        countA = countA + 1

print("종료! 문자 a는 총 %d번 사용되었습니다." % countA)    