import sys
import math
input = sys.stdin.readline


def update(s, e, idx, val, node):
    if idx < s or idx > e:
        return
    
    tree[node] += val
    if s != e:
        mid = (s+e)//2
        update(s, mid, idx, val, 2*node)
        update(mid+1, e, idx, val, 2*node+1)


def sum_n(s, e, l, r, node):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e)//2
    return sum_n(s, mid, l, r, 2*node) + sum_n(mid+1, e, l, r, 2*node + 1)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
h = [-1]*1000001
arr = [-1]*(N+1)
for i in range(N):
    h[A[i]] = i
for i in range(N):
    arr[i] = h[B[i]]
tree = [0 for _ in range(1<<(math.ceil(math.log2(N))+1))]
ans = 0
for i in range(N):
    j = arr[i]
    ans += sum_n(0, N-1, j+1, N-1, 1)
    update(0, N-1, j, 1, 1)
print(ans)
