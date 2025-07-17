N = int(input())
M = int(input())
seq = [1]*(N+1)

for i in range(2, N+1):
    seq[i] = seq[i-1] + seq[i-2]
ans = 1
tmp = 0
for i in range(M):
    num = int(input())
    ans *= seq[num-tmp-1]
    tmp = num
ans *= seq[N-tmp]

print(ans)
