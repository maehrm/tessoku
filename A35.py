N = int(input())
A = list(map(int, input().split()))

currentA = A
for level in range(N - 1, 0, -1):
    tmp = []
    is_taro_turn = True if level % 2 == 1 else False
    for i in range(level):
        if is_taro_turn:
            tmp.append(max(currentA[i], currentA[i + 1]))
        else:
            tmp.append(min(currentA[i], currentA[i + 1]))
    currentA = tmp

print(currentA[0])
