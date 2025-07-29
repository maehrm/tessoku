import bisect

cards = []
Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        bisect.insort(cards, x)
    elif t == 2:
        i = bisect.bisect_left(cards, x)
        cards.pop(i)
    else:
        i = bisect.bisect_left(cards, x)
        if i < len(cards):
            print(cards[i])
        else:
            print(-1)
