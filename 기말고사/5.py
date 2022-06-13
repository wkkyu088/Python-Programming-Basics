# 컴퓨터공학과 2019112018 원규진
import random
import time

def changeNumList(num):
    numList = []
    numList.append(num//100)
    numList.append(num//10-num//100*10)
    numList.append(num-num//10*10)
    return numList

def isUserWin(user, computer):
    count = 0
    for i in range(3):
        if user[i] == 0 and (computer[i] == 8 or computer[i] == 9):
            count += 1
        elif user[i] > computer[i]:
            count += 1
    if count >= 2:
        return True
    else: 
        return False


print("** 카드 대결 게임 **")

countWin = 0
countGame = 0
start = time.time()
while True:
    countGame += 1
    print("%d번째 대결 : 컴퓨터가 3장의 카드를 뽑았습니다." %countGame)
    print("당신도 3장의 카드를 뽑아주세요")
    userInput = int(input("세 장의 카드 (3자리 수) 입력 : "))
    userCard = changeNumList(userInput)

    computerCard = []
    for c in range(3):
        computerCard.append(random.randint(0,9))
    
    print("컴퓨터 : [%d][%d][%d]" %(computerCard[0], computerCard[1], computerCard[2]))
    print("사용자 : [%d][%d][%d]" %(userCard[0], userCard[1], userCard[2]))
    
    if isUserWin(userCard, computerCard):
        countWin += 1
        print("당신의 %d번째 승리입니다." %countWin)

    if countWin == 3:
        end = time.time()
        print("3번 승리하는데 %.2f초 걸렸습니다" %(end-start))
        break
    print()