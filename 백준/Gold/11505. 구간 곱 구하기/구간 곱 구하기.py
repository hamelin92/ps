import sys
import math

N, M, K = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0 for _ in range(1<<(math.ceil(math.log2(N))+1))]
R = 1000000007

def construct_tree(s, e, k):
    global R
    if s == e:
        tree[k] = nums[s]
        return tree[k]
    else:
        mid = (s+e)//2
        left = construct_tree(s, mid, 2*k)
        right = construct_tree(mid+1, e, 2*k+1)
        tree[k] = (left*right)%R
        return tree[k]

def update(s, e, idx, t, node):
    global R
    if idx < s or idx > e:
        return tree[node]
    if s == e:
        tree[node] = t
        return t
    mid = (s+e)//2
    left = update(s, mid, idx, t, 2*node)
    right = update(mid+1, e, idx, t, 2*node+1)
    tree[node] = (left*right)%R
    return tree[node]

def interval(s, e, l, r, node):
    global R
    if l > e or r < s:
        return 1
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e)//2
    left = interval(s, mid, l, r, 2*node)
    right = interval(mid+1, e, l, r, 2*node+1)
    return (left*right)%R

construct_tree(0, N-1, 1)

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        idx = b-1
        update(0, N-1, idx, c, 1)
        nums[idx] = c
    else:
        print(interval(0, N-1, b-1, c-1, 1))

