N_str = input()
l = len(N_str)
N = int(N_str)
N_list = list(N_str)
ans = [0]*10
memo = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [9, 20, 20, 20, 20, 20, 20, 20, 20, 20],
    [189, 300, 300, 300, 300, 300, 300, 300, 300, 300]
    ]
d = 100
while len(memo) < l:
    t = memo[-1][1]
    next = [9*t + memo[-1][i] for i in range(10)]
    d *= 10
    for i in range(1, 10):
        next[i] += d
    memo.append(next)
r = l - 1
num = int(N_list[0])
ans[0] += (num-1)*memo[r][1] + memo[r][0]
for k in range(1, 10):
    ans[k] += num*memo[r][k]
for k in range(1, num):
    ans[k] += 10**r
ans[num] += int(N_str[1:])+1 if N_str[1:] != "" else 1
for i in range(1, l):
    r = l - i - 1
    num = int(N_list[i])
    ans[0] += (num)*memo[r][1]
    for k in range(1,10):
        ans[k] += num*memo[r][k]
    for k in range(num):
        ans[k] += 10**r
    ans[num] += int(N_str[i+1:])+1 if N_str[i+1:] != "" else 1
print(*ans)
