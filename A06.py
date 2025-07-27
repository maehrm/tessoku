N, Q = map(int, input().split())
A = list(map(int, input().split()))
acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + A[i]
for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l - 1])
