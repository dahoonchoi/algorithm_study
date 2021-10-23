# 하이킹을 합니다.
# 해수면 아래로 지나갈 때 계곡에 들어갑니다.

# 위로 올라갈 때는 'U' 아래로 내려갈 때는 'D'
# 하이킹은 항상 해수면 위에서 시작됩니다.

# 계곡을 들어가는 횟수에 대해서 출력하시오


# input 
# steps : path 에 대한 length
# path : 'U' 'D' 에 대한 배열

# output
# valley = 계곡을 들어가는 횟수

# url = https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    valley = 0
    sealevel = 0

    for p in path:
        if p == 'U':
            sealevel += 1
        elif p == 'D':
            sealevel -= 1

        if sealevel == -1 and p =='D':
            valley += 1


    print(valley)

path = ['U','D','D','D','U','D','U','U']
countingValleys(8,path)