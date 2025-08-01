from collections import deque


def bfs(n):
    que = deque()
    que.append(n)
    while que:
        cur = que.popleft()
        for nxt in G[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                que.append(nxt)


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
dist[0] = 0
bfs(0)
for d in dist:
    print(d)
