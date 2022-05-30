def round2(x, y):
    return round(x, y)

num = float(input("실수? "))
roundN = int(input("소수점 몇 자리를 표시할까요? "))
print(round2(num, roundN))
