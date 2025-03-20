import sys

input = sys.stdin.readline

seq = list(map(int, input().split()))
dp = [[[999999 for i in range(5)] for j in range(5)] for _ in range(len(seq))]
dp[-1][0][0] = 0
n = len(seq) - 1

def energy(a, b):
    if a*b == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a-b) == 2:
        return 4
    else:
        return 3
    
for s in range(n):
    for i in range(5):
        for j in range(5):
            e = energy(seq[s], j)
            dp[s][seq[s]][i] = min(dp[s][seq[s]][i], dp[s-1][j][i] + e)
            dp[s][i][seq[s]] = min(dp[s][i][seq[s]], dp[s-1][i][j] + e)

if n == 0:
    print(0)
else:
    m = 999999
    for i in range(5):
        for j in range(5):
            m = min(m, dp[n-1][i][j])
    print(m)