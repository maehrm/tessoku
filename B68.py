# B68 - ALGO Express https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eo
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
P = list(map(int, input().split()))
G = [[0] * (N + 2) for _ in range(N + 2)]
s = 0                           # 正の利益
for i in range(N):
    if P[i] >= 0:               
        G[0][i + 1] = P[i]      # Source -> Node(i + 1)へ
        s += P[i]               
    else:
        G[i + 1][N + 1] = -P[i] # Node(i + 1) -> Tへ
        
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = float('inf')

mincut = max_flow(G, 0, N + 1)
print(s - mincut)               # 利益の最大化する値から最小の損を引く
