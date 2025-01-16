N, K = map(int, input().split())
heights = list(map(int, input().split()))
d = [heights[i] - heights[i+1] for i in range(N-1)]

d.sort()
print(heights[-1] - heights[0] + sum(d[:K-1]))
