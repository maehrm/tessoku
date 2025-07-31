N, Q = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
XY = []
for _ in range(Q):
    x, y = map(int, input().split())
    XY.append((x - 1, y))

# 2^30 = 1073741824 なので、Y の上限を満たす。
LIM = 30
dp = [[0] * N for _ in range(LIM)]
for i in range(N):
    dp[0][i] = A[i]
for i in range(1, LIM):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

for x, y in XY:
    cur = x
    for i in range(LIM):
        if (y >> i) & 1:
            cur = dp[i][cur]
    print(cur + 1)
