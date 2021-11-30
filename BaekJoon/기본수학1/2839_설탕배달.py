import sys

def main():
    a = int(sys.stdin.readline())

    # 5로 나누어지면 바로 5의 몫 반환
    if a % 5 == 0:
        return a // 5
    else :
        # 5의 몫 부터 거꾸로 반복한다.
        for i in reversed(range(0, a // 5 + 1)):
            take = a
            # 받은 값에 5로 나눈 몫의 값을 뺀다
            take -= (i * 5)

            # 몫의 값을 3으로 나누었을 때 0 이게 되면 3의 나머지 값과
            # 합한 값을 return 한다 
            if take % 3 == 0:
                return i + (take // 3)

    return -1

if __name__ == '__main__':
    print(main())