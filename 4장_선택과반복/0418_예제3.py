num1 = int(input("수1? "))
num2 = int(input("수2? "))

print(num1, "+", num2, "=")

answer = int(input("? "))
if answer == (num1+num2):
    print("정답입니다.")
else:
    print("틀렸습니다.")