# 컴퓨터공학과 2019112018 원규진

x = int(input("큰수?: "))
y = int(input("작은수?: "))

while True:
    if y == 0:
        r = x
        break
    r = x % y
    x = y
    y = r

print(r)