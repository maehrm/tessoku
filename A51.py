stack = []

Q = int(input())
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, book_name = query.split()
        stack.append(book_name)
    elif query[0] == "2":
        print(stack[-1])
    else:
        del stack[-1]
