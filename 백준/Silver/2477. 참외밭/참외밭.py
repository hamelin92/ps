N = int(input())
edges = [list(map(int, input().split())) for _ in range(6)]
dir_all = [edges[i][0] for i in range(6)]
directions = [0]*4
concave = []
for i in range(6):
    directions[edges[i][0]-1] += 1
    if directions[edges[i][0]-1] == 2:
        concave.append(edges[i][0])
large = 1
small = 1

for i in range(6):
    if (dir_all[i] in concave) and (dir_all[i+1-6] in concave) and (dir_all[i-1] in concave):
        small *= edges[i][1]
    elif edges[i][0] in concave:
        continue
    else:
        large *= edges[i][1]
print(N * (large - small))