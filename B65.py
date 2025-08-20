# B65 - Road to Promotion Hard https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_el
import sys

sys.setrecursionlimit(10**6)


def dfs(n):
    visited[n] = True
    rank = -1
    for nxt in G[n]:
        if visited[nxt]:
            continue
        rank = max(rank, dfs(nxt))
    ans[n] = rank + 1
    return ans[n]


N, T = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

ans = [0] * N
visited = [False] * N
dfs(T - 1)
print(*ans)
