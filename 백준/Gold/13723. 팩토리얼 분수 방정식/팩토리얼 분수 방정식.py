from collections import defaultdict

def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            b[p::p] = [False for _ in range(p, n + 1, p)]
    return ps


N = int(input())
if N == 1:
    print(1)
else:
    ps = primes(N)
    factors = defaultdict(int)
    ans = 1
    for p in ps:
        if p > N:
            break
        m = N
        while m > 0:
            m //= p
            factors[p] += m
    for f in factors.keys():
        ans *= factors[f]*2 + 1
    print(ans)