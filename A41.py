N = int(input())
S = input()
ans = False
for i in range(N - 2):
    if S[i] == "B" and S[i + 1] == "B" and S[i + 2] == "B":
        ans = True
    if S[i] == "R" and S[i + 1] == "R" and S[i + 2] == "R":
        ans = True
print("Yes") if ans else print("No")
