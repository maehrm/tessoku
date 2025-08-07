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


N = int(input())
C = [input() for _ in range(N)]
G = [[0] * (2 * N + 2) for _ in range(2 * N + 2)]
for i in range(N):
    G[0][i + 1] = 1             # Source -> 生徒ノード
    G[i + 1 + N][2 * N + 1] = 1 # 席ノード -> Sink
    for j in range(N):
        if C[i][j] == "#":
            G[i + 1][j + 1 + N] = 1
print(max_flow(G, 0, 2 * N + 1))
