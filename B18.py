# B18 - Subset Sum with Restoration https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq
N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j] : i番目のカードを使って、合計jが作れるか
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(S + 1):
        if dp[i][j]:
            # カードA[i]を使わない
            dp[i + 1][j] = True
            # カードA[i]を使う
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] = True

if not dp[-1][-1]:
    print(-1)
else:
    ans = []
    i, j = N, S
    while i > 0:
        if dp[i - 1][j]:
            i -= 1
        elif j - A[i - 1] >= 0 and dp[i - 1][j - A[i - 1]]:
            ans.append(i)
            j -= A[i - 1]
            i -= 1
    print(len(ans))
    print(*ans[::-1])
    
# B14 - Another Subset Sum https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm
# と類似問題。
#
# B14 は、K <= 10**8 ということで、DPはメモリ的に無理。N <= 30 なので、全列挙も無理。
# ということで、配列を半分に分けて全列挙
#
# 本問は、N <= 60 で配列を半分に分けても全列挙は無理だが、S <= 10**4 なのでDPを選択
