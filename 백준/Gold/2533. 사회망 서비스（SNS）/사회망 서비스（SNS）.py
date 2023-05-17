import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(v):
    for nv in T[v]:
        if not visit[nv]:
            visit[nv] = 1
            dfs(nv)
            dp[v][0] += dp[nv][1]
            dp[v][1] += min(dp[nv][0], dp[nv][1])


N = int(input())
T = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    T[u].append(v)
    T[v].append(u)
dp = [[0, 1] for _ in range(N+1)]
visit = [0]*(N+1)
visit[1] = 1
dfs(1)
print(min(dp[1]))