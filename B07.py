T = int(input())
N = int(input())
ans = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    ans[L] += 1
    ans[R] -= 1
for i in range(T):
    ans[i + 1] += ans[i]
print(*ans[:-1], sep="\n")
