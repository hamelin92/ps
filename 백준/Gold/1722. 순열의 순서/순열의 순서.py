import sys

input = lambda: sys.stdin.readline().rstrip()

f = [1]
for i in range(1, 20):
	f.append(f[-1]*i)

n = int(input())
order = list(range(1, n+1))
c = list(map(int, input().split()))
if c[0] == 1:
	k = c[1] - 1
	perm = []
	for i in range(n):
		m = k//f[n-i-1]
		k = k%f[n-i-1]
		perm.append(order.pop(m))
	print(*perm)
else:
	ord = 1
	p = c[1:]
	for i in range(n-1):
		m = order.index(p[i])
		ord += m*f[n-i-1]
		order.pop(m)
	print(ord)
