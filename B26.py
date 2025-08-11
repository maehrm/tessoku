# B26 - Output Prime Numbers https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cy
def get_prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


N = int(input())
ans = get_prime_list(N + 1)
for i in range(2, N + 1):
    if ans[i]:
        print(i)
