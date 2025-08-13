# B12 - Equation https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck
# ニュートン法
N = int(input())
x = N ** (1 / 3)
while True:
    fx = x**3 + x - N
    dfx = 3 * x**2 + 1
    nx = x - fx / dfx
    if abs(nx - x) < 0.001:
        print(nx)
        break
    x = nx
