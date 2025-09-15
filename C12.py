# C12 - Taro the Novel Writer https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fj
N, M, K = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[B].append(A)

# count[f][t] = 区間 [f, t] に完全に収まる辺の数    
count = [[0] * (N + 1) for _ in range(N + 1)]
for f in range(1, N + 1):
    c = 0
    for t in range(f, N + 1):
        for a in edges[t]:
            if a >= f:
                c += 1
        count[f][t] = c

# dp[k][i] : 先頭iページをk章に分けたときの最大良さ
dp = [[-float("inf")] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 0

for k in range(1, K + 1):       # k章目を作る。
    for i in range(k, N + 1):   # k章目はiページまで
        best = -float("inf")
        for j in range(k - 1, i): # k-1章目はjページまで
            val = dp[k - 1][j] + count[j + 1][i]
            if val > best:
                best = val
        dp[k][i] = best

print(dp[K][N])
