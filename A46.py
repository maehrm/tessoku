def solv(N):
    visited = [False] * N
    current_city = 0
    visited[current_city] = True
    route = [current_city]
    while len(route) < N:
        min_dist = float("inf")
        nxt_city = -1
        for i in range(N):
            if visited[i]:
                continue
            dist = get_distance(current_city, i)
            if min_dist > dist:
                min_dist = dist
                nxt_city = i
        visited[nxt_city] = True
        route.append(nxt_city)
        current_city = nxt_city
    route.append(0)
    return route


def get_distance(cur, nxt):
    cur_x, cur_y = XY[cur]
    nxt_x, nxt_y = XY[nxt]
    return (nxt_x - cur_x) ** 2 + (nxt_y - cur_y) ** 2


def two_opt(tour):  # 2-opt
    improved = True
    while improved:
        improved = False
        for i in range(1, N - 1):
            for j in range(i + 1, N):
                a, b = tour[i - 1], tour[i]
                c, d = tour[j], tour[j + 1]
                old_dist = get_distance(a, b) + get_distance(c, d)
                new_dist = get_distance(a, c) + get_distance(b, d)
                if new_dist < old_dist:
                    tour[i : j + 1] = tour[i: j + 1][::-1]
                    improved = True
        if improved:
            break
    return tour


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = solv(N)
ans = two_opt(ans)
for a in ans:
    print(a + 1)
