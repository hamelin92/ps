import math

n = int(input())
csod = 0
for i in range(2, math.floor(math.sqrt(n))+1):
    k = n//i
    csod += i*(k-i+1) + (k-i)*(k+i+1)//2
    csod %= 1000000
print(csod)