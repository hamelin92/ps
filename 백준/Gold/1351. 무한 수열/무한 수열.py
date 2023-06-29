N, P, Q = map(int, input().split())
memo = {0: 1}

def seq(n):
    i, j = n//P, n//Q
    if memo.get(n):
        return memo[n]
    if not memo.get(i):
        memo[i] = seq(i)
    if not memo.get(j):
        memo[j] = seq(j)
    return memo[i] + memo[j]

print(seq(N))