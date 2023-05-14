import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 100000000

def djaikstra(graph: dict, start: int, end: int, n: int):
    if start == end:
        return 0
    q = []
    costs = [INF]*(n+1)
    heappush(q, [0, start])
    while q:
        cost, node = heappop(q)
        if costs[node] < cost:
            continue
        if node == end:
            break
        for nxt, nxtc in graph[node]:
            nxtc += cost
            if costs[nxt] > nxtc:
                costs[nxt] = nxtc
                heappush(q, [nxtc, nxt])
    return costs[end]

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, t = map(int, input().split())
    G[u].append([v, t])
    G[v].append([u, t])
v1, v2 = map(int, input().split())
res = []
for i in range(2):
    v1, v2 = v2, v1
    l = djaikstra(G, 1, v1, N) + djaikstra(G, v1, v2, N) + djaikstra(G, v2, N, N)
    res.append(l)
ans = min(res)
if ans < INF:
    print(ans)
else:
    print(-1)
