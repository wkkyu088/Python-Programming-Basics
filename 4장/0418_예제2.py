print("나는 1~20 사이의 정수 하나를 선택하였습니다.")
print("당신이 맞혀보세요.")

answer = 10
n = int(input("맞힐 수는? "))
if n == answer:
    print("축하합니다. 정답입니다.")
else:
    print("틀렸습니다. 정답은", answer, "입니다.")