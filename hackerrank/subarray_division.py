# 첫번째 라인은 정수 n을 포함 한다, 초콜릿 바의 사각형의 갯수 입니다.
# The first line contains an integer n, the number of squares in the chocolate bar.
# 두번째 라인은 공백을 포함한 정수 n 이다, 초콜릿 사각형의 위치는 0<=i<n 이다
# The second line contains n space-separated integers , the numbers on the chocolate squares where 0<=i<n.
# 세번째 라인은 두개의 공백을 포함한 정수 n,m 이다, 론은 생일 일자와 그의 생일 달이다.
# The third line contains two space-separated integers, n and m, Ron's birth day and his birth month.

import math

def birthday(s, d, m):
    total = 0
    count = 0

    # 전체 배열에서 더해야하는 갯수를 빼고 +1 을 하면 총 계산하는 count 값이 나온다.
    for loca in range(len(s)-m+1):
        # 배열의 시작지점과 시작지점으로부터 더해야하는 갯수의 위치까지 합을 구한다.
        total =  sum(s[loca:loca+m])
        # 생일 일자와 같은날 일 때 count +1을 해준다.
        if total == d:
            count = count + 1
    print(count)


location = [1,2,1,3,2]
day = 3
month = 2


birthday(location,day,month)
