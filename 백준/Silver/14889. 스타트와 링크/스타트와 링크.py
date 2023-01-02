from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst = list(range(N))
sums = [0]*N
total = 0
for i in range(N):
	sums[i] += sum(S[i])
	total += sum(S[i])
	for j in range(N):
		sums[i] += S[j][i]
min_balance = 26*N*N
for cb in combinations(lst,N//2):
	tmp = 0
	for c in cb:
		tmp += sums[c]
	diff = abs(total - tmp)
	if diff < min_balance:
		min_balance = diff
print(min_balance)