N, K = map(int, input().split())
dp = [[0 for j in range(K+1)] for i in range(N+1)]
for j in range(K+1):
    dp[0][j] = 1
for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] += dp[i][j-1]
        for k in range(i):
            dp[i][j] += dp[k][j-1]
        dp[i][j] %= 1000000000
print(dp[N][K])