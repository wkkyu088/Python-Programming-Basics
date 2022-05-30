print("*** 구구단 출력 프로그램 ***")
for i in range(1, 10):
    for j in range(2, 10):
        print("%d*%d=%-2d" %(j, i, j*i), end=" ")
    print()