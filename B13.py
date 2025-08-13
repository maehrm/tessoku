# B13 - Supermarket 2 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cl
# (2) 尺取法を用いる方法
N, K = map(int, input().split())
A = list(map(int, input().split()))
left, right = 0, 0
sum = 0
ans = 0
for left in range(N):
    while right < N and sum + A[right] <= K:
        sum += A[right]
        right += 1
    ans += right - left
    sum -= A[left]
print(ans)    

# # (1) 二分探索を用いる方法
# import bisect

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# acc = [0]
# for i in range(N):
#     acc.append(acc[-1] + A[i])
# ans = 0
# for i in range(N + 1):
#     j = bisect.bisect_right(acc, acc[i] + K)
#     ans += j - i - 1
# print(ans)
