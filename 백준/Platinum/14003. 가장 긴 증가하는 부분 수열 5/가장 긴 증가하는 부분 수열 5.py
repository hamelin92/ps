import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [0 for _ in range(N)]
X = [A[0]]
D[0] = 1
lis = []
for i in range(1, N):
    l = 1
    r = len(X)
    if X[-1] < A[i]:
        X.append(A[i])
        D[i] = r+1
    elif X[0] >= A[i]:
        X[0] = A[i]
        D[i] = 1
    else:
        l = bisect_left(X, A[i])
        D[i] = l+1
        if X[l] > A[i] > X[l-1]:
            X[l] = A[i]
        
print(len(X))
lis_id = len(X)
for k in range(N-1, -1, -1):
    if D[k] == lis_id:
        lis.append(A[k])
        lis_id -= 1
print(*lis[::-1])
