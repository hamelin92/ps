import sys

input = sys.stdin.readline

N, M = map(int, input().split())

m = [list(input().rstrip('\n')) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
safezone = 0
partitions = dict()

def next_zone(s, x, y):
    if s == "D":
        return (x+1, y)
    elif s == "U":
        return (x-1, y)
    elif s == "L":
        return (x, y-1)
    elif s == "R":
        return (x, y+1)
    return None

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            stack = []
            s = (i, j)
            while not visit[s[0]][s[1]]:
                stack.append(s)
                visit[s[0]][s[1]] = 1
                s = next_zone(m[s[0]][s[1]], s[0], s[1])
            end = s
            if partitions.get(end) is None:
                for e in stack:
                    partitions[e] = end
            else:
                for e in stack:
                    partitions[e] = partitions[end]
print(len(set(partitions.values())))

