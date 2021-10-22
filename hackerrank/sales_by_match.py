# 많은 종류의 양말이 가득 있습니다.
# 양말의 짝을 찾아서 몇개의 한 쌍이 나오는 지 구하시오

# input
# n : 각 양말의 갯수
# ar : 양말의 종류

# output
# answer : 한쌍이 만들어지는 수

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    answer = 0
    # set = > 배열의 중복을 없애주는 파이썬 함수
    # 중복을 제거한 배열에서 각 배열의 갯수를 pairs 저장한다.
    pairs = [ar.count(i)  for i in set(ar)]

    for p in range(len(pairs)):
        answer = answer + int(pairs[p] / 2)

    print(answer)

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sockMerchant(7,ar)