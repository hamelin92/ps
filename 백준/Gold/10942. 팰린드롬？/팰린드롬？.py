import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [[0]*N for _ in range(N)]

dp[N-1][N-1] = 1
for i in range(N-1):
     dp[i][i] = 1
     if nums[i] == nums[i+1]:
        dp[i][i+1] = 1


for l in range(2, N):
    for s in range(N-l):
        e = s+l
        if nums[s] == nums[e] and dp[s+1][e-1]:
                dp[s][e] = 1

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
