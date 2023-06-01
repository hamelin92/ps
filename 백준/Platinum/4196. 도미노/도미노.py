import sys
sys.setrecursionlimit(10**9)


def scc(v):
    global idx, scc_num
    visit[v] = idx
    parent = idx
    idx += 1
    stack.append(v)

    for nxt in G[v]:
        if not visit[nxt]:
            parent = min(parent, scc(nxt))
        elif not check[nxt]:
            parent = min(parent, visit[nxt])
    
    if parent == visit[v]:
        while stack:
            top = stack.pop()
            check[top] = 1
            scc_idx[top] = scc_num
            if v == top:
                break
        scc_num += 1
    return parent


input = sys.stdin.readline
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    s = V+1
    G = [[] for _ in range(s)]
    idx = 1
    stack = []
    scc_num = 1
    scc_idx = [0]*s
    check = [0]*s
    visit = [0]*s
    
    ans = 0
    for _ in range(E):
        x, y = map(int, input().split())
        G[x].append(y)

    for i in range(1, s):
        if not visit[i]:
            scc(i)

    scc_deg = [0]*scc_num

    for i in range(1, s):
        for w in G[i]:
            if scc_idx[w] == scc_idx[i]:
                continue
            scc_deg[scc_idx[w]] += 1
        
    for i in range(1, scc_num):
        if not scc_deg[i]:
            ans += 1
    print(ans)