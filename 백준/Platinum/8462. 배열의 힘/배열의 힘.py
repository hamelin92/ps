import sys
import math


def add(x):
    global res
    cnt[x] += 1
    res += (cnt[x]*2 - 1)*x


def remove(x):
    global res
    cnt[x] -= 1
    res -= (cnt[x]*2 + 1)*x


input = sys.stdin.readline
n, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
cnt = [0] * 1000001
ans = [0]*t
sqrt = int(math.sqrt(n))
queries = [[i, *map(int, input().split())] for i in range(t)]
queries.sort(key=lambda x: (x[1]//sqrt, x[2]))
res = s = e = 0
for i in range(t):
    idx, l, r = queries[i][0], queries[i][1],  queries[i][2]
    while s < l:
        remove(a[s])
        s += 1
    while s > l:
        s -= 1
        add(a[s])
    while e < r:
        e += 1
        add(a[e])
    while e > r:
        remove(a[e])
        e -= 1
    ans[idx] = res
print(*ans, sep="\n")