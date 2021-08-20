# 
# 배열로 들어온 두수를 비교해서 큰 값의 위치에 +1  
# 

def compareTriplets(a, b):
    # Write your code here
    left = 0
    right = 0
    
    for n in range(0,3):
        if a[n] > b[n] :
            left += 1
        elif a[n] < b[n] :
            right += 1
    
    return [left,right]

# range의 개념에 대해서 알게되었습니다.
# range(start_value, length)