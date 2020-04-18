vert = [False] * 8
hori = [False] * 8
topright = [False] * (8 * 2 - 1)
topleft = [False] * (8 * 2 - 1)
queens = []
skip_row = []


def put_queen(x, y):
    vert[x] = True
    hori[y] = True
    topright[x + y] = True
    topleft[7 + (x - y)] = True
    queens.append((x, y))


def elim_queen(x, y):
    vert[x] = False
    hori[y] = False
    topright[x + y] = False
    topleft[7 + (x - y)] = False
    queens.remove((x, y))


def is_blank(x, y):
    if not vert[x] and not hori[y] and not topright[x+y] and not topleft[7+(x-y)]:
        return True


def search_blank_in_row(y):
    blanks = []
    for x in range(8):
        if is_blank(x, y):
            blanks.append(x)
    return blanks


def put_queen_in_row(y):
    #print("put_queen_row",y, queens)
    if y == 8:
        return True     # 8 Queens have already been existed; reached the solution.
    if y in skip_row:
        return put_queen_in_row(y + 1)   # skip rows where a queen already exists as the precondition

    for x in search_blank_in_row(y):
        put_queen(x, y)
        if put_queen_in_row(y + 1):
            return True
        else:
            elim_queen(x, y)    # can't put next queen; eliminate it
    return False    # all candidate blanks are failed


def main():
    # prepare
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        put_queen(x, y)
        skip_row.append(y)

    # 8 queen main
    put_queen_in_row(0)

    # draw queens
    board = [list('........') for x in range(8)]
    for q_x, q_y in queens:
        board[q_x][q_y] = 'Q'
    [print(''.join(x)) for x in board]
    return


main()