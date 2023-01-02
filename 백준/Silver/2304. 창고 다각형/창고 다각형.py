N = int(input())
polys = [list(map(int, input().split())) for _ in range(N)]
polys.sort()
N_x, heights = zip(*polys)
max_h = max(heights)
l_max = heights[0]
r_max = heights[N-1]
l_area = 0
r_area = 0
l_idx = 0
r_idx = N-1
while heights[l_idx] < max_h:
    if heights[l_idx] > l_max:
        l_area += heights[l_idx] * (N_x[l_idx+1] - N_x[l_idx])
        l_max = heights[l_idx]
    else:
        l_area += l_max * (N_x[l_idx+1] - N_x[l_idx])
    l_idx += 1
while heights[r_idx] < max_h:
    if heights[r_idx] > r_max:
        r_area += heights[r_idx] * (N_x[r_idx] - N_x[r_idx-1])
        r_max = heights[r_idx]
    else:
        r_area += r_max * (N_x[r_idx] - N_x[r_idx-1])
    r_idx -= 1
mid_val = max_h * (N_x[r_idx] - N_x[l_idx]+1)
print(mid_val + l_area + r_area)