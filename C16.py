# C16 - Flights https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fn
import bisect

N, M, K = map(int, input().split())
ASBT = []
for i in range(M):
    a, s, b, t = map(int, input().split())
    ASBT.append((a - 1, s, b - 1, t + K))

ASBT.sort(key=lambda x: x[3])

dp = [[] for _ in range(N)]  # (到着時刻, 乗れた本数) のタプル配列
ans = 0

for a, s, b, t in ASBT:
    arr = dp[a]  # 出発空港aに到着した履歴
    # 出発時刻sまでに空港aに到着していた履歴の中で一番遅いもの
    time = bisect.bisect_right(arr, (s, float("inf"))) - 1
    if time >= 0:
        max_prev = arr[time][1]
    else:
        max_prev = 0  # 最初のフライト
    cur = max_prev + 1
    if dp[b] and dp[b][-1][1] >= cur:  # より良い結果があるなら追加しない
        continue
    dp[b].append((t, cur))
    ans = max(ans, cur)

print(ans)
