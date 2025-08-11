# B27 - Calculate LCM https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cz
def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


A, B = map(int, input().split())
print(A // gcd(A, B) * B)
