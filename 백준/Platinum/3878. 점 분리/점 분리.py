import sys


def ccw(origin, v1, v2): # origin -> v1 -> v2
    return (v1[0]-origin[0]) * (v2[1] - origin[1]) - (v1[1]-origin[1]) * (v2[0] - origin[0])


def convex_hull(pts, num):
    pts = sorted(pts)
    if len(pts) <= 1:
        return pts
    lower = []
    upper = []
    for i in range(num):
        j = num - 1 - i
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], pts[i]) <= 0:
            lower.pop()
        lower.append(pts[i])
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], pts[j]) <= 0:
            upper.pop()
        upper.append(pts[j])
    return lower[:-1]+upper[:-1]


def is_crossing(l1, l2):
    c1 = ccw(l1[0], l1[1], l2[0])*ccw(l1[0], l1[1], l2[1])
    c2 = ccw(l2[0], l2[1], l1[0])*ccw(l2[0], l2[1], l1[1])
    if c1 <= 0 and c2 <= 0:
        if c1 == 0 and c2 == 0:
            if min(l1[0][0], l1[1][0]) <= max(l2[0][0], l2[1][0]) and min(l1[0][1], l1[1][1]) <= max(l2[0][1], l2[1][1]):
                if min(l2[0][0], l2[1][0]) <= max(l1[0][0], l1[1][0]) and min(l2[0][1], l2[1][1]) <= max(l1[0][1], l1[1][1]):
                    return True
        else:
            return True
    return False
    

input = sys.stdin.readline
T = int(input())
for tc in range(T):
    n, m = map(int, input().split()) # n : 검정 점의 개수, m : 흰 점의 개수
    black = [list(map(int, input().split())) for _ in range(n)]
    white = [list(map(int, input().split())) for _ in range(m)]
    cvhb = convex_hull(black, n)
    cvhw = convex_hull(white, m)
    n, m = len(cvhb), len(cvhw)
    if n < 3 and m < 3:
        if is_crossing([cvhb[0], cvhb[1%n]], [cvhw[0], cvhw[1%m]]):
            print("NO")
        else:
            print("YES")
        continue
    ccw1_cnt = [0, 0]
    ccw2_cnt = [0, 0]
    ans = True
    for i in range(n):
        line1 = [cvhb[i], cvhb[(i+1)%n]]
        for j in range(m):
            line2 = [cvhw[j], cvhw[(j+1)%m]]
            ccw1 = ccw(line1[0], line2[0], line2[1])
            ccw2 = ccw(line2[0], line1[0], line1[1])
            if ccw1 > 0:
                ccw1_cnt[0] += 1
            elif ccw1 < 0:
                ccw1_cnt[1] += 1
            if ccw2 > 0:
                ccw2_cnt[0] += 1
            elif ccw2 < 0:
                ccw2_cnt[1] += 1
            if is_crossing(line1, line2):
                ans = False
        if not ans:
            break
    if max(ccw1_cnt) == n*m or max(ccw2_cnt) == n*m:
        ans = False
    if ans:
        print("YES")
    else:
        print("NO")