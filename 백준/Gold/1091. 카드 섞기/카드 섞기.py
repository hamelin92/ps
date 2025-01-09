N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
D = list(range(N))

def shuffle():
    global S, D
    n = len(S)
    res = [-1]*n
    for i in range(n):
        res[S[i]] = D[i]
    D = res

order = 2**(1+N//2)

ans = 0
for i in range(order):
    check = 0

    for j in range(N):
        if ans > 0:
             if D[j] != j:
                 break
        else:
            break
    else:
        ans = -1
        break

    for j in range(N):
        if P[D[j]] != j%3: 
            check = 1
            break
    if check:
        shuffle()
        ans += 1
    else:
        break
else:
    ans = -1

print(ans)