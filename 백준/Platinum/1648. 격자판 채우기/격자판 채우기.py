def count(idx, bit):
    if idx >= N*M:
        if bit == 0:
            return 1
        else:
            return 0
    if dp[idx][bit] != -1:
        return dp[idx][bit]
    dp[idx][bit] = 0
    if bit & (1<<0):
        dp[idx][bit] = count(idx+1, bit>>1)
    else:
        if idx%M != M-1 and bit&2 == 0:
            dp[idx][bit] += count(idx+2, bit >> 2)
        dp[idx][bit] += count(idx+1, (bit>>1) | (1<<(M-1)))
    dp[idx][bit] %= 9901
    return dp[idx][bit]
    

N, M = map(int, input().split())
if N%2 and M%2:
    print(0)
elif N == 1 or M == 1:
    print(1)
else:
    dp = [[-1 for j in range(1<<M)] for i in range(N*M)]
    print(count(0, 0))
