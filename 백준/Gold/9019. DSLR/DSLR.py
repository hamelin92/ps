import sys
from collections import deque

dslr = [
    lambda x: (x<<1)%10000,
    lambda x: (x-1)%10000,
    lambda x: (x*10)%10000 + x//1000,
    lambda x: x//10 + (x%10)*1000
]
dslr_str = ["D", "S", "L", "R"]
T = int(sys.stdin.readline())
for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visit = [False]*10000
    start = [-1, 0, A]
    visit[A] = start
    que = deque([start])
    while que:
        q = que.popleft()
        if q[-1] == B:
            break
        for k in range(4):
            nval = dslr[k](q[-1])
            if not visit[nval]:
                visit[nval] = [q[-1], k, nval]
                que.append([q[-1], k, nval])
    ans = []
    while q[0] >=0:
        ans.append(q[1])
        q = visit[q[0]]
    print(*[dslr_str[k] for k in ans[::-1]], sep="")
