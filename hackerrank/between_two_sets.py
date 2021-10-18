# 정수로 구성되어 있는 두개의 배열에 대해서
# 첫번째 배열의 배수이며
# 두번째 배열의 약수인 값을 출력하시오

import math
import os
import random
import re
import sys
from math import gcd

def getTotalX(a, b):
    # 최소공배수
    l_lcm = getLCM(a)
    # 최대공약수
    l_gcd = getGCD(b)
    count = 0

    # 최대공약수가 최소공배수 보다 작을 때 동안 반복  
    while l_gcd >= l_lcm :
        if l_lcm%getLCM(a) == 0:
            if l_gcd%l_lcm == 0:
                count = count + 1
        l_lcm =  l_lcm + 1 

    print(count)

# 최대공약수
def getGCD(num):
    gcd_nums = None
    for i in range(len(num)):
        if (i == 0):
            gcd_nums = num[i]
        else:
            
            gcd_nums = gcd(gcd_nums,num[i])

    return gcd_nums        

# 최소공배수
def getLCM(num):
    lcm_nums = None
    for i in range(len(num)):
        if (i == 0):
            lcm_nums = num[i]
        else:
            lcm_nums = LCM(lcm_nums,num[i])

    return lcm_nums

def LCM(a,b):
    lcm = None
    max_gcd = gcd(a,b)

    lcm = (a/max_gcd)*(b/max_gcd)*max_gcd

    return int(lcm)

a = [2,3,6]
b = [42,84]

getTotalX(a,b)

