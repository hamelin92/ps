from collections import defaultdict


def dfs(q, n):
	if n == 4:
		answers[0] = 1
		return
	for r in relation[q]:
		if visit[r] == 0:
			visit[r] = 1
			dfs(r,n+1)
			visit[r] = 0
	else:
		return


N, M = map(int, input().split())
relation = defaultdict(list)
visit = [0]*N
answers = [0]
for rel in range(M):
	u, v = map(int, input().split())
	relation[u].append(v)
	relation[v].append(u)
for s in range(N):
	visit[s] = 1
	dfs(s, 0)
	visit[s] = 0
	if answers[0] == 1:
		print(1)
		break
else:
	print(0)
