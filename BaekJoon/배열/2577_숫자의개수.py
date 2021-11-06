import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

n = a * b * c

answer = [str(n).count(str(i)) for i in range(10)]


print(*answer, sep='\n')