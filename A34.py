N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = max(A)
grundy = [0] * (MAX_A + 1)
for i in range(MAX_A + 1):
    s = set()
    if i >= X:
        s.add(grundy[i - X])
    if i >= Y:
        s.add(grundy[i - Y])
    m = 0                       # mex値
    while m in s:
        m += 1
    grundy[i] = m

nim_sum = 0
for i in range(N):
    nim_sum ^= grundy[A[i]]

print("First") if nim_sum != 0 else print("Second")

# import sys

# sys.setrecursionlimit(10**6)

# def calc_grundy(n):
#     if n in grundy:
#         grundy[n]
#     if n < X:
#         grundy[n] = 0
#         return 0
#     s = set()
#     if n >= X:
#         s.add(calc_grundy(n - X))
#     if n >= Y:
#         s.add(calc_grundy(n - Y))
#     m = 0
#     while m in s:
#         m += 1
#     grundy[n] = m
#     return m


# N, X, Y = map(int,input().split())
# A = list(map(int,input().split()))

# grundy = {}
# nim_sum = 0
# for i in range(N):
#     nim_sum ^= calc_grundy(A[i])

# print("First") if nim_sum != 0 else print("Second")
