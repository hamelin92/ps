import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(i, parent):
    for e in tree[i]:
        if not visit[e[0]]:
            visit[e[0]] = 1
            dfs(e[0], i)
        if e[0] != parent:
            nw = max(weights[e[0]]) + e[1]
            if weights[i][0] < nw:
                weights[i][0] = nw
                weights[i].sort()


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append([b, w])
    tree[b].append([a, w])
weights = [[0, 0] for _ in range(n+1)]
visit = [0]*(n+1)
visit[1] = 1
dfs(1, 0)
print(max(sum(weights[i]) for i in range(1, n+1)))
