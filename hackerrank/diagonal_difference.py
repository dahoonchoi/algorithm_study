# Function description

# Complete the Diagonal Difference function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers

# 1 2 3
# 3 5 9
# 6 7 1

# return (1+5+1) - (6+5+3)

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    left = 0
    right = 0
    total = 0
    
    #coordinate 행렬은 기존의 length 보다 1 작기 때문
    crdn = n - 1 
    
    for num in range(0,n):
        left += arr[num][num]
        right += arr[num][crdn-num]
     
    total = left - right 
    
    # 절대값 abs
    return abs(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
