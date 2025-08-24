# A50 - 山型足し算 https://atcoder.jp/contests/tessoku-book/tasks/future_contest_2018_qual_a

# とりあえず、高い山から低くしていくという単純な方法
# ACをもらうための作戦。今後、改善する。
N = 100
Q_MAX = 1000

A = [list(map(int, input().split())) for _ in range(N)]
ans = []

for _ in range(Q_MAX):
    max_h = 0
    x = y = -1
    for i in range(N):
        for j in range(N):
            if A[i][j] > max_h:
                max_h = A[i][j]
                y, x = i, j

    if max_h == 0:
        break

    H = min(100, max(1, max_h))
    ans.append((x, y, H))

    for i in range(N):
        dy = abs(i - y)
        if dy >= H:
            continue
        for j in range(N):
            c = H - dy - abs(j - x)
            if c > 0:
                A[i][j] -= c
                if A[i][j] < 0:
                    A[i][j] = 0

print(len(ans))
for x, y, h in ans:
    print(x, y, h)
