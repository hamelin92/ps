import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
rgbs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for i in range(N)]
ans = 1000001
dp[0] = [1000001]*3
for k in range(3):
    dp[0][k] = rgbs[0][k]
    for i in range(1, N):
        for j in range(3):
            dp[i][j] = rgbs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
    dp[0][k] = 1000001
    ans = min(ans, dp[-1][(k+1)%3], dp[-1][(k+2)%3])
print(ans)