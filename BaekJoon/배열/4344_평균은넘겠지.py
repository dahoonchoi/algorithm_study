import sys

n = int(sys.stdin.readline())

for i in range(n):
    score = list(map(int,sys.stdin.readline().split()))
    student = score[0]

    score.pop(0)

    avg_score = round(sum(score)/student,3)

    up_score = [up for up in score if up > avg_score]

    answer = "{:.3f}%".format((len(up_score)/len(score))*100)

    print(answer)

    

    
