# B51 - Bracket https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dx
S = input()
stack = []
for i in range(len(S)):
    if S[i] == "(":
        stack.append(i)
    elif S[i] == ")":
        if stack:
            k = stack.pop()
            print(k + 1, i + 1)
