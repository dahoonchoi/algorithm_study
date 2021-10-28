# 하나의 랭킹 점수판이 주어진다
# 주어진 점수판에서 플레이어가 받은 점수의 추가로 순위를 출력하시오

# input
# ranked : 점수판
# player : 플레이어 점수

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):

    distinct = sorted(list(set(ranked)), reverse = True)
    l_dis = len(distinct)

    for p in player:
        while l_dis > 0 and p >= distinct[l_dis-1]:
            l_dis -= 1

        print(l_dis+1)


    # 효율성...X
    # for p in player:
    #     b = []
    #     b = ranked[:]
    #     b.append(p)

    #     z = list(set(b))
    #     z.sort(reverse=True)

    #     print(z)
    #     print(z.index(p)+1)


ranks = [100,90,90,80,75,60]
player = [50,65,77,90,102]

climbingLeaderboard(ranks,player)