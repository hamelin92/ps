import sys
import math
input = sys.stdin.readline

def update(s, e, i, j, k, v):
    if s > j or e < i or s > e:
        return tree[v]
    if i <= s and e <= j:
        tree[v] += k
        return tree[v]
    mid = (s+e)//2
    update(s, mid, i, j, k, 2*v)
    update(mid+1, e, i, j, k, 2*v+1)

def get_value(s, e, x, v):
    global ans
    if x < s or x > e:
        return 0
    if s <= x and x <= e:
        ans += tree[v]
        if s == e:
            return 0
        mid = (s+e)//2
        get_value(s, mid, x, 2*v)
        get_value(mid+1, e, x, 2*v+1)
        return tree[v]


N = int(input())
A = list(map(int, input().split()))
M = int(input())
tree = [0 for _ in range(1<<(math.ceil(math.log2(N))+1))]
for _ in range(M):
    q = list(map(int, input().split()))
    q[1] -= 1
    if q[0] == 1:
        q[2] -= 1
        update(0, N-1, q[1], q[2], q[3], 1)
    else:
        ans = 0
        get_value(0, N-1, q[1], 1)
        print(A[q[1]]+ans)