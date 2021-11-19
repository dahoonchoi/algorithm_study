import sys 

answer = []
input_num = list(map(str,sys.stdin.readline().split()))

for i in range(len(input_num)):
    reve_num = ''
    reve_list = list(map(str,reversed(input_num[i])))

    for r in reve_list:
        reve_num += r

    answer.append(int(reve_num))

print(max(answer))
