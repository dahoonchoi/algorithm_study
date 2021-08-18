# 001.
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . 
# The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.


# The result of the integer division .
# The result of the float division is .


def Calculation(value1,value2):

    a = value1
    b = value2

    if __name__ == "__main__":
        try:
            # 정수형 값만 반환합니다.
            print(a//b)
            # 항상 Float 값을 반환 합니다.
            print(a/b)
        except ValueError as e:
            print(e)

Calculation(2,4)

# 할당연산자 /와 //의 차이에 대해서 알 수 있었습니다.
