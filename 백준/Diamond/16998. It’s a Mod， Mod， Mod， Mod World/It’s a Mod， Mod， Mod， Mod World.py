import sys
from math import gcd
input = sys.stdin.readline

def summation(p, q, m):
    global res
    if p == 0 or m == 0:
        return 0
    if q == 1:
        return p*m*(m+1)//2
    elif p > q:
        return (p//q)*((m*(m+1))//2) + summation(p%q, q, m)
    else:
        return m*((m*p)//q) + m//q - summation(q, p, (p*m)//q)
    


w = int(input())
for _ in range(w):
    a, b, n = map(int, input().split())
    d = gcd(a, b)
    print((a*n*(n+1))//2 - b*summation(a//d, b//d, n))
