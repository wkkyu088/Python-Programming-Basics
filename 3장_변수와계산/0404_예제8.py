print("** 원리금 계산 프로그램 **")
N = int(input("저축금액: "))
x = int(N*0.0375)
y = int(x*0.15)
r = N + x - y
print("원금: %10d원" %N)
print("이자: %10d원" %x)
print("세금: %10d원" %y)
print("최종: %10d원" %r)