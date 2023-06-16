import sys

input = sys.stdin.readline
N = int(input())
chords = [[0]*100 for _ in range(100)]
for _ in range(N):
    a, b = map(lambda x: int(x)-1, input().split())
    chords[a][b] = 1
    chords[b][a] = 1
dp = [[0]*100 for _ in range(100)]
for i in range(100):
    for j in range(i, -1, -1):
        for k in range(j, i):
            dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + chords[j][i])

print(dp[0][99])
