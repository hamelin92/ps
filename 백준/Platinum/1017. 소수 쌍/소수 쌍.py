import sys
sys.setrecursionlimit(10**5)

def dfs(idx):
    if idx == 0 or visit[idx]:
        return False
    visit[idx] = True
    for i in range(len(comb[idx])):
        if comb[idx][i]:
            if second_match[i] == -1 or dfs(second_match[i]):
                first_match[idx] = i
                second_match[i] = idx
                return True
    return False


input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
first = []
second = []
is_first = nums[0]%2
for i in range(N):
    if nums[i]%2 == is_first:
        first.append(nums[i])
    else:
        second.append(nums[i])
if len(first) != len(second):
    print(-1)
    exit()
comb = [[0]*len(second) for _ in range(len(first))]
visit = [0]*N
primes = [1]*2001
primes[0] = 0
primes[1] = 0
ans = []
for i in range(2, 2001):
    if primes[i]:
        for j in range(2*i, 2001, i):
            primes[j] = 0
for i in range(len(first)):
    for j in range(len(second)):
        if primes[first[i]+second[j]]:
            comb[i][j] = 1
for i in range(len(second)):
    if comb[0][i]:
        paired = 1
        first_match = [-1]*len(first)
        second_match = [-1]*len(second)
        first_match[0] = i
        second_match[i] = 0
        for j in range(1, len(first)):
            visit = [0]*len(first)
            if dfs(j):
                paired += 1
        if paired == len(second):
            ans.append(second[i])
if ans:
    ans.sort()
    print(*ans)
else:
    print(-1)
