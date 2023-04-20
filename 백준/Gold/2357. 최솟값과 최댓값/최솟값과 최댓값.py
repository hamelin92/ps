import sys


N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
tree = [False]*300000

def construct_tree(s, e, k):
    if s == e:
        tree[k] = [nums[s], nums[e]]
        return [nums[s], nums[e]]
    else:
        mid = (s+e)//2
        left = construct_tree(s, mid, 2*k)
        right = construct_tree(mid+1, e, 2*k+1)
        tree[k] = [
            min(left[0], right[0]),
            max(left[1], right[1]),
            ]
        return tree[k]


def interval(s, e, l, r, node):
    if l > e or r < s:
        return [1000000001, 0]
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e)//2
    left = interval(s, mid, l, r, 2*node)
    right = interval(mid+1, e, l, r, 2*node+1)
    return [
        min(left[0], right[0]),
        max(left[1], right[1])
        ]

construct_tree(0, N-1, 1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(*interval(0, N-1, a-1, b-1, 1))


