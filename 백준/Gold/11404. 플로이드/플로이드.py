import sys
from collections import deque


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if not graph[a][b]:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)
for s in range(1, n+1):
    costs = [0]*(1+n)
    que = deque()
    for e in range(1, n+1):
        if graph[s][e]:
            que.append(e)
            costs[e] = graph[s][e]
    while que:
        q = que.popleft()
        for e in range(1, n+1):
            if e != s and graph[q][e] and (costs[e] > costs[q] + graph[q][e] or not costs[e]):
                costs[e] = costs[q] + graph[q][e]
                que.append(e)
    print(*costs[1:])