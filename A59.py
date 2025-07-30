class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.sz = 1
        while self.sz < n:
            self.sz *= 2
        self.tree = [0] * (2 * self.sz)
        # 葉ノードに値をセット
        for i in range(n):
            self.tree[self.sz + i] = data[i]
        # 親ノードを構築(下から上へ)
        for i in range(self.sz - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, x):
        i += self.sz
        self.tree[i] = x
        while i > 1:  # 葉から親へ辿る処理
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def query(self, l, r):
        l += self.sz
        r += self.sz
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


N, Q = map(int, input().split())
A = [0] * N
seg = SegmentTree(A)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, pos, x = query
        seg.update(pos - 1, x)
    elif query[0] == 2:
        _, l, r = query
        print(seg.query(l - 1, r - 1))
