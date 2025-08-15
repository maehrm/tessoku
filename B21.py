# B21 - Longest Subpalindrome https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ct
N = int(input())
S = input()

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    
for len in range(2, N + 1):
    for i in range(N - len + 1):
        j = i + len - 1
        if S[i] == S[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

print(dp[0][N - 1])
