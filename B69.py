# B69 - Black Company 2 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ep
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
C = [list(map(int, input().strip())) for _ in range(N)]

SIZE = 24 + N + 2  # 24h + N人 + (source + sink )
G = [[0] * SIZE for _ in range(SIZE)]
source = 0
sink = SIZE - 1
for j in range(24):  # source -> 各時間へ(容量M)
    G[source][j + 1] = M

for i in range(N):  # 各時間 -> 人(容量1)
    for j in range(24):
        if C[i][j] == 1:
            G[j + 1][25 + i] = 1

for i in range(N):  # 人 -> sink(容量10)
    G[25 + i][sink] = 10

maxflow = max_flow(G, source, sink)
if maxflow == 24 * M:
    print("Yes")
else:
    print("No")
