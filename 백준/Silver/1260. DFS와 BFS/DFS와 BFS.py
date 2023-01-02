from collections import deque


def DFS(start):
	global N
	result = [start+1]
	stack = [start]
	visit = [0]*N
	visit[start] = 1
	while stack:
		q = stack[-1]
		for n in range(N):
			if graph[q][n] == 1 and visit[n] == 0:
				stack.append(n)
				visit[n] = 1
				result.append(n+1)
				break
		else:
			stack.pop()
	return result


def BFS(start):
	global N
	result = []
	queue = deque([start])
	visit = [0]*N
	visit[start] = 1
	while queue:
		q = queue.popleft()
		result.append(q+1)
		for n in range(N):
			if graph[q][n] == 1 and visit[n] == 0:
				queue.append(n)
				visit[n] = 1
	return result


N, M, V = map(int, input().split())
graph = [[0]*N for _ in range(N)]
for edge in range(M):
	u,v = map(int, input().split())
	graph[u-1][v-1] = graph[v-1][u-1] = 1
print(*DFS(V-1))
print(*BFS(V-1))
