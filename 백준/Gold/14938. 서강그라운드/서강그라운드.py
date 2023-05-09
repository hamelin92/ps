def delete_min(v_set, arr):
    min_el = -1
    for i in v_set:
        if min_el < 0:
            min_el = i
            continue
        if arr[i] < arr[min_el]:
            min_el = i
    return min_el


def djikstra(G: list, V: set, start, n: int):
    global inf
    costs = [inf]*(n+1)
    S = {start}
    costs[start] = 0
    for u in V-S:
        if G[start][u] < inf:
            costs[u] = G[start][u]
    while len(S) < n:
        u = delete_min(V-S, costs)
        S = S|{u}
        for j in range(1, n+1):
            if G[u][j] < inf and set([j]).issubset(V-S) and costs[u] + G[u][j] < costs[j]:
                costs[j] = costs[u] + G[u][j]
    return costs


n, m, r = map(int, input().split())
t = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(r)]
inf = 1000001
graph = [[inf]*(n+1) for _ in range(n+1)]
for e in edges:
    graph[e[0]][e[1]] = min(graph[e[0]][e[1]], e[2])
    graph[e[1]][e[0]] = min(graph[e[1]][e[0]], e[2])
max_items = 0
costs = [inf]*(n+1)
nodes = set(range(1, n+1))
for start in range(1, n+1):
    costs = djikstra(graph, nodes, start, n)
    cnt = 0
    for i in range(1, n+1):
        if costs[i] <= m:
            cnt += t[i-1]
    if max_items < cnt:
        max_items = cnt
print(max_items)