# C04 - Divisor Enumeration https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fb
N = int(input())
i = 1
ans = []
while i * i <= N:
    q, r = divmod(N, i)
    if r == 0:
        ans.append(i)
        ans.append(q)
    i += 1
ans.sort()
print(*ans, sep='\n')
