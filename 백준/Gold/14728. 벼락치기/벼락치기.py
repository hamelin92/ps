import sys

input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())
part = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, T+1):
        if j >= part[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-part[i][0]] + part[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[-1]))
