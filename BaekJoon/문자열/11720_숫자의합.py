import sys

length = sys.stdin.readline()
number = int(sys.stdin.readline())

numbers = list(map(int,str(number)))

print(sum(numbers))