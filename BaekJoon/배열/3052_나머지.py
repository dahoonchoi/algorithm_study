import sys
count = 0
arr = []

for i in range(10):
    arr.append(int(sys.stdin.readline())%42)

answer = len(set(arr))

print(answer)