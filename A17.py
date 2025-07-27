import heapq


def dijkstra(node):  # ダイクストラ法
    dist = [float("inf")] * N
    dist[node] = 0
    prev = [-1] * N
    que = []
    heapq.heappush(que, (dist[node], node))
    while que:
        node = heapq.heappop(que)
        pos = node[1]
        for n in G[pos]:
            nex = n[0]
            if dist[nex] > dist[pos] + n[1]:
                dist[nex] = dist[pos] + n[1]
                prev[nex] = pos
                heapq.heappush(que, (dist[nex], nex))
    return dist, prev


def get_path(arr):
    ans = [N - 1]
    i = N - 1
    while i != 0:
        ans.append(arr[i])
        i = arr[i]
    ans.reverse()
    return ans


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    G[i].append((i + 1, A[i]))
    if i < N - 2:
        G[i].append((i + 2, B[i]))
dist, prev = dijkstra(0)
ans = list(map(lambda x: x + 1, get_path(prev)))
print(len(ans))
print(*ans)
