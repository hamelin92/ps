import sys
input = sys.stdin.readline


def matmul(A, B):
    global mod
    # A, B : n by n matrices
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%mod for j in range(n)] for i in range(n)]

def matpow(A, t):
    seq = []
    D = A[:]
    while t > 1:
        seq.append(t%2)
        t = t//2
    for exp in seq[::-1]:
        if exp:
            A = matmul(matmul(A, A), D)
        else:
            A = matmul(A, A)
    return A

mod = 1000003
N, S, E, T = map(int, input().split())
G = [[0]*5*N for _ in range(5*N)]
for i in range(N):
    for j in range(1, 5):
        G[i*5+j][i*5+j-1] = 1
for i in range(N):
    w = list(map(int, list(input().strip("\n"))))
    for j in range(N):
        if w[j]:
            G[i*5][j*5+w[j]-1] = 1
ans = matpow(G, T)
print(ans[5*(S-1)][5*(E-1)]%mod)