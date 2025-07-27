from atcoder.segtree import SegTree

N = int(input())
A = list(map(int, input().split()))
st = SegTree(max, -1, A)
D = int(input())
for _ in range(D):
    L, R = map(lambda x: int(x) - 1, input().split())
    print(max(st.prod(0, L), st.prod(R + 1, N)))
