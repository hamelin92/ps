import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))
psum = 0
psum_dict = defaultdict(int)
psum_dict[0] = 1
cnt = 0

for i in range(N):
	psum += A[i]
	cnt += psum_dict[psum-K]
	psum_dict[psum] += 1
print(cnt)
