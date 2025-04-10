import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()

ans = 0
sums = set()
for x in U:
    for y in U:
        d = x+y
        sums.add(d)

for k in range(N-1, -1, -1):
    for z in range(k):
        if U[k]-U[z] in sums and U[k] > ans:
            ans = U[k]
print(ans)