import sys

sys.setrecursionlimit(1000000)

N, R, Q = map(int, sys.stdin.readline().split())
subnodes = [1]*(N+1)
tree = [[] for _ in range(N+1)]

for _ in range(1, N):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def count_node(parent, node):
    for child in tree[node]:
        if child != parent:
            subnodes[node] += count_node(node, child)
    return subnodes[node]

count_node(-1, R)

for _ in range(Q):
    sys.stdout.write(f'{subnodes[int(sys.stdin.readline())]}\n')