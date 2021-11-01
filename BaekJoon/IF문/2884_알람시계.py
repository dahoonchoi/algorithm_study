import sys
hour,minute = list(map(int,sys.stdin.readline().split()))

# 45분을 뺏을 때 음수이면
if minute - 45 < 0 :
    # 한시간을 뺀다
    hour -= 1
    # 시간이 0시 일때는 23시로 돌린다
    if hour < 0 :
        hour = 23
    minute = 60 + (minute-45)

else :
    minute -= 45

print(hour, minute)