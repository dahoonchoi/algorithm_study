# 이분탐색에서 기준점이 중요한데 
# 해당 문제는 돌과의 거리에 기준을 둔다.

def solution(distance, rocks, n):
    answer = 0
    # 시작점과 종료점의 Default 값을 구한다.
    start, end = 0, distance
    # 이분탐색에서 가장 중요한 것은 정렬
    rocks.sort()
    # start 가 end 보다 작거나 같을 때까지 반복한다.
    while start <= end :
        # 거리값의 평균을 구한다 (이 값보다 큰 값이 있는 지 확인한다.)
        mid = (start+end) // 2
        # 이전의 돌과의 거리를 구해야하기때문에 선언했다. 
        pre_stone = 0
        del_stone = 0
        for stone in rocks:
            # 중간 값보다 큰 값을 찾아야 하기때문에 중간값보다 작으면 넘어가고 
            # Delete값을 올려준다
            if mid > stone - pre_stone:
                del_stone += 1
            # 거리가 중간값과 같거나 크면 필요한 값이기 때문에 삭제하지 않고 
            # 다음돌과의 거리를 비교한다.
            else :
                pre_stone = stone
            # 삭제한 돌이 n 값(삭제할 돌갯수) 보다 크면 반복문을 나가준다.
            if del_stone > n :
                break
        # 삭제한돌의 갯수가 크다는 것은 거리값의 평균이 너무 크다는 것이다.
        if del_stone > n :
            end = mid - 1
        # 더 삭제를 안해도 된다고 하면 적절하다는 것이다.
        # 더 적절한 값을 찾기위해 시작값을 1늘려준다.
        else :
            start = mid + 1
            answer = mid

    return answer

rocks = [2,14,11,21,17]
print(solution(25,rocks,2))