# s: integer, starting point of Sam's house location.
# Sam 의 집의 시작점
# t: integer, ending location of Sam's house location.
# Sam 의 집의 종료점
# a: integer, location of the Apple tree.
# 사과나무 위치
# b: integer, location of the Orange tree.
# 오렌지나무 위치
# apples: integer array, distances at which each apple falls from the tree.
# 사과와 사과나부로의 거리
# oranges: integer array, distances at which each orange falls from the tree.
# 오렌지와 오렌지 나무의 거리

# 사과와 오렌지나무가 떨어졌을 때 집의 영역으로 들어오는 갯수를 출력하세요

# input
# 1행 : s, t
# 2행 : a, b
# 3행 : m, n
# 4행 : apple distancec
# 5행 : orange distancec

def countApplesAndOranges(s, t, a, b, apples, oranges):

    in_apple = 0
    in_orange = 0

    for apple in apples:
        if s <= a+apple & a+apple < t  :
            in_apple += 1

    # 오렌지나무위치와 오렌지가 떨어진 지점을 더한다.
    for orange in oranges:
        # 집의 시작점보다 크고 종료점보다 작은 값이 있으면 1 증가시킨다.
        if s <= b+orange & b+orange < t  :
            in_orange += 1

    print(in_apple)
    print(in_orange)
    
countApplesAndOranges(2,3,1,5,[-2,2,1],[5,-6])