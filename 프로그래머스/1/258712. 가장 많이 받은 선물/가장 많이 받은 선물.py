def solution(friends, gifts):
    answer = 0
    fr_id = dict()
    fl = len(friends)
    next_gifts = [0]*fl
    gift_pts = [0]*fl
    for f in range(fl):
        fr_id[friends[f]] = f
    gift = [[0]*fl for _ in range(fl)]
    for g in gifts:
        A, B = g.split()
        gift[fr_id[A]][fr_id[B]] += 1
        gift_pts[fr_id[A]] += 1
        gift_pts[fr_id[B]] -= 1
    for gfrom in range(fl):
        for gto in range(gfrom+1, fl):
            if gfrom != gto:
                if gift[gfrom][gto] < gift[gto][gfrom]:
                    next_gifts[gto] += 1
                elif gift[gfrom][gto] == gift[gto][gfrom]:
                    if gift_pts[gfrom] < gift_pts[gto]:
                        next_gifts[gto] += 1
                    elif gift_pts[gfrom] > gift_pts[gto]:
                        next_gifts[gfrom] += 1
                else:
                    next_gifts[gfrom] += 1
    answer = max(next_gifts)
    return answer