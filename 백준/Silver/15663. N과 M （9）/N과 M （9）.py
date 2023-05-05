def sequence(k):
    global M, ans
    if k == M:
        print(*res)
        return
    last = 0
    for j in range(N):
        if not visited[j] and last != nums[j]:
            visited[j] = 1
            res.append(nums[j])
            last = nums[j]
            sequence(k+1)
            visited[j] = 0
            res.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0]*N
res = []
sequence(0)
