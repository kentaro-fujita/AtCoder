n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == t:
            ans += 1
            break
        elif S[mid] < t:
            left = mid + 1
        else:
            right = mid - 1

print(ans)
