import sys

xaxis = int(sys.stdin.readline())
yaxis = int(sys.stdin.readline())

if xaxis >= 0 and yaxis >= 0:
    print('1') 
elif xaxis < 0 and yaxis >= 0:
    print('2') 
elif xaxis < 0 and yaxis < 0:
    print('3') 
elif xaxis >= 0 and yaxis < 0:
    print('4') 