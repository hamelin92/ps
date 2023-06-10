import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    mbti = input().split()
    ans = 0
    if N >= 33:
        print(ans)
        continue
    g = [[0]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            dist = 0
            for k in range(4):
                if mbti[i][k] != mbti[j][k]:
                    dist += 1
            g[i][j] = dist
            g[j][i] = dist
    ans = g[0][1] + g[1][2] + g[0][2]
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, g[i][j] + g[j][k] + g[i][k])
    print(ans)
