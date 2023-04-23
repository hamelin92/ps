from itertools import combinations

T = int(input())
C = [[1]*n for n in range(1, 31)]
for i in range(1, 30):
    for k in range(1, i):
        C[i][k] = C[i-1][k-1] + C[i-1][k]
for t in range(T):
    K, N = map(int, input().split())
    print(C[N][K])

