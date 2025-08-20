# B17 - Frog 1 with Restoration https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cp
N = int(input())
h = list(map(int, input().split()))
dp = [float("inf")] * N
dp[0] = 0
prev = [-1] * N
for i in range(1, N):
    val = dp[i - 1] + abs(h[i - 1] - h[i])
    if dp[i] > val:
        dp[i] = val
        prev[i] = i - 1
    if i > 1:
        val = dp[i - 2] + abs(h[i - 2] - h[i])
        if dp[i] > val:
            dp[i] = val
            prev[i] = i - 2

ans = []
i = N - 1
while i != -1:
    ans.append(i + 1)
    i = prev[i]
print(len(ans))
print(*ans[::-1])
