N = int(input())
TD = [list(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda x: x[1])

MAX_D = max(d for t, d in TD)

# dp[i][j]: 問題iまでで、時間j以内に解ける問題の最大数
dp = [[-1] * (MAX_D + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    t, d = TD[i]
    for j in range(MAX_D + 1):
        # 前問題までの状態をcopy
        dp[i + 1][j] = dp[i][j]
        # 問題iが解ける条件
        if j - t >= 0 and j <= d:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - t] + 1)

print(max(dp[N]))

# 貪欲法を使うと思ったのですが、7つのテストケースでWA
#
# N = int(input())

# TD = [list(map(int, input().split())) for _ in range(N)]
# # 終了時間が早い順。終了時間が同じなら短い時間で解ける問題が先にくるように。
# TD.sort(key = lambda x: (x[1], x[0]))

# ans = 0
# current_time = 0
# for i in range(N):
#     if current_time + TD[i][0] <= TD[i][1]:
#         ans += 1
#         current_time += TD[i][0]

# print(ans)
