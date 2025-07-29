import heapq

hq = []

Q = int(input())
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, yen = map(int, query.split())
        heapq.heappush(hq, yen)
    elif query[0] == "2":
        print(hq[0])
    else:
        heapq.heappop(hq)
