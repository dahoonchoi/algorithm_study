import sys


def main():
    num = int(sys.stdin.readline())
    fold = 1
    cont = 1

    while fold < num:
        fold += cont * 6 
        cont += 1

    print(cont)

if __name__ == '__main__':
    main()