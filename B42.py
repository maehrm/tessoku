# B42 - Two Faced Cards https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_do
N = int(input())
s = [0] * 4
for _ in range(N):
    a, b = map(int, input().split())
    s[0] += max(0, a + b)
    s[1] += max(0, a - b)
    s[2] += max(0, -a + b)
    s[3] += max(0, -a - b)

print(max(s))
