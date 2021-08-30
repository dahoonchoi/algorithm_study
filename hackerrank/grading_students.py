# 전달 받은 값보다 큰 5의 배수의 값을 구한다
# 만약 5의 배수값과 전달받은 값의 차가 3이상이면 최초의 5의 배수를 산출한다.
# 만약 차가 3이하라면 기존에 전달받은 값을 산출한다.
# 40점 이하라도 그대로 출력한다.


# input
# 73,67,38,33

# output
# [75, 67, 40, 33]

def gradingStudents(grades):
    answer = []
    for gr in grades:
        # 5의 배수 산출하기
        sin = 0
        while(sin<gr):
            sin += 5
        #5의 배수와의 차를 구한다.
        dif = sin-gr
        if(sin<40):
            #40보다 작으면 무조건 기존 값 출력
            answer.append(gr)
        elif(dif<3):
            answer.append(sin)
        elif(dif>=3):
            answer.append(gr)
    print(answer)


gradingStudents([73,67,38,33])

#.append (리스트안에 값을 추가하는 방법)