L, C = map(int, input().split())
spells = sorted(input().split())
aeiou = {"a", "e", "i", "o", "u"}
check = [False]*C
res = []

def combi(n, r, i, cnt):
    if len(res) == r:
        if cnt and r-cnt >= 2:
            print(*res, sep="")
        return
    for j in range(i+1, n):
        if spells[j] in aeiou:
            cnt += 1
        res.append(spells[j])
        combi(n, r, j, cnt)
        if res and res[-1] in aeiou:
            cnt -= 1
        res.pop()

combi(C, L, -1, 0)