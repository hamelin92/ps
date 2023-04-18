from math import gcd

N = int(input())
divider = N
for r in range(N-1, 0, -1):
    divider *= r
numbers = [input().strip("\n") for _ in range(N)]
k = int(input())

nums = [(len(n), int(n)%k) for n in numbers]
dp = [[0 for j in range(k)] for _ in range(2**N)]
bits = [2**i for i in range(N)]
lengths = [0]*(2**N)
for p in range(2**N):
    for j in range(N):
        if p < bits[j]:
            break
        if p&bits[j]:
            lengths[p] += nums[j][0]
rem = [1]*(lengths[-1]+1)
for i in range(1, len(rem)):
    rem[i] = (rem[i-1]*10)%k
dp[0][0] = 1
for p in range(1, 2**N):
    for i in range(N):
        b = bits[i]
        if p < b:
            break
        elif b == p:
            dp[p][nums[i][1]] = 1
        elif b&p:
            add = rem[lengths[p-b]] * nums[i][1]
            for r in range(k):
                dp[p][(r+add)%k] += dp[p-b][r]
ans = dp[-1][0]
d = gcd(ans, divider)
print(ans//d, "/", divider//d, sep="")
