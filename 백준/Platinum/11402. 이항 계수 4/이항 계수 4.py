def padic(n, p):
    res = []
    while n:
        n, c = divmod(n, p)
        res.append(c)
    return res


N, K, M = map(int, input().split())
nl = padic(N, M)
kl = padic(K, M)
kl += [0]*(len(nl) - len(kl))
cb = [[0]*(M+1) for _ in range(M+1)]
cb[0][0] = 1
cb[1][0] = 1
cb[1][1] = 1
for i in range(2, M+1):
    for j in range(i+1):
        cb[i][j] = cb[i-1][j]+cb[i-1][j-1]
ans = 1
for k in range(len(nl)):
    ans *= cb[nl[k]][kl[k]]
print(ans%M)

