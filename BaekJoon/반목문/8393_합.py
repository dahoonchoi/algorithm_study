import sys 

number = int(sys.stdin.readline())
answer = 0

for i in range(number+1):
    answer += i

print(answer)