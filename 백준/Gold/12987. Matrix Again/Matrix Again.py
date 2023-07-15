import sys
from math import sqrt, floor
input = sys.stdin.readline

def matsum(mat1, mat2):
    global N, M
    return [[(mat1[i][j] + mat2[i][j])%M for j in range(N)] for i in range(N)]

def matmul(mat1, mat2):
    global N, M
    return [[sum(mat1[i][k]*mat2[k][j] for k in range(N))%M for j in range(N)] for i in range(N)]

def matpow(mat, t):
    global I
    seq = []
    if t == 0:
        return I
    elif t == 1:
        return mat
    D = mat[:]
    pow = 1
    while t > 1:
        seq.append(t%2)
        t = t//2
    for exp in seq[::-1]:
        if exp:
            D = matmul(matmul(D, D), mat)
            pow = 2*pow + 1
        else:
            D = matmul(D, D)
            pow = 2*pow
        dic[pow] = D
    return D

def mat_series(mat, t):
    global O
    if t == 0:
        return O
    elif t == 1:
        return mat
    odd = t%2
    half = t//2
    evensum = mat_series(mat, half)
    if odd:
        return matsum(matsum(evensum, matmul(dic[half], evensum)), dic[t])
    else:
        return matsum(evensum, matmul(dic[half], evensum))


N, K, M = map(int, input().split())
A = [list(map(lambda x: int(x)%M, input().split())) for _ in range(N)]
I = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
O = [[0]*N for i in range(N)]
dic = {0: I, 1: A}
matpow(A, K)
ans = mat_series(A, K)
for i in range(N):
    print(*ans[i])