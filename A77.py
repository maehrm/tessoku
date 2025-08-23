# A77 - Yokan Party（★4） https://atcoder.jp/contests/tessoku-book/tasks/typical90_a
def binary_search():
    ok, ng = 0, L + 1
    while ng - ok != 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def check(x):
    last_cut, piece_count = 0, 0  # 最後に切った場所, 羊羹の個数
    for a in A:
        if a - last_cut >= x:  # x(cm)以上になったら切る。
            last_cut = a
            piece_count += 1
    if L - last_cut >= x:  # 最後の長さがx(cm)以上なら切る。
        piece_count += 1
    return piece_count >= K + 1  # 羊羹がK + 1個以上なら、x(cm)で切り分けられる。


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
print(binary_search())
