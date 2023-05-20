import sys

input = sys.stdin.readline

N = int(input())
dp_min = [0, 0, 0]
dp_max = [0, 0, 0]
for i in range(N):
    nums = list(map(int, input().split()))
    min_l = []
    max_l = []
    for j in range(3):
        min_l.append(nums[j] + min(dp_min[max(0, j-1):min(3, j+2)]))
        max_l.append(nums[j] + max(dp_max[max(0, j-1):min(3, j+2)]))
    dp_min = min_l[:]
    dp_max = max_l[:]

print(max(dp_max), min(dp_min))
