numbers = set(range(1,10001))
remove_number = set()
answer = []

for number in numbers:
    for n in str(number):
        number += int(n)
    remove_number.add(number)

answer = numbers-remove_number
answer = sorted(answer)

print(*answer, sep='\n')