# B44 - Grid Operations https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dq
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
rows = [i for i in range(N)]
for _ in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        rows[x], rows[y] = rows[y], rows[x]
    elif t == 2:
        print(A[rows[x]][y])
