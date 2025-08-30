# A50 - 山型足し算 https://atcoder.jp/contests/tessoku-book/tasks/future_contest_2018_qual_a
# 参考：answer_A50_extra.py 9997221081点
import math
import numpy as np
import random
import time
import sys

# 定数の設定・入力
N = 100
Q = 1000
A = np.array([list(map(int, input().split())) for i in range(N)])

# 初期解を生成
X = [random.randint(0, N - 1) for i in range(Q)]
Y = [random.randint(0, N - 1) for i in range(Q)]
H = [1] * Q
B = np.zeros((3 * N, 3 * N))
for i in range(Q):
    B[Y[i]][X[i]] += 1

# H = 1, 2, ..., N に設定された場合の「増減分」を持った numpy 配列を作る
delta = [None] * (N + 1)
for i in range(1, N + 1):
    delta[i] = np.array(
        [
            [max(i - abs(y) - abs(x), 0) for x in range(-i + 1, i)]
            for y in range(-i + 1, i)
        ]
    )


# 現在のスコアを取得する関数
def get_score():
    return 200000000 - np.absolute(A - B[N : 2 * N, N : 2 * N]).sum()


# 山登り法の設定
# （現在のスコアを np.absolute(A - B[N:2*N, N:2*N]).sum() として、これを最大化するという方法で実装する）
TIME_LIMIT = 5.4
current_score = get_score()
ti = time.time()

# 山登り法スタート
loops = 0
while time.time() - ti < TIME_LIMIT:
    # 「小さな変更」をランダムに選ぶ
    t = random.randint(0, Q - 1)
    h_limit = 14
    if current_score >= 199900000:
        h_limit = 1
    elif current_score >= 199500000:
        h_limit = 7
    old_x, new_x = X[t], X[t] + random.randint(-1, +1)
    old_y, new_y = Y[t], Y[t] + random.randint(-1, +1)
    old_h, new_h = H[t], H[t] + random.randint(-h_limit, +h_limit)
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or new_h <= 0 or new_h > N:
        continue

    # X[t] = new_x, Y[t] = new_y, H[t] = new_h に変更（書籍中の Change(t, new_x, new_y, new_h) の呼び出しに対応）
    B[
        N + Y[t] - H[t] + 1 : N + Y[t] + H[t], N + X[t] - H[t] + 1 : N + X[t] + H[t]
    ] -= delta[H[t]]
    X[t], Y[t], H[t] = new_x, new_y, new_h
    B[
        N + Y[t] - H[t] + 1 : N + Y[t] + H[t], N + X[t] - H[t] + 1 : N + X[t] + H[t]
    ] += delta[H[t]]

    # スコアを計算
    new_score = get_score()

    # スコアに応じて採用／不採用を決める
    temperature = 180.0 - 179.0 * (time.time() - ti) / TIME_LIMIT
    probability = math.exp(min((new_score - current_score) / temperature, 0))
    if random.random() < probability:
        # 採用の場合
        current_score = new_score
    else:
        # 不採用の場合：X[t] = old_x, Y[t] = old_y, H[t] = old_h に戻す（書籍中の Change(t, old_x, old_y, old_h) の呼び出しに対応）
        B[
            N + Y[t] - H[t] + 1 : N + Y[t] + H[t], N + X[t] - H[t] + 1 : N + X[t] + H[t]
        ] -= delta[H[t]]
        X[t], Y[t], H[t] = old_x, old_y, old_h
        B[
            N + Y[t] - H[t] + 1 : N + Y[t] + H[t], N + X[t] - H[t] + 1 : N + X[t] + H[t]
        ] += delta[H[t]]

    loops += 1

# 出力
print(Q)
for i in range(Q):
    print(X[i], Y[i], H[i])
print("score =", current_score, file=sys.stderr)
print("loops =", loops, file=sys.stderr)

# とりあえず、高い山から低くしていくという単純な方法
# ACをもらうための作戦。今後、改善する。9633344494点ゲット

# N = 100
# Q_MAX = 1000

# A = [list(map(int, input().split())) for _ in range(N)]
# ans = []

# for _ in range(Q_MAX):
#     max_h = 0
#     x = y = -1
#     for i in range(N):
#         for j in range(N):
#             if A[i][j] > max_h:
#                 max_h = A[i][j]
#                 y, x = i, j

#     if max_h == 0:
#         break

#     H = min(100, max(1, max_h))
#     ans.append((x, y, H))

#     for i in range(N):
#         dy = abs(i - y)
#         if dy >= H:
#             continue
#         for j in range(N):
#             c = H - dy - abs(j - x)
#             if c > 0:
#                 A[i][j] -= c
#                 if A[i][j] < 0:
#                     A[i][j] = 0

# print(len(ans))
# for x, y, h in ans:
#     print(x, y, h)
