N = int(input())
tab_err = list(map(int, input().split()))
tab_cor = list(map(int, input().split()))
diff = [tab_cor[_] - tab_err[_] for _ in range(N)]

ans = 0

while True:
    s, e = -1, -1
    sign = 1
    for i in range(N):
        if diff[i] != 0:
            s = e = i
            if diff[i] < 0:
                sign = -1
            break
    for j in range(s+1, N):
        if diff[j] * sign > 0:
            e = j
        else:
            break
    if s >= 0:
        ans += 1
        for k in range(s, e+1):
            diff[k] -= sign
    else:
        break
print(ans)