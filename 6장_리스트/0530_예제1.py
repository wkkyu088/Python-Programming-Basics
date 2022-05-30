num = int(input("학생 수? "))

scores = []
for i in range(num):
    n = int(input("%d번째 학생의 성적: " %i))
    scores.append(n)
    
print("평균점수는 %.1f점 입니다." %(sum(scores)/len(scores)))
