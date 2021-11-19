text = input()
alphabet = list(map(chr,range(65,91)))
li_text = list(map(str,text.upper()))

answer = []

for alph in alphabet:
    answer.append(li_text.index(alph) if alph in li_text else -1)
    
print(*answer,end=" ")