
N = int(input())
blocks = [0] + list(map(int, input().split()))
mh = min(500000, sum(blocks))
dp = [[0]*(mh+1) for _ in range(N+1)]
for j in range(1, mh+1):
    dp[0][j] = -1
for i in range(1, N+1):
    for j in range(mh+1):
        dp[i][j] = dp[i-1][j]
        if j-blocks[i] >= 0 and dp[i-1][j-blocks[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-blocks[i]] + blocks[i])
        if blocks[i] - j >= 0 and dp[i-1][blocks[i]-j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][blocks[i]-j] + j)
        if j + blocks[i] <= mh and dp[i-1][j+blocks[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j+blocks[i]])
print(dp[N][0] if dp[N][0] else -1)