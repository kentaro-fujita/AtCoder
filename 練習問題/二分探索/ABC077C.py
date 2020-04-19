from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for b in B:
    ans += bisect_left(A, b) * (N - bisect_right(C, b))

print(ans)