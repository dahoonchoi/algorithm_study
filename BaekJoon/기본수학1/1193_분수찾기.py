import sys

def main():
    num = int(sys.stdin.readline())
    line = 0
    
    # 대각선 몇번째 Line 에 있는 숫자인 지 찾는다.
    line_cont = 1
    line_buff = 0

    while line_buff < num :
        line_buff = line_buff + line_cont
        line_cont += 1
        # 라인 값은 하나씩 증가한다.
        line += 1

    # 1 부터 라인 갯수만큼 반복을 하면서 해당 라인의 가장 첫번째에 있는 값을 구한다.
    value_cont = 1
    value_first = 1

    # 짝수번째 Line 이면 라인의 첫번째 값이 1이 증가하고
    # 홀수번째 Line 이면 라인의 첫번째 값이 4의 배수 만큼 증가한다.
    for i in range(1,line) :
        if i % 2 != 0:
            value_first += 1
        else :
            value_first += 4 * value_cont
            value_cont += 1

    row = 0
    # col == line 이면 첫번째 col이 -1 로 값이 틀려지기 때문에 미리 line + 1을 해놓는다. 
    col = line + 1


    if line % 2 == 0 :
        for d in range(value_first - 1, num) :
            row += 1
            col -= 1

    # 홀수번 라인이면 가장 첫번째 값이 라인에서 가장 높은 순서이기 때문에 내려갈 수록 -1 을 해준다.
    else :
        for d in range(num - 1, value_first) :
            row += 1
            col -= 1 
    
    print("%d/%d"%(row,col))


if __name__ == "__main__" :
    main()