m = {}
Q = int(input())
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, name, point = query.split()
        m[name] = int(point)
    elif query[0] == "2":
        _, name = query.split()
        print(m[name])
