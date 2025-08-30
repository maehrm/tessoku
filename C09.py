# C09 - Taro's Vacation https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ac
N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(2)] # dp[0][i]: 前日勉強してない,dp[1][i]:前日勉強した
for i in range(N):
    dp[0][i + 1] = max(dp[0][i], dp[1][i])
    dp[1][i + 1] = dp[0][i] + A[i]
    
print(max(dp[0][N], dp[1][N]))

