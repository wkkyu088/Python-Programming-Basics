num1 = input("수1? ")
num2 = input("수2? ")

sum = int(input(num1 + "+" + num2 + "= ? "))
sub = int(input(num1 + "-" + num2 + "= ? "))
mul = int(input(num1 + "*" + num2 + "= ? "))

num1, num2 = int(num1), int(num2)
check = 0
if sum == (num1+num2): check += 1
if sub == (num1-num2): check += 1
if mul == (num1*num2): check += 1

score = 100/3*check
print("당신의 점수는", round(score, 2), "점 입니다.")