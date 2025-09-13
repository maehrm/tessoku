# C11 - Election https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fi
N, K = map(int, input().split())
A = list(map(int, input().split()))

low, hight = 0, max(A)
eps = 1e-6                      # 1e-9:TLE, 1e-5:WAが1つ
while hight - low >= eps:
    mid = (low + hight) / 2
    s = sum(int(a / mid) for a in A)
    if s >= K:
        low = mid
    else:
        hight = mid

ans = [int(a / low) for a in A]
print(*ans)
