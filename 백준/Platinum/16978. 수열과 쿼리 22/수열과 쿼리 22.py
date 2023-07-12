import sys
import math
from collections import defaultdict
input = sys.stdin.readline


def construct(s, e, v):
    if s > e:
        return 0
    if s == e:
        tree[v] = A[s]
        return tree[v]
    mid = (s+e)//2
    l = construct(s, mid, 2*v)
    r = construct(mid+1, e, 2*v+1)
    tree[v] = l+r
    return tree[v]

def update(s, e, i, k, v):
    if s > i or e < i or s > e:
        return tree[v]
    if s <= i and i <= e:
        tree[v] += k
        if s == e:
            return tree[v]
    mid = (s+e)//2
    update(s, mid, i, k, 2*v)
    update(mid+1, e, i, k, 2*v+1)

def get_value(s, e, i, j, v):
    if s > j or e < i:
        return 0
    if i <= s and e <= j:
        return tree[v]
    mid = (s+e)//2
    return get_value(s, mid, i, j, 2*v) + get_value(mid+1, e, i, j, 2*v+1)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
tree = [0 for _ in range(1<<(math.ceil(math.log2(N))+1))]
construct(0, N-1, 1)
q1 = []
q2 = defaultdict(list)
res = []
for i in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:
        q[1] -= 1
        q1.append(q[1:])
    else:
        q[2] -= 1
        q[3] -= 1
        q2[q[1]].append([i]+q[2:])
for q in q2[0]:
    res.append([q[0], sum(A[q[1]:q[2]+1])])
for k in range(len(q1)):
    update(0, N-1, q1[k][0], q1[k][1]-A[q1[k][0]], 1)
    A[q1[k][0]] = q1[k][1]
    for q in q2[k+1]:
        res.append([q[0], get_value(0, N-1, q[1], q[2], 1)])
res.sort(key=lambda x: x[0])
for i in range(len(res)):
    print(res[i][1])