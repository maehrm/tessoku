H, W, N = map(int, input().split())
s = [[0] * (W + 1) for _ in range(H)]
for _ in range(N):
    A, B, C, D = map(lambda x: int(x) - 1, map(int, input().split()))
    for i in range(A, C + 1):
        s[i][B] += 1
        s[i][D + 1] -= 1

for i in range(H):
    for j in range(W):
        if j == 0:
            continue
        s[i][j] += s[i][j - 1]
    print(*s[i][:-1])
