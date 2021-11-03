import sys

number = int(sys.stdin.readline()) 

for i in range(number):
    b, c = map(int,sys.stdin.readline().split())
    print(b+c)
    