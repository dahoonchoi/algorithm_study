# 2마리의 고양이와 쥐가 있다.
# 각각의 위치에 있는데 쥐에게 가장먼저 도달하는 고양이를 찾아라
# 쥐는 움직이지 않고 고양이는 같은 속도로 움직이는 것을 가정한다.
# 만약 두 고양이가 동시에 도착하면 쥐는 도망갈 수 있다.

# input 
# x : A cat position
# y : B cat position
# z : Mouse position

# output
# 가장먼저 도달하는 고양이

# url = https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    # 고양이과 쥐의 포지션의 차의 절대값으로 비교
    if abs(z-x) < abs(z-y) :
        return 'Cat A'
    elif abs(z-x) > abs(z-y) :
        return 'Cat B'
    elif abs(z-x) == abs(z-y) :
        return 'Mouse C'

print(catAndMouse(1,2,3))