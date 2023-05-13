import heapq
N, K = map(int, input().split())
inf = 200001
visit = [0]*200001
costs = [inf]*200001
que = []
heapq.heappush(que, [0, N])
while que:
    q = heapq.heappop(que)
    if costs[q[1]] < q[0]:
        continue
    visit[q[1]] = 1
    costs[q[1]] = q[0]
    if q[1] > 0 and not visit[q[1]-1]:
        next_node = q[1]-1
        next_lth = q[0] + 1
        if costs[next_node] > next_lth:
            costs[next_node] = next_lth
            heapq.heappush(que, [next_lth, next_node])
    if q[1] < K and not visit[q[1]+1]:
        next_node = q[1]+1
        next_lth = q[0] + 1
        if costs[next_node] > next_lth:
            costs[next_node] = next_lth
            heapq.heappush(que, [next_lth, next_node])
    if q[1] < K and not visit[2*q[1]]:
        next_node = 2*q[1]
        next_lth = q[0]
        if costs[next_node] > next_lth:
            costs[next_node] = next_lth
            heapq.heappush(que, [next_lth, next_node])
print(costs[K])