import sys

input = lambda: int(sys.stdin.readline().rstrip())

N = input()
v = [input() for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
ans = 0
for i in range(1, N+1):  
    for l in range(i+1):
        r = i - l
        if l > 0:
            dp[l][r] = dp[l-1][r]+v[l-1]*i
        if r > 0:
            dp[l][r] = max(dp[l][r], dp[l][r-1] + v[N-r]*i)
        ans = max(ans, dp[l][r])
print(ans)