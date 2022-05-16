# 컴퓨터공학과 2019112018 원규진

print("*** 화성 생존 계산 프로그램 ***")
currentPotato = 100
costPerDay = 3
plantPerWeek = 10
getNextWeek = 40

print("현재감자:", currentPotato, "개, 하루 소비:", costPerDay, "개")
print("매주 심는 감자:", plantPerWeek, "개, 다음주에 생산되는 감자:", getNextWeek, "개")

num = int(input("몇 주후의 감자 수를 계산할까요? "))
result = currentPotato + (- plantPerWeek + getNextWeek - costPerDay*7)*num
print(num, "주 후의 감자의 개수는", result, "개입니다.")