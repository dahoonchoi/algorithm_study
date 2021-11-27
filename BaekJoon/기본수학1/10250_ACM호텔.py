import sys
import math

cont = int(sys.stdin.readline())

for i in range(cont):
    floor, room, person = map(int, sys.stdin.readline().split())

    # 호실은 층과 N번째 손님을 나눴을 때의 몫을 올림 한다.
    p_room = math.ceil( person / floor )
    p_floor = ( person % floor  ) 

    # 층과 N 번째 손님이 같은 경우 가장 높은 층인 floor 값을 받는다
    if p_floor == 0:
        p_floor = floor

    p_floor *= 100

    print(p_room + p_floor)