import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
house = []
chick = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chick.append((i, j))
min_val = 10000
for choices in combinations(chick, M):
    chick_d = sum(min(abs(h[0]-c[0])+abs(h[1]-c[1]) for c in choices) for h in house)
    if chick_d < min_val:
        min_val = chick_d
print(min_val)