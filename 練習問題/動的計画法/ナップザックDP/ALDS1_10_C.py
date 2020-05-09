q = int(input())

ans = []
for _ in range(q):
    X = list(input())
    n = int(len(X))

    Y = list(input())
    m = len(Y)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    ans.append(dp[n][m])

for a in ans:
    print(a)
