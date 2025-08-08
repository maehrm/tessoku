N = int(input())

LIM = 1500
grid = [[0] * (LIM + 1) for _ in range(LIM + 1)]
for _ in range(N):
    x, y = map(int, input().split())
    grid[y][x] += 1

# 累積和を求める。
acc = [[0] * (LIM + 1) for _ in range(LIM + 1)]    
for y in range(1, LIM + 1):
    for x in range(1, LIM + 1):
        acc[y][x] = (acc[y][x - 1] + acc[y - 1][x] - acc[y - 1][x - 1] + grid[y][x])

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(acc[d][c] - acc[b - 1][c] - acc[d][a - 1] + acc[b - 1][a - 1])
