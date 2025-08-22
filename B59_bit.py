# B59 - Number of Inversions https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ef
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i


N = int(input())
A = list(map(int, input().split()))
bit = BIT(N + 1)
ans = 0
for i in range(N - 1, -1, -1):
    ans += bit.sum(A[i] - 1)
    bit.add(A[i], 1)
print(ans)

# BIT(Binary Indexed Tree)を用いた転置数の数え方 - Mae向きなブログ https://maehrm.hatenablog.com/entry/2025/01/25/153716
