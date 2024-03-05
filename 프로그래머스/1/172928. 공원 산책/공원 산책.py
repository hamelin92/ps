def solution(park, routes):
    height = len(park)
    weight = len(park[0])
    s = [0, 0]
    vec = {"E": [0, 1], "W":[0, -1], "S":[1, 0], "N":[-1, 0]}
    for h in range(height):
        for w in range(weight):
            if park[h][w] == "S":
                s[0], s[1] = h, w
                print(s)
                for route in routes:
                    flag = 0
                    v, num = route.split()
                    n = int(num)
                    nh, nw = s[0] + n*vec[v][0], s[1] + n*vec[v][1]
                    if 0 <= nh < height and 0 <= nw < weight:
                        for y in range(min(s[0], nh), max(s[0], nh)+1):
                            for x in range(min(s[1], nw), max(s[1], nw)+1):
                                if park[y][x] == "X":
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                        else:
                            s[0], s[1] = nh, nw
                            print(nh, nw, route)
                return s