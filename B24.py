# B24 - Many Boxes https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cw
import bisect

N = int(input())
XY = []
for _ in range(N):
    XY.append(list(map(int, input().split())))

XY.sort(key=lambda xy: (xy[0], -xy[1]))  # X:昇順, Y:降順
ans = []
for _, y in XY:  # LIS
    i = bisect.bisect_left(ans, y)
    if i == len(ans):
        ans.append(y)
    else:
        ans[i] = y

print(len(ans))
