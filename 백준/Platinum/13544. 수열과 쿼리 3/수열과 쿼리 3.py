import sys
import math
from bisect import bisect_right

def merge(left: list, right: list):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == len(left):
        res.extend(right[j:])
    elif j == len(right):
        res.extend(left[i:])
    return res


def init(l: int, r: int, v: int):
    if l == r:
        tree[v].append(A[l])
        return
    mid = (l+r)//2
    init(l, mid, 2*v)
    init(mid+1, r, 2*v+1)
    tree[v] = merge(tree[2*v], tree[2*v+1])


def query(K: int, L: int, R: int, l: int, r: int, v: int):

    if r < L or R < l:
        return 0
    if L <= l and r <= R:
        return len(tree[v]) - bisect_right(tree[v], K)
    mid = (l+r)//2
    return query(K, L, R, l, mid, 2*v) + query(K, L, R, mid+1, r, 2*v+1)


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
tree = [[] for _ in range(1<<(math.ceil(math.log2(N))+1))]
init(0, N-1, 1)
last_ans = 0
for _ in range(M):
    a, b, c = map(lambda x: int(x)^last_ans, input().split())
    last_ans = query(c, a, b, 1, N, 1)
    print(last_ans)
