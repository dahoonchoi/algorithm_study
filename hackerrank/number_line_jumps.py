# 두마리의 캥거루가 있습니다.
# 서로 다른 시작점과 다른 보폭에서
# 만날 수 있으면 Yes 없으면 No 가 출력 되도록 하시오

# x1 : A 캥거루 시작점
# v1 : B 캥거루 시작점
# x2 : A 캥거루 보폭
# y2 : B 캥거루 보폭

def kangaroo(x1, v1, x2, v2):
    a_kang = x1
    b_kang = x2
    cont = 0

    # 무한루프
    while 1:
        # 보폭이 큰 캥거루의 거리가 멀면 No 출력
        if v1 >= v2 and a_kang+v1 > b_kang+v2:
            msg = 'NO'
            break
        elif v1 <= v2 and a_kang+v1 < b_kang+v2:
            msg = 'NO'
            break
        else:
            a_kang = a_kang+v1
            b_kang = b_kang+v2
            # cont 가 10000 넘으면 No 출력
            cont = cont +1
            if a_kang == b_kang :
                msg = 'YES'
                break
            elif cont > 10000 :
                msg = 'NO'
                break
    print(msg) 

kangaroo(63,8,94,3)