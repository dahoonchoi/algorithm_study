# 새를 관찰한 타입별로 배열안에 들어있다.
# 타입별로 목격된 수가 가장 높은 타입의 값을 구하라
# 만약 목격 된 수가 같을 경우 낮은 타입의 값을 구하라

# input 
# arr : 목격된 타입의 배열

import math
import os
import random
import re
import sys

def migratoryBirds(arr):

    # 타입은 1부터 6까지이기 때문에 1부터 6까지의 값을 count 함수를 써서
    # 몇개가 들어가있는 지 확인한다
    n = [arr.count(i) for i in range(1,6)]

    for l in range(len(n)):
        if n[l] == max(n):    
            # value(n[l]) 중 가장 작은 type 값(l) 을 가지고 와야하기 때문에
            # 가장 큰 값과 비교할 값이 같으면 바로 return 시켜준다
            return l+1

ar = [1,2,3,4,5,4,3,2,1,3,4]

migratoryBirds(ar)