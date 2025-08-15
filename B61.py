# B61 - Influencer https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eh
N, M = map(int, input().split())
G = [0] * N
for _ in range(M):
    a, b = map(lambda n:int(n) - 1, input().split())
    G[a] += 1
    G[b] += 1
max, max_idx = G[0], 0
for i in range(1, N):
    if G[i] > max:
        max = G[i]
        max_idx = i
print(max_idx + 1)
