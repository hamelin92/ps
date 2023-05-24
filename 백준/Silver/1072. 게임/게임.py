X, Y = map(int, input().split())
k = 1
Z = 100*Y//X
r = 100*Y%X
c = 100-Z-1
if c <= 0:
    print(-1)
else:
    rr = (r-X)%c
    k = (X-r+rr)//c
    print(k)