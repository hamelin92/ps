from collections import deque

A, B = map(int, input().split())
que = deque([[A, 0]])

while que:
    q = que.popleft()
    if q[0] == B:
        print(q[1]+1)
        break
    qq = q[0]*2
    sq = 10*q[0] + 1
    if qq <= B:
        que.append([qq, q[1]+1])
    if sq <= B:
        que.append([sq, q[1]+1])
else:
    print(-1)
    
