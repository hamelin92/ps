import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    tuples = [list(map(int, input().split())) for _ in range(n+2)]
    que = deque()
    visited = [0]*(n+2)
    que.append(0)
    ans = "no answer"

    while que:
        q = que.popleft()
        visited[q] = 1
        if q == n+1:
            ans = "happy"
            break
        for i in range(n+2):
            if visited[i] == 0 and abs(tuples[q][0] - tuples[i][0]) + abs(tuples[q][1]- tuples[i][1]) <= 1000:
                que.append(i)
    else:
        if visited[-1] == 0:
            ans = "sad"
    print(ans)