def get_prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime


lst = get_prime_list(300000)

Q = int(input())
for _ in range(Q):
    X = int(input())
    print("Yes") if lst[X] else print("No")
