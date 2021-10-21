# 러시아는 1700~1917년은 Julian calendar 를 따르고
# 1919년 부터 Gregorian calendar를 따른다
#
# Julian calendar Gregorian calendar 전환은 1918년도에 이루어졌다.
# 전환되는 과정인 1918년은 1월 31일에서 다음날이 2월 14일이 되었다 
# 결국 1918년은 9월이 되기 전 14일정도가 있다.
#

# Julian calendar 의 윤년은 4로 나누어지는 날이다
# Gregorian calendar 의 윤년은 400으로 나누지거나 4로나누어지고 100으로 나누어지지 않는날이다

# 해당 해의 256번째의 일자를 구하라

import math
import os
import random
import re
import sys


def dayOfProgrammer(year):

    # 윤년일 때는 그것보다 하루적은 12일로 계산한다
    if (year < 1918 and year%4 == 0) or (year > 1918 and (year%400 == 0 or (year%4 == 0 and year%100 != 0))):
        return '12.09.%s' %year
    # 달력의 전환일인 1918년은 14일을 더 계산한다
    elif year == 1918:
        return '26.09.%s' %year
    # default 값은 13일 이다.
    else :
        return '13.09.%s' %year

dayOfProgrammer(2016)