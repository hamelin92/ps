from itertools import combinations

N = int(input())
M = [list(input().split()) for _ in range(N)]

T = []
O = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def monitor_student(i,j):
    for d in range(4):
        nx, ny = i+dx[d], j+dy[d]
        while 0 <= nx < N and 0<= ny < N:
            if M[nx][ny] == "S":
                return True
            elif M[nx][ny] == "O":
                break
            nx, ny = nx+dx[d], ny+dy[d]
    return False

for i in range(N):
    for j in range(N):
        if M[i][j] == "T":
            T.append((i,j))
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                imsi = []
                while 0 <= nx < N and 0<= ny < N:
                    if M[nx][ny] == "X":
                        imsi.append((nx,ny))
                    elif M[nx][ny] == "S":
                        for e in imsi:
                            O.add(e)
                        break
                    nx, ny = nx+dx[d], ny+dy[d]

ans = "YES"
for cb in combinations(O,min(len(O), 3)):
    for o in cb:
        M[o[0]][o[1]] = "O"
    for t in T:
        if monitor_student(t[0],t[1]):
            break
    else:
        ans = "YES"
        break
    for o in cb:
        M[o[0]][o[1]] = "X"
else:
    ans = "NO"
    
print(ans)
