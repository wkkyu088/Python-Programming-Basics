import random

print("** 숫자 맞히기 게임 **")
print("컴퓨터: 숫자 하나를 선택하였습니다. (1~20)")
print("당신이 맞혀보세요\n")

answer = random.randint(1,20)
while True:
    num = int(input("당신이 생각하는 숫자는? "))
    if num < answer:
        print("틀렸습니다. "+str(num)+"보다 큰 수 입니다.")
    elif num > answer:
        print("틀렸습니다. "+str(num)+"보다 작은 수 입니다.")
    else:
        print("축하합니다. 정답입니다.")
        break