import sys
from math import comb

input = sys.stdin.readline
N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
cnt = 0
mods = [0]*M
mods[0] = 1
for i in range(1, N+1):
    A[i] = (A[i] + A[i-1])%M
    mods[A[i]] += 1
for i in range(M):
    if mods[i] >= 2:
        cnt += comb(mods[i], 2)
print(cnt)
