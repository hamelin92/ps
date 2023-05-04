def sequence(i, k):
    global M
    if k == M:
        print(*res)
        return
    for j in range(i, N):
        res.append(nums[j])
        sequence(j, k+1)
        res.pop()


N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
res = []
sequence(0, 0)