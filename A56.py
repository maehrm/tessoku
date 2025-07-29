BASE = 9973
MOD = 1000000007

N, Q = map(int, input().split())
S = input()

hashes = [0] * (N + 1)
power = [1] * (N + 1)
for i in range(N):
    hashes[i + 1] = (hashes[i] * BASE + (ord(S[i]) - ord('a') + 1)) % MOD
    power[i + 1] = (power[i] * BASE) % MOD

for _ in range(Q):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    h1 = (hashes[b + 1] - hashes[a] * power[b + 1 - a]) % MOD
    h2 = (hashes[d + 1] - hashes[c] * power[d + 1 - c]) % MOD
    if h1 == h2:
        print("Yes")
    else:
        print("No")
