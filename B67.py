from atcoder.dsu import DSU

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a - 1, b - 1))

edges.sort(reverse=True)
dsu = DSU(N)
ans = 0
for i in range(M):
    c, a, b = edges[i]
    if not dsu.same(a, b):
        ans += c
        dsu.merge(a, b)
print(ans)
