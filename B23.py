# B23 - Traveling Salesman Problem https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cv
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dist = [[0] * N for _ in range(N)]

for i in range(N - 1):
    xi, yi = XY[i]
    for j in range(i + 1, N):
        xj, yj = XY[j]
        dist[i][j] = math.sqrt((xj - xi) ** 2 + (yj - yi) ** 2)
        dist[j][i] = dist[i][j]

dp = [[float("inf")] * N for _ in range(1 << N)]
dp[1 << 0][0] = 0

for state in range(1, 1 << N):  # 全ての状態を試す
    for i in range(N):
        if not (state & (1 << i)):  # 都市iを訪れていなければスキップ
            continue
        if dp[state][i] == float("inf"):
            continue
        for j in range(N):  # 次に都市jを訪れるとする。
            if state & (1 << j):  # 都市jを訪問済みならスキップ
                continue
            next_state = state | (1 << j)
            new_cost = dp[state][i] + dist[i][j]
            if new_cost < dp[next_state][j]:  # より短い距離が見つかったら更新
                dp[next_state][j] = new_cost

ans = float("inf")
all_visited = (1 << N) - 1  # 全都市訪問済みの状態
for i in range(N):
    # 都市iを最後に訪れたとき、都市i => 都市0への距離を加算
    ans = min(dp[all_visited][i] + dist[i][0], ans)
print(ans)
