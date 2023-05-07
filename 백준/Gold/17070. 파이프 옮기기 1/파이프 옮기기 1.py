N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for i in range(N)] for j in range(N)]
dp[0][0] = [0, 0, 0]
dp[0][1] = [1, 0, 0]
for i in range(N):
    for j in range(1, N):
        if not maps[i][j]:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][1]
            if i > 0:
                dp[i][j][2] += dp[i-1][j][1] + dp[i-1][j][2]
                if not maps[i-1][j] and not maps[i][j-1]:
                    dp[i][j][1] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
                
print(sum(dp[N-1][N-1]))