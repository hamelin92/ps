import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)
for i in range(N):
    w, v = map(int, input().split())
    if w > K:
        continue
    for j in range(K, 0, -1):
        if j + w <= K and dp[j]:
            dp[j+w] = max(dp[j+w], dp[j]+v)
    dp[w] = max(dp[w], v)
print(max(dp))