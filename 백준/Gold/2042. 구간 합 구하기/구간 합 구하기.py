import sys
N, M, K = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0]*3000000

def construct_tree(s, e, k):
    if s == e:
        tree[k] = nums[s]
        return nums[s]
    else:
        mid = (s+e)//2
        tree[k] = construct_tree(s, mid, 2*k)+construct_tree(mid+1, e, 2*k+1)
        return tree[k]

def update(s, e, idx, val, node):
    if idx < s or idx > e:
        return
    
    tree[node] += val
    if s != e:
        mid = (s+e)//2
        update(s, mid, idx, val, 2*node)
        update(mid+1, e, idx, val, 2*node+1)


def interval(s, e, l, r, node):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e)//2
    return interval(s, mid, l, r, 2*node) + interval(mid+1, e, l, r, 2*node+1)

construct_tree(0, N-1, 1)

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        idx = b-1
        d = c - nums[b-1]
        nums[b-1] = c
        update(0, N-1, idx, d, 1)
    else:
        print(interval(0, N-1, b-1, c-1, 1))

