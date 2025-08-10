# B28 - Fibonacci Easy (mod 1000000007) https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ap
import sys

sys.setrecursionlimit(10**6)


def mat_mul(a, b):
    return [[(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
             (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD,],
            [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
             (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD,]]


def pow(a, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n % 2 == 0:
        return pow(mat_mul(a, a), n // 2)
    else:
        return mat_mul(a, pow(mat_mul(a, a), n // 2))


def fibonacci(n):
    a = [[1, 1], [1, 0]]
    a = pow(a, n)
    return a[0][1]


MOD = 10**9 + 7
N = int(input())
print(fibonacci(N))

# 参考
# 行列を使ってフィボナッチ数列 - Mae向きなブログ https://maehrm.hatenablog.com/entry/2015/05/05/084607
