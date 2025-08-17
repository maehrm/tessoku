# B39 - Taro's Job https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dl
import heapq

N, D = map(int, input().split())
jobs = [[] for _ in range(D + 1)]
for _ in range(N):
    x, y = map(int, input().split())
    jobs[x].append(y)           # x日以降にできる仕事をまとめる

hq = []
ans = 0
for day in range(1, D + 1):
    for j in jobs[day]:         # day日目にできる仕事をheapに追加し、
        heapq.heappush(hq, -j)
    if hq:  # 最初、このチェックがなくていくつかのテストケースでREに。
        ans += -heapq.heappop(hq) # 取り出す。
    
print(ans)
