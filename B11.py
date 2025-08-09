def binary_search(x):
    ok, ng = -1, N
    while ng - ok != 1:
        mid = (ng + ok) // 2
        if A[mid] >= x:
            ng = mid
        else:
            ok = mid
    return ok


N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    X = int(input())
    print(binary_search(X) + 1)
