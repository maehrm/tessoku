# B63 - 幅優先探索 https://atcoder.jp/contests/tessoku-book/tasks/abc007_3
from collections import deque


def bfs(cur_y, cur_x):
    que = deque()
    que.append((cur_y, cur_x))
    while que:
        cur_y, cur_x = que.popleft()
        if cur_x == gx and cur_y == gy:
            return c[cur_y][cur_x]
        for dy, dx in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nxt_y, nxt_x = cur_y + dy, cur_x + dx
            if nxt_x < 0 or nxt_y < 0 or nxt_x >= C or nxt_y >= R:
                continue
            if c[nxt_y][nxt_x] == "#":
                continue
            if c[nxt_y][nxt_x] == '.':
                c[nxt_y][nxt_x] = c[cur_y][cur_x] + 1
                que.append((nxt_y, nxt_x))


R, C = map(int, input().split())
sy, sx = map(lambda n: int(n) - 1, input().split())
gy, gx = map(lambda n: int(n) - 1, input().split())
c = [list(input()) for _ in range(R)]

c[sy][sx] = 0
print(bfs(sy, sx))
