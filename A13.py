import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    j = bisect.bisect_right(A, A[i] + K)
    ans += j - (i + 1)
print(ans)
