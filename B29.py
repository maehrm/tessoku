# B29 - Power Hard https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_db
def pow(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow((a * a) % mod, b // 2, mod) % mod
    else:
        return a * pow((a * a) % mod, b // 2, mod) % mod


MOD = 1000000007
a, b = map(int, input().split())
print(pow(a, b, MOD))
