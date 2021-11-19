import sys

input_length = int(sys.stdin.readline())

for i in range(1,input_length+1):
    chg_count, chg_text = map(str,sys.stdin.readline().split())

    answer = [t * int(chg_count) for t in chg_text]
    
    print(*answer,sep="")
