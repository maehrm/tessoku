# C14 - Commute Route https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fl
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
    return dist


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))


# ノード(0)から各ノードへの最短距離を求める
dist1 = dijkstra(0)

# ノード(N-1)から各ノードへの最短距離を求める。
dist2 = dijkstra(N - 1)

ans = 1
min_dist = dist1[N - 1]
for i in range(1, N):
    if dist1[i] + dist2[i] == min_dist:  # ノードiは最短距離上の交差点
        ans += 1
print(ans)
