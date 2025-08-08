def count_black(mat):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j] == "#":
                cnt += 1
    return cnt


H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

ans = 0
for row_mask in range(1 << H):  # 1<=H<=10 なので全探索
    copy_c = [c[i][::] for i in range(H)]
    row_cnt = 0  # 何行選んだのかカウントする。
    for i in range(H):
        if (row_mask >> i) & 1:
            row_cnt += 1
            for j in range(W):
                copy_c[i][j] = "#"
            if row_cnt >= K:
                ans = max(ans, count_black(copy_c))
                break
    col_cnt = K - row_cnt
    if col_cnt > 0:             # 列方向で選ぶ余地があれば、黒が少ない列を選択する
        b_cnt = 0
        col_black_counts = []
        for j in range(W):
            for i in range(H):
                if copy_c[i][j] == "#":
                    b_cnt += 1
            col_black_counts.append((b_cnt, j))
        col_black_counts.sort()
        for i in range(col_cnt):
            for j in range(H):
                copy_c[i][j] = "#"
            ans = max(ans, count_black(copy_c))
print(ans)
