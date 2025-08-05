N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
A = [0] + A
ans = [0] * N
for i in range(N - 1, 0, -1):
    ans[A[i]] += ans[i] + 1
print(*ans)
