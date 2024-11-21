from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
N, R, Q = map(int, sys.stdin.readline().split())
subnodes = [1]*(N+1)
tree = defaultdict(set)
for _ in range(1, N):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].add(v)
    tree[v].add(u)
sub = [int(sys.stdin.readline()) for _ in range(Q)]
visit = [0]*(N+1)

def remove_parent(parent, node):
    if parent in tree[node]:
        tree[node].remove(parent)
    for child in tree[node]:
        remove_parent(node, child)

remove_parent(-1, R)

def count_node(node):
    if visit[node]:
        return subnodes[node]
    visit[node] = 1
    for child in tree[node]:
        subnodes[node] += count_node(child)
    return subnodes[node]

for s in sub:
    sys.stdout.write(f'{count_node(s)}\n')
