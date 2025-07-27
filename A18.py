N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S + 1)
dp[0] = True
for i in range(N):
    for j in range(S, A[i] - 1, -1):
        if dp[j - A[i]]:
            dp[j] = True

print("Yes") if dp[S] else print("No")

