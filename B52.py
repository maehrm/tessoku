# B52 - Ball Simulation https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dy
N, X = map(int, input().split())
X -= 1
A = list(input())
A[X] = "@"
for i in range(X - 1, -1, -1):  # Xの左を白が続く限り青色へ
    if A[i] == ".":
        A[i] = "@"
    else:
        break
for i in range(X + 1, N):       # Xの右を白が続く限り青色へ
    if A[i] == ".":
        A[i] = "@"
    else:
        break
print("".join(A))
