# C05 - Lucky Numbers https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fc
N = int(input()) - 1
ans = ["4"] * 10
for i in range(10):
    if (N >> i) & 1:
        ans[9 - i] = "7"
print("".join(ans))
