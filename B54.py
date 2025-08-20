# B54 - Counting Same Values https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ea
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
count = {}
for i in range(N):
    if A[i] not in count:
        count[A[i]] = 0
    count[A[i]] += 1
ans = 0
for _, v in count.items():
    ans += v * (v - 1) // 2
print(ans)
