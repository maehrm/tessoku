H, W = map(int, input().split())
c = []
for _ in range(H):
    c.append(list(input()))
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if c[i][j] == '#':
            dp[i][j] = 0
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
print(dp[-1][-1])
