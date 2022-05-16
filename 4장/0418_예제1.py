num1 = int(input("첫 번째 수? "))
num2 = int(input("두 번째 수? "))

if num1 > num2:
    print("두 수 중 큰 수는", num1, "이고 작은 수는", num2, "입니다.")
elif num2 > num1:
    print("두 수 중 큰 수는", num2, "이고 작은 수는", num1, "입니다.")
else: 
    print("두 수는 같습니다.")
