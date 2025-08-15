def digit_sum(n):               # 格桁の合計を求める。
    ret = 0
    while n > 0:
        n, r = divmod(n, 10)
        ret += r
    return ret


N, K = map(int, input().split())

MAX = K.bit_length()            # 必要なビット数
dp = [[0] * MAX for _ in range(N + 1)] # dp[i][j]: iに対して2**j回操作した値

for i in range(1, N + 1):       # iに対して1回操作した値
    dp[i][0] = i - digit_sum(i)
    
for j in range(1, MAX):         # ダブリング
    for i in range(1, N + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]
        
for i in range(1, N + 1):
    cur = i
    for j in range(MAX):
        if (K >> j) & 1:
            cur = dp[cur][j]
    print(cur)
