N, Q = map(int, input().split())
A = [i for i in range(N + 1)]
is_reverse = False
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x, y = q
        if is_reverse:
            A[N - x + 1] = y
        else:
            A[x] = y
    elif q[0] == 2:
        if is_reverse:
            is_reverse = False
        else:
            is_reverse = True
    else:
        _, x = q
        if is_reverse:
            x = N - x + 1
        print(A[x])
