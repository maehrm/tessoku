D, N = map(int, input().split())
dp = [24] * (D + 1)
dp[0] = 0

for i in range(N):
    L, R, H = map(int, input().split())
    for j in range(L, R + 1):
        dp[j] = min(dp[j], H)

print(sum(dp))
