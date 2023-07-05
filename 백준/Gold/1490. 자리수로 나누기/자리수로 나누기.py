from math import lcm
n = input()
N = int(n)
n = set(map(int, list(n)))
l = 1
for s in n:
    if s == 0:
        continue
    l = lcm(l, s)
r = N%l
k = 1
while (-r)%l >= k:
    r = (10*r)%l
    k *= 10
print(N*k + (-r)%l)
