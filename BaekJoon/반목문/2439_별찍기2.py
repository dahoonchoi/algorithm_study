import sys

star = int(sys.stdin.readline())

for y in range(1,star+1):
    for x in range(star-y):
        print(' ',end='')
    for x in range(1,y+1):
        print('*',end='')
    print()