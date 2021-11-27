import sys

cont = int(sys.stdin.readline())
person = []

for i in range(cont):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())

    # 0F 부터 시작하기 때문에 +1을 해줍니다.
    for f in range(0, floor + 1):
        # 1호부터 room 호까지 있기 때문에 +1 을 해줍니다.
        for r in range(1, room + 1):
            # 0F 초기 세팅해줍니다.
            if f == 0:
                person.append(r)
            else:
                # 0호는 항상 1이기 때문에 0을 줍니다.
                if r-1 <= 0 :
                    b_person = 0
                else :
                    # 그 외의 호는 이전의 호의 값을 가지고 옵니다.
                    b_person = person[-1] 
                # 리스트의 전체 길이에서 room 의 값을 빼면 한층 아래의 위치를 확인할 수 있다
                # 그리고 이전 호의 값을 가지고와서 서로 합해준다.
                person.append(person[len(person)-room] + b_person)          
        
    # 리스트의 가장 마지막 값을 출력한다.
    print(person[-1])