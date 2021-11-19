def PhoneValue(alphabet):
    
    if alphabet >= 65 and alphabet < 68:
        return 2
    elif  alphabet >= 68 and alphabet < 71:
        return 3
    elif  alphabet >= 71 and alphabet < 74:
        return 4
    elif  alphabet >= 74 and alphabet < 77:
        return 5
    elif  alphabet >= 77 and alphabet < 80:
        return 6
    elif  alphabet >= 80 and alphabet < 84:
        return 7
    elif  alphabet >= 84 and alphabet < 87:
        return 8
    elif alphabet >= 87:
        return 9

def main():
    input_text = list(map(str,input()))
    answer = 0 

    for alph in sorted(input_text):
        answer += PhoneValue(ord(alph)) + 1

    print(answer)


if __name__ == "__main__":
    main()

