N, M, L, K = map(int, input().split())
meteors = [list(map(int, input().split())) for _ in range(K)]
x_axis = {-1}
y_axis = {-1}
for m in meteors:
    x_axis.add(m[0])
    y_axis.add(m[1])
sorted_x = sorted(x_axis)
sorted_y = sorted(y_axis)
endpt_x = [0]*len(x_axis)
endpt_y = [0]*len(y_axis)
x_axis_id = dict()
y_axis_id = dict()

ptx, pty = 0, 0
for i in range(1, max(len(x_axis), len(y_axis))):
    if i < len(x_axis):
        x_axis_id[sorted_x[i]] = i
        while ptx+1 < len(x_axis) and sorted_x[ptx+1] <= sorted_x[i] + L:
            ptx += 1
        endpt_x[i] = ptx

    if i < len(y_axis):
        y_axis_id[sorted_y[i]] = i
        while pty+1 < len(y_axis) and sorted_y[pty+1] <= sorted_y[i] + L:
            pty += 1
        endpt_y[i] = pty

greed = [[0]*(len(x_axis)) for _ in range(len(y_axis))]
for m in meteors:
    for i in range(y_axis_id[m[1]], len(y_axis)):
        for j in range(x_axis_id[m[0]], len(x_axis)):
            greed[i][j] += 1

cnt = 0
for i in range(1, len(y_axis)):
    for j in range(1, len(x_axis)):
        x = endpt_x[j]
        y = endpt_y[i]
        tmp_cnt = greed[y][x] - greed[i-1][x] - greed[y][j-1] + greed[i-1][j-1]
        if cnt < tmp_cnt:
            cnt = tmp_cnt
print(K-cnt)