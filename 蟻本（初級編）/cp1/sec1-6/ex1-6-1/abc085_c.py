n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n+1):
        k = n - i - j
        if 0 <= k <= n and 10000*i + 5000*j + 1000*k == y:
            print(i, j, k)
            exit()

print(-1, -1, -1)
