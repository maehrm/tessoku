N, W = map(int, input().split())
weights, values = [], []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
dp = [-1] * (W + 1)
dp[0] = 0
for i in range(N):
    for j in range(W, weights[i] - 1, -1):
        if dp[j - weights[i]] != -1:
              dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
print(max(dp))
