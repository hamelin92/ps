def matmul(A, B):
    global m, mod
    return [[sum(A[i][k]*B[k][j] for k in range(m))%mod for j in range(m)] for i in range(m)]

def matpow(A, t):
    stk = []
    res = A[:]
    while t > 1:
        stk.append(t%2)
        t //= 2
    while stk:
        q = stk.pop()
        if q:
            res = matmul(matmul(res, res), A)
        else:
            res = matmul(res, res)
    return res

n, m = map(int, input().split())
mod = 1000000007
a = []
for i in range(m):
    row = [0]*m
    if i == 0:
        row[0] = 1
        row[-1] = 1
    else:
        row[i-1] = 1 
    a.append(row)
if n < m:
    print(1)
elif n < 2*m:
    print(n-m+2)
else:
    v = matpow(a, n-m+1)
    print(sum(v[0])%mod)