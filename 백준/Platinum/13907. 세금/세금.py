import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 100000000

def djaikstra(start: int, end: int):
    global INF
    q = []
    ans = INF
    dj[start][0] = 0
    heappush(q, [0, start, 0])
    while q:
        cost, node, cnt = heappop(q)
        flag = False
        for i in range(cnt):
            if dj[node][i] < cost:
                flag = True
                break
        if flag or dj[node][cnt] < cost:
            continue
        if node == end:
            ans = min(ans, dj[node][cnt])
            continue
        for e in G[node]:
            nv = e[0]
            nw = e[1] + cost
            if cnt + 1 < N and nw < dj[nv][cnt+1]:
                dj[nv][cnt+1] = nw
                heappush(q, [nw, nv, cnt+1])
    return min(dj[D])

N, M, K = map(int, input().split())
S, D = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b, w])
    G[b].append([a, w])
dj = [[INF]*(N+1) for _ in range(N+1)]
taxes = [int(input()) for _ in range(K)]
print(djaikstra(S, D))
for t in taxes:
    for j in range(1, N+1):
        if dj[D][j] != INF:
            dj[D][j] = dj[D][j] + t*j
    print(min(dj[D]))

