# A73 - Marathon Route https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bu
import heapq


def dijkstra(node):  # ダイクストラ法
    ans = [[float("inf"), 0] for _ in range(N)]
    ans[node][0], ans[node][1] = 0, 0
    que = []
    heapq.heappush(que, (0, 0, node)) # (距離, -木の数, Node)
    while que:
        dist, minus_tree, pos = heapq.heappop(que)
        tree = -minus_tree
        if dist > ans[pos][0] or (dist == ans[pos][0] and tree < ans[pos][1]):
            continue
        for nxt_pos, nxt_dist, nxt_tree in G[pos]:
            new_dist = ans[pos][0] + nxt_dist
            new_tree = ans[pos][1] + nxt_tree
            if (new_dist < ans[nxt_pos][0]) or (new_dist == ans[nxt_pos][0] and new_tree > ans[nxt_pos][1]):
                ans[nxt_pos][0] = new_dist
                ans[nxt_pos][1] = new_tree
                heapq.heappush(que, (new_dist, -new_tree, nxt_pos))
    return ans


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    G[a - 1].append((b - 1, c, d))
    G[b - 1].append((a - 1, c, d))

print(*dijkstra(0)[-1])
