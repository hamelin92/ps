import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

nge = [-1]*N
stack = []

for i in range(N-1):
    stack.append(i)
    if A[i] >= A[i+1]:
        continue
    else:
        while stack:
            if A[stack[-1]] < A[i+1]:
                nge[stack.pop()] = A[i+1]
            else:
                break
print(*nge)