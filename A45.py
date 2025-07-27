N, C = input().split()
N = int(N)
A = list(input())
d = {"W": 0, "R": 1, "B": 2}
for i in range(N):
    A[i] = d[A[i]]

if sum(A) % 3 == d[C]:
    print("Yes")
else:
    print("No")
