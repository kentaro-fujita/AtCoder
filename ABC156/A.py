def main():
    N, R = map(int, input().split(' '))

    if N < 10:
        sub = 100 * (10 - N)
        print(R + sub)
    else:
        print(R)


if __name__ == '__main__':
    main()
