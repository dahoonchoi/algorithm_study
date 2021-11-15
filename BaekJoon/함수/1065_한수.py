import sys

request = int(sys.stdin.readline())

def HanNumber(req):
    count = 0
    arr = []

    for m_num in range(1,req+1):
        if m_num < 100 :
            count += 1
        else :
            arr = list(map(int,str(m_num)))
            if arr[0] - arr[1] == arr[1] - arr[2]:
                count += 1

    return count

print(HanNumber(request))