import sys

def get_x(f, g):
    return (f[1]-g[1])/(g[0]-f[0])


input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0 for _ in range(n)]

line = [[b[0], dp[0]]]
for i in range(1, n):
    l = 0
    r = len(line)-1
    while l < r:
        mid = (l+r)//2
        if get_x(line[mid], line[mid+1]) <= a[i]:
            l = mid+1
        else:
            r = mid
    dp[i] = line[l][0]*a[i] + line[l][1]
    line.append([b[i], dp[i]])
    while len(line) > 2 and get_x(line[-3], line[-2]) > get_x(line[-2], line[-1]):
        line.pop(-2)
print(dp[n-1])
