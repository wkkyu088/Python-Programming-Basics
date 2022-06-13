# 컴퓨터공학과 2019112018 원규진
import random

# (1)
def changeNumList(num):
    numList = []
    numList.append(num//100)
    numList.append(num//10-num//100*10)
    numList.append(num-num//10*10)
    return numList

# (2)
def getRandomNumber(num):
    numList = []
    while True:        
        r = random.randint(0,9)
        if r not in numList:
            numList.append(r)
        if len(numList) == num:
            return numList

# (1)    
# num = int(input("세자리 정수 입력: "))
# l = changeNumList(num)
# print(num, ">>", l)

# (2)
# num = int(input("뽑을 구슬의 개수는 (1~10): "))
# l = getRandomNumber(num)
# print(l)