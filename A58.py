import math
import sys

sys.setrecursionlimit(10**9)


class RMQ:
    def __init__(self, n):
        self.n = 2 ** math.ceil(math.log2(n))  # nが2のべき乗になるように調整
        self.dat = [0 for _ in range(2 * self.n)]

    def update(self, i, x):
        i += self.n
        self.dat[i] = x
        while i >= 2:  # 葉から親へ辿る処理
            i //= 2
            self.dat[i] = max(self.dat[i * 2], self.dat[i * 2 + 1])

    def find(self, s, t):
        return self.__query(s, t, 1, 0, self.n)

    def __query(self, l, r, k, a, b):
        if r <= a or b <= l:  # 交差しない?
            return -float("inf")
        if l <= a and b <= r:  # 完全に含む?
            return self.dat[k]
        m = (a + b) // 2
        vl = self.__query(l, r, k * 2, a, m)
        vr = self.__query(l, r, k * 2 + 1, m, b)
        return max(vl, vr)


N, Q = map(int, input().split())
rmq = RMQ(N)
for _ in range(Q):
    com, *arg = map(int, input().split())
    if com == 1:
        pos, x = arg
        rmq.update(pos - 1, x)
    elif com == 2:
        l, r = arg
        print(rmq.find(l-1, r-1))
