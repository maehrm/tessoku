# B64 - Shortest Path with Restoration https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ek
# B64 - Shortest Path with Restoration https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ek
import heapq


def dijkstra(node):  # ダイクストラ法
    dist = [float("inf")] * N
    dist[node] = 0
    prev = [-1] * N  # 経路算出用
    que = []
    heapq.heappush(que, (0, node))
    while que:
        d, pos = heapq.heappop(que)
        if d > dist[pos]:
            continue
        for nex, w in G[pos]:
            if dist[nex] > dist[pos] + w:
                dist[nex] = dist[pos] + w
                prev[nex] = pos  # 経路を記録
                heapq.heappush(que, (dist[nex], nex))
    # 各ノードへの最短距離, 経路情報
    return [-1 if d == float("inf") else d for d in dist], prev


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))


_, path = dijkstra(0)
ans = []
i = N - 1
while i != -1:
    ans.append(i + 1)
    i = path[i]
print(*ans[::-1])
