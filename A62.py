import sys

sys.setrecursionlimit(10**6)


def dfs(n):
    if visited[n]:
        return
    visited[n] = True
    for nxt in G[n]:
        dfs(nxt)
    return


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * N
dfs(0)
if all(visited):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
