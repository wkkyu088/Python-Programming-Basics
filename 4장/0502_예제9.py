print("**** 순차 합을 구하는 프로그램 ****")
start = int(input("어디부터의 합을 구할까요? "))
end = int(input("어디까지의 합을 구할까요? "))

sum = 0
for i in range(start, end+1):
    sum = sum + i
print(start, "부터", end, "까지의 합은", sum, "입니다.")