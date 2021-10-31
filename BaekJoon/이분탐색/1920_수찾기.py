
# # # 수정
# import sys

# find_len = int(sys.stdin.readline())
# find_list = list(map(int,sys.stdin.readline().split()))

# # # 기존
# # find_len = int(input())
# # find_list = list(map(int,input().split()))


# pre_len = int(sys.stdin.readline())
# pre_list = list(map(int,sys.stdin.readline().split()))

# find_list = [4,1,5,2,3,12,45,77,80,36,78,90]
# find_len = len(find_list)
# pre_list = [1,3,7,9,5,8]
# pre_len = len(pre_list)

# def calculator(pre,find):
#     start, end = 0, find_len-1

#     while start <= end:
#         mid = (start+end)//2
#         if pre == find[mid]:
#             return True
#         elif pre > find[mid]:
#             start = mid + 1
#         elif pre < find[mid]:
#             end = mid - 1

# find = sorted(find_list)
# for pre in pre_list:
#     if calculator(pre,find):
#         print(1)
#     else :
#         print(0)


# # 수정
import sys

find_len = int(sys.stdin.readline())
find_list = list(map(int,sys.stdin.readline().split()))
pre_len = int(sys.stdin.readline())
pre_list = list(map(int,sys.stdin.readline().split()))

find_list = [4,1,5,2,3,12,45,77,80,36,78,90]
find_len = len(find_list)
pre_list = [1,3,7,9,5,8]
pre_len = len(pre_list)

def calculator(pre,find):
    start, end = 0, find_len-1

    while start <= end:
        mid = (start+end)//2
        if pre == find[mid]:
            return True
        elif pre > find[mid]:
            start = mid + 1
        elif pre < find[mid]:
            end = mid - 1

find_list.sort()
for pre in pre_list:
    if calculator(pre,find_list):
        print(1)
    else :
        print(0)

