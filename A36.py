N, K = map(int, input().split())
D = 2 * N - 2
if D > K:
    print("No")
else:
    if (K - D) % 2 == 0:
        print("Yes")
    else:
        print("No")
