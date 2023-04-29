import sys
sys.getrecursionlimit = 10000

def d(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


def distance(s, e):
    if e-s < 3:
        minimum = 800000001
        for i in range(s, e):
            for j in range(i+1, e+1):
                nd = d(pts[i], pts[j])
                if nd < minimum:
                    minimum = nd
        return minimum
    mid = (s+e)//2
    left = distance(s, mid)
    right = distance(mid, e)
    min_d = min(left, right)
    pole = list(filter(lambda x: (x[0]-pts[mid][0])**2 < min_d, pts[s:e+1]))
    pole.sort(key=lambda x: x[1])
    for b in range(len(pole)-1):
        for t in range(b+1, len(pole)):
            if (pole[t][1] - pole[b][1])**2 < min_d:
                min_d = min(min_d, d(pole[t], pole[b]))
            else:
                break
    return min_d


N = int(sys.stdin.readline())
pts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pts.sort()
print(distance(0, N-1))