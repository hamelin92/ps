import sys

N = int(sys.stdin.readline())
info = []
for _ in range(N):
    n, *foods = sys.stdin.readline().strip("\n").split()
    n = int(n)
    info.append(foods)
info.sort()
if info:
    for l in range(len(info[0])):
        print("--"*l, info[0][l], sep="")
for i in range(1, N):
    lev = 0
    for l in range(len(info[i])):
        if l >= len(info[i-1]) or info[i-1][l] != info[i][l]:
            break
        else:
            lev = l+1
    for l in range(lev, len(info[i])):
        print("--"*l, info[i][l], sep="")