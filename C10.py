# C10 - A Long Grid https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fh
def mod_pow(b, n, mod):
    # b^n % mod を自作
    ret = 1
    while n:
        if n & 1:
            ret = (ret * b) % mod
        b = (b * b) % mod
        n >>= 1
    return ret
        
MOD = 1000000007
W = int(input())
print(12 * mod_pow(7, W - 1, MOD) % MOD)
