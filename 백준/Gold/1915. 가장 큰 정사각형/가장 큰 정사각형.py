import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, list(input().rstrip("\n")))) for _ in range(n)]
max_sq = 0
for i in range(n):
    if nums[i][0] > max_sq:
        max_sq = 1
if max_sq == 0:
    for j in range(m):
        if nums[0][j] > max_sq:
            max_sq = 1
for i in range(1, n):
    for j in range(1, m):
        if nums[i][j] == 1:
            nums[i][j] = min(nums[i-1][j-1], nums[i][j-1], nums[i-1][j]) + 1
            if nums[i][j] > max_sq:
                max_sq = nums[i][j]
print(max_sq**2)
