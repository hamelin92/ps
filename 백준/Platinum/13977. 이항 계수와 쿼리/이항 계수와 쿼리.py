def modulo_inverse(a, b):
    s0, s1 = 0, 1
    if a > b:
        s0, s1 = 1, 0
    while a > 1 and b > 1:
        d = b//a
        s0, s1 = s1, s0 - d * s1
        a, b = b - d*a, a
    return s1


def powers(A,B):
    global modulo
    A = D = A%modulo
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2

    for exp in seq[::-1]:
        if exp:
            A = (A ** 2) * D
        else:
            A = (A ** 2)
        A = A%modulo
    return A if B > 0 else 1


computed = 1
modulo = 1000000007
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]
max_n = max(queries, key=lambda x: x[0])[0]+1
factorials = [1]*max_n
for i in range(2, max_n):
    factorials[i] = factorials[i-1]*i%modulo
divs = list(map(lambda x: modulo_inverse(x, modulo) ,factorials[:]))
for i in range(M):
    N, K = queries[i]
    print(factorials[N]*divs[K]*divs[N-K]%modulo)
    
