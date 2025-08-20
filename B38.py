# B38 - Heights of Grass https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dk
N = int(input())
S = input()

# 左から
h = [1] * N
for i in range(N - 1):
    if S[i] == "A":
        h[i + 1] = h[i] + 1

# 右から
for i in range(N - 2, -1, -1):
    if S[i] == "B":
        h[i] = max(h[i], h[i + 1] + 1)

print(sum(h))

# N = int(input())
# S = input()

# # 左から
# L = [1] * N
# for i in range(N - 1):
#     if S[i] == "A":
#         L[i + 1] = L[i] + 1

# # 右から
# R = [1] * N
# for i in range(N - 2, -1, -1):
#     if S[i] == "B":
#         R[i] = R[i + 1] + 1

# ans = 0
# for i in range(N):
#     ans += max(L[i], R[i])
# print(ans)
