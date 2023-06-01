import sys
sys.setrecursionlimit(10**9)


def scc(v):
    global idx
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
        scc_el = []
        while stack:
            top = stack.pop()
            check[top] = 1
            scc_el.append(top)
            if v == top:
                break
        scc_el.sort()
        scc_el.append(-1)
        scc_list.append(scc_el)
    return parent


input = sys.stdin.readline
V, E = map(int, input().split())
s = V+1
G = [[] for _ in range(s)]
idx = 1
stack = []
scc_list = []
check = [0]*s
visit = [0]*s
for _ in range(E):
    x, y = map(int, input().split())
    G[x].append(y)

for i in range(1, V+1):
    if not visit[i]:
        scc(i)
scc_list.sort()
print(len(scc_list))
for comp in scc_list:
    print(*comp)