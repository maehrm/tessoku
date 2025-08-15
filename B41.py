X, Y = map(int, input().split())
ans = [(X, Y)]
while not (X == 1 and Y == 1):
    if X > Y:
        X -= Y
    else:
        Y -= X
    ans.append((X, Y))

ans = ans[:-1][::-1]
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
