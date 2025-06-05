import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
h = [0] + list(map(int, input().split()))
sign = [0]*N
stack = []

for i in range(N,0,-1):
    while stack:
        if stack[-1][0] < h[i]:
            t = stack.pop()
            sign[t[1]] = i
        else:
            break
    stack.append([h[i], i-1])
print(*sign)



