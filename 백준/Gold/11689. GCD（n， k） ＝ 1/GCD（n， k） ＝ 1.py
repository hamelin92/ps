from math import sqrt, floor
from collections import defaultdict

n = int(input())
factors = defaultdict(int)
ans = 1

while not n%2:
    n //= 2
    factors[2] += 1

for i in range(3, floor(sqrt(n))+1, 2):
    while not n%i:
        n //= i
        factors[i] += 1
else:
    if n > 1:
        factors[n] += 1

for k in factors.keys():
    ans *= (k-1) * (k ** (factors[k]-1))
print(ans)