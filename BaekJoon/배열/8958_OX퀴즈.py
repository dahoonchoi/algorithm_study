import sys

n = int(sys.stdin.readline())
score = 0

for i in range(n):
    total = 0

    quizs = list(sys.stdin.readline())
    for quiz in quizs:
        if quiz == 'O':
            score += 1
            total += score
        else :
            score = 0

    print(total)

