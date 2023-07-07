S, T = map(int, input().split())

a, b = 0, 0
for i in range(1, T+1):
    d = i%2
    t = T//i
    a += ((-1)**d)*t

for i in range(1, S):
    d = i%2
    s = (S-1)//i
    b += ((-1)**d)*s
print(a-b)