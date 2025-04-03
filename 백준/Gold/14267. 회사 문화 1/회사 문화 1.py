import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = list(map(int, input().split()))
points = [0]*(n)

for _ in range(m):
    i, w = map(int, input().split())
    points[i-1] += w

for i in range(1, n):
    points[i] += points[num[i]-1]

print(*points)
