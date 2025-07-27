import sys
sys.setrecursionlimit(2 * 10**5)

def solv(l, r):
    if r - l <= 0:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]

    # 左端のブロックを取り除く
    left_score = solv(l + 1, r)
    if l + 1 <= P[l] <= r:
        left_score += A[l]

    # 右端のブロックを取り除く
    right_score = solv(l, r - 1)
    if l <= P[r] <= r - 1:
        right_score += A[r]

    dp[l][r] = max(left_score, right_score)
    return dp[l][r]

N = int(input())
P = [0] * N
A = [0] * N
for i in range(N):
    p_val, a_val = map(int, input().split())
    P[i] = p_val - 1
    A[i] = a_val

dp = [[-1] * N for _ in range(N)]
print(solv(0, N - 1))


# 参考 鉄則本 A21 - Block Game (2Q, ★4) - けんちょんの競プロ精進記録 https://drken1215.hatenablog.com/entry/2024/09/28/123219
# N = int(input())
# P, A = [0] * N, [0] * N
# for i in range(N):
#     p, a = map(int, input().split())
#     p -= 1
#     P[i], A[i] = p, a

# dp = [[0] * N for _ in range(N)]
# for len in range(1, N + 1):  # 区間の長さ
#     for l in range(N - len + 1):  # 左端のブロック
#         r = l + len - 1  # 右端のブロック
#         dp[l][r] = 0     # 必要？
#         for k in range(l, r + 1):  # 区間の中で最後に k の要素を取り除く
#             score = 0
#             if k > l:
#                 score += dp[l][k-1]
#             if k < r:
#                 score += dp[k+1][r]
#             if P[k] >= l and P[k] <= r:
#                 score += A[k]
#             dp[l][r] = max(dp[l][r], score)

# print(dp[0][N - 1])
