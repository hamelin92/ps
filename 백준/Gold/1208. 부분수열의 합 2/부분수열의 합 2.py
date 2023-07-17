import sys
from collections import defaultdict
input = sys.stdin.readline

def get_sums(idx, s):
    global N
    if idx == N:
        dic[s] += 1
        return
    get_sums(idx+1, s+seq[idx])
    get_sums(idx+1, s)


def cnt(idx, s):
    global N, ans
    if idx == N//2:
        ans += dic[S-s]
        return
    cnt(idx+1, s+seq[idx])
    cnt(idx+1, s)


N, S = map(int, input().split())
seq = list(map(int, input().split()))
dic = defaultdict(int)
ans = 0
get_sums(N//2, 0)
cnt(0, 0)
if S == 0:
    print(ans-1)
else:
    print(ans)