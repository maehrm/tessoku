# C06 - Regular Graph https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fd
N = int(input())
ans = [i + 1 for i in range(N)] + [1]
print(N)
for i in range(N):
    print(ans[i], ans[i + 1])
