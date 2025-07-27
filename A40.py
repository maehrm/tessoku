N = int(input())
A = list(map(int, input().split()))
c = {}
for a in A:
    if a not in c:
        c[a] = 0
    c[a] += 1
ans = 0
for k, v in c.items():
    ans += v * (v - 1) * (v - 2) // 6
print(ans)
