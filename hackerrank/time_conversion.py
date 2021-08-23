# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# 12시간 형태로 AM/PM이 구분되어 있습니다. 24시간 형태로 전환하세요
# 메모: 12:00:00 AM 은 24시간 전환으로 00:00:00 입니다.
# 12:00:00 PM은 12:00:00 입니다.

def timeConversion(s):
    # 특정위치를 splite를 해서 가지고 와야할지...
    # 데이터 타임형식으로 변환해야할지...
    print(s[8])


timeConversion('07:05:45PM')