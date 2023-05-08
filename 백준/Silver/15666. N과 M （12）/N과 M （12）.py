def sequence(i, k):
    global M, ans
    if k == M:
        print(*res)
        return
    last = 0
    for j in range(i, N):
        if last != nums[j]:
            res.append(nums[j])
            last = nums[j]
            sequence(j, k+1)
            res.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
res = []
sequence(0, 0)
