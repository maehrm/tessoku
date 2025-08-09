# A76 - River Crossing https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bx
import bisect

MOD = 1_000_000_007
N, W, L, R = map(int, input().split())
A = [0] + list(map(int, input().split())) + [W]
dp = [0] * (N + 2)  # 足場iにたどり着く方法の総数
dp[0] = 1  # 西岸は1通り
dp_sum = [0] * (N + 3)  # dpの累積和
dp_sum[1] = 1
for i in range(1, N + 2):
    left = bisect.bisect_left(A, A[i] - R, hi=i)
    right = bisect.bisect_right(A, A[i] - L, hi=i)
    dp[i] = (dp_sum[right] - dp_sum[left]) % MOD
    dp_sum[i + 1] = (dp_sum[i] + dp[i]) % MOD

print(dp[-1])

# (2) 若干改善したつもりが焼け石に水
# import bisect

# MOD = 1_000_000_007
# N, W, L, R = map(int, input().split())
# A = [0] + list(map(int, input().split())) + [W]
# dp = [0] * (N + 2)
# dp[0] = 1
# for i in range(1, N + 2):
#     left = bisect.bisect_left(A, A[i] - R, hi=i)
#     right = bisect.bisect_right(A, A[i] - L, hi=i)
#     for j in range(left, right):
#         dp[i] = (dp[i] + dp[j]) % MOD
# print(dp[-1])

# (1) 当然、TLE
# MOD =  1_000_000_007
# N, W, L, R = map(int, input().split())
# A = [0] + list(map(int, input().split())) + [W]
# dp = [0] * (N + 2)
# dp[0] = 1
# for i in range(1, N + 2):
#     for j in range(i):
#         dist = A[i] - A[j]
#         if dist >= L and dist <= R:
#             dp[i] = (dp[i] + dp[j]) % MOD
# print(dp[-1])
