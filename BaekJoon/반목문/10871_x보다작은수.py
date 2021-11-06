import sys

length, find = map(int,sys.stdin.readline().split())
findlist = list(map(int,sys.stdin.readline().split()))

for f in findlist:
    if f < find:
        print(f) 
