import sys
import heapq

input = sys.stdin.readline
n = int(input())
ho = [list(map(int, input().split())) for _ in range(n)]
hos = []
d = int(input())
hq = []
for i in range(n):
    if abs(ho[i][1]-ho[i][0]) <= d:
        ho[i].sort()
        hos.append(ho[i])
hos.sort(key=lambda x: x[1])
ans = 0
for r in hos:
    if not hq:
        heapq.heappush(hq, r)
    else:
        while hq[0][0] < r[1] - d:
            heapq.heappop(hq)
            if not hq:
                break
        heapq.heappush(hq, r)
    ans = max(ans, len(hq))
print(ans)