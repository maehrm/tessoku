# B62 - Print a Path https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ei
import sys

sys.setrecursionlimit(10**6)


def dfs(current_node):
    if visited[current_node]:
        return False
    visited[current_node] = True
    if current_node == N:
        path.append(current_node)
        return True
    for next_node in G[current_node]:
        if dfs(next_node):
            path.append(current_node)
            return True
    return False


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

path = []
visited = [False] * (N + 1)
dfs(1)
print(*path[::-1])
