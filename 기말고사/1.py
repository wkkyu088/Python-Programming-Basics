# 컴퓨터공학과 2019112018 원규진

def getSum(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum
    
def getSumCount(y):
    sum = 0
    idx = 0
    for i in range(1, y+1):
        sum += i
        if sum > y:
            idx = i-1
            break
    return idx
    
    
num = int(input("?: "))
c = getSumCount(num)
s = getSum(c)
print("%d %d %d" %(c,s,num))