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
N, M = map(int, input().split())
s = 2*N+1
G = [[] for _ in range(s)]
scc_num = 1
idx = 1
stack = []
scc_idx = [0]*s
check = [0]*s
visit = [0]*s
for _ in range(M):
    x, y = map(int, input().split())
    G[-x].append(y)
    G[-y].append(x)

for i in range(1, N+1):
    if not visit[i]:
        scc(i)

for i in range(1, N+1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
else:
    print(1)