D = int(input())
N = int(input())
ans = [0] * (D + 2)
for _ in range(N):
    L, R = map(int, input().split())
    ans[L] += 1
    ans[R + 1] -= 1
for i in range(1, D + 1):
    ans[i] += ans[i - 1]
    print(ans[i])
