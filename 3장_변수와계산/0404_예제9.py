print("** 원리금 계산 프로그램 **")
N = int(input("저축금액: "))
x = int(N*0.0375)
y = int(x*0.15)
r = N + x - y
print("원금: {0:10,d}원".format(N))
print("이자: {0:10,d}원".format(x))
print("세금: {0:10,d}원".format(y))
print("최종: {0:10,d}원".format(r))