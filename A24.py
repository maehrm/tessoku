import bisect

N = int(input())
A = list(map(int, input().split()))
ans = []
for a in A:
    i = bisect.bisect_left(ans, a)
    if i == len(ans):
        ans.append(a)
    else:
        ans[i] = a
print(len(ans))
