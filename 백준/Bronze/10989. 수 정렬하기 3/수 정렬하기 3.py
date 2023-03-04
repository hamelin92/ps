import sys

N = int(sys.stdin.readline())
num_cnt = [0]*10001
for i in range(N):
    num_cnt[int(sys.stdin.readline())] += 1
for n in range(10001):
    if num_cnt[n]:
        for k in range(num_cnt[n]):
            print(n)