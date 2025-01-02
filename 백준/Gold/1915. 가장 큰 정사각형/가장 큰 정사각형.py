
n, m = map(int, input().split())
nums = [[0]*(m+1)] + [[0]+[int(num) for num in input()] for _ in range(n)]
max_sq = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if nums[i][j] == 1:
            nums[i][j] = min(nums[i-1][j-1], nums[i][j-1], nums[i-1][j]) + 1
            if nums[i][j] > max_sq:
                max_sq = nums[i][j]
print(max_sq**2)
