from collections import deque


def bfs(src, dst, operations):
    if src == dst:
        return 0
    visited = {src}
    que = deque()
    que.append((src, 0))
    while que:
        cur, cnt = que.popleft()
        for op in operations:
            nxt = cur ^ op
            if nxt == dst:
                return cnt + 1
            if nxt not in visited:
                visited.add(nxt)
                que.append((nxt, cnt + 1))
    return -1


N, M = map(int, input().split())
A = list(map(int, input().split()))
src = int("".join(map(str, A)), 2)  # 初期状態
dst = (1 << N) - 1  # 最終状態

operations = []
for _ in range(M):
    x, y, z = map(int, input().split())
    mask = (1 << (N - x)) | (1 << (N - y)) | (1 << (N - z))
    operations.append(mask)

print(bfs(src, dst, operations))

# 全探索 => 当然TLE
# 
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# src = int("".join(map(str, A)), 2) # 初期状態
# dst = (1 << N) - 1                 # 最終状態

# operations = []
# for _ in range(M):
#     x, y, z = map(int, input().split())
#     mask = (1 << (N - x)) | (1 << (N - y)) | (1 << (N - z))
#     operations.append(mask)

# ans = float("inf")
# for pat in range(1 << M):       # 全探索
#     tmp = src
#     cnt = 0
#     for i in range(M):
#         if (pat >> i) & 1:
#             tmp ^= operations[i]
#             cnt += 1
#             if cnt > ans:
#                 break
#     if tmp == dst:
#         ans = min(ans, cnt)

# print(ans) if ans != float('inf') else print(-1)
