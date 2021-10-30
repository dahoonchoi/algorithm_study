a = int(input())
b = input()

answer = 0
count = 0

for bl in reversed(range(len(b))):
    print(int(b[bl]) * a)
    
    answer += (int(b[bl]) * a)*(10**count)
    count += 1 

print(answer)