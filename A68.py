# A68 - Maximum Flow https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bp
from collections import deque


# Edmonds-Karpアルゴリズム
def max_flow(graph, source, sink):
    flow = 0
    parent = [0] * len(graph)
    ans = 0
    while bfs(graph, source, sink, parent):
        flow = float("inf")
        v = sink
        while v != source:
            flow = min(flow, graph[parent[v]][v])
            v = parent[v]
        v = sink
        while v != source:
            graph[parent[v]][v] -= flow
            graph[v][parent[v]] += flow
            v = parent[v]
        ans += flow
    return ans


def bfs(graph, source, sink, parent):
    visit = [False] * len(graph)
    visit[source] = True
    que = deque()
    que.append(source)
    while que:
        u = que.popleft()
        for v in range(len(graph)):
            if not visit[v] and graph[u][v] > 0:
                visit[v] = True
                parent[v] = u
                if v == sink:
                    return True
                que.append(v)
    return False


N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1][b - 1] = c
print(max_flow(G, 0, N - 1))
