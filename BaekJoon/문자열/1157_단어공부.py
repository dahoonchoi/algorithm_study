input_text = list(map(str,input().upper()))

compare_text = []
compare_text += set(input_text)

input_cont = [input_text.count(i) for i in compare_text]

max_cont = max(input_cont)

if input_cont.count(max_cont) > 1:
    print('?')
else :
    print(compare_text[input_cont.index(max_cont)])

