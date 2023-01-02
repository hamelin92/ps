from math import gcd
N = int(input())
D = [1] * (N+1)
for i in range(2,N+1):
    D[i] = D[i-1] + D[i-2]
answer = 0
cong = 1000000007
for i in range(1, N+1):
    answer += D[gcd(i+1, N+1)-1]
    answer %= cong
print(answer)