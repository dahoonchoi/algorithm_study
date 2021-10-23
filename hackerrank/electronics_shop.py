# 한 사람이 가지고 있는 예산으로
# 키보드와 USB 를 사려고 한다.
# 가격을 비교해 가지고 있는 예산 안에 가장 비싸게 산 값을 구하라 

# input 
# [list] keyboards : 키보드의 가격
# [list] drives : USB 의 가격 
# [int ] b : 가지고 있는 예산

# output
# 가지고 있는 예산으로 가장 비싼 물품

# url = https://www.hackerrank.com/challenges/electronics-shop/problem

import os
import sys

def getMoneySpent(keyboards, drives, b):
    price = 0
    
    for k in keyboards:
        for d in drives:
            # 이전 가격보다 크고 예산보다 같거나 작을 시 price 에 값을 넣는다.
            if price < k+d and b >= k+d:
                price = k+d
    # 예산으로 두가지 물건을 다 살 수 없을 경우는 -1 을 반환한다.
    if price == 0:
        return -1
    
    return price

budget = 1
keyboards = [3,1]
drives = [5,2,8] 
print(getMoneySpent(keyboards,drives,budget))