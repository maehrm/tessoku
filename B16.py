# B16 - Frog 1 https://atcoder.jp/contests/tessoku-book/tasks/dp_a
N = int(input())
h = list(map(int, input().split()))
dp = [float("inf")] * N
dp[0] = 0
for i in range(1, N):
    dp[i] = min(dp[i], dp[i - 1] + abs(h[i - 1] - h[i]))
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + abs(h[i - 2] - h[i]))
print(dp[-1])
