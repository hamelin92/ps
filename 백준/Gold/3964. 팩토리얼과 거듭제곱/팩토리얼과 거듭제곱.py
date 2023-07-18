import sys
from math import sqrt, ceil, log
input = sys.stdin.readline


def find_primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            b[p::p] = [False for _ in range(p, n + 1, p)]
    return ps


def factorization(m):
    factors = {}
    cnt = 0
    mm = ceil(sqrt(m))
    for p in primes:
        if p > mm:
            if m > 1:
                factors[m] = 1
            break
        cnt = 0
        while m > 0 and m%p == 0:
            m //= p
            cnt += 1
        if cnt > 0:
            factors[p] = cnt
    else:
        if m > 1:
            factors[m] = 1
    return factors

primes = find_primes(1000000)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    factors = factorization(k)
    i = ceil(max(log(n, k), 1))*n
    for f in factors.keys():
        nn = n
        fcnt = 0
        while nn:
            nn //= f
            fcnt += nn
        i = min(i, fcnt//factors[f])
    print(i)

