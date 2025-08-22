# B59 - Number of Inversions https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ef
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


N = int(input())
A = list(map(int, input().split()))
seg = SegmentTree([0] * (N + 1), lambda x, y: x + y, 0)
ans = 0
for a in A:
    ans += seg.query(a, N + 1)  # 今見ている値aより大きい値がすでに何個出現したか。
    seg.update(a, 1)
print(ans)
