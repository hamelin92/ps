import sys
from pprint import pprint
R, C, T = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air = []
for r in range(R):
    if len(air) >= 2:
        break
    if A[r][0] == -1:
        air.append(r)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for t in range(T):
    dusts = []
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                dd = A[r][c]//5
                dust = [dd]
                exp = []
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and not (nc == 0 and nr in air):
                        exp.append((nr, nc))
                        A[r][c] -= dd
                dust.append(exp)
                dusts.append(dust)
    for dust in dusts:
        for nd in dust[1]:
            A[nd[0]][nd[1]] += dust[0]
    cw = 1
    for a in range(2):
        k = 0
        if a == 1:
            cw = -1
        s = [air[a]-cw, 0]
        while k < 4:
            nr = s[0] + cw*dr[k]
            nc = s[1] + dc[k]
            if a*air[a] <= nr < a*R+(1-a)*(air[a]+1) and 0 <= nc < C:
                if nr == air[a] and nc == 0:
                    A[s[0]][s[1]] = 0
                    break
                else:
                    A[s[0]][s[1]] = A[nr][nc]
                s[0], s[1] = nr, nc
            else:
                k += 1
        A[air[a]][1] = 0
print(sum(sum(A[i]) for i in range(R))+2)
