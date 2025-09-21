# C13 - Select 2 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fk
MOD = 1000000007
N, P = map(int, input().split())
A = list(map(int, input().split()))
A_mod = [a % MOD for a in A]
count = {}
for a in A_mod:
    if not a in count:
        count[a] = 0
    count[a] += 1
ans = 0
if P == 0:
    # 0と0の組み合わせ
    ans += count[0] * (count[0] - 1) // 2
    # 0と非0の組み合わせ
    ans += count[0] * (N - count[0])
else:
    for a in count:
        b = (P * pow(a, MOD - 2, MOD)) % MOD
        if b not in count:
            continue
        if a != b:
            ans += count[a] * count[b]
        else:
            ans += count[a] * (count[a] - 1)
    ans //= 2
print(ans)
