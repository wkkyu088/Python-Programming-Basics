import time

print("** 마음속으로 10초 프로그램 **")

cmd1 = input(("Enter를 누르면 시작됩니다: "))
start = time.time()
cmd2 = input(("Enter를 누르면 끝납니다: "))
end = time.time()

result = end - start
if result < 10:
    print("%.3f초가 걸렸습니다. %.3f초 빨리 눌렀네요." %(result, 10-result))
elif result > 10:
    print("%.3f초가 걸렸습니다. %.3f초 늦게 눌렀네요." %(result, result-10))
else:
    print("%.3f초가 걸렸습니다. 정확히 10초입니다!" %(result))