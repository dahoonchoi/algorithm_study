# 선생님이 학생들에세 특정 페이지를 펼치라고 이야기한다.
# 책의 첫장의 1페이지는 항상 오른쪽에 위치해 있다.
# 특정 페이지를 말했을 때 앞으로 넘기던 뒤로 넘기던 가장 적게 넘기는 횟수에 대해서
# 출력하라

# input 
# n : 총 페이지 번호
# p : 펼처야할 페이지 번호

# output
# 펼쳐야할 페이지를 찾는데 가장 적게 넘기는 횟수

# url = https://www.hackerrank.com/challenges/drawing-book/problem

import math
import os
import random
import re
import sys


def pageCount(n, p):
    print(p//2,n//2-p//2)

pageCount(6,2)