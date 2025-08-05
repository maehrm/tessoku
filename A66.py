from atcoder.dsu import DSU

N, Q = map(int, input().split())
dsu = DSU(N)
for _ in range(Q):
    q, u, v = map(int, input().split())
    if q == 1:
        dsu.merge(u - 1, v - 1)
    elif q == 2:
        if dsu.same(u - 1, v - 1):
            print("Yes")
        else:
            print("No")
