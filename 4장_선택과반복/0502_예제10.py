print("*** 간단한 구구단 프로그램 ***")
num = int(input("몇 단을 할까요? "))
end = int(input("몇까지 곱셈을 할까요? "))

for i in range(end):
    print("%dx%d=%d" %(num, i+1, num*(i+1)), end='')
    if (i+1) % 5 == 0:
        print()
    elif i != end-1:
        print(', ', end='')