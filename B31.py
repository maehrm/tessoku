# B31 - Divisors Hard https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dd
N = int(input())

ans = N // 3
ans += N // 5
ans += N // 7
ans -= N // (3 * 5)
ans -= N // (3 * 7)
ans -= N // (5 * 7)
ans += N // (3 * 5 * 7)

print(ans)
