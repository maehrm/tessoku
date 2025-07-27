N, M = map(int, input().split())
A = []
for _ in range(M):
    A.append(list(map(int, input().split())))

dp = [float('inf') for _ in range(1 << N)]
dp[0] = 0
for mask in range(1 << N):
    if dp[mask] == float('inf'):
        continue
    for i in range(M):
        val = 0
        for j in range(N):
            val |= A[i][j] << j
        dp[mask | val] = min(dp[mask | val], dp[mask] + 1)

print(dp[-1]) if dp[-1] != float('inf') else print("-1")
