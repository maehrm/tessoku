# B14 - Another Subset Sum https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm
def binary_search(k):
    l, r = 0, len(S2) - 1
    while l <= r:
        mid = (l + r) // 2
        if S2[mid] == k:
            return True
        elif S2[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return False


N, K = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[: N // 2]  # 前半
A2 = A[N // 2 :]  # 後半

S1 = []  # 前半の和の組合せ
for mask in range(1 << len(A1)):
    sum = 0
    for i in range(len(A1)):
        if (mask >> i) & 1:
            sum += A1[i]
    S1.append(sum)

S2 = []  # 後半の和の組合せ
for mask in range(1 << len(A2)):
    sum = 0
    for i in range(len(A2)):
        if (mask >> i) & 1:
            sum += A2[i]
    S2.append(sum)

S2.sort()
for i in range(len(S1)):
    if binary_search(K - S1[i]):
        print("Yes")
        break
else:
    print("No")
