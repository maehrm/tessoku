# C18 - Pick Two（★6） https://atcoder.jp/contests/tessoku-book/tasks/typical90_s
INF = 10**18
N = int(input())
A = list(map(int, input().split()))
dp = [[INF] * 2 * N for _ in range(2 * N)]
for i in range(2 * N - 1):
    dp[i][i + 1] = abs(A[i] - A[i + 1])
for j in range(3, 2 * N + 1, 2): # 奇数個の区間は消去不能なので、stepは2でよい
    for i in range(2 * N - j):
        ll, rr = i, i + j
        for k in range(ll + 1, rr):
            dp[ll][rr] = min(dp[ll][rr], dp[ll][k] + dp[k + 1][rr])
        dp[ll][rr] = min(dp[ll][rr], dp[ll + 1][rr - 1] + abs(A[ll] - A[rr]))
print(dp[0][2 * N - 1])
