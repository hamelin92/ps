from collections import deque

N = int(input()) # 전체 도시의 수
M = int(input()) # 계획된 도시의 수
cities = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
plan_set = set(plan)
available = {plan[0]}
que = deque()
que.append(plan[0]-1)
while que:
    q = que.popleft()
    for i in range(N):
        j = i+1
        if cities[q][i] and j not in available:
            available.add(j)
            que.append(i)
if plan_set.issubset(available):
    print("YES")
else:
    print("NO")