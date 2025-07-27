N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]
LR.sort(key=lambda x: x[1])
ans = 0
t = 0
for i in range(N):
    l, r = LR[i]
    if t <= l:
        t = r
        ans += 1
print(ans)
