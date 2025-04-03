import sys

input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())
dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1,N+1):
    K, S = map(int, input().split())
    for j in range(1, T+1):
        if j >= K:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-K] + S)
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[-1]))
