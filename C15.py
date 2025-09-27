# C15 - Many Meetings https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fm
N = int(input())
K = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
max_time = 0
for i in range(N):
    LR[i][1] += K
    max_time = max(max_time, LR[i][1])

sorted_by_end_time = sorted(LR, key=lambda x: x[1])
dpL = [0] * (max_time + 1)
now = 0
count = 0
for L, R in sorted_by_end_time:
    if now <= L:
        count += 1
        now = R
        dpL[now] = count

sorted_by_start_time = sorted(LR, key=lambda x: -x[0])
dpR = [0] * (max_time + 1)
now = max_time
count = 0
for L, R in sorted_by_start_time:
    if now >= R:
        count += 1
        now = L
        dpR[now] = count

for i in range(1, max_time):
    dpL[i] = max(dpL[i], dpL[i - 1])
for i in range(max_time - 1, -1, -1):
    dpR[i] = max(dpR[i], dpR[i + 1])

for L, R in LR:
    ans = dpL[L] + 1 + dpR[R]
    print(ans)
