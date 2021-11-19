count = int(input())


def GroupDelte(word):
    over_word = []
    over_word += set(word)

    word_count = [word.count(w) for w in over_word]

    index_num = 0
    for w_cont in word_count:
        if w_cont > 1:
            index_list = [i for i , value in enumerate(word) if value == over_word[index_num]]
            for v in range(0,len(index_list)-1):
                if index_list[v+1] - index_list[v] > 1:
                    return 0
        index_num += 1
    return 1

def main():
    answer = 0

    for i in range(count):
        word =  list(map(str,input()))
        answer += GroupDelte(word)
    print(answer)

if __name__ == '__main__':
    main()