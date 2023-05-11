import sys
import heapq

inf = 300001
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
G = {i:[] for i in range(V+1)}
vset = [0]*(V+1)
for _ in range(E):
    s, e, t = map(int, input().split())
    G[s].append([t, e])
costs = [inf]*(V+1)
que = []
next_node, next_lth = K, 0
heapq.heappush(que, [0, K])
while que:
    q = heapq.heappop(que)
    if costs[q[1]] < q[0]:
        continue
    vset[q[1]] = 1
    costs[q[1]] = q[0]
    for e in G[q[1]]:
        if not vset[e[1]]:
            next_node = e[1]
            next_lth = q[0] + e[0]
            if costs[next_node] > next_lth:
                costs[next_node] = next_lth
                heapq.heappush(que, [next_lth, next_node])

for i in range(1, V+1):
    if costs[i] < inf:
        print(costs[i])
    else:
        print("INF")