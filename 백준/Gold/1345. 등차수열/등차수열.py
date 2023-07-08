import sys

n, a = map(int, sys.stdin.readline().split())
s = []
if n:
    s = list(map(lambda x: int(x)-a, sys.stdin.readline().split()))

mind = -1
maxd = 10000000
for k in range(n):
    mind = max(mind, s[k]/(k+1))
    maxd = min(maxd, (s[k]+1)/(k+1))
if n == 0:
    print(0)
elif maxd <= mind or maxd <= 0:
    print(-1)
else:
    print(max(0, mind))