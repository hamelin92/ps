import sys
from collections import defaultdict
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N = int(input())
tree = defaultdict(list)
parents = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parents[1] = -1

def dfs(v):
    for t in tree[v]:
        if not parents[t]:
            parents[t] = v
            dfs(t)
    
dfs(1)
print(*parents[2:], sep="\n")