from collections import deque

N = int(input()) # 전체 도시의 수
M = int(input()) # 계획된 도시의 수
cities = [list(map(int, input().split())) for _ in range(N)]

plan = list(map(int, input().split()))
available = {plan[0]} # 시작지점부터 해서 연결되어 접근 가능한 도시를 모아놓은 집합
que = deque() # 출발지를 큐에 넣고 탐색
que.append(plan[0]-1)

while que:
    q = que.popleft()
    for i in range(N):
        j = i+1
        if cities[q][i] and j not in available:
            # 도시 q에 연결된 도시 중 이미 이동 가능한 도시 집합에 없는 경우만 큐에 다시 넣고 해당 집합에 추가
            available.add(j)
            que.append(i)

if set(plan).issubset(available):
    # 이동가능한 도시들 집합에 계획된 도시들 집합이 포함된다면 YES, 아니면 NO
    print("YES")
else:
    print("NO")
