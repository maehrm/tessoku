def bsearch(X, A):
    l, r = 0, len(A)
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == X:
            return mid + 1
        elif A[mid] < X:
            l = mid + 1
        else:
            r = mid - 1


N, X = map(int, input().split())
A = list(map(int, input().split()))
print(bsearch(X, A))
