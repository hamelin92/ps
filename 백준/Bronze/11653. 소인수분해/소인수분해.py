from math import sqrt, floor


def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in range(p, n + 1, p):
                b[i] = False
    return ps


def factorization(n):
    factors = []
    prime_list = primes(floor(sqrt(n)) + 1)
    for p in prime_list:
        while n%p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


for ft in factorization(int(input())):
    print(ft)