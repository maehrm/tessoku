N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        t = K - (i + j)
        if t >= 1 and t <= N:
            ans += 1
        elif t < 0:
            break
print(ans)
