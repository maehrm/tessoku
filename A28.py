N = int(input())
val = 0
for _ in range(N):
    t, a = input().split()
    if t == "+":
        val += int(a)
    elif t == "-":
        val -= int(a)
    elif t == "*":
        val *= int(a)
    if val < 0:
        val += 10000
    val %= 10000
    print(val)
