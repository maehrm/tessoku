N = int(input())
ans = [0] * 10
for i in range(10):
    if N & (1 << 10 - (i + 1)):
        ans[i] = 1
print(*ans, sep="")
