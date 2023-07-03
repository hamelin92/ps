import sys
from math import sqrt

def matmul(A, B):
    # 2 by 2
    return [[sum(A[i][k]*B[k][j] for k in range(2))%1000 for j in range(2)] for i in range(2)]

def pow(m):
    global a
    t = [[1, 0], [0, 1]]
    stk = []
    while m:
        stk.append(m%2)
        m //= 2
    while stk:
        e = stk.pop()
        if e:
            t = matmul(matmul(t, t), a)
        else:
            t = matmul(t, t)
    return t


T = int(sys.stdin.readline())
a = [[6, -4], [1, 0]]
for i in range(1, T+1):
    n = int(sys.stdin.readline())
    res = pow(n-1)[1]
    ans = (28*res[0] + 6*res[1]-1)%1000
    ans = str(ans)
    ans = "0"*(3-len(ans)) + ans
    print(f"Case #{i}: {ans}")

    