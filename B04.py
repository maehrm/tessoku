bin = input()
val = 1
ans = 0
for i in range(len(bin) - 1, -1, -1):
    ans += int(bin[i]) * val
    val <<= 1
print(ans)

# これでは味気ないので。
# print(int(input(), 2))
