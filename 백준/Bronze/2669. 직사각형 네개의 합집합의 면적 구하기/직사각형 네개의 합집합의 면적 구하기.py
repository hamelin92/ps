def r_geo(a,b,c,d):
    result = set()
    for i in range(c-a):
        for j in range(d-b):
            result.add((a+i, b+j))
    return result
rect_union = set()
for num in range(4):
    cords = list(map(int,input().split()))
    rect_union = rect_union | r_geo(*cords)
print(len(rect_union))
