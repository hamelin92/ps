import sys
from math import gcd

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
d = 0
for i in range(n-1):
    j = i+1
    d = gcd(d, max(num[i], num[j]) - min(num[i], num[j]))
print(d)