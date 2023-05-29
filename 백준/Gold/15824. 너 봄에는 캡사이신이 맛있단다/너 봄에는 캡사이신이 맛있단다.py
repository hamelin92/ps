import sys

def pow(a, s):
    global mod
    if s == 0:
        return 1
    seq = []
    d = a
    while s > 1:
        seq.append(s%2)
        s = s//2
    for exp in seq[::-1]:
        if exp:
            a = (a ** 2) * d
        else:
            a = (a ** 2)
        a %= mod
    return a


input = sys.stdin.readline
mod = 1000000007
N = int(input())
sch = list(map(int, input().split()))
sch.sort()
ans = 0
for i in range(N):
    ans += sch[i]*(pow(2, i)-pow(2, N-i-1))
print(ans%mod)