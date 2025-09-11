import sys

sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


def dfs(n):
    global cnt, ccnt

    visit[n] = 1
    cycle.add(n)
    idx[n] = ccnt
    ccnt += 1
    if visit[s[n]] == 1:
        if s[n] in cycle:
            cnt += idx[s[n]] - len(cycle)
        return
    else:
        dfs(s[n])


T = int(input())
for t in range(T):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    idx = [0] * (n+1)
    cnt = n
    visit = [0]*(n+1)
    for i in range(1, n+1):
        ccnt = 0
        if not visit[i]:
            cycle = set()
            dfs(i)

    print(cnt)