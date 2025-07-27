MOD = 1000000007

def combi(n, r):
    a = 1                       # 分子
    for i in range(2, n + 1):
        a = (a * i) % MOD
    b = 1                       # 分母
    for i in range(2, r + 1):
        b = (b * i) % MOD
    for i in range(2, n - r + 1):
        b = (b * i) % MOD
    ret = a * pow(b, MOD - 2, MOD) % MOD # 逆元を使う
    return ret


n, r = map(int, input().split())
print(combi(n, r))
