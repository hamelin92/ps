import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def bs(target):
    l, r = 0, len(b_sub)-1
    while l < r:
        if b_sub[l] == b_sub[r] and b_sub[l] == target:
            break
        mid = (l+r)//2
        if b_sub[mid] < T-s:
            l = mid + 1
        elif b_sub[mid] > T-s:
            r = mid - 1
        elif b_sub[r] > T-s:
            r -= 1
        elif b_sub[l] < T-s:
            l += 1
    return l, r


T = int(input())
n = int(input())
a = [0]+list(map(int, input().split()))
m = int(input())
b = [0]+list(map(int, input().split()))
a_sub = []
b_sub = []
for i in range(1, n+1):
    a[i] += a[i-1]
    for l in range(i):
        a_sub.append(a[i]-a[l])
for i in range(1, m+1):
    b[i] += b[i-1]
    for l in range(i):
        b_sub.append(b[i]-b[l])
a_sub.sort()
b_sub.sort()
ans = 0
for s in a_sub:
    l, r = bisect_left(b_sub, T-s), bisect_right(b_sub, T-s)
    if l < len(b_sub) and b_sub[l] == T-s:
        ans += r-l
print(ans)