# B32 - Game 5 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_de
N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (N + 1)
for i in range(1, N + 1):
    for j in range(K):
        if i >= a[j]:  # i個石がある状態。a[j]個以上なければ取れない。
            if not dp[i - a[j]]:  # a[j]個取った状態がFalse(相手が負け)なら自分(First)が勝てる。
                dp[i] = True

if dp[-1]:
    print("First")
else:
    print("Second")
