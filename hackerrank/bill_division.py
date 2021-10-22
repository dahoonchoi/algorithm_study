# bill 과 anna 가 저녁식사를 계산하려고 한다.
# 계산 방식은 자신이 먹지않은 항목에 대해서는 빼고
# 나머지 금액에서 반을 나눈다.

# bill 이 계산해야할 금액을 구하시오

# 나누는 값이 같으면 'Bon Appetit' 가 출력되도록 하시오

# bill = bill 이 주문한 항목의 가격
# k = anna 가 먹지 않은 항목의 index 값
# b = 총 합계

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    # bill 의 배열에서 먹지않은 인덱스를 빼준다
    bill.pop(k)
    
    # 지불하는 비용이 같다면 'Bon Appetit'
    if sum(bill) / 2 == b :
        print('Bon Appetit')
    # 다르면 값의 차를 출력한다.
    else :
        print(b-int(sum(bill) / 2 ))


bill = [3,10,2,9]
k = 1
b = 7

bonAppetit(bill,k,b)