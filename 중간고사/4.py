# 컴퓨터공학과 2019112018 원규진

hours = int(input("Working Hours: "))
total = 12800*hours

if hours >= 40:
    total = total + 10000*(hours//4)
    total = total*1.1
else:
    total = total + 9000*(hours//4)
    total = total*1.02
    
print("Total Pay: {0:,d} Won".format(int(total)))