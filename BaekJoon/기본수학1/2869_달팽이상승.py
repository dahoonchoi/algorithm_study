import sys
import math

a, b, v = map(int,sys.stdin.readline().split())

loca = math.ceil( (v - b) / (a - b))

if loca == v :
    loca = v - 1

print(loca)


