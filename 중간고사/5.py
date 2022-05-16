# 컴퓨터공학과 2019112018 원규진

print("*** 계산기 프로그램 ***")
n1 = int(input("첫 번째 정수: "))
n2 = int(input("두 번째 정수: "))
op = input("원하는 연산 (+ - * /): ")

if op == '+':
    print(str(n1)+op+str(n2)+'='+str(n1+n2))
else:
    if op == '-':
        print(str(n1)+op+str(n2)+'='+str(n1-n2))
    else:
        if op == '*':
            print(str(n1)+op+str(n2)+'='+str(n1*n2))
        else:
            print(str(n1)+op+str(n2)+'='+str(round(n1/n2, 2)))