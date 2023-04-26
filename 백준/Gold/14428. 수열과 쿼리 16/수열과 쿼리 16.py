from sys import stdin
import math
maxnum = [1000000001, 1000000001]

def lmin(a, b):
    return min(a, b, key=lambda x: (x[1], x[0]))

def construct_tree(s, e, k):
    if s == e:
        tree[k] = A[s]
        return tree[k]
    else:
        mid = (s+e)//2
        left = construct_tree(s, mid, 2*k)
        right = construct_tree(mid+1, e, 2*k+1)
        tree[k] = lmin(left, right)
        return tree[k]

def update(s, e, idx, val, node):
    if idx < s or idx > e:
        return maxnum
    if s == e:
        tree[node] = val
        return
    if s != e:
        mid = (s+e)//2
        update(s, mid, idx, val, 2*node)
        update(mid+1, e, idx, val, 2*node+1)
        tree[node] = lmin(tree[node*2], tree[node*2+1])


def interval(s, e, l, r, node):
    if l > e or r < s:
        return maxnum
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e)//2
    return lmin(interval(s, mid, l, r, 2*node), interval(mid+1, e, l, r, 2*node+1))


N = int(stdin.readline())
A = list(map(list, enumerate(map(int, stdin.readline().split()), 1)))
M = int(stdin.readline())
queries = [list(map(int, stdin.readline().split())) for _ in range(M)]
tree = [0 for _ in range(1<<(math.ceil(math.log2(N))+1))]
construct_tree(0, N-1, 1)
for q in queries:
    if q[0] == 1:
        A[q[1]-1][1] = q[2]
        update(0, N-1, q[1]-1, A[q[1]-1], 1)
    else:
        print(interval(0, N-1, q[1]-1, q[2]-1, 1)[0])
