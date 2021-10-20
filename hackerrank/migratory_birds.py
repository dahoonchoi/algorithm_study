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
    
    max_sight = 0
    rep_sight = 0
    max_type = 0

    # 처음 받은 배열의 총길이를 구한다
    for org in range(len(ar)):
        # 배열의 각 위치마다 비교할 값을 구한다.
        print(ar[org])
        for rep in range(len(ar)):
            
            # 배열의 값이 같은지 비교한다.
            if ar[org] == ar[rep]:
                rep_sight = rep_sight + 1
        print(ar[org],'sight :',rep_sight)

        if max_sight <= rep_sight:
            print('max_sight',':',rep_sight)
            print('max_type :', arr[org])
            max_type = arr[org]
            max_sight = rep_sight
        
        print('----------')

        rep_sight = 0

ar = [1,2,3,4,5,4,3,2,1,3,4]

migratoryBirds(ar)