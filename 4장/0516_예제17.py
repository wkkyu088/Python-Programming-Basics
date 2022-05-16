import datetime

print("** 파일저장 프로그램 **")

fileName = input("저장할 파일이름: ")
fileLine = int(input("저장할 라인 수: "))

f = open(fileName, "w")

for i in range(fileLine):
    print(i+1, end=": ")
    line = input()
    d = datetime.datetime.now()
    stamp = "%02d:%02d:%02d " %(d.hour, d.minute, d.second)
    f.write(stamp + line.replace(" ", "_") + "\n")

f.close()
print("저장 완료")