import sys

def matrix_multiplication(A, B):
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] ^= A[i][k] & B[k][j]
    return C

def find_repeated_multiplication(K):
    seen = set()
    seen.add(tuple(map(tuple, K)))
    count = 2
    T = matrix_multiplication(K, K)
    while tuple(map(tuple, T)) not in seen:
        seen.add(tuple(map(tuple, T)))
        count += 1
        T = matrix_multiplication(T, K)
    return count

n = int(sys.stdin.readline())
K = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(find_repeated_multiplication(K))
