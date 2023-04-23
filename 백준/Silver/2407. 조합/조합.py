
N, K = map(int, input().split())
K = min(K, N-K)
C = [[1]*n for n in range(1, N+2)]
for i in range(1, N+1):
    for k in range(max(i-N+K, 1), min(i, K+1)):
        C[i][k] = C[i-1][k-1] + C[i-1][k]
print(C[N][K])

