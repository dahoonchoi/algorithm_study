# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# 12시간 형태로 AM/PM이 구분되어 있습니다. 24시간 형태로 전환하세요
# 메모: 12:00:00 AM 은 24시간 전환으로 00:00:00 입니다.
# 12:00:00 PM은 12:00:00 입니다.

# input
# 06:40:03PM
# 

# output
# 18:40:03
#

def timeConversion(s):
    # PM, AM 의 값을 가지고 옵니다.
    key = s[8:]

    if key == 'PM':
        # PM 이고 12시이면 12 값을 넣습니다.
        if s[0:2] == '12':
            hour = 12
        # 만약 12시가 아니라면 12를 더합니다.
        else:
            hour = int(s[0:2]) + 12
        s = str(hour) + s[2:8]
    elif key == 'AM':
        # AM 이고 12시 이면 00 값을 넣습니다.
        if s[0:2] == '12':
            hour = '00'
            s = hour + s[2:8]
        else :
            s = s[0:8]
    print(s)

timeConversion('06:40:03AM')

# 처음에는 import time 으로 구상해보았지만
# string 형식으로 받아오기 때문에 string 을 잘라서 변환해보았습니다.