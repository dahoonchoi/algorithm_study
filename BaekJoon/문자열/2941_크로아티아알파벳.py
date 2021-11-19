def main():
    word = input()
    croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    for c in croatia:
        word = word.replace(c,'*')

    print(len(word))


if __name__ == "__main__":
    main()