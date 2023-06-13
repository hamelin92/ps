import sys
import math

def init(node, s, e):
    if s == e:
        tree[node] = seq[s]
    else:
        init(node<<1, s, (s+e)//2)
        init(node<<1|1, (s+e)//2+1, e)
        tree[node] = tree[node<<1] + tree[node<<1|1]


def update_lazy(node, s, e):
    if lazy[node]:
        tree[node] += (e-s+1)*lazy[node]
        if s != e:
            lazy[node<<1] += lazy[node]
            lazy[node<<1|1] += lazy[node]
        lazy[node] = 0


def update_range(node, s, e, l, r, d):
    update_lazy(node, s, e)
    if l > e or r < s:
        return
    if l <= s and e <= r:
        tree[node] += (e-s+1)*d
        if s != e:
            lazy[node<<1] += d
            lazy[node<<1|1] += d
        return
    update_range(node<<1, s, (s+e)//2, l, r, d)
    update_range(node<<1|1, (s+e)//2+1, e, l, r, d)
    tree[node] = tree[node<<1] + tree[node<<1|1]


def query(node, s, e, l, r):
    update_lazy(node, s, e)
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]
    lsum = query(node<<1, s, (s+e)//2, l, r)
    rsum = query(node<<1|1, (s+e)//2+1, e, l, r)
    return lsum + rsum


input = sys.stdin.readline
N, M, K = map(int, input().split())
size = 1<<(math.ceil(math.log2(N)) + 1)
tree = [0 for _ in range(size)]
lazy = [0 for _ in range(size)]
seq = [int(input()) for _ in range(N)]
init(1, 0, N-1)
for i in range(M+K):
    w, *q = map(int, input().split())
    q[0] -= 1
    q[1] -= 1
    if w == 1:
        # range update
        update_range(1, 0, N-1, q[0], q[1], q[2])
    else:
        # sum
        print(query(1, 0, N-1, q[0], q[1]))
