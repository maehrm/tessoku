# C08 - ALGO4 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ff
def check(a, b):
    ret = 0
    for i in range(4):
        if a[i] != b[i]:
            ret += 1
    return ret


N = int(input())
kuji = []
for _ in range(N):
    s, t = input().split()
    s = str(s).zfill(4)
    kuji.append((s, int(t)))

ans = []
for number in range(10000):
    number = str(number).zfill(4)
    for s, t in kuji:
        k = check(s, number)
        if t == 1 and k != 0:
            break
        if t == 2 and k != 1:
            break
        if t == 3 and k < 2:
            break
    else:
        ans.append(number)

if len(ans) == 1:
    print(ans[0])
else:
    print("Can't Solve")
