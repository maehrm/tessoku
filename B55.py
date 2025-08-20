# B55 - Difference https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eb
import bisect

Q = int(input())
A = []
for _ in range(Q):
    type, x = map(int, input().split())
    if type == 1:
        bisect.insort(A, x)
    elif type == 2:
        if not A:
            print(-1)
            continue
        idx = bisect.bisect_left(A, x)
        if idx == len(A):
            ans = abs(A[idx - 1] - x)
        elif idx == 0:
            ans = abs(A[idx] - x)
        else:
            ans = min(abs(A[idx] - x), abs(A[idx - 1] - x))
        print(ans)
