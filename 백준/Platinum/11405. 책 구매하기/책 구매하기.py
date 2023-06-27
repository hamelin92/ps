import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split()) # N: 사람 수, M: 서점 수
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
max_v = N+M+2
inf = 100000000
# s: max_v-2 : 소스 정점 번호, e = max_v-1 : 싱크 정점 번호
s, e = max_v-2, max_v-1
c = [[0] * max_v for _ in range(max_v)] # 간선의 용량
d = [[0] * max_v for _ in range(max_v)] # 비용
f = [[0] * max_v for _ in range(max_v)] # 흐르는 중인 유량
g = [[] for i in range(N+M+2)]

def add_edge(start, end, cap, dis):
    g[start].append(end)
    g[end].append(start)
    c[start][end] = cap
    c[end][start] = 0
    d[start][end] = dis
    d[end][start] = -dis

for i in range(M, M+N):
    # 사람 -> 싱크
    add_edge(i, e, A[i-M], 0)

for i in range(M):
    # 소스 -> 서점
    add_edge(s, i, B[i], 0)

for i in range(M):
    cost = list(map(int, input().rstrip().split()))
    for j in range(M, M+N):
        # 서점 -> 사람
        add_edge(i, j, inf, cost[j-M])

res = 0
s, e = max_v -2, max_v-1
while True:
    prv = [-1] * max_v
    dist = [inf] * max_v
    inque = [0] * max_v
    que = deque([s])
    dist[s] = 0
    inque[s] = 1
    while que:
        cur = que.popleft()
        inque[cur] = 0
        for nxt in g[cur]:
            if c[cur][nxt] - f[cur][nxt] > 0 and dist[nxt] > dist[cur] + d[cur][nxt]:
                dist[nxt] = dist[cur] + d[cur][nxt]
                prv[nxt] = cur
                if not inque[nxt]:
                    que.append(nxt)
                    inque[nxt] = 1
    if prv[e] == -1:
        break
    flow = 100000000
    idx = e
    while idx != s:
        flow = min(flow, c[prv[idx]][idx] - f[prv[idx]][idx])
        idx = prv[idx]
    idx = e
    while idx != s:
        res += flow*d[prv[idx]][idx]
        f[prv[idx]][idx] += flow
        f[idx][prv[idx]] -= flow
        idx = prv[idx]
print(res)

