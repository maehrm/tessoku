# B40 - Divide by 100 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dm
N = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(N):
    r = A[i] % 100
    if r not in d:
        d[r] = 0
    d[r] += 1
ans = 0
for val in (0, 50):  # 余り0,50は特別扱い
    if val in d and d[val] >= 2:
        ans += (d[val] * (d[val] - 1)) // 2
for k in range(1, 50):
    if k in d and (100 - k) in d:
        ans += d[k] * d[100 - k]

print(ans)
