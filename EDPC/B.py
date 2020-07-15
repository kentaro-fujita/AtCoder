N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0

for i in range(1, N):
    for j in range(1, K+1):
        if i - j < 0:
            break
        else:
            step = abs(h[i] - h[i-j])
            dp[i] = min(dp[i], dp[i-j]+step)

print(dp[N-1])
