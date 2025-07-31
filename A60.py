N = int(input())
A = list(map(int, input().split()))

stack = []
ans = [-1] * N

for i, a in enumerate(A):
    while stack and stack[-1][1] <= a:
        stack.pop()
    if stack:
        ans[i] = stack[-1][0] + 1
    stack.append((i, a))

print(*ans)
