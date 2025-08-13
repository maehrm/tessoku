# B09 - Papers https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ch
MAX = 1500
grid = [[0] * (MAX + 1) for _ in range(MAX + 1)]

N = int(input())
for _ in range(N):  # imos法
    a, b, c, d = map(int, input().split())
    grid[b][a] += 1
    grid[b][c] -= 1
    grid[d][a] -= 1
    grid[d][c] += 1

for y in range(MAX + 1):  # 横方向累積
    for x in range(MAX):
        grid[y][x + 1] += grid[y][x]

for x in range(MAX + 1):  # 縦方向累積
    for y in range(MAX):
        grid[y + 1][x] += grid[y][x]

ans = 0
for y in range(MAX + 1):
    for x in range(MAX + 1):
        if grid[y][x] > 0:
            ans += 1

print(ans)
