def main():
    S, T = input().split(' ')
    A, B = map(int, input().split(' '))
    U = input()

    if U == S:
        A -= 1
    if U == T:
        B -= 1
    
    print('{} {}'.format(A,B))


if __name__ == '__main__':
    main()