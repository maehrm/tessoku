# B56 - Palindrome Queries https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ec
BASE = 9973
MOD = 1000000007

N, Q = map(int, input().split())
S = input()
S_rev = S[::-1]  # 文字列逆順

h = [0] * (N + 1)
h_r = [0] * (N + 1)
p = [1] * (N + 1)

for i in range(N):
    h[i + 1] = (h[i] * BASE + (ord(S[i]) - ord("a") + 1)) % MOD
    h_r[i + 1] = (h_r[i] * BASE + (ord(S_rev[i]) - ord("a") + 1)) % MOD
    p[i + 1] = (p[i] * BASE) % MOD

for _ in range(Q):
    L, R = map(lambda x: int(x) - 1, input().split())
    L_rev = N - R - 1
    R_rev = N - L - 1
    h1 = (h[R + 1] - h[L] * p[R + 1 - L]) % MOD
    h2 = (h_r[R_rev + 1] - h_r[L_rev] * p[R_rev + 1 - L_rev]) % MOD
    if h1 == h2:
        print("Yes")
    else:
        print("No")
