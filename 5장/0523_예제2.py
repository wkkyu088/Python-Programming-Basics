def is_prime(x):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
    return flag
            

a = int(input("Number? "))
if is_prime(a):
    print("%d는 소수입니다." %a)
else:
    print("%d는 소수가 아닙니다." %a)