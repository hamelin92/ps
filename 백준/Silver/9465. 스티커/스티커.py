import sys

input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    for i in range(2):
        dp[i][0] = stickers[i][0]
    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1]+stickers[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1]+stickers[1][i], dp[1][i-1])
    print(max(dp[0][-1], dp[1][-1]))