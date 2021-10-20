# 최댓값과 최솟값을 기록한 Count 값을 출력하시오

def breakingRecords(scores):
    max_value = 0
    min_value = 0
    max_count = 0
    min_count = 0

    for sco in range(len(scores)) :
        if sco == 0:
            max_value = scores[sco]
            min_value = scores[sco]
        # 가장 큰 값보다 다음 들어올 값이 더 클시.
        elif max_value < scores[sco]:
            max_value = scores[sco]
            max_count = max_count + 1
        # 가장 작은 값보다 다음 들어올 값이 더 작을시.
        elif min_value > scores[sco]:
            min_value = scores[sco]
            min_count = min_count + 1

    print(max_count,min_count)

input = [10,5,20,20,4,5,2,25,1]
breakingRecords(input)