from math import comb

while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    print(comb(N, K))