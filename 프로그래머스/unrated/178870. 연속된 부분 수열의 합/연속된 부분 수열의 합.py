def solution(sequence, k):
    lst = []
    sums = [0]+sequence[:]
    for i in range(1, len(sums)):
        sums[i] += sums[i-1]
    l = r = 0
    while r < len(sums):
        val = sums[r] - sums[l]
        if val == k:
            lst.append([l, r])
            l += 1
        elif val > k:
            l += 1
        else:
            r += 1    
    min_value = min(lst, key=lambda x: (x[1]-x[0], x[0]))
    return [min_value[0], min_value[1]-1]
