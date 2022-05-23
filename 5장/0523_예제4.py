import random

def add_number(dicenum):
    global num
    num = num + dicenum
    return dicenum

num = 0
count = 0
while(True):
    cmd = int(input("현재위치 %d: 1.주사위 굴리기 2.종료: " %num))
    if cmd == 1:
        count = count + 1
        dicenum = random.randint(1,6)
        add_number(dicenum)
        print("주사위를 굴려 %d가 나왔습니다." %dicenum)
    elif cmd == 2:
        print("%d번 주사위를 굴려 %d칸 전진했습니다." %(count, num))
        break