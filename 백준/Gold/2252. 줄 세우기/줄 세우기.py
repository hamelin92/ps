import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
order = defaultdict(list)
in_degree = [0]*(N+1)
visit = [0]*(N+1)
que = deque()
t = []
for m in range(M):
    n, b = map(int, sys.stdin.readline().split())
    order[n].append(b)
    in_degree[b] += 1
for i in range(1, N+1):
    if in_degree[i] == 0:
        que.append(i)
        visit[i] = 1
while que:
    q = que.popleft()
    t.append(q)
    for nxt in order[q]:
        if not visit[nxt]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                visit[nxt] = 1
                que.append(nxt)
if len(t) == N:
    print(*t)
else:
    print(0)
