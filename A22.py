N = int(input())
A = list(map(lambda x:int(x) - 1, input().split()))
B = list(map(lambda x:int(x) - 1, input().split()))
dp = [-float('inf') for _ in range(N)]
dp[0] = 0
for i in range(N - 1):
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)
print(dp[-1])

