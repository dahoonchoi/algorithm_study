import sys

length = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

high = max(arr)

new_score = [i/high*100 for i in arr]

print(round(sum(new_score)/length,2))