# 2021-08-23
# 5가지 정수가 들어있는 배열 중 4개의 합이
# 최소값과 최대값이 될 수 있도록 출력
# input [1,2,3,4,5]
# output (10,14)

def miniMaxSum(arr):
    left = 0
    right = 0
    length = len(arr)
    
    #배열안을 오름차순해준다.
    arr.sort()
    
    for val in range(0,length-1):
        left += arr[val]
        
    for val in range(1,length):
        right += arr[val]  
    
    print(left,right)

miniMaxSum([1,2,3,4,5])