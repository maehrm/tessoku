# B43 - Quiz Contest https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dp
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = [M] * N
for i in range(M):
    ans[A[i] - 1] -= 1
print(*ans, sep="\n")
