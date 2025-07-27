def check(m):
    sum = 0
    for i in range(N):
        sum += m // A[i]
    if sum >= K:
        return True
    else:
        return False


N, K = map(int, input().split())
A = list(map(int, input().split()))

ng, ok = 0, 10**9
while ng + 1 != ok:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
