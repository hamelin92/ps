N, L = map(int, input().split())
while L*(L-1) <= 2*N and L <= 100:
    s = L*(L-1)//2
    if N-s >= 0 and (N-s) % L == 0:
        print(*[l for l in range((N-s)//L, (N-s)//L+L)])
        break
    L += 1
else:
    print(-1)
