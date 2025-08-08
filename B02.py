factors = [i for i in range(1, 101) if 100 % i == 0 ]
A, B = map(int, input().split())
for n in factors:
    if A <= n and n <= B:
        print("Yes")
        break
else:
    print("No")
