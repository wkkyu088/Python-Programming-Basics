def get_Max(x, y):
    # if x > y: 
    #     return x
    # elif x < y: 
    #     return y
    return max(x, y)

num1 = float(input("첫번째 실수? "))
num2 = float(input("두번째 실수? "))
print(str(num1)+"와 "+str(num2)+"중 더 큰 수는 "+str(get_Max(num1, num2))+"입니다.")