# 주어진 정수의 갯수에 따라 
# 0보다 큰 수면 postive 0보다 작은 수면 negative 0과 같으면 0에 넣어
# 비율을 구하는 알고리즘

import math
import os
import random
import re
import sys

def plusMinus(arr):
    postive = 0
    negative = 0
    zero = 0
    
    for n in arr:
        if n > 0 :
            postive += 1
        elif n < 0 :
            negative += 1
        elif n == 0 :
            zero += 1
            
    return (postive, negative, zero)