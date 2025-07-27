N = int(input())
A = list(map(int, input().split()))
B = A[::]
B.sort()
d = {}
rank = 0
for i in range(N):
    if B[i] not in d:
        rank += 1
    d[B[i]] = rank
for i in range(N):
    B[i] = d[A[i]]
print(*B)
