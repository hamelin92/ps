import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
answer = []
graph = [[] for _ in range(n + 1)]
deg = [0 for _ in range(n+1)]
queue = []

for i in range(m):
	A, B = map(int, input().split())
	graph[A].append(B)
	deg[B] += 1

for i in range(1, n + 1):
	if deg[i] == 0:
		heapq.heappush(queue, i)

while queue:
	tmp = heapq.heappop(queue)
	answer.append(tmp)
	for i in graph[tmp]:
		deg[i] -= 1
		if deg[i] == 0:
			heapq.heappush(queue, i)
print(*answer)