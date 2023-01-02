N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_ind = sorted(list(range(N)), key=lambda x: B[x])
A.sort(reverse=True)
S = 0
for i in range(N):
    S += A[i]*B[B_ind[i]]
print(S)
