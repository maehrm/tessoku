# C07 - ALGO-MARKET https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fe
import bisect

N = int(input())
C = list(map(int, input().split()))
C.sort()
acc = [C[0]]
for i in range(1, N):
    acc.append(acc[-1] + C[i])
Q = int(input())
for _ in range(Q):
    X = int(input())
    print(bisect.bisect_right(acc, X))
