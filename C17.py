# C17 - Strange Data Structure? https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fo
from collections import deque

front = deque()
back = deque()

Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == "A":         # 末尾に追加
        X = query[1]
        back.append(X)
    elif query[0] == "B":       # 中央に追加
        X = query[1]
        front.append(X)
    elif query[0] == "C":       # 先頭を削除
        front.popleft()
    else:                       # 先頭の氏名を答える
        print(front[0])
    # バランス調整
    if len(front) < len(back):
        front.append(back.popleft())
    if len(front) > len(back) + 1:
        back.appendleft(front.pop())

