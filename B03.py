def binary_search(l, yen):
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == yen:
            return True
        elif A[mid] < yen:
            l = mid + 1
        else:
            r = mid - 1
    return False


N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = False
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if A[i] + A[j] >= 1000:
            break
        if binary_search(j + 1, 1000 - (A[i] + A[j])):
            ans = True
            break
    if ans:
        break
print("Yes") if ans else print("No")
