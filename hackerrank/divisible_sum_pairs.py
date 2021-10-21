# 주어진 배열에서 배열의 두값을 더해서 k 값이 나오는 count 값을 계산하라는 문제입니다.
# n : 배열의 총 길이
# k : 주어진 배열의 두 값을 합해서 나온 값으로 나눌 수 있는 값
# ar : 배열

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    
    count = 0

    # 처음 받은 배열의 총길이를 구한다
    for org in range(len(ar)):
        # 배열의 각 위치마다 더해야 할 값의 위치를 구한다.
        for rep in range(len(ar)):
            div = 0

            # 값은 위치에 있는값은 넘어간다.
            if org == rep:
                break
            else :
                # 더해야할 값과 기존값의 합을 구한다.
                div = ar[org] + ar[rep]

            # k 를 나누었을 때 나머지가 0 일 시 count 값을 1 증가시킨다.
            if div%k == 0:
                count = count + 1

    print(count)

n = 2
k = 2
ar = [8,10]

divisibleSumPairs(n,k,ar)