lamps = list(input())
N = len(lamps)
def toggle(a):
    if a == 'Y':
        return 'N'
    else:
        return 'Y'
cnt = 0
for i in range(N):
    if lamps[i] == 'Y':
        cnt += 1
        for j in range(i,N,i+1):
            lamps[j] = toggle(lamps[j])
print(cnt)