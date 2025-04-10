import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()

sums = set(U)
for x in U:
    for y in U:
        d = x+y
        if d < U[-1]:
            sums.add(d)
ans = 0

for k in range(N-1, -1, -1):
    for z in range(k):
        if U[k]-U[z] in sums and U[k] > ans:
            ans = U[k]
print(ans)