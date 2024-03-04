def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))
    for pt in photo:
        s = 0
        for p in pt:
            if score.get(p) is not None:
                s += score.get(p)
        answer.append(s)
    return answer
