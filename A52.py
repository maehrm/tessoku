from collections import deque

que = deque()
Q = int(input())
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, name = query.split()
        que.append(name)
    elif query[0] == "2":
        print(que[0])
    else:
        que.popleft()
