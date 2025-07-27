import heapq


def dijkstra(node):  # ダイクストラ法
    dist = [float("inf")] * N
    dist[node] = 0
    que = []
    heapq.heappush(que, (dist[node], node))
    while que:
        node = heapq.heappop(que)
        pos = node[1]
        for n in G[pos]:
            nex = n[0]
            if dist[nex] > dist[pos] + n[1]:
                dist[nex] = dist[pos] + n[1]
                heapq.heappush(que, (dist[nex], nex))
    return dist


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    G[i].append((i + 1, A[i]))
    if i < N - 2:
        G[i].append((i + 2, B[i]))
print(dijkstra(0)[-1])
