# C19 - Gasoline Optimization Problem https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fq
class SegmentTree:
    def __init__(self, data, op, e):
        self.op = op  # 演算
        self.e = e  # 単位元
        n = len(data)
        self.sz = 1
        while self.sz < n:
            self.sz *= 2
        self.tree = [self.e] * (2 * self.sz)
        # 葉ノードに値をセット
        for i in range(n):
            self.tree[self.sz + i] = data[i]
        # 親ノードを構築(下から上へ)
        for i in range(self.sz - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, x):
        i += self.sz
        self.tree[i] = x
        while i > 1:  # 葉から親へ辿る処理
            i //= 2
            self.tree[i] = self.op(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l, r):
        l += self.sz
        r += self.sz
        res = self.e
        while l < r:
            if l % 2 == 1:
                res = self.op(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.op(res, self.tree[r])
            l //= 2
            r //= 2
        return res


N, L, K = map(int, input().split())
seg = SegmentTree([float("inf")] * (L + 1), min, float("inf"))
gas = {}  # 同じ位置のガソリンスタンドの最安値だけを登録
for _ in range(N):
    a, c = map(int, input().split())
    if a in gas and gas[a] <= c:
        continue
    gas[a] = c
    seg.update(a, c)

ans = 0
for pos in range(L - K):
    x = seg.query(pos + 1, min(L, pos + K + 1))
    if x == float("inf"):
        print(-1)
        exit()
    ans += x
print(ans)
