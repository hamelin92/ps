N = int(input())
M = int(input())
S = input()
ans = 0
for i in range(M-2*N):
    if S[i] == "I":
        s = "I"
        for k in range(i+1, i+2*N+1):
            if s == S[k]:
                break
            s = S[k]
        else:
            ans += 1
print(ans)