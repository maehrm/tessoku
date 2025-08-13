# B19 - Knapsack 2 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr
N, W = map(int, input().split())
weights, values = [], []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

MAX_VALUE = sum(values)
# dp[i][j] = i番目までの品物で、価値jを達成する最小重さ
dp = [[float('inf')] * (MAX_VALUE + 1) for _ in range(N + 1)]
dp[0][0]= 0
for i in range(N):
    for j in range(MAX_VALUE + 1):
        if j - values[i] >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - values[i]] + weights[i])
        else:
            dp[i + 1][j] = dp[i][j]
        
for v in range(MAX_VALUE, -1, -1):
    if dp[N][v] <= W:
        print(v)
        break
