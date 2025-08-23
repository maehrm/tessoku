# C03 - Stock Queries https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fa
D = int(input())
stock_price = [0] * D
stock_price[0] = int(input())
for i in range(D - 1):
    stock_price[i + 1] = stock_price[i] + int(input())
Q = int(input())
for _ in range(Q):
    s, t = map(lambda x: int(x) - 1, input().split())
    if stock_price[s] > stock_price[t]:
        print(s + 1)
    elif stock_price[s] < stock_price[t]:
        print(t + 1)
    else:
        print("Same")
