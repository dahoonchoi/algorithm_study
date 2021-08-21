# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .

# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.

# 배열로 들어온 값의 합 계산

def aVeryBigSum(ar):
    # Write your code here
    total = 0
    length = len(ar)
    
    for n in range(0,length):
        total += ar[n]
    
    return total
    