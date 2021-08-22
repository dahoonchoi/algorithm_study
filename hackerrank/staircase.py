# 2021-08-23
# 하나의 값 n이 주어지면
# 그 수에 맞게 오른쪽 정렬의 계단식으로 #이 증가
# input 3
# output 
#      #
#     ##
#    ###

def staircase(n):
    for row in range(1,n+1):

        # 오른쪽정렬이기 때문에 행마다 공백 삽입
        for blank in range(0,n-row):
            print(' ',end='')

        for col in range(1,row+1):
        # python2 는 print시 defult로 \n이 되기 때문에 end='' 사용
            print('#',end='')
        print('') 

staircase(6)