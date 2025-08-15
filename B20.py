# B20 - Edit Distance https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs
# レーベンシュタイン距離(編集距離)
def levenshtein_distance(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = i
    for j in range(len(t) + 1):
        dp[0][j] = j
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,     # 文字の削除
                               dp[i - 1][j - 1] + 1, # 文字の置換
                               dp[i][j - 1] + 1     # 文字の挿入
                               )
    return dp[-1][-1]

S = input()
T = input()
print(levenshtein_distance(S, T))

# 編集距離 - Mae向きなブログ https://maehrm.hatenablog.com/entry/2023/03/04/105124
# レーベンシュタイン距離 - Mae向きなブログ https://maehrm.hatenablog.com/entry/2017/02/26/174628
# 平成26年度秋季基本情報午後問8 - Mae向きなブログ https://maehrm.hatenablog.com/entry/2019/02/09/222025
