# You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# 아이에 생일 케익을 담당하고 있습니다.
# 당신은 각 해마다 하나의 초가 있을 것이라고 결심했습니다.
# 가장 큰 초만 불 수 있습니다. 가장 큰 초는 얼마나 있는지 계산하세요.

def birthdayCakeCandles(candles):
    count = 0
    # Max value
    mav = 0

    for c in candles:
        if c > mav:
            # 최대값이 변경되어 count 초기화
            count = 1
            # 최대값보다 c 값이 크면 최대값에 c
            mav = c
        elif c == mav:
            # 같으면 count 값만 증가
            count += 1
    
    print(count) 



birthdayCakeCandles([3,2,1,3])