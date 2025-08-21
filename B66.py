# B66 - Typhoon https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_em
from atcoder.dsu import DSU

N, M = map(int, input().split())
AB = []
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    AB.append((a, b))

Q = int(input())
query = []
removed = [False] * M
for _ in range(Q):
    q = list(map(int, input().split()))
    query.append(q)
    if q[0] == 1:
        removed[q[1] - 1] = True

dsu = DSU(N)
for i in range(M):  # 削除されない辺はつないでおく
    if not removed[i]:
        dsu.merge(AB[i][0], AB[i][1])

query = query[::-1]             # query を逆順にたどる。
ans = []
for i in range(Q):
    if query[i][0] == 1:
        a, b = AB[query[i][1] - 1]
        dsu.merge(a, b)
    else:
        u, v = query[i][1], query[i][2]
        if dsu.same(u - 1, v - 1):
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans[::-1], sep="\n")
