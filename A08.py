H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
acc = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        acc[i][j] = X[i - 1][j - 1] + acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1]
Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = acc[C][D] - acc[C][B - 1] - acc[A - 1][D] + acc[A - 1][B - 1]
    print(ans)
