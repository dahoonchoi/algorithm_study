# 한 행렬의 값을 받는다.
# 받은 행렬의 값을 마방진으로 변경하려고 한다
# 마방진으로 변경할 때 최소로 변경할 수 있는 값을 출력하라

# input
# [LIST] S : 행렬

# output
# 행렬을 마방진으로 변경할 때 최소로 변경할 수 있는 값 

import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    answer = 0
    # 한 행렬에 대한 차를 임시 저장 buffer
    buff = 0

    base = [
        [8,3,4,1,5,9,6,7,2],
        [8,1,6,3,5,7,4,9,2],
        [4,3,8,9,5,1,2,7,6],
        [6,1,8,7,5,3,2,9,4],
        [2,7,6,9,5,1,4,3,8],
        [2,9,4,7,5,3,6,1,8],
        [6,7,2,1,5,9,8,3,4],
        [4,9,2,3,5,7,8,1,6]
    ]

    # 비교하기 편하기 위해 이중배열을 하나의 배열로 수정
    org = sum(s,[])

    for row in base :
        # row의 총 길이로 각 항목의 차를 계산
        for coor in range(len(row)):
            # 차에 대한 절대값을 buff 에 임시저장
            buff += abs(row[coor] - org[coor])
        # 해당 row가 처음 동작되면 buff 값 무조건 answer 에 저장
        if base.index(row) == 0:
            answer = buff
        # 그 이후 부터는 answer 보다 작은 값일 때마다 저장
        elif buff < answer :
            answer = buff
        #buff 초기화
        buff = 0

    return answer
        
square = [[4,8,2], [4, 5, 7], [6, 1, 6]]
print(formingMagicSquare(square))