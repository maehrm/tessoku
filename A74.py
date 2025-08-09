N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
row = []
for i in range(N):
    for j in range(N):
        if P[i][j] != 0:
            row.append((P[i][j], j))
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if row[i][0] > row[j][0]:
            row[i], row[j] = row[j], row[i]
            ans += 1

for i in range(N - 1):
    for j in range(i + 1, N):
        if row[i][1] > row[j][1]:
            row[i], row[j] = row[j], row[i]
            ans += 1

print(ans)
