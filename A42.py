N, K = map(int, input().split())

A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        cnt = 0
        for i in range(N):
            if a <= A[i] and A[i] <= a + K and b <= B[i] and B[i] <= b + K:
                cnt += 1
        ans = max(ans, cnt)
        
print(ans)
