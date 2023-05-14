import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
G = [0]*(1+len(A))
G[0] = 1
deg = 1
for a in A:
    for d in range(deg, 0, -1):
        G[d] = (G[d]+a * G[d-1])%100003
    
    deg += 1
Q = int(input())
for _ in range(Q):
    q = int(input())
    print(G[q])