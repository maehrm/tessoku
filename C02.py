# C02 - Two Balls https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ez
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
print(sum(A[0:2]))
