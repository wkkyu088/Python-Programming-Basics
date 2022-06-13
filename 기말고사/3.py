# 컴퓨터공학과 2019112018 원규진

n = int(input("총 표시할 라인 수? "))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()