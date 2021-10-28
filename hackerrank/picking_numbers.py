# 배열이 주어지고 두개의 차가 1보다 작거나 1과 같은 값은 갯수를
# 출력하시오

# input
# array

# output
# 1과 같거나 작은 갯수

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    answer = 0
    
    for i in a:
    # find 1 or 0 value
       c = a.count(i)
       d = a.count(i-1)

       if c+d > answer:
           answer = c+d
           

    return answer

a = [4,6,5,3,3,1]
pickingNumbers(a)