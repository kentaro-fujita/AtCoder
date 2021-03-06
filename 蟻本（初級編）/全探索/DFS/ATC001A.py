import sys
sys.setrecursionlimit(10**8)


def dfs(x, y):
    d[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == 0 and c[nx][ny] != "#":
            dfs(nx, ny)


n, m = map(int, input().split())
c = [list(input()) for i in range(n)]

d = [[0] * m for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if c[i][j] == "s":
            dfs(i, j)

for i in range(n):
    for j in range(m):
        if c[i][j] == "g" and d[i][j]:
            print("Yes")
            exit()
print("No")
