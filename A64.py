import heapq

def dijkstra(node):  # ダイクストラ法
    dist = [float("inf")] * N
    dist[node] = 0
    que = []
    heapq.heappush(que, (0, node))
    while que:
        d, pos = heapq.heappop(que)
        if d > dist[pos]:
            continue
        for nex, w in G[pos]:
            if dist[nex] > dist[pos] + w:
                dist[nex] = dist[pos] + w
                heapq.heappush(que, (dist[nex], nex))
    return [-1 if d == float('inf') else d for d in dist]


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

ans = dijkstra(0)
print(*ans, sep="\n")
