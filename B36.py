# B36 - Switching Lights https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_di
N, K = map(int, input().split())
S = input()
cnt = 0
for i in range(N):
    if S[i] == "1":
        cnt += 1
if K % 2 == cnt % 2:
    print("Yes")
else:
    print("No")
