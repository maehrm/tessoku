N = int(input())
A = list(map(int, input().split()))
acc = [0] * (N + 1)
for i in range(1, N + 1):
    acc[i] = acc[i - 1] + A[i - 1]
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    atari = acc[R] - acc[L - 1]
    len = R - (L - 1)
    if 2 * atari > len:
        print("win")
    elif 2 * atari == len:
        print("draw")
    else:
        print("lose")
